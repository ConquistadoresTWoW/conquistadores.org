FROM python:3.13.3-slim-bookworm AS base
LABEL maintainer="Ozkar L. Garcell <ozkar.garcell@gmail.com>"

WORKDIR /app

# Create non-root user (same defaults as before)
ARG UID=1000
ARG GID=1000
RUN groupadd -g "${GID}" conquistador \
  && useradd -m -u "${UID}" -g "${GID}" conquistador

USER conquistador

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=. \
    UV_PROJECT_ENVIRONMENT=/home/conquistador/.local \
    PATH=/home/conquistador/.local/bin:$PATH


# ---------- Build stage ----------
FROM base AS app-build

# Copy uv binaries
COPY --from=ghcr.io/astral-sh/uv:0.9.21 /uv /uvx /usr/local/bin/

# Dependency files only (for cache)
COPY --chown=conquistador:conquistador pyproject.toml uv.lock* ./

# Compile/install deps into user env
RUN uv sync --frozen --no-install-project

CMD ["bash"]


# ---------- Runtime stage ----------
FROM base AS app

# Bring in built environment + uv
COPY --from=app-build --chown=conquistador:conquistador /home/conquistador/.local /home/conquistador/.local
COPY --from=app-build /usr/local/bin/uv /usr/local/bin/uvx /usr/local/bin/

# App source
COPY --chown=conquistador:conquistador . .

WORKDIR /app/conquistadores

EXPOSE 8000
