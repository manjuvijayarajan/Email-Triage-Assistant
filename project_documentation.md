# Email Triage Assistant – Project Documentation

## 1. Introduction
The Email Triage Assistant is an AI-powered system designed to automate email management by summarizing email threads, categorizing messages, and generating smart responses.

---

## 2. Problem Statement
Users receive a large number of emails daily, making it difficult to identify important messages. Manual sorting and replying is time-consuming and inefficient.

---

## 3. Objectives
- Automate email classification
- Summarize long email threads
- Suggest appropriate actions
- Improve productivity

---

## 4. System Architecture
The system follows an agent-based pipeline:
Email Thread → Summarizer → Classifier → Decision Agent → Auto Responder → Database

---

## 5. Module Description

### Summarizer
Extracts key information from email threads.

### Classifier
Categorizes emails into Urgent, Normal, or Promotional.

### Agent
Decides the next action based on category.

### Responder
Generates automatic replies.

### Database
Stores processed emails and decisions using SQLite.

---

## 6. Technologies Used
- Python
- Streamlit
- SQLite

---

## 7. How to Run the Project
1. Create a virtual environment  
2. Install dependencies  
3. Run the Streamlit application  

---

## 8. Future Enhancements
- Gmail API integration
- LLM-based responses
- Notification system
