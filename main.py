import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (PADRÃO GLOBAL OPERATIONS) ---
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
        /* Estilização para leitura sobre o fundo futurista */
        .stMarkdown, .stTable, .stChatMessage, [data-testid="stMetricValue"], .stChatInput {{
            background-color: rgba(0, 0, 0, 0.8) !important;
            border-radius: 15px;
            padding: 15px;
            color: #00ffcc !important;
        }}
        /* Ajuste para o texto das métricas */
        [data-testid="stMetricLabel"] {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# --- 2. CONFIGURAÇÃO SEGURA (CÉREBRO BLINDADO) ---
# O sistema busca a chave nos 'Secrets' para o GitHub parar de reclamar
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Bigode
             
