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
        background-position: center;
    }}
    /* Cria uma caixa escura para os escritos aparecerem na frente */
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

# --- 2. CÉREBRO DA IA (CHAVE DIRETA NO CÓDIGO) ---
# Usando a sua chave que aparece no print do AI Studio
API_KEY = "AIzaSyANo25ILgwmDm20Dc_pHdnbsylm_QGX560"
genai.configure(api_key=API_KEY)
cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. INTERFACE OPERACIONAL ---
st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")

col1, col2 = st.columns
