FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ADD . /app
WORKDIR /app

RUN uv sync --locked

# Run tests
CMD ["uv", "run", "pytest"]
