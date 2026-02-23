# FastMCP Server — Minimal Docker Example

A minimal [FastMCP](https://gofastmcp.com) server deployable with Docker, compatible with **Claude Code** and **GitHub Copilot** (VS Code).

---

## Project Structure

```
.
├── server.py          # FastMCP server (stdio transport)
├── server_http.py     # FastMCP server (HTTP transport)
├── Dockerfile         # For stdio transport (Claude Code via docker run -i)
├── Dockerfile.http    # For HTTP transport (remote / compose)
├── docker-compose.yml # Starts HTTP server on port 8000
└── .vscode/
    └── mcp.json       # GitHub Copilot MCP configuration
```

---

## Transport Methods

MCP supports two transport modes — choose based on your use case:

| Transport | Use case | Config |
|-----------|----------|--------|
| **stdio** | Local Docker container spawned per session | `docker run -i --rm <image>` |
| **HTTP**  | Remote server, shared across clients | `http://localhost:8000/mcp` |

---

## Option A — stdio Transport (Claude Code)

Best for local dev. Claude Code spawns the container and communicates via stdin/stdout.

### 1. Build the image

```bash
docker build -t fastmcp-demo .
```

### 2. Register with Claude Code

```bash
claude mcp add demo-server -- docker run -i --rm fastmcp-demo
```

#### 2.1 Verify

```bash
claude mcp list
# Then inside a Claude Code session:
/mcp
```

### 3. Connect from GitHub Copilot (VS Code)

The `.vscode/mcp.json` file is already configured. VS Code will auto-discover it.
Open VS Code → Command Palette → `MCP: List Servers` to confirm.


---

## Option B — HTTP Transport (Claude Code + GitHub Copilot)

Best for team sharing or remote deployment. Run the server once, connect from anywhere.

### 1. Start with Docker Compose

```bash
docker compose up -d
# Server is now at http://localhost:8000/mcp
```

### 2. Connect from Claude Code

```bash
claude mcp add --transport http demo-server http://localhost:8000/mcp
```

### 3. Connect from GitHub Copilot (VS Code)

The `.vscode/mcp.json` file is already configured. VS Code will auto-discover it.
Open VS Code → Command Palette → `MCP: List Servers` to confirm.

---

## Adding Your Own Tools

Edit `server.py` (or `server_http.py`) and add decorated functions:

```python
@mcp.tool
def my_tool(input: str) -> str:
    """Tool description shown to the LLM."""
    return input.upper()
```

FastMCP automatically infers the tool name, parameters, and schema from the function signature and docstring.

---

## Tips

- **Secrets**: Pass environment variables with `-e` in `docker run` or via `env:` in `docker-compose.yml`. For Claude Code: `claude mcp add -e MY_KEY=value demo -- docker run -i -e MY_KEY --rm fastmcp-demo`
- **stdio limitation**: stdio transport only works when the MCP client (Claude Code) can directly spawn the process. If Claude Code runs inside a container itself, use HTTP transport instead.
- **GitHub Copilot**: Requires VS Code 1.99+ and the GitHub Copilot extension. HTTP transport is generally more reliable for Copilot.