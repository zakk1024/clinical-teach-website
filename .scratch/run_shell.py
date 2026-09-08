import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto("http://127.0.0.1:8777/tests/harness.html")
        await pg.wait_for_timeout(12000)
        txt = await pg.evaluate("() => document.body.innerText")
        fails = [l for l in txt.splitlines() if "FAIL" in l]
        print("shell PASS:", txt.count("PASS"), "FAIL:", len(fails))
        for f in fails: print(f)
        await b.close()

asyncio.run(main())
