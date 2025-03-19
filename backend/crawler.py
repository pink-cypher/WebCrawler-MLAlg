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

async def crawl_worker(self, session, queue, results, base_url, excluded_urls, max_depth):
        """Worker function for concurrent crawling"""
        while not queue.empty():
            current_url, current_depth = await queue.get()
            
            if current_url in self.crawled_urls or current_depth > max_depth:
                queue.task_done()
                continue
                
            self.crawled_urls.add(current_url)
            
            html, status = await self.fetch_page(session, current_url)
            if html:
                page_data = self.extract_page_data(html, current_url)
                results.append(page_data)
                
                # Update tree
                self.update_url_tree(current_url, page_data)
                
                # Only continue if haven't reached max depth
                if current_depth < max_depth:
                    soup = BeautifulSoup(html, 'html.parser')
                    links = [link.get('href') for link in soup.find_all('a', href=True)]
                    
                    
                    for link in links:
                        normalized_url = self.normalize_url(current_url, link)
                        if (normalized_url and
                            normalized_url not in self.crawled_urls and
                            self.filter_url(normalized_url, excluded_urls, base_url)):
                            await queue.put((normalized_url, current_depth + 1))
            
            queue.task_done()
    
    def update_url_tree(self, url, page_data):
        parsed = urlparse(url)
        path_parts = parsed.path.strip('/').split('/')
        
        current = self.url_tree
        domain = f"{parsed.scheme}://{parsed.netloc}"
        
        if domain not in current:
            current[domain] = {'data': {}, 'children': {}}
        
        current = current[domain]
        
        for part in path_parts:
            if part:
                if part not in current['children']:
                    current['children'][part] = {'data': {}, 'children': {}}
                current = current['children'][part]
        
        current['data'] = page_data

async def crawl_site(self, base_url, depth=3, excluded_urls=None, concurrency=10):
        if self.scan_in_progress:
            self.logger.warning("A crawl operation is already in progress")
            return None
            
        self.scan_in_progress = True
        self.scan_start_time = datetime.now()
        
        excluded_urls = excluded_urls or []
        self.crawled_urls.clear()
        self.url_tree.clear()
        self.max_concurrent_requests = concurrency
        
        results = []
        
        try:
            connector = aiohttp.TCPConnector(limit=concurrency)
            timeout = aiohttp.ClientTimeout(total=30)
            
            async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                queue = asyncio.Queue()
                await queue.put((base_url, 0))
                workers = [
                    asyncio.create_task(
                        self.crawl_worker(session, queue, results, base_url, excluded_urls, depth)
                    )
                    for _ in range(concurrency)
                ]
                await queue.join()
                for worker in workers:
                    worker.cancel()
                await asyncio.gather(*workers, return_exceptions=True)
        
        except Exception as e:
            self.logger.error(f"Error during crawl: {str(e)}")
        finally:
            self.scan_in_progress = False
            self.scan_end_time = datetime.now()
            
            scan_time = (self.scan_end_time - self.scan_start_time).total_seconds()
            self.logger.info(f"Crawl completed. Crawled {len(results)} URLs in {scan_time:.2f} seconds")
            
        return {
            'results': results,
            'url_tree': self.url_tree,
            'stats': {
                'urls_crawled': len(results),
                'scan_time_seconds': (self.scan_end_time - self.scan_start_time).total_seconds(),
                'start_time': self.scan_start_time.isoformat(),
                'end_time': self.scan_end_time.isoformat()
            }
        }
