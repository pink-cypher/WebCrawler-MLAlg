import re
import os
from urllib.parse import urlparse, unquote
from collections import Counter

# Common directory names for websites
COMMON_DIRECTORIES = [
    'admin', 'login', 'home', 'register', 'signup', 'user', 'dashboard',
    'account', 'profile', 'settings', 'config', 'setup', 'install',
    'api', 'static', 'assets', 'images', 'img', 'css', 'js', 'scripts',
    'docs', 'documentation', 'help', 'faq', 'support', 'contact',
    'downloads', 'upload', 'media', 'files', 'backup', 'secure',
    'private', 'public', 'blog', 'forum', 'community', 'shop', 'store',
    'checkout', 'cart', 'search', 'about', 'services', 'products',
    'portfolio', 'news', 'events', 'gallery', 'archive', 'system',
    'wp-admin', 'wp-content', 'wordpress', 'joomla', 'drupal', 'magento'
]

class DirectoryFuzzer:
    def __init__(self):
        self.directory_words = set(COMMON_DIRECTORIES)
        self.word_counts = Counter()
    
    def extract_directory_names(self, urls):
        """Extract potential directory names from a list of URLs"""
        for url in urls:
            try:
                # Parse the URL
                parsed_url = urlparse(url)
                
                # Get the path and split into parts
                path = unquote(parsed_url.path)
                
                # Split the path by slashes and clean each part
                parts = [p for p in path.split('/') if p]
                
                # Add each path part that looks like a directory
                for part in parts:
                    # Skip parts that look like files with extensions
                    if '.' not in part:
                        # Clean the directory name
                        clean_dir = re.sub(r'[^a-zA-Z0-9_-]', '', part.lower())
                        if clean_dir and len(clean_dir) > 2:
                            self.directory_words.add(clean_dir)
                            self.word_counts[clean_dir] += 1
            
            except Exception as e:
                print(f"Error processing URL '{url}': {str(e)}")
    
    def extract_from_crawled_data(self, crawled_data_path):
        """Extract directory names from crawled data CSV"""
        import csv
        urls = []
        
        try:
            with open(crawled_data_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'url' in row and row['url']:
                        urls.append(row['url'])
        except Exception as e:
            print(f"Error reading crawled data from '{crawled_data_path}': {str(e)}")
        
        self.extract_directory_names(urls)
        return len(urls)
    
    def analyze_content_for_directories(self, crawled_data_path):
        """Analyze content for words that might be directories"""
        import csv
        
        try:
            with open(crawled_data_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'content' in row and row['content']:
                        content = row['content']
                        
                        # Find words that look like they could be directories
                        # Examples: /admin/, /login/, "admin section", etc.
                        dir_patterns = [
                            r'/([a-zA-Z0-9_-]{3,})/?',  # Words in URL paths
                            r'"([a-zA-Z0-9_-]{3,})\s+section"',  # "admin section"
                            r'"([a-zA-Z0-9_-]{3,})\s+area"',  # "login area"
                            r'"([a-zA-Z0-9_-]{3,})\s+page"'  # "contact page"
                        ]
                        
                        for pattern in dir_patterns:
                            matches = re.findall(pattern, content)
                            for match in matches:
                                clean_dir = match.lower()
                                if clean_dir and len(clean_dir) > 2:
                                    self.directory_words.add(clean_dir)
                                    self.word_counts[clean_dir] += 1
        
        except Exception as e:
            print(f"Error analyzing content from '{crawled_data_path}': {str(e)}")
    
    def generate_wordlist(self, min_length=3, max_length=20):
        """Generate a directory wordlist"""
        # Filter out words that are too short or too long
        filtered_words = [word for word in self.directory_words 
                          if min_length <= len(word) <= max_length]
        
        # Sort by frequency (most common first) then alphabetically
        sorted_words = sorted(filtered_words, 
                              key=lambda w: (-self.word_counts[w], w))
        
        return sorted_words
    
    def save_wordlist_to_file(self, output_path, wordlist=None):
        """Save the wordlist to a file"""
        if wordlist is None:
            wordlist = self.generate_wordlist()
        
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write the wordlist to file
            with open(output_path, 'w', encoding='utf-8') as f:
                for word in wordlist:
                    f.write(f"{word}\n")
            
            print(f"Successfully saved directory wordlist to: {output_path}")
            return True
        
        except Exception as e:
            print(f"Error saving wordlist to '{output_path}': {str(e)}")
            return False
    
    def ensure_variety(self, max_repetition_percentage=20):
        """Ensure variety in the wordlist (limit each root word to 20% repetition)"""
        # Group words by their first 3 characters as a simple "root"
        roots = {}
        for word in self.directory_words:
            if len(word) >= 3:
                root = word[:3]
                if root not in roots:
                    roots[root] = []
                roots[root].append(word)
        
        # Filter out words to ensure each root has at most max_repetition_percentage
        filtered_words = set()
        for root, words in roots.items():
            if len(words) <= 1:
                filtered_words.update(words)
                continue
            
            # Calculate how many words to keep
            max_allowed = max(1, int(len(self.directory_words) * max_repetition_percentage / 100))
            
            # Keep the most frequent words from this root
            sorted_by_freq = sorted(words, key=lambda w: -self.word_counts[w])
            filtered_words.update(sorted_by_freq[:max_allowed])
        
        self.directory_words = filtered_words

# Function to be called from other modules
def create_directory_wordlist(crawled_data_path, output_path):
    """Generate a directory fuzzer wordlist from crawled data and save it to a file"""
    fuzzer = DirectoryFuzzer()
    
    # Extract directory names from URLs in crawled data
    num_urls = fuzzer.extract_from_crawled_data(crawled_data_path)
    print(f"Analyzed {num_urls} URLs from crawled data")
    
    # Analyze page content for additional directory names
    fuzzer.analyze_content_for_directories(crawled_data_path)
    
    # Ensure variety in the wordlist
    fuzzer.ensure_variety()
    
    # Generate and save the wordlist
    wordlist = fuzzer.generate_wordlist()
    fuzzer.save_wordlist_to_file(output_path, wordlist)
    
    print(f"Generated directory wordlist with {len(wordlist)} entries")
    return wordlist

# Generate a wordlist directly from a list of URLs (without a CSV file)
def create_wordlist_from_urls(urls, output_path):
    """Generate a directory fuzzer wordlist directly from a list of URLs"""
    fuzzer = DirectoryFuzzer()
    
    # Extract directory names from the provided URLs
    fuzzer.extract_directory_names(urls)
    print(f"Analyzed {len(urls)} URLs")
    
    # Ensure variety in the wordlist
    fuzzer.ensure_variety()
    
    # Generate and save the wordlist
    wordlist = fuzzer.generate_wordlist()
    fuzzer.save_wordlist_to_file(output_path, wordlist)
    
    print(f"Generated directory wordlist with {len(wordlist)} entries")
    return wordlist