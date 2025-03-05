<!-- Badges -->
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/genius-harry/simulating-deep-research)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- Table of Contents -->
## Table of Contents
- [Simulating Deep research](#simulating-deep-research)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Notes](#notes)
  
# Simulating Deep research

This project is a web research tool powered by a Large Language Model (LLM). It enables users to input any research question, then automates web searching, content scraping, and summarization to provide a detailed, comprehensive answer. Built with Python, it integrates APIs such as OpenAI, SerpAPI, and FireCrawl for efficient operation.

## Features

-   **Search:** Performs Google searches via SerpAPI using LLM-generated search terms.
-   **Scrape:** Extracts markdown content from websites using FireCrawl.
-   **Summarize:** Generates 500-600 word summaries of scraped content with OpenAI's GPT-4o.
-   **Iterative Research:** Repeats search, scrape, and summarize steps until sufficient data is collected, guided by a decision model.
-   **Modular Code:** Organized into separate Python files for clarity and maintainability.

## Project Structure
```
📁 simulating-deep-research/
│
├── main.py            # Main script to run the application
├── api_keys.py       # Loads API keys from environment variables
├── search.py        # Handles web searches with SerpAPI
├── scrape.py        # Manages web scraping with FireCrawl
├── summarize.py      # Summarizes content using OpenAI
├── models.py        # Defines Pydantic models for data structure
├── .env             # Stores API keys (not tracked by Git)
├── .gitignore       # Excludes sensitive files from Git
├── requirements.txt   # Lists Python dependencies
└── README.md        # This file
```

## Prerequisites

-   Python 3.11+: Required to run the project.
-   API Keys:
    -   OpenAI API Key ([https://platform.openai.com/](https://platform.openai.com/))
    -   SerpAPI API Key ([https://serpapi.com/](https://serpapi.com/))
    -   FireCrawl API Key ([https://firecrawl.dev/](https://firecrawl.dev/))

## Setup

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/genius-harry/simulating-deep-research.git](https://github.com/genius-harry/simulating-deep-research.git)
    cd simulating-deep-research
    ```

2.  **Install Dependencies:**

    Use pip to install required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**

    Create a `.env` file in the root directory and add your API keys:

    ```
    OPENAI_API_KEY=your_openai_key_here
    SERPAPI_API_KEY=your_serpapi_key_here
    FIRECRAWL_API_KEY=your_firecrawl_key_here
    ```

## Usage

1.  **Launch the Tool:**

    Run the main script:

    ```bash
    python main.py
    ```

2.  **Input a Research Question:**

    Enter any question when prompted, e.g.:

    ```
    Enter your research question: What are the latest advancements in renewable energy?
    ```

3.  **Review the Results:**

    The tool will:

    -   Generate search terms using the LLM.
    -   Search Google and scrape content from top results.
    -   Summarize the content iteratively.
    -   Deliver a final answer (600+ words) with sources.

    Sample output:

    ```
    --- Iteration 1 ---
    Scraping website: [https://example.com](https://example.com)
    Summarizing content for: [https://example.com](https://example.com)
    Summary (first 500 chars): ...

    Final Answer:
    [600+ word summary]
    Sources:
     - [https://example.com/source1](https://example.com/source1)
     - [https://example.com/source2](https://example.com/source2)
    ```

<!-- New note for virtual environments -->
Before installing dependencies, consider using a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

## Troubleshooting

If you encounter issues, check the following:
- Verify that your API keys are correctly set in the .env file.
- Ensure your Python version is 3.11 or higher.
- Check your network connection for API access issues.

## Roadmap

Future enhancements:
- Improve error handling and logging.
- Add more configurable options for iterations.
- Enhance the UI/UX for console interactions.

## How It Works

-   **Search Term Creation:** The LLM crafts relevant search phrases from the user’s question.
-   **Web Search:** SerpAPI retrieves top Google results for each term.
-   **Content Extraction:** FireCrawl scrapes markdown content from websites.
-   **Summarization:** GPT-4o produces 500-600 word summaries per site.
-   **Iteration:** A decision model checks if enough data is collected; if not, it refines search terms and repeats, otherwise compiles a final answer.

## Dependencies

See `requirements.txt` for details:

-   `langchain`
-   `openai`
-   `requests`
-   `pydantic`
-   `python-dotenv`

## Contributing

1.  Fork the repo.
2.  Create a branch (`git checkout -b feature-branch`).
3.  Commit changes (`git commit -m "Add feature"`).
4.  Push to your fork (`git push origin feature-branch`).
5.  Submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Notes

-   Verify API keys are active and have adequate usage limits.
-   Limited to 10 iterations to avoid infinite loops.
-   Outputs may vary due to updates in OpenAI’s GPT-4o model.