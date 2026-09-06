
import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await (await b.new_context()).new_page()
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("http://127.0.0.1:8777/tests/harness.html")
        for i in range(40):
            await asyncio.sleep(1)
            if await pg.title() == "HARNESS-DONE": break
        print(await pg.evaluate("document.getElementById('out').textContent"))
        print("console/page errors:", errs if errs else "無")
        await b.close()
asyncio.run(main())
