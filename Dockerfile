FROM python:3.13.11-slim-bookworm AS base
LABEL maintainer="Ozkar L. Garcell <ozkar.garcell@gmail.com>"

WORKDIR /app

ARG UID=1000
ARG GID=1000
RUN groupadd -g "${GID}" conquistador \
  && useradd -m -u "${UID}" -g "${GID}" conquistador

USER conquistador

ENV PYTHONUNBUFFERED=1 \
  PYTHONPATH=. \
  UV_PROJECT_ENVIRONMENT=/home/conquistador/.local \
  PATH=/home/conquistador/.local/bin:$PATH


FROM base AS app-build

COPY --from=ghcr.io/astral-sh/uv:0.9.21 /uv /uvx /usr/local/bin/

COPY --chown=conquistador:conquistador pyproject.toml uv.lock* ./

RUN uv sync --frozen --no-install-project

CMD ["bash"]


FROM base AS app

COPY --from=app-build --chown=conquistador:conquistador /home/conquistador/.local /home/conquistador/.local
COPY --from=app-build /usr/local/bin/uv /usr/local/bin/uvx /usr/local/bin/

COPY --chown=conquistador:conquistador . .

WORKDIR /app/conquistadores

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "--preload", "config.wsgi:application"]