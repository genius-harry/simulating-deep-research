from langchain.text_splitter import CharacterTextSplitter
from openai import OpenAI

def summarize_website_content(content: str, api_key: str) -> str:
    client = OpenAI(api_key=api_key)
    text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=50)
    chunks = text_splitter.split_text(content)
    input_text = "\n\n".join(chunks)
    if len(input_text) > 4000:
        input_text = input_text[:4000]
    summarization_prompt = (
        "Please summarize the following text in approximately 500-600 words:\n\n" + input_text
    )
    messages = [
        {"role": "system", "content": "You are a summarization assistant."},
        {"role": "user", "content": summarization_prompt}
    ]
    summary_completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=messages,
    )
    summary_text = summary_completion.choices[0].message.content.strip()
    if summary_text.startswith("```"):
        summary_text = summary_text.strip("`").strip()
    return summary_text