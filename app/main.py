import streamlit as st
import time
import sys
import os


# =========================
# MUST BE FIRST STREAMLIT CALL
# =========================
st.set_page_config(
    page_title="AETHER SPACE",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# IMPORT PATH FIX
# =========================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pipeline.rag_pipeline import ingest_data, rag_chat


# =========================
# STATE
# =========================
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "ingested" not in st.session_state:
    st.session_state.ingested = False


# =========================
# 🌌 INTRO SCREEN (RUN ONCE)
# =========================
if not st.session_state.loaded:

    st.markdown("""
    <style>

    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        animation: pulseBG 6s infinite alternate;
    }

    @keyframes pulseBG {
        0% { filter: brightness(1); }
        100% { filter: brightness(1.15); }
    }

    .intro {
        height: 90vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        animation: fadeIn 1.2s ease-in-out;
    }

    .logo {
        font-size: 52px;
        font-weight: 800;
        color: #60a5fa;
        text-shadow: 0 0 20px rgba(96,165,250,0.7);
        animation: glow 2s infinite alternate;
        letter-spacing: 2px;
    }

    .sub {
        margin-top: 12px;
        font-size: 14px;
        color: #94a3b8;
        overflow: hidden;
        white-space: nowrap;
        border-right: 2px solid #60a5fa;
        width: 0;
        animation: typing 3s steps(40, end) forwards, blink 0.8s infinite;
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px #3b82f6; }
        to { text-shadow: 0 0 35px #60a5fa; }
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: scale(0.98);}
        to {opacity: 1; transform: scale(1);}
    }

    @keyframes typing {
        from { width: 0; }
        to { width: 320px; }
    }

    @keyframes blink {
        50% { border-color: transparent; }
    }

    </style>

    <div class="intro">
        <div class="logo">⚡ AETHER SPACE</div>
        <div class="sub">Initializing AI Knowledge Engine...</div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)
    st.session_state.loaded = True
    st.rerun()


# =========================
# 🎨 MAIN UI STYLING
# =========================
st.markdown("""
<style>

/* background */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

/* center container */
.block-container {
    max-width: 800px;
    margin: auto;
    padding-top: 2rem;
}

/* chat bubbles 3D */
[data-testid="stChatMessage"] {
    background: rgba(30, 41, 59, 0.7);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 12px;
    margin-bottom: 12px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    backdrop-filter: blur(10px);
    transition: 0.25s ease;
}

[data-testid="stChatMessage"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
}

/* floating input */
div[data-testid="stChatInput"] {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 50%;
    background: rgba(15, 23, 42, 0.8);
    border-radius: 14px;
    padding: 8px;
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
}

/* buttons */
.stButton button {
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    color: white;
    border: none;
    font-weight: 600;
    transition: 0.2s;
}

.stButton button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 20px rgba(99,102,241,0.5);
}

/* title */
h1 {
    text-align: center;
    color: #60a5fa;
}

</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR (INGEST ONLY)
# =========================
with st.sidebar:

    st.title("📁 Knowledge Base")

    uploaded_files = st.file_uploader(
        "Upload PDFs / CSVs",
        type=["pdf", "csv"],
        accept_multiple_files=True
    )

    file_type = st.selectbox("File Type", ["pdf", "csv"])

    if st.button("🚀 Ingest Data"):
        if uploaded_files:
            with st.spinner("Building knowledge base..."):
                for file in uploaded_files:
                    ingest_data(file, file_type)

            st.session_state.ingested = True
            st.success("Done! Chat is ready.")
            time.sleep(1)
            st.rerun()

        else:
            st.warning("Please upload files")


# =========================
# AUTO HIDE SIDEBAR AFTER INGESTION
# =========================
if st.session_state.ingested:
    st.markdown(
        "<script>document.body.setAttribute('data-sidebar-state','collapsed');</script>",
        unsafe_allow_html=True
    )


# =========================
# MAIN TITLE
# =========================
st.title("⚡ AETHER SPACE")
st.caption("Your Dark Knowledge Assistant")


# =========================
# CHAT INPUT
# =========================
query = st.chat_input("Ask anything...")

if query:
    with st.spinner("Thinking..."):
        answer, docs = rag_chat(query)
        st.session_state.chat_history.append((query, answer))


# =========================
# CHAT DISPLAY
# =========================
for q, a in st.session_state.chat_history[::-1]:

    with st.chat_message("user"):
        st.write(q)

    with st.chat_message("assistant"):
        st.write(a)