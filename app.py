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
        model="gpt-4o",
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
API_DISABLED = False 

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
    st.info("Contact the developer (Atharv (9511274546) for a private demonstration.")
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
