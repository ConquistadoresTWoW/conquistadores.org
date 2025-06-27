FROM python:3.13.3-slim-bookworm AS app-build
LABEL maintainer="Ozkar L. Garcell <ozkar.garcell@gmail.com>"

WORKDIR /app

ARG UID=1000
ARG GID=1000

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" conquistador \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" conquistador \
  && chown conquistador:conquistador -R /app

COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /usr/local/bin/

USER conquistador

COPY --chown=conquistador:conquistador pyproject.toml uv.lock* ./

ENV PYTHONUNBUFFERED="true" \
  PYTHONPATH="." \
  UV_COMPILE_BYTECODE=1 \
  UV_PROJECT_ENVIRONMENT="/home/conquistador/.local" \
  PATH="${PATH}:/home/conquistador/.local/bin" \
  USER="conquistador"

RUN uv sync --frozen --no-install-project

CMD ["bash"]

###############################################################################

FROM python:3.13.3-slim-bookworm AS app
LABEL maintainer="Ozkar L. Garcell <ozkar.garcell@gmail.com>"

WORKDIR /app

ARG UID=1000
ARG GID=1000
ARG DEBUG="false"

RUN apt-get update \
  && apt-get install -y --no-install-recommends curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" conquistador \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" conquistador \
  && chown conquistador:conquistador -R /app

USER conquistador

ENV PYTHONUNBUFFERED="true" \
  PYTHONPATH="." \
  UV_PROJECT_ENVIRONMENT="/home/conquistador/.local" \
  PATH="${PATH}:/home/conquistador/.local/bin" \
  USER="conquistador"

COPY --chown=conquistador:conquistador --from=app-build /home/conquistador/.local /home/conquistador/.local
COPY --from=app-build /usr/local/bin/uv /usr/local/bin/uvx /usr/local/bin/
COPY --chown=conquistador:conquistador . .

WORKDIR /app/conquistadores

EXPOSE 8000