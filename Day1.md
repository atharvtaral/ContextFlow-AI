# 🤖 ContextFlow AI

> **Day 1: Foundation & API Integration** > A production-level AI system starts here. This project focuses on building a context-aware AI agent from the ground up.

---

## 📅 Project Journal - Day 1
**Focus:** Building the Core Chatbot & Environment Setup

### ✅ What I Accomplished
* **Environment Setup:** Initialized project folder in VS Code and configured a `venv` (virtual environment).
* **Security:** Implemented `python-dotenv` to securely manage API keys via `.env`.
* **Core Development:** Developed the primary logic in `app.py` to interface with the OpenAI API.
* **Milestone:** Successfully executed a functional chatbot loop within the terminal.

### 🧠 Technical Learnings
* **API Integration:** Mastering the input-process-output flow of the OpenAI model.
* **Environment Management:** Understanding why `venv` is critical for dependency isolation.
* **Model Structure:** Analyzing how the model processes and returns JSON response objects.

---

## 🔍 Day 1 Observations
| Feature | Observation |
| :--- | :--- |
| **Performance** | Responses are extremely fast for short-form inputs. |
| **Stability** | API connectivity is highly reliable when configuration is correct. |
| **Architecture** | The current structure is simple but highly scalable. |
| **Memory** | **Critical Gap:** The model currently treats every input independently (Stateless). |

### 💡 Key Insight
> *"AI models do not 'remember' past conversations by default. Context must be manually managed and fed back into the system."*

---

## ❗ Challenges & Missing Features
* **Statelessness:** No conversation history storage.
* **Context Awareness:** The bot cannot reference previous user statements.
* **Data Persistence:** All data is lost once the terminal session ends.

---

## 🚀 Next Steps (Day 2)
- [ ] **Persistent Storage:** Implement auto-saving of Q&A pairs into a `JSON` file.
- [ ] **Memory Logic:** Develop a retrieval system so the bot "remembers" the user.
- [ ] **RAG Foundation:** Begin structuring the Base for Retrieval-Augmented Generation.

---

## 📂 Project Structure
```text
contextflow-ai/
├── app.py              # Main chatbot logic
├── .env                # Secure API keys (Don't upload to GitHub!)
├── .gitignore          # To ignore venv/ and .env
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
