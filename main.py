from tools.search import google_search
from tools.scraper import scrape_text_from_url
from tools.analyzer import get_summarizer

# Load summarizer pipeline
summarizer = get_summarizer()

# Main function that handles the full pipeline
def run_agent(query):
    search_results = google_search(query, num_results=5)
    if not search_results:
        return "❌ No relevant search results found."

    # Go through each search result and try to summarize its content
    for result in search_results:
        url = result.get("link")
        if not url:
            continue

        content = scrape_text_from_url(url)
        if not content:
            continue

        try:
            summary = summarizer(content, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
            return summary
        except:
            continue

    return "❌ Unable to extract content or summarize from any of the search results."