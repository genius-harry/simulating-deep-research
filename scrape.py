import requests

def firecrawl_scrape(url: str, api_key: str) -> str:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True
    }
    response = requests.post("https://api.firecrawl.dev/v1/scrape", headers=headers, json=payload)
    data = response.json()
    print(f"Scraping website: {url}")
    return data.get("data", {}).get("markdown", "")