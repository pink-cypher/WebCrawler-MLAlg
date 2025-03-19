from fastapi import FastAPI, Query
from crawler import crawl_site, load_urls_from_csv
from nlp import nlp_clean_csv
from ml import generate_credentials
from fastapi.middleware.cors import CORSMiddleware

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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5174"] if you want to lock it down
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)