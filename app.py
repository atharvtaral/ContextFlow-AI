## Dat 1 
# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     response = client.responses.create(
#         model="gpt-4.1-mini",
#         input=user_input
#     )

#     print("AI:", response.output_text)




## DAY 2
# import os
# import json
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# FILE_PATH = "data/chat_history.json"

# # Load memory
# def load_memory():
#     if not os.path.exists(FILE_PATH):
#         return []
#     with open(FILE_PATH, "r") as f:
#         return json.load(f)

# # Save memory
# def save_memory(memory):
#     with open(FILE_PATH, "w") as f:
#         json.dump(memory, f, indent=4)

# memory = load_memory()

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         print("Exiting... Bye!")
#         break

#     # API call (Indented inside while loop)
#     response = client.chat.completions.create(
#         model="gpt-4o-mini", 
#         messages=[{"role": "user", "content": user_input}]
#     )

#     ai_output = response.choices[0].message.content
#     print("AI:", ai_output)

#     # Save conversation (Indented inside while loop)
#     memory.append({
#         "question": user_input,
#         "answer": ai_output
#     })

#     print("Saving memory...")
#     save_memory(memory)
#     print("Saved!")



# import json
# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# import numpy as np

# # .env file load karne (API Key sathi)
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Path set karne
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# MEMORY_FILE = os.path.join(DATA_DIR, "chat_history.json")

# # Ensure 'data' directory exists (Directory nasel tar create karel)
# if not os.path.exists(DATA_DIR):
#     os.makedirs(DATA_DIR)

# # 📂 Load memory with error handling
# def load_memory():
#     if not os.path.exists(MEMORY_FILE):
#         return []
#     try:
#         with open(MEMORY_FILE, "r", encoding="utf-8") as f:
#             data = json.load(f)
#             return data if isinstance(data, list) else []
#     except (json.JSONDecodeError, FileNotFoundError):
#         return []

# # 💾 Save memory safely
# def save_memory(memory):
#     with open(MEMORY_FILE, "w", encoding="utf-8") as f:
#         json.dump(memory, f, indent=4, ensure_ascii=False)

# # 1. Initialization: Start hotana memory load kara
# memory = load_memory()

# print("--- 🚀 ContextFlow AI Started (Type 'exit' to stop) ---")

# while True:
#     user_input = input("You: ")
    
#     if user_input.lower() == 'exit':
#         print("Stopping... Goodbye!")
#         break

#     # 🔍 2. RETRIEVAL STEP: Junya memory madhun relevant data shodhne
#     relevant_chats = []
#     for chat in memory:
#         # Tujhya JSON madhle 'question' key vaprun shodhne
#         old_q = chat.get("question", "").lower()
#         if any(word in old_q for word in user_input.lower().split()):
#             relevant_chats.append(chat)
    
#     # Fakt shevatchya 3 relevant gappa context mhanun ghya
#     relevant_memory = relevant_chats[-3:]

#     # 🏗️ 3. CONTEXT BUILDING: AI la 'athvan' karun denyasathi string banvane
#     context_text = ""
#     if relevant_memory:
#         context_text = "Background Context from past conversations:\n"
#         for chat in relevant_memory:
#             # 'question' ani 'answer' keys vapra
#             context_text += f"- User: {chat.get('question', '')}\n- AI: {chat.get('answer', '')}\n\n"

#     # 📝 4. AUGMENTED PROMPT: Context + Navin Prashna
#     final_prompt = f"""
#     You are a helpful AI assistant with memory capabilities.
#     Below is the relevant history of the conversation. Use it to provide consistent answers.
    
#     {context_text}
    
#     Current User Question: {user_input}
#     """

#     # 🤖 5. GENERATION: OpenAI API call
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": final_prompt}],
#         )

#         ai_response = response.choices[0].message.content
#         print(f"AI: {ai_response}")

#         # 📦 6. STORAGE: Navin interaction 'question' ani 'answer' format madhe save karne
#         memory.append({
#             "question": user_input, 
#             "answer": ai_response
#         })
#         save_memory(memory)
        
#     except Exception as e:
#         print(f"Something went wrong: {e}")


## Day 4

# import json
# import os
# import numpy as np
# from openai import OpenAI
# from dotenv import load_dotenv

# # .env file load karne
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Path set karne
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# MEMORY_FILE = os.path.join(DATA_DIR, "chat_history.json")

# if not os.path.exists(DATA_DIR):
#     os.makedirs(DATA_DIR)

# # --- NEW UTILITY FUNCTIONS FOR DAY 4 ---

# def get_embedding(text):
#     """Text la vector (Numbers) madhe convert karne sathi."""
#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=text
#     )
#     return response.data[0].embedding

# def cosine_similarity(vec1, vec2):
#     """Don vectors madhla 'Arthik' antar mojnya sathi."""
#     v1, v2 = np.array(vec1), np.array(vec2)
#     return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# def retrieve_semantic(user_input, memory, top_k=2):
#     """Semantic similarity chya aadhare relevant history shodhne."""
#     if not memory:
#         return []

#     # Navin input che embedding generate kara
#     input_vector = get_embedding(user_input)
    
#     scored_memory = []
#     for chat in memory:
#         # Fakt embedding aslelya chats madhech shodhly jail
#         if "embedding" in chat:
#             score = cosine_similarity(input_vector, chat["embedding"])
#             scored_memory.append((score, chat))
    
#     # Highest score pramane sort kara
#     scored_memory.sort(key=lambda x: x[0], reverse=True)
#     return [item[1] for item in scored_memory[:top_k]]

# # --- CORE FUNCTIONS ---

# def load_memory():
#     if not os.path.exists(MEMORY_FILE):
#         return []
#     try:
#         with open(MEMORY_FILE, "r", encoding="utf-8") as f:
#             data = json.load(f)
#             return data if isinstance(data, list) else []
#     except (json.JSONDecodeError, FileNotFoundError):
#         return []

# def save_memory(memory):
#     with open(MEMORY_FILE, "w", encoding="utf-8") as f:
#         json.dump(memory, f, indent=4, ensure_ascii=False)

# # 1. Initialization
# memory = load_memory()

# print("--- 🚀 ContextFlow AI (Day 4: Semantic Search) Started ---")

# while True:
#     user_input = input("You: ")
    
#     if user_input.lower() == 'exit':
#         print("Stopping... Goodbye!")
#         break

#     # 🔍 2. SEMANTIC RETRIEVAL: Arthachya aadhare history shodhne
#     relevant_memory = retrieve_semantic(user_input, memory)

#     # 🏗️ 3. CONTEXT BUILDING
#     context_text = ""
#     if relevant_memory:
#         context_text = "Relevant Context from past conversations:\n"
#         for chat in relevant_memory:
#             context_text += f"- User: {chat.get('question', '')}\n- AI: {chat.get('answer', '')}\n\n"

#     # 📝 4. AUGMENTED PROMPT
#     final_prompt = f"""
#     You are an intelligent AI assistant with semantic memory.
#     Use the following historical context to answer the current question if relevant.
    
#     {context_text}
    
#     Current User Question: {user_input}
#     """

#     # 🤖 5. GENERATION
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": final_prompt}],
#         )

#         ai_response = response.choices[0].message.content
#         print(f"AI: {ai_response}")

#         # 📦 6. STORAGE WITH EMBEDDINGS:
#         # Navin interaction sobat tyacha 'Vector' pan save kara
#         print("(Saving semantic memory...)")
#         user_vector = get_embedding(user_input)
        
#         memory.append({
#             "question": user_input, 
#             "answer": ai_response,
#             "embedding": user_vector
#         })
#         save_memory(memory)
        
#     except Exception as e:
#         print(f"Something went wrong: {e}")


## DAY 5

# import os
# import chromadb
# from openai import OpenAI
# from dotenv import load_dotenv

# # 1. Setup & Environment
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # ChromaDB Persistent Storage (He folders create karel)
# # DB 'data/chroma_db' madhe save hoil jyamule JSON chi garaj nahi
# chroma_client = chromadb.PersistentClient(path="./data/chroma_db")
# collection = chroma_client.get_or_create_collection(name="contextflow_memory")

# print("--- 🧠 ContextFlow AI (Day 5: ChromaDB Edition) Started ---")

# # --- FUNCTIONS ---

# def get_embedding(text):
#     """Text che 1536-dimensional vector banavne."""
#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=text
#     )
#     return response.data[0].embedding

# def add_to_db(user_q, ai_a):
#     """Memory ChromaDB madhe save karne."""
#     vector = get_embedding(user_q)
#     # Unique ID banavnyasathi timestamp kiwa count vapru shakto
#     msg_id = str(collection.count() + 1)
    
#     collection.add(
#         ids=[msg_id],
#         embeddings=[vector],
#         metadatas=[{"question": user_q, "answer": ai_a}],
#         documents=[f"User: {user_q} | AI: {ai_a}"]
#     )
#     print("✅ Memory indexed in Vector DB.")

# def retrieve_context(user_input):
#     """Semantic search vaprun relevant gappa shodhne."""
#     query_vector = get_embedding(user_input)
    
#     # ChromaDB swataha similarity calculate karto (No more manual loops!)
#     results = collection.query(
#         query_embeddings=[query_vector],
#         n_results=2 # Top 2 relevant messages
#     )
    
#     context = ""
#     # Results return kartana metadatas madhun data kadhne
#     if results['metadatas'] and results['metadatas'][0]:
#         for meta in results['metadatas'][0]:
#             context += f"User: {meta['question']}\nAI: {meta['answer']}\n\n"
#     return context

# # --- MAIN LOOP ---

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit': break

#     # 1. Retrieve Context from ChromaDB
#     past_context = retrieve_context(user_input)

#     # 2. Build Prompt
#     final_prompt = f"""
#     You are a professional AI Assistant. 
#     Use the following history to maintain context:
#     {past_context}
    
#     Current Question: {user_input}
#     """

#     # 3. Get AI Response
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": final_prompt}]
#         )
#         ai_response = response.choices[0].message.content
#         print(f"AI: {ai_response}")

#         # 4. Save to Vector DB
#         add_to_db(user_input, ai_response)

#     except Exception as e:
#         print(f"Error: {e}")

## Day 6import streamlit as st
import chromadb
from openai import OpenAI
import os
from dotenv import load_dotenv
import PyPDF2
import streamlit as st

# --- Environment Setup ---
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Persistent ChromaDB Setup ---
chroma_client = chromadb.PersistentClient(path="./data/chroma_db")
collection = chroma_client.get_or_create_collection(name="contextflow_memory")

# --- Helper Functions (Execution chya aadhi pahijet) ---

def add_to_memory(user_input, ai_response):
    msg_id = str(collection.count() + 1)
    collection.add(
        documents=[ai_response],
        metadatas=[{"user_input": user_input}],
        ids=[msg_id]
    )

def process_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content
    
    # Text chunks karne (1000 characters each)
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    
    # PDF count for unique IDs
    pdf_session_count = st.session_state.get('pdf_count', 0)
    
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{"source": "uploaded_pdf", "chunk_id": i}],
            ids=[f"pdf_chunk_{pdf_session_count}_{i}"]
        )
    return len(chunks)

def query_ai(user_input, top_k=10):
    # 1. Search in ChromaDB
    results = collection.query(
        query_texts=[user_input],
        n_results=top_k
    )
    
    context_text = ""
    context_used = []
    
    # 2. Extract Data from Results
    if results['documents'] and results['documents'][0]:
        for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
            # Check kara ki source PDF aahe ki Chat
            if meta.get('source') == 'uploaded_pdf':
                label = f"PDF Chunk {meta.get('chunk_id')}"
                context_text += f"[FROM PDF]: {doc}\n\n"
            else:
                label = f"Chat: {meta.get('user_input', 'Past Memory')}"
                context_text += f"[FROM PAST CHAT]: {doc}\n\n"
            
            context_used.append(label)

    # 3. Final Prompt (AI la strict sangne ki context vapra)
    prompt = f"""You are a Gen AI Assistant. Use the provided context to answer the user's question. 
    If the context contains '[FROM PDF]', that is the information from the uploaded document.
    
    CONTEXT:
    {context_text}
    
    USER QUESTION: {user_input}"""
    
    # 4. OpenAI Call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional AI assistant. Always prioritize the provided context to answer."},
            {"role": "user", "content": prompt}
        ]
    )
    
    ai_text = response.choices[0].message.content
    
    # AI cha response memory madhe save kara (Future reference sathi)
    add_to_memory(user_input, ai_text)
    
    return ai_text, context_used

# --- UI Setup ---
st.set_page_config(page_title="ContextFlow AI", page_icon="🤖", layout="wide")
st.title("🤖 ContextFlow AI - Smart RAG Chat")

# =========================================================
# 🛑 KILL SWITCH (API SAFETY CONTROL)
# Set this to True to stop all API calls and show a warning.
# Set this to False to enable the app.
# =========================================================
API_DISABLED = True 

if API_DISABLED:
    st.error("### 🛑 Service Temporarily Suspended")
    st.warning("""
    **Notice to Visitors:**
    Due to high API usage costs and token limits, this live demo has been 
    temporarily paused by the developer. 
    
    You can still explore the **Source Code on GitHub** to understand the 
    RAG architecture and implementation.
    
    *Reason: Budget protection for OpenAI API.*
    """)
    st.info("Contact the developer (Atharv) for a private demonstration.")
    st.stop() # This prevents any further code from running!
# =========================================================

st.title("🤖 ContextFlow AI - Smart RAG Chat")
# ... (pudhcha sarta code: messages, functions, etc.)

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if 'pdf_count' not in st.session_state:
    st.session_state.pdf_count = 0

# --- Sidebar Upload Option ---
with st.sidebar:
    st.header("📂 Document RAG")
    uploaded_file = st.file_uploader("Upload a PDF to chat with it", type="pdf")
    
    if uploaded_file is not None:
        if st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                num_chunks = process_pdf(uploaded_file)
                st.session_state.pdf_count += 1
                st.success(f"PDF processed! {num_chunks} chunks added.")

# --- Chat Interface (Display History) ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input & AI Logic ---
if prompt := st.chat_input("Ask me something..."):
    
    # 1. User Message Display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. AI Response Generation
    with st.chat_message("assistant"):
        ai_response, context_list = query_ai(prompt)
        st.markdown(ai_response)
        
        # 3. Sidebar Refresh (Memory Visualization)
        with st.sidebar:
            st.header("🧠 Neural Memory (RAG)")
            st.write("Context retrieved from database:")
            if context_list:
                for idx, mem in enumerate(context_list, 1):
                    st.info(f"**Source {idx}:** {mem}")
            else:
                st.write("No specific past context used.")

    # 4. Save AI Response
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
