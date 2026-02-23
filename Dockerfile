# Dockerfile for FastMCP server (stdio transport)
# Used when Claude Code runs the container directly via `docker run -i`
FROM python:3.12-slim

WORKDIR /app

# Install FastMCP
RUN pip install --no-cache-dir fastmcp

COPY server.py .

# IMPORTANT: Do NOT use ENTRYPOINT/CMD with shell form — stdio must be raw
ENTRYPOINT ["python", "server.py"]