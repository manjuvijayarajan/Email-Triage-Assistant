def summarize_thread(emails):
    text = " ".join([mail["body"] for mail in emails])
    return text[:200]
