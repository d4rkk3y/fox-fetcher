from mcp.server.fastmcp import FastMCP
from playwright.async_api import async_playwright
import newspaper

# Create an MCP server
mcp = FastMCP("Demo", json_response=True)

@mcp.tool()
async def fetch_url(url: str) -> str:
    """Fetch the HTML content of the given URL using Playwright.

    Args:
        url: The URL to fetch.
    
    Returns:
        The HTML content of the page.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        content = await page.content()
        parsed_content = newspaper.article(url=url, input_html=content).text
        await browser.close()
        return parsed_content


# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport='streamable-http')