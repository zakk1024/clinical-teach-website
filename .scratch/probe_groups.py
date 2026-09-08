import asyncio
from playwright.async_api import async_playwright

JS = """() => {
  const zone = document.getElementById('m10-path-cards');
  return [...zone.children].map(el => ({tag: el.tagName, cls: el.className, group: el.dataset ? (el.dataset.group||'') : '', text: el.textContent.slice(0,40)}));
}"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto("http://127.0.0.1:8777/pages/index.html")
        await pg.wait_for_selector("#m10-path-cards .card", state="attached", timeout=8000)
        await pg.wait_for_timeout(1500)
        for row in await pg.evaluate(JS):
            print(row)
        await b.close()

asyncio.run(main())
