import logging
from datetime import date, datetime, timezone

import httpx
from apps.events.models import Events
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

logger = logging.getLogger(__name__)

today = date.today()
start_of_today_dt = datetime.combine(
    today, datetime.min.time(), tzinfo=timezone.utc
)
start_of_today_epoch = int(start_of_today_dt.timestamp())


def fetch_events():
    headers = {
        "Authorization": settings.RH_API_KEY,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",  # noqa: E501
    }

    with httpx.Client() as client:
        resp = client.get(
            f"https://raid-helper.dev/api/v3/servers/{settings.SERVER_ID}/events",
            headers=headers,
        )
        resp.raise_for_status()
        events = resp.json()["postedEvents"]
        upcoming_events = [
            e for e in events if e["startTime"] >= start_of_today_epoch
        ]
        for event in upcoming_events:
            _, _ = Events.objects.update_or_create(
                event_id=event["id"],
                title=event["title"],
                defaults={
                    "leader": event["leaderName"],
                    "image": event["imageUrl"],
                    "start": datetime.fromtimestamp(
                        event["startTime"], tz=timezone.utc
                    ),
                    "attendees": event["signUpCount"],
                    "discord_channel_id": event["channelId"],
                },
            )


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            fetch_events,
            trigger=CronTrigger(hour="*/4"),
            id="fetch_events",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'fetch_events'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(day_of_week="mon", hour="00", minute="00"),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
