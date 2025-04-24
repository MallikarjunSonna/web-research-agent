# 📚 Project Documentation: Web Research Agent

## 1. Agent Structure

The Web Research Agent is divided into three major parts:

- **Search (search.py):** Uses SerpAPI to get real-time search results.
- **Scraper (scraper.py):** Extracts raw text from result URLs using `requests` and `BeautifulSoup`.
- **Analyzer (analyzer.py):** Uses HuggingFace Transformers to summarize long-form text.

The logic is orchestrated in `main.py` and served via a Streamlit interface in `streamlit_app.py`.

---

## 2. Prompt & Design Logic

We don’t use OpenAI prompts. Instead:

- The app accepts natural queries (e.g., "Recent ISRO missions").
- It fetches search results using SerpAPI.
- Scraped content is passed to HuggingFace's summarization pipeline (transformers).
- Only readable, long-paragraph content is considered for summarization.

---

## 3. External Tools

- **SerpAPI**: Acts as a Google Search API. Requires a secret API key stored in `.env`.
- **HuggingFace Transformers**: Provides summarization models (like `t5-small`).
- **BeautifulSoup**: Used for parsing HTML and extracting readable text.
- **Streamlit**: Provides the front-end UI.

---

## 4. Error Handling

- Handles broken URLs gracefully (logs and skips).
- Catches SerpAPI quota issues or invalid API keys.
- Uses try-except blocks to catch runtime failures like scraping or summarization errors.
- UI provides fallback messages like "Could not fetch result."

---

## 5. How to Extend

You can:
- Plug in OpenAI for advanced summarization.
- Add support for multi-lingual summarization.
- Extend to return bullet points or source links.
- Cache results to avoid repeated API hits.
