# 📂 ContextFlow AI

**Goal:** Build an AI chatbot with memory and RAG to handle long conversations efficiently.

---

## 📅 Project Journal - Day 2  
**Focus:** Persistent Storage & State Management  

### ✅ What I Accomplished
- **Data Schema Design:** Created `data/chat_history.json` to store interactions as Q&A pairs.  
- **Storage Logic:** Built `save_memory()` function using Python's `json` module to append new logs.  
- **Retrieval Foundation:** Implemented `load_memory()` to read existing logs into the application.  
- **Bug Fix:** Resolved file-saving issues by ensuring the `data/` directory exists and handling file paths correctly.  

---

### 🧠 Technical Learnings
- **JSON Serialization:** Learned how to convert Python objects into a persistent `.json` file.  
- **Exception Handling:** Managing `json.JSONDecodeError` for empty or corrupted files.  
- **State vs. Storage:** Understanding that saving data (Storage) is different from using data (Context).  

---

### 🔍 Day 2 Observations

| Feature | Observation |
|---------|------------|
| **Data Persistence** | Chat logs remain intact even after stopping and restarting the script. |
| **I/O Overhead** | Writing to a local JSON file is nearly instantaneous. |
| **Memory Sync** | Current Gap: Data is being saved but not yet injected back into the AI's prompt. |
| **Scalability** | As the file grows, a "Rolling Window" or "Summarization" strategy will be needed. |

---

### ❗ Challenges & Missing Features
- **Model Ignorance:** The AI still doesn't "know" what's in the JSON file until we send it back.  
- **Context Loading:** Need logic to pass the last 5–10 messages into the API messages array.  
- **Token Budgeting:** Risk of exceeding token limits if the entire history is sent.  

---

### 🚀 Next Steps (Day 3)
- [ ] **Context Injection:** Modify the chatbot loop to include previous JSON data in the API call.  
- [ ] **Rolling Window Memory:** Implement logic to send only the most recent context.  
- [ ] **RAG Step 1:** Verify if the bot can answer "What did I say earlier?".  

---

## 📂 Project Structure
```text
contextflow-ai/
├── app.py # Main chatbot logic
├── data/
│ └── chat_history.json # 💾 Persistent conversation storage
├── .env # Secure API keys
├── .gitignore # Ignoring venv/ and .env
├── requirements.txt # Project dependencies
└── README.md # Project documentation
