from summarizer import summarize_thread
from classifier import classify_email
from agent import decide_action
from responder import generate_reply

def process_thread(thread):
    summary = summarize_thread(thread["emails"])
    category = classify_email(summary)
    action = decide_action(category)
    reply = generate_reply(category)

    return {
        "thread_id": thread["thread_id"],
        "summary": summary,
        "category": category,
        "action": action,
        "reply": reply
    }
