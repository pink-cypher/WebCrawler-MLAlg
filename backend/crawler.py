import aiohttp
import asyncio
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urljoin
import requests

# ---------- Save crawled data to CSV ----------
def save_to_csv(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"Saving {len(data)} records to: {path}")

    keys = ['id', 'title', 'content', 'url', 'links']
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Successfully saved to {path}")

# ---------- Load URLs from CSV ----------
def load_urls_from_csv(csv_path: str):
    urls = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['website']:
                urls.append(row['website'].strip())
    return urls

# ---------- Upload CSV file to Neo4j ----------
def upload_csv_to_backend(csv_file_path):
    try:
        url = "http://localhost:5000/upload_csv"
        with open(csv_file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files)
            response.raise_for_status()  # Will raise an exception for non-200 status codes
            print(f"Upload successful: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error uploading CSV: {e}")


# Example usage after the crawler finishes:
csv_file_path = 'backend/data/crawled_data.csv'
if __name__ == "__main__":
    upload_csv_to_backend(csv_file_path)


# ---------- Fetch a page ----------
async def fetch_page(session, url, timeout=10):
    try:
        async with session.get(url, ssl=False, timeout=timeout) as response:
            if response.status == 200:
                print(f"Crawled: {url} (Status: {response.status})")
                return await response.text()
            else:
                print(f"Failed to crawl: {url} (Status: {response.status})")
                return None
    except Exception as e:
        print(f"Error crawling {url}: {str(e)}")
        return None

# ---------- Crawl site function ----------
async def crawl_site(base_url, depth=2):
    crawled_urls = set()
    crawled_data = []
    async with aiohttp.ClientSession() as session:
        queue = [(base_url, 0)]

        while queue:
            current_url, current_depth = queue.pop(0)

            if current_url in crawled_urls or current_depth > depth:
                continue

            page_content = await fetch_page(session, current_url)

            if page_content:
                soup = BeautifulSoup(page_content, 'html.parser')

                title = soup.title.string if soup.title else "No title"
                text = ' '.join(tag.get_text() for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'span']))

                links = [urljoin(current_url, link.get('href')) for link in soup.find_all('a', href=True)]
                links_str = ','.join(links)  # Save as a comma-separated string

                crawled_data.append({
                    'id': len(crawled_data) + 1,
                    'title': title,
                    'content': text,
                    'url': current_url,
                    'links': links_str
                })

                for link in links:
                    queue.append((link, current_depth + 1))

                crawled_urls.add(current_url)
                print(f'Crawled: {current_url} at depth {current_depth}')
            else:
                print(f"Skipping {current_url} due to error or no content")

    # Save crawled data to CSV after crawling is done
    save_to_csv(crawled_data, 'backend/data/crawled_data.csv')

    return crawled_data

