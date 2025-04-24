# 🔍 Web Research Agent

This project is a simple AI-based research assistant that mimics web browsing and summarizing. It uses `Streamlit` for the front end and `transformers`, `requests`, `bs4`, and `SerpAPI` to simulate web research and summarization

---

## 📌 Features

- Accepts natural language queries
- Performs web search via SerpAPI
- Scrapes text from real web pages
- Summarizes content using HuggingFace Transformers
- Interactive Streamlit UI

---

## 📁 Project Structure

```
web-research-agent/
│
├── streamlit_app.py          # Streamlit UI
├── main.py                   # Orchestrates the agent logic
│
├── tools/
│   ├── search.py             # Web search via SerpAPI
│   ├── scraper.py            # Scrapes text from a URL
│   └── analyzer.py           # HuggingFace summarizer
│
├── .env                      # Your SerpAPI key
├── requirements.txt          # Project dependencies
```

---

## 🚀 How to Run

```bash
git clone <your-repo-url>
cd web-research-agent

python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows

pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## ✅ Example Output

**Input:**  
`Find recent news on India's space program`

**Output:**  
`ISRO launched Aditya-L1 to study the sun, aiming to better understand solar storms...`

---

## 🧠 Technologies Used

- Python 3
- Streamlit
- HuggingFace Transformers
- SerpAPI (Google Search API)
- BeautifulSoup4

---

## 👨‍💻 Author

**Mallikarjun Sonna**  
📧 mallusonna43@gmail.com

---

## 🧪 Tests

This project includes basic tests to ensure functionality.

Run tests using:

```bash
python -m unittest discover -s tests

