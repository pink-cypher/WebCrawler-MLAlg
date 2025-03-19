import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin

async def fetch_page(session, url):
    try:
        async with session.get(url, ssl=False, headers={'User-Agent': 'Mozilla/5.0'}) as response:
            return await response.text()
    except Exception as e:
        print(f"Failed to fetch {url}: {str(e)}")
        return ""

async def crawl_site(base_url, depth=2):
    crawled_urls = set()

    async with aiohttp.ClientSession() as session:
        queue = [(base_url, 0)]

        while queue:
            current_url, current_depth = queue.pop(0)
            
            if current_url in crawled_urls or current_depth > depth:
                continue

            print(f"Crawling: {current_url} at depth {current_depth}")
            crawled_urls.add(current_url)

            page_content = await fetch_page(session, current_url)
            if not page_content:
                continue  # Skip if fetching failed

            soup = BeautifulSoup(page_content, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a', href=True)]

            for link in links:
                absolute_url = urljoin(current_url, link)

                if absolute_url not in crawled_urls:
                    queue.append((absolute_url, current_depth + 1))

    return list(crawled_urls)