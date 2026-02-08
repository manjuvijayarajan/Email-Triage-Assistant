def decide_action(category):
    if category == "urgent":
        return "auto_reply"
    if category == "promotion":
        return "ignore"
    return "suggest_reply"
