import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, Playwright


async def scrape(playwright: Playwright, url: str):
    try:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        response = await page.goto(url)
        content =  await page.content()
        await browser.close()
        return content
    except Exception as e:
        print(str(e))
        return ""

def get_body_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.find('body')
    if body:
        return str(body)
    else:
        return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = cleaned_content.replace("\n", " ").strip()
    return cleaned_content

async def main(url: str):
    async with async_playwright() as p:
        return await scrape(p, url)

if __name__ == '__main__':
    asyncio.run(main())
