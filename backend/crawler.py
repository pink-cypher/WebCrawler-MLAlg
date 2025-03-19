import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch_page(self, session, url, timeout=10):
        "Fetch a page with timeout and error handling"
        try:
            async with session.get(url, timeout=timeout) as response:
                if response.status == 200:
                    self.logger.info(f"Crawled: {url} (Status: {response.status})")
                    return await response.text(), response.status
                else:
                    self.logger.warning(f"Failed to crawl: {url} (Status: {response.status})")
                    return None, response.status
        except Exception as e:
            self.logger.error(f"Error crawling {url}: {str(e)}")
            return None, 0

async def crawl_site(base_url, depth=2):
    crawled_urls = set()

    async with aiohttp.ClientSession() as session:
        queue = [(base_url, 0)]

        while queue:
            current_url, current_depth = queue.pop(0)
            if current_url in crawled_urls or current_depth > depth:
                continue

            crawled_urls.add(current_url)
            page_content = await fetch_page(session, current_url)

            soup = BeautifulSoup(page_content, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a', href=True)]
            
            for link in links:
                absolute_url = current_url + link if link.startswith('/') else link
                queue.append((absolute_url, current_depth + 1))
                print(f"Crawled: {absolute_url}")  # Save to DB later

    return list(crawled_urls)"test"