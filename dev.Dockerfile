FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

RUN apt update && apt install --no-install-recommends -y \
    tzdata \
    ca-certificates \ 
    curl \
    gnupg \
    wait-for-it && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/lib/apt && \
    rm -rf /var/lib/dpkg && \
    rm -rf /var/cache && \
    rm -rf /var/log

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --dev

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []

COPY --chmod=755 ./compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint

COPY --chmod=755 ./compose/start /start
RUN sed -i 's/\r$//g' /start
