from flask import Flask, jsonify, request
from neo4j import GraphDatabase
from flask_cors import CORS
from dotenv import load_dotenv
import os
import csv
import asyncio
from crawler import crawl_site  # Import the crawl_site function from crawler.py
from services import Neo4jService  # Neo4j helper class

# Load environment variables from .env file
load_dotenv()

# Neo4j connection details from .env or defaults
URI = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "yourpassword")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Connect to Neo4j
try:
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
except Exception as e:
    print(f"❌ Error connecting to Neo4j: {e}")

# Neo4j service instance (wrapper class)
neo4j_service = Neo4jService(URI, USER, PASSWORD)

# Utility to run arbitrary queries (if needed)
def run_query(query, params=None):
    with driver.session() as session:
        result = session.run(query, parameters=params)
        return [record.data() for record in result]

# ---------- POST /crawl ----------
@app.route("/crawl", methods=["POST"])
@app.route("/crawl", methods=["POST"])
def crawl():
    base_url = request.json.get('base_url')
    if not base_url:
        return jsonify({"error": "Base URL is required"}), 400

    depth = request.json.get('depth', 2)
    print(f"Starting crawl for base URL: {base_url} with depth: {depth}")

    crawled_data = asyncio.run(crawl_site(base_url, depth))

    neo4j_service.add_crawled_data(crawled_data)

    return jsonify({"message": f"Successfully crawled and saved {len(crawled_data)} pages"}), 200


# ---------- GET /nodes ----------
@app.route("/nodes", methods=["GET"])
def get_nodes():
    try:
        query = "MATCH (n:Page) RETURN n LIMIT 10"
        result = run_query(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- GET /linked_pages?url=<page_url> ----------
@app.route("/linked_pages", methods=["GET"])
def get_linked_pages():
    target_url = request.args.get("url")
    if not target_url:
        return jsonify({"error": "URL parameter is required"}), 400

    try:
        query = """
        MATCH (p:Page)-[:LINKS_TO]->(target:Page {url: $url})
        RETURN p.url AS linked_pages
        """
        result = run_query(query, params={"url": target_url})
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- POST /upload_csv ----------
@app.route("/upload_csv", methods=["POST"])
@app.route("/upload_csv", methods=["POST"])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    os.makedirs('uploads', exist_ok=True)
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    try:
        with driver.session() as session, open(file_path, mode='r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                session.run(
                    "MERGE (n:Page {url: $url}) "
                    "SET n.title = $title, "
                    "    n.content = $content, "
                    "    n.links = $links",
                    url=row['url'],
                    title=row.get('title', ''),
                    content=row.get('content', ''),
                    links=row.get('links', '')
                )
        os.remove(file_path)
        return jsonify({"message": "CSV uploaded successfully to Neo4j"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- Run Flask ----------
if __name__ == "__main__":
    app.run(debug=True)
