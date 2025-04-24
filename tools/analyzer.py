from transformers import pipeline

# Load summarization model
def get_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")





