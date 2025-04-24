import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Perform a Google search using SerpAPI
def google_search(query, num_results=5):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": num_results,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        return results.get("organic_results", [])
    return []





