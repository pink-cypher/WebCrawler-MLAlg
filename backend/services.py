from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Neo4jService:
    def __init__(self, uri, user, password):
        # Get connection details from .env file
        self.uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.username = os.getenv("NEO4J_USER", "neo4j")
        self.password = os.getenv("NEO4J_PASSWORD", "avalon-element-tennis-beach-sofia-735")

        # Create a driver instance to connect to the database
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_session(self):
        """Returns a session for interacting with the DB."""
        return self.driver.session()

    def close(self):
        """Close the driver connection."""
        self.driver.close()

    def add_crawled_data(self, data):
        with self.driver.session() as session:
            for item in data:
                session.run(
                    """
                    MERGE (p:Page {url: $url})
                    SET p.content = $content
                    """,
                    url=item["url"],
                    content=item["content"]
                )

# Example usage
#neo4j_service = Neo4jService()
#session = neo4j_service.get_session()

# Make sure to close the session when done
#session.close()

def store_page_data(session, url, title, content):
    """Store crawled page data in Neo4j"""
    cypher_query = """
    MERGE (page:Page {url: $url})
    SET page.title = $title, page.content = $content
    RETURN page
    """
    session.run(cypher_query, url=url, title=title, content=content)

def store_link_between_pages(session, from_url, to_url):
    """Store link between pages in Neo4j"""
    cypher_query = """
    MATCH (from:Page {url: $from_url}), (to:Page {url: $to_url})
    MERGE (from)-[:LINKS_TO]->(to)
    """
    session.run(cypher_query, from_url=from_url, to_url=to_url)

def get_pages_linked_to_url(session, target_url):
    cypher_query = """
    MATCH (p:Page)-[:LINKS_TO]->(target:Page {url: $url})
    RETURN p.url AS linked_pages
    """
    result = session.run(cypher_query, url=target_url)
    return [record["linked_pages"] for record in result]
