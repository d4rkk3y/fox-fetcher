# Fox Fetcher MCP Server

An MCP (Model Context Protocol) server providing a `fetch_url` tool that uses Playwright to fetch HTML content from websites.

## Features

- `fetch_url(url: str) -> str`: Fetches the HTML content of the given URL using headless Chromium via Playwright.

## Setup

1. Ensure [uv](https://docs.astral.sh/uv/) is installed.

2. Install dependencies and sync the lockfile:
   ```
   uv sync
   ```

3. Install Playwright browsers:
   ```
   playwright install
   ```

4. Run the MCP server:
   ```
   uv run main.py
   ```

The server will start with streamable HTTP transport (default port 8000).

## Usage

Connect to the MCP server using an MCP client (e.g., Claude Desktop, Cursor, etc.).

Available tools:
- `fetch_url`: Provide a URL (e.g., "https://example.com") to retrieve the page's HTML content.

### Example Tool Call
```
fetch_url(url="https://example.com")
```

Returns the full HTML of the page after DOM content is loaded.

## Development

- Edit [`main.py`](main.py) to add more tools or resources.
- Update [`pyproject.toml`](pyproject.toml) for new dependencies.