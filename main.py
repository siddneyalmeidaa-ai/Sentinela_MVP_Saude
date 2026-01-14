import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (IMAGEM ATRÁS, TEXTO NA FRENTE) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/siddneyalmeidaa-ai/Sentinela_MVP_Saude/main/1768384879706.jpg");
        background-attachment: fixed;
        background-size: cover;
    }}
    /* Camada para o texto brilhar na frente da imagem */
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.8) !important;
        border-radius: 20px;
        padding: 30px;
        margin-top: 50px;
        border: 1px solid #00ffcc;
    }}
    .stChatMessage, .stTable, [data-testid="stMetricValue"] {{
        background-color: rgba(15, 15, 15, 0.9) !important;
        color: #00ffcc !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 2. CONEXÃO COM A IA ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Bigode, a chave ainda não foi salva nos Secrets do Streamlit!")
    st.stop()

# --- 3. PAINEL OPERACIONAL ---
st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")

col1, col2 = st.columns(2) # O erro da imagem 13 estava aqui (faltava o 2)
col1.metric("STATUS", "ONLINE")
col2.metric("ALVO", "ANIMA COSTA")

if prompt := st.chat_input("Dê sua ordem..."):
    with st.chat_message("user"):
        st.write(prompt)
    res = cerebro_ia.generate_content(prompt)
    with st.chat_message("assistant"):
        st.write(res.text)
        
