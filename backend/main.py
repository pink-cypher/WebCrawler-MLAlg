from fastapi import FastAPI, Query
from crawler import crawl_site, load_urls_from_csv
from nlp import nlp_clean_csv
from ml import generate_credentials
from directory_fuzzer import create_directory_wordlist, create_wordlist_from_urls
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()

@app.post("/crawl")
async def start_crawl(url: str = Query(...), depth: int = Query(2)):
    crawled_data = await crawl_site(url, depth)

    urls = [entry['url'] for entry in crawled_data]

    return {
        "message": "Crawling completed",
        "urls_crawled": len(urls),
        "crawled_urls": urls
    }

@app.post("/nlp/clean")
def clean_data():
    nlp_clean_csv('backend/data/crawled_data.csv', 'backend/data/cleaned_data.csv')
    return {"message": "Data cleaned successfully"}

@app.post("/ml/generate")
def generate_creds():
    creds = generate_credentials('backend/data/cleaned_data.csv')
    return {"credentials": creds}

@app.post("/fuzzer/generate")
def generate_fuzzer_wordlist(csv_path: str = Query('backend/data/crawled_data.csv')):
    """Generate a directory fuzzer wordlist from the crawled data"""
    # Ensure the directory exists
    os.makedirs(os.path.dirname('backend/data/directory_wordlist.txt'), exist_ok=True)
    
    # Generate the wordlist
    wordlist = create_directory_wordlist(
        crawled_data_path=csv_path,
        output_path='backend/data/directory_wordlist.txt'
    )
    
    return {
        "message": "Directory fuzzer wordlist generated successfully",
        "wordlist_path": 'backend/data/directory_wordlist.txt',
        "word_count": len(wordlist),
        "sample": wordlist[:10]  # Return a sample of the first 10 words
    }

@app.post("/fuzzer/generate-from-urls")
async def generate_fuzzer_from_urls(url: str = Query(...), depth: int = Query(2)):
    """Crawl a website and directly generate a directory fuzzer wordlist"""
    # First, crawl the website
    crawled_data = await crawl_site(url, depth)
    urls = [entry['url'] for entry in crawled_data]
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname('backend/data/directory_wordlist.txt'), exist_ok=True)
    
    # Generate the wordlist directly from the URLs
    wordlist = create_wordlist_from_urls(
        urls=urls,
        output_path='backend/data/directory_wordlist.txt'
    )
    
    return {
        "message": "Website crawled and directory fuzzer wordlist generated",
        "urls_crawled": len(urls),
        "wordlist_path": 'backend/data/directory_wordlist.txt',
        "word_count": len(wordlist),
        "sample": wordlist[:10]
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5174"] if you want to lock it down
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)