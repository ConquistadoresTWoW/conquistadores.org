import logging

import httpx
from apps.events.models import Events, Raids
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

logger = logging.getLogger(__name__)

EVENTS_URL = "https://raidres.fly.dev/api/events"
RAIDS_URL = "https://raidres.fly.dev/raids/raids.json"
COOKIE = "d.access_token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..D3JUsr6MDVRfpjk0.fmzuHyiJyRyB03Z5lWDHQ2NUBFHhs8NvEZbbQ8v94NeexA780d5g1GpHXzEIv4M1a6KQ8tKhiFJz.mgciqdOrHqMsRJLjBNC_6Q; d.refresh_token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..P9aYRHac29tHbraE.Rp1DJZTg8kLhzIKdCoSJGSUvgiFh-eoWeXLMAWEL.hPnb3yLn0hpXx_TC-yywvA; d.expiry=1750955730; jwt=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..pdS5Dkqsz7fNhkVc0A3-Cw.AOCuuXlJv6_Bi8MJ6aQEzdr0qw6yklFXHSXDJfrMIuIy3E7NSdngqz5oyaKZlZOzeRIrRijpbnqK6z4MZuYf95_vVcnTiz08bpx7KjLBanWoNhjX1f9b43CZBBB7puuJ7nYEr3m19UtDMlmZeKqtTy-7RpBDIZh86H11xAS8_eZkfaXT3U_psitiDKs3ikx8s7wYPpCMZyLbgSamLNMG4FbNXWyJJug7XmEjlbRsOAKDQrqx589VWCszRxOX4zav9qeD0rFMTGEfzi7IVnkK_4sb7ECUPLAbCVioZhDLEptlbu0DxZ3JYCAfbbuAJyqpZfl24y5CrY7I6eEDWhLR-frhBJoJ4-HBEhqEm3Oa3HJVmQ68YSQNYRai9FE1QvRUcumUQqFEOcVz735jjOAx8LpYEaHFTuhBCfTCAHsCdMpT_kjo8eHPStinXeLeBEhFrYbVBXCrqfoOFvAiuhf8-REmTUvDrOBlB2FIi1R8yS_zXOud-RcSDFI90mQLJHchAz3ybWDujBjmuQsvYrRLMZ8ptbRuhdzvxh1Fqa093EBEOTNUmmthb45WTEy3ubzsdFebjNAKtG6ElKHLD5SSLx_r9U6hZnnv81lCAmkogyLIpndFQIIu46VYxuNKAXH6WRCHDjViefqis5sGDQaIW3lZrGRirUR7-MQjVxxxnFZCVmo6VWSy0nSpjwSMBtc3RtZkV9DmJZp90oQvZPxsyBmC1s56RpvxkF6F-OCUYHoqXmNlL7jSYLakocc1RPsK.Phxf6D23aG3Y2LooH4fm2g"


def fetch_raids():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",  # noqa: E501
    }

    with httpx.Client() as client:
        resp = client.get(RAIDS_URL, headers=headers)
        resp.raise_for_status()
        raids = resp.json()
        for raid in raids:
            _, _ = Raids.objects.update_or_create(
                reference=raid["reference"],
                name=raid["name"],
                defaults={
                    "raid_id": raid["id"],
                    "max_attendance": raid["maxAttendance"],
                },
            )


def fetch_events():
    headers = {
        "Cookie": COOKIE,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",  # noqa: E501
    }

    with httpx.Client() as client:
        resp = client.get(EVENTS_URL, headers=headers)
        resp.raise_for_status()
        events = resp.json()
        for event in events:
            _, _ = Events.objects.update_or_create(
                event_id=event["id"],
                reference=event["reference"],
                defaults={
                    "raid_id": Raids.objects.filter(
                        raid_id=event["raidId"]
                    ).first(),
                    "description": event["description"],
                    "start_time": event["startTime"],
                    "lock_at_start_time": event["lockAtStartTime"],
                    "locked": event["locked"],
                    "reservation_limit": event["reservationLimit"],
                    "allow_comments": event["allowComments"],
                    "signups": event["signups"],
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
            fetch_raids,
            trigger=CronTrigger(day="*/1"),
            id="fetch_raids",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'fetch_raids'.")

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
