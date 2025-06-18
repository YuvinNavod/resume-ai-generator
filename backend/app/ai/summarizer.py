from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text: str) -> str:
    if len(text.split()) < 50:
        return text
    summary = summarizer(text, max_length=60, min_length=15, do_sample=False)
    return summary[0]['summary_text']
