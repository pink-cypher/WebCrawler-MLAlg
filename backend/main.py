from fastapi import FastAPI
from crawler import crawl_site
from ml import MarkovModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/crawl")
async def start_crawl(url: str, depth: int = 2):
    try:
        urls = await crawl_site(url, depth)
        return {"crawled_urls": urls}
    except Exception as e:
        print(f"Error during crawl: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.post("/ml/generate")
def start_credential_generation():
    # Dummy data - later pull from crawled data!
    data = ["admin", "login", "test"]
    model = MarkovModel()
    model.train(data)
    generated = [model.generate() for _ in range(10)]
    return {"credentials": generated}