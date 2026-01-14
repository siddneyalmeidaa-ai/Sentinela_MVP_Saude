import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://raw.githubusercontent.com/siddneyalmeidaa-ai/Sentinela_MVP_Saude/main/1768384879706.jpg");
            background-attachment: fixed;
            background-size: cover;
        }}
        .stMarkdown, .stTable, .stChatMessage, [data-testid="stMetricValue"], .stChatInput {{
            background-color: rgba(0, 0, 0, 0.8) !important;
            border-radius: 15px;
            padding: 15px;
            color: #00ffcc !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# --- 2. CONFIGURAÇÃO SEGURA (CÉREBRO) ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Chave não encontrada nos Secrets do Streamlit!")
    st.stop()

# --- 3. INTERFACE OPERACIONAL ---
st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")

col1, col2 = st.columns(2)
col1.metric("STATUS", "85% LIBERADO")
col2.metric("ALVO", "ANIMA COSTA")

if "chat_log" not in st.session_state:
    st.session_state.chat_log = [{"role": "assistant", "content": "🛡️ Sistema Online. Como vamos escalar?"}]

for m in st.session_state.chat_log:
    with st
    
