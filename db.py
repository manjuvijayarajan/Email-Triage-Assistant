import sqlite3

conn = sqlite3.connect("emails.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS email_logs (
    thread_id TEXT,
    summary TEXT,
    category TEXT,
    action TEXT,
    reply TEXT
)
""")

def save_email(data):
    cursor.execute(
        "INSERT INTO email_logs VALUES (?, ?, ?, ?, ?)",
        (data["thread_id"], data["summary"], data["category"], data["action"], data["reply"])
    )
    conn.commit()
