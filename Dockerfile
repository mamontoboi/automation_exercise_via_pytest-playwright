FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.9.9 /uv /bin/uv

ADD . /app
WORKDIR /app

RUN uv sync --locked

CMD ["uv", "run", "pytest"]
