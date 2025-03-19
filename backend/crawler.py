import aiohttp
import asyncio
from bs4 import BeautifulSoup
<<<<<<< HEAD
import csv
import os

def save_to_csv(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    print(f"Saving {len(data)} records to: {path}")

    keys = ['id', 'content', 'url']
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Successfully saved to {path}")

# Load URLs from TRACE-provided CSV
def load_urls_from_csv(csv_path: str):
    urls = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['website']:
                urls.append(row['website'].strip())
    return urls

async def fetch_page(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.text()
=======
from urllib.parse import urljoin, urlparse
import logging
from datetime import datetime

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
>>>>>>> a530d28d76556a047671f79e7413b82f45e26bbc

async def crawl_site(base_url, depth=2):
    crawled_urls = set()
    queue = [(base_url, 0)]
    crawled_data = []

    async with aiohttp.ClientSession() as session:
        while queue:
            current_url, current_depth = queue.pop(0)
            if current_url in crawled_urls or current_depth > depth:
                continue

            try:
                page_content = await fetch_page(session, current_url)
                soup = BeautifulSoup(page_content, 'html.parser')

                # Extract text
                text = ' '.join(tag.get_text() for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'span']))

<<<<<<< HEAD
                crawled_data.append({
                    'id': len(crawled_data) + 1,
                    'content': text,
                    'url': current_url
                })

                # Extract links
                links = [link.get('href') for link in soup.find_all('a', href=True)]
                for link in links:
                    absolute_url = current_url + link if link.startswith('/') else link
                    queue.append((absolute_url, current_depth + 1))

                crawled_urls.add(current_url)
                print(f'Crawled: {current_url} at depth {current_depth}')

            except Exception as e:
                print(f'Error crawling {current_url}: {e}')

    # Save raw crawled data to CSV
    save_to_csv(crawled_data, 'backend/data/crawled_data.csv')

    return crawled_data
=======
    return list(crawled_urls)"test"
>>>>>>> a530d28d76556a047671f79e7413b82f45e26bbc
