import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_openai_api_key():
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        raise Exception("Please set your OPENAI_API_KEY environment variable.")
    return key

def get_serpapi_api_key():
    key = os.environ.get('SERPAPI_API_KEY')
    if not key:
        raise Exception("Please set your SERPAPI_API_KEY environment variable.")
    return key

def get_firecrawl_api_key():
    key = os.environ.get('FIRECRAWL_API_KEY')
    if not key:
        raise Exception("Please set your FIRECRAWL_API_KEY environment variable.")
    return key