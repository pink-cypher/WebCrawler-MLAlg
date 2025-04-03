from flask import Flask, jsonify, request
from neo4j import GraphDatabase
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Neo4j Connection Details from environment variables
URI = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "yourpassword")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow Svelte frontend to access API

# Connect to Neo4j
try:
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
except Exception as e:
    print(f"❌ Error connecting to Neo4j: {e}")

# Function to run queries
def run_query(query, params=None):
    with driver.session() as session:
        result = session.run(query, parameters=params)
        return [record.data() for record in result]

# API endpoint to fetch nodes
@app.route("/nodes", methods=["GET"])
def get_nodes():
    try:
        query = "MATCH (n) RETURN n LIMIT 10"
        result = run_query(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
