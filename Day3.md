# 🤖 ContextFlow AI

**Day 3: Memory Retrieval & Context Injection**  
*Closing the gap between storage and intelligence. Today, the AI officially "remembered" who the user is.*

---

## 📅 Project Journal - Day 3  
**Focus:** Implementing Retrieval-Augmented Generation (RAG) Step 1  

### ✅ What I Accomplished
- **Retrieval Logic:** Developed a keyword-matching algorithm to scan `chat_history.json` for relevant past interactions.  
- **Context Augmentation:** Successfully injected retrieved "question/answer" pairs into the system prompt.  
- **Stateful Conversations:** The chatbot can now recall specific details (like Name and Interests) across different sessions.  
- **Bug Fixing:** Resolved a critical `KeyError: 'user'` by aligning the Python code with the existing JSON schema.  

---

### 🧠 Technical Learnings
- **Prompt Engineering:** Learned how to structure "Context + Current Question" so the LLM prioritizes history.  
- **Keyword-Based Search:** Basics of information retrieval using Python’s `any()` and `.split()` methods.  
- **Schema Consistency:** Importance of matching JSON keys (`user` / `assistant`) across all functions.  

---

### 🔍 Day 3 Observations

| Feature | Observation |
|---------|------------|
| **Memory Recall** | Bot successfully identified the user's name ("Atharv") from a previous session. |
| **Context Window** | Implemented "Last 3 relevant chats" to keep prompt concise and cost-effective. |
| **Stability** | `try-except` and `.get()` methods now prevent crashes due to missing data. |
| **Logic** | Major win: The bot is no longer stateless—it has functional long-term memory. |

---

### 💡 Key Insight
> "Retrieval-Augmented Generation isn't just about storing data; it's about contextually 'reminding' the AI of the user's intent before it speaks."

---

### ❗ Challenges & Missing Features
- **Keyword Limitations:** Search only works if the user uses similar words; retrieval may fail if phrasing changes.  
- **Token Growth:** As history grows, simple JSON reading becomes slower and more expensive.  
- **Lack of Semantic Search:** System doesn’t "understand" meaning yet—it only matches text.  

---

### 🚀 Next Steps (Day 4)
- [ ] **Vector Embeddings:** Research and implement semantic search.  
- [ ] **Summarization:** Summarize older conversations to save space and tokens.  
- [ ] **Advanced RAG:** Upgrade from flat JSON to a more robust memory structure (e.g., vector DB).  

---

### 📂 Project Structure
```text
contextflow-ai/
├── app.py # Main logic (Updated with Retrieval & Context logic)
├── data/
│ └── chat_history.json # 💾 Local Database (growing with every chat)
├── .env
├── .gitignore
└── requirements.txt
