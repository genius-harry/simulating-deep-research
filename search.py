import requests
from typing import List
from api_keys import get_serpapi_api_key

def google_search(query: str, num_results: int = 3) -> List[str]:
    api_key = get_serpapi_api_key()
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": num_results,
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    results = []
    for res in data.get("organic_results", []):
        link = res.get("link")
        if link:
            results.append(link)
        if len(results) >= num_results:
            break
    return results