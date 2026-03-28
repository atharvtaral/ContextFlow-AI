# 🤖 ContextFlow AI – End-to-End Gen AI Assistant

## 📝 Business Problem
Employees waste time searching across scattered chat logs and documents.  
**🎯 Objective:** Build an AI assistant that remembers conversations, reads PDFs, and delivers context-aware answers instantly.

---

## 💻 Project Overview
ContextFlow AI is a full-stack Generative AI project that evolved over six days from a simple terminal-based chat to a professional, document-aware RAG (Retrieval-Augmented Generation) system with a **Streamlit UI**.  
The project demonstrates **🧠 vector memory**, **🔍 semantic retrieval**, **📄 multi-modal data integration**, and **🚀 production-grade AI system design**.

---

## 🌐 Live Demo
Experience ContextFlow AI in action!  
[🚀 Launch the Web App](https://contextflow-ai-1232.streamlit.app/) – Try the chat interface, upload PDFs, and explore AI memory retrieval live.

---

<p align="center">
  <img src="architecture.png" width="800" title="Project Architecture">
</p>

## 🎥 Live Demo Architecture
Watch ContextFlow AI in action on YouTube!  
[▶️ Watch on YouTube](https://youtu.be/vVQ5xvr7E8I) – See the chat interface, PDF uploads, and AI memory retrieval in a quick walkthrough.

---

## 📅 Project Timeline & Highlights

### Day 1: Initial Chat Prototype
- **Focus:** Build a basic chat loop using OpenAI GPT API.  
- **Achievements:**  
  - Implemented a simple terminal-based chat.  
  - Stored conversation in JSON for context preservation.  
  - Demonstrated AI can respond with basic memory of previous messages.

**Technical Keywords:** GPT-3.5-turbo, JSON memory, chat loop, session context.

---

### Day 2–3: Context Preservation & Memory Management
- **Focus:** Persistent chat memory across sessions.  
- **Achievements:**  
  - Loaded prior conversation from `chat_history.json`.  
  - Implemented context window of last N messages for coherent responses.  
  - Introduced basic memory management for long-term session continuity.

**Technical Keywords:** Persistent memory, context window, session state, memory optimization.

---

### Day 4: Optimized Memory Handling
- **Focus:** Improve memory retrieval and reduce context redundancy.  
- **Achievements:**  
  - Summarized older chats to prevent token overflow.  
  - Tested memory window scaling (3 → 10 previous messages).  
  - Identified trade-offs between context depth and response latency.

**Technical Keywords:** Memory summarization, context optimization, token management, AI coherence.

---

### Day 5: Scalable RAG with Vector Databases
- **Focus:** Implement ChromaDB for vector memory storage.  
- **Achievements:**  
  - Migrated from JSON to **ChromaDB vector database** for scalable memory.  
  - Verified AI can recall user-specific details across full script restarts.  
  - Implemented fast similarity search using vector embeddings.

**Challenges & Solutions:**  
| Challenge | Solution |
|-----------|---------|
| Cold Start | Handled empty DB gracefully. |
| Duplicate Memory | Prevented redundant entries using vector IDs. |
| Performance Lag | ChromaDB indexing improved query speed vs JSON. |

**Technical Keywords:** Vector DB, embeddings, semantic search, RAG, persistent storage, similarity search.

---

### Day 6: Professional UI & Document-Aware RAG
- **Focus:** Streamlit UI + PDF multi-modal retrieval.  
- **Achievements:**  
  - Developed interactive **Streamlit chat interface** with dynamic sidebar.  
  - Integrated **PDF processing pipeline (PyPDF2)** for document-based RAG queries.  
  - Visualized AI’s memory retrieval in real-time for transparency.  
  - Enhanced retrieval logic: Prioritize PDF content over chat memory for document-specific questions.

**Challenges & Solutions:**  
| Challenge | Root Cause | Solution |
|-----------|------------|---------|
| ModuleNotFoundError | Environment mismatch | Used `python -m streamlit run app.py` |
| Dimension Mismatch | ChromaDB embedding size mismatch | Reset vector DB for new 1536-dim OpenAI embeddings |
| Duplicate Element ID | Multiple Streamlit input calls | Refactored to a single input loop |
| Hallucination / Context Gap | AI suggested wrong locations | Increased `top_k` and reinforced correct memory |
| Memory Blindness | AI missed PDF content | Rewrote query function to handle PDF metadata separately |

**Technical Keywords:** Multi-modal RAG, Streamlit UI, PyPDF2, embeddings, vector search, session_state, source attribution.

---

## 🧠 Technical Learnings
- **Chunking Strategy:** Split PDFs into 1000-character segments to stay within LLM token limits.  
- **State Management:** Used Streamlit `session_state` for persistent chat UI.  
- **Semantic Memory:** Vector DB stores chat and PDF embeddings for accurate retrieval.  
- **Source Attribution:** Tracked whether response came from user chat or uploaded document.  
- **Performance Optimization:** Vector indexing enables sub-second retrieval for thousands of messages.  

---

## 🔍 Key Observations
| Feature | Observation |
|---------|------------|
| UI Responsiveness | Streamlit handles live chat and sidebar memory smoothly. |
| RAG Accuracy | Correctly retrieves technical information from PDFs and chat. |
| User Trust | Sidebar memory visualization shows AI “thinking” process. |

---

## 💡 Project Insight
> "Building an AI is easy; building an AI that remembers correctly, retrieves context efficiently, and explains its sources is the real challenge. Combining Vector Databases, Streamlit UI, and multi-modal RAG creates a production-ready Gen AI system."

---

## 📂 Final Project Structure
```text
contextflow-ai/
├── app.py              # Final Streamlit UI + RAG logic
├── data/
│   └── chroma_db/      # Vector Database (chat + PDF chunks)
├── .env                # OpenAI API Key
├── requirements.txt    # streamlit, PyPDF2, chromadb, openai
└── README.md           # Comprehensive project documentation
