FROM python:3.12.8-slim-bookworm

# Install curl for HEALTHCHECK
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies first (layer cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the module
# The sys.path hack in app/services/resolver_service.py needs
# root-level routes/ and services/ directories accessible at /app/
COPY . /app/

# Create non-root user and data directory for SQLite
RUN groupadd -r resolver && \
    useradd -r -g resolver -d /app -s /sbin/nologin resolver && \
    mkdir -p /app/data && \
    chown -R resolver:resolver /app/data

USER resolver

EXPOSE 8788

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8788/health || exit 1

ENTRYPOINT ["./entrypoint.sh"]