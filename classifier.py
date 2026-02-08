def classify_email(summary):
    summary = summary.lower()
    if "meeting" in summary or "today" in summary:
        return "urgent"
    if "discount" in summary or "offer" in summary:
        return "promotion"
    return "normal"
