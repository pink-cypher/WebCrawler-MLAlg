import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
from datetime import datetime

class Crawler:
    def __init__(self, logger=None):
        self.crawled_urls = set()
        self.url_tree = {}
        self.logger = logger or logging.getLogger(__name__)
        self.max_concurrent_requests = 10  # Configurable concurrency limit
        self.scan_in_progress = False
        self.scan_start_time = None
        self.scan_end_time = None

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

def normalize_url(self, base_url, link):
        """Normalize URLs to prevent duplicate crawling"""
        if not link:
            return None
            
        # Handle relative URLs
        if link.startswith('/'):
            return urljoin(base_url, link)
        
        # Handle full URLs
        if link.startswith(('http://', 'https://')):
            return link
            
        # Handle relative paths
        return urljoin(base_url, link)

def filter_url(self, url, excluded_urls, base_domain):
        """Filter URLs based on exclusion list and domain constraints"""
        if not url:
            return False
            
        # Check if URL is in exclusion list
        for excluded in excluded_urls:
            if excluded in url:
                return False
                
        # Stay within the same domain if configured
        parsed_url = urlparse(url)
        parsed_base = urlparse(base_domain)
        
        if parsed_url.netloc and parsed_url.netloc != parsed_base.netloc:
            return False
            
        return True
    
    def extract_page_data(self, html, url):
        """Extract useful data from the page"""
        if not html:
            return {
                'url': url,
                'title': '',
                'word_count': 0,
                'char_count': 0,
                'links_found': 0,
                'time_crawled': datetime.now().isoformat()
            }
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else ''
        
        # Extract text content
        text_content = soup.get_text()
        word_count = len(text_content.split())
        char_count = len(text_content)
        
        # Extract links
        links = [link.get('href') for link in soup.find_all('a', href=True)]
        
        # Extract logos, labels, and class titles (as requested in SRS document)
        logo_elements = soup.find_all(class_=lambda c: c and 'logo' in c.lower())
        label_elements = soup.find_all(['label'])
        class_titles = [elem.get('class', []) for elem in soup.find_all(class_=True)]
        
        extracted_words = []
        for element in logo_elements + label_elements:
            if element.string:
                extracted_words.append(element.string.strip())
                
        for classes in class_titles:
            extracted_words.extend([c for c in classes if len(c) > 3])
            
        return {
            'url': url,
            'title': title,
            'word_count': word_count,
            'char_count': char_count,
            'links_found': len(links),
            'time_crawled': datetime.now().isoformat(),
            'extracted_words': extracted_words,
            'links': links
        }

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