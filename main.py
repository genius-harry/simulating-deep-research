import json
from typing import List, Dict
from openai import OpenAI
from models import SearchQuery, DecisionOutput
from api_keys import get_openai_api_key, get_serpapi_api_key, get_firecrawl_api_key
from search import google_search
from scrape import firecrawl_scrape
from summarize import summarize_website_content


# Initialize OpenAI client
openai_api_key = get_openai_api_key()
client = OpenAI(api_key=openai_api_key)

# Get user input
user_input = input("Enter your research question: ")

# Generate initial search terms
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful research assistant. "
            "Given the research question from the user, output a valid JSON containing a key 'search_terms' with a list of relevant search phrases. "
            "Make sure your output adheres exactly to the following JSON schema."
        )
    },
    {
        "role": "user",
        "content": user_input
    }
]

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=messages,
    response_format=SearchQuery,
)
result = completion.choices[0].message.parsed
current_search_terms = result.search_terms

# Loop parameters
max_loops = 10
iteration = 0
searched_terms = set(current_search_terms)
aggregated_content: Dict[str, str] = {}  # URL -> scraped markdown
website_summaries: Dict[str, str] = {}   # URL -> summary

serpapi_api_key = get_serpapi_api_key()
firecrawl_api_key = get_firecrawl_api_key()

while iteration < max_loops:
    print(f"\n--- Iteration {iteration + 1} ---")
    # Step 1: Search and scrape
    for term in current_search_terms:
        urls = google_search(term, num_results=3)
        searched_terms.add(term)
        for url in urls:
            if url not in aggregated_content:
                scraped_text = firecrawl_scrape(url, firecrawl_api_key)
                aggregated_content[url] = scraped_text

    # Step 2: Summarize content
    for url, content in aggregated_content.items():
        if url not in website_summaries and content.strip():
            print(f"Summarizing content for: {url}")
            summary = summarize_website_content(content, openai_api_key)
            website_summaries[url] = summary
            print(f"Summary for {url} (first 500 chars):\n{summary[:500]}...\n")

    # Step 3: Build context and decide
    retrieved_context = "\n\n".join(website_summaries.values())
    print("\nRetrieved context for decision model (first 500 chars):")
    print(retrieved_context[:500] + "...\n")

    research_context = {
        "user_query": user_input,
        "retrieved_content": retrieved_context,
        "searched_terms": list(searched_terms)
    }

    decision_messages = [
        {
            "role": "system",
            "content": (
                "You are a research assistant. Given the research context (provided as JSON) that includes the user's query, "
                "the retrieved summaries from various websites, and the list of search terms already used, decide if further research is needed. "
                "If additional research is required, output valid JSON with 'should_continue': true and 'new_search_terms' listing additional terms to search for. "
                "If enough research is done, output 'should_continue': false, and provide a final answer in 'final_answer', should be at least 600 words, make sure to use all the sources, along with a list of 'sources'. "
                "Ensure your output is valid JSON and adheres exactly to this schema."
            )
        },
        {
            "role": "user",
            "content": json.dumps(research_context)
        }
    ]

    decision_completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=decision_messages,
        response_format=DecisionOutput,
    )
    decision_data = decision_completion.choices[0].message.parsed
    print("\nDecision model parsed output:")
    print(decision_data)

    if not decision_data.should_continue:
        final_answer = decision_data.final_answer or "No answer provided."
        sources = decision_data.sources or []
        print("\nFinal Answer:")
        print(final_answer)
        print("\nSources:")
        for src in sources:
            print(f" - {src}")
        break
    else:
        new_terms = decision_data.new_search_terms or []
        current_search_terms = [term for term in new_terms if term not in searched_terms]
        if not current_search_terms:
            print("No new search terms generated. Ending research loop.")
            break

    iteration += 1

if iteration >= max_loops:
    print("Reached maximum research iterations without a final answer.")