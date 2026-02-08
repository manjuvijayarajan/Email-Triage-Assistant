def generate_reply(category):
    if category == "urgent":
        return "Thanks for the update. I will take action immediately."
    if category == "normal":
        return "Thanks for the email. I will get back to you soon."
    return "No reply needed."
