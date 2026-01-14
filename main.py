import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. VISUAL (TEXTO NA FRENTE DA IMAGEM) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/siddneyalmeidaa-ai/Sentinela_MVP_Saude/main/1768384879706.jpg");
        background-attachment: fixed;
        background-size: cover;
    }}
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.85) !important;
        border-radius: 20px;
        padding: 40px;
        color: #00ffcc !important;
        border: 1px solid #00ffcc;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 2. CÉREBRO DA IA (CHAVE DIRETA) ---
# Substituindo o erro de "Secrets" pela chave soldada
API_KEY = "AIzaSyANo25ILgwmDm20Dc_pHdnbsylm_QGX560"
genai.configure(api_key=API_KEY)
cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. PAINEL OPERACIONAL ---
st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")

col1, col2 = st.columns(2)
col1.metric("STATUS", "85% LIBERADO")
col2.metric("ALVO", "ANIMA COSTA")

if prompt := st.chat_input("Dê sua ordem operacional..."):
    try:
        # Instrução da Gêmea Fênix (Padrão Ouro)
        instrucao = "Responda apenas com: ENTRA, NÃO ENTRA ou PULA."
        res = cerebro_ia.generate_content(f"{instrucao} Pergunta: {prompt}")
        st.write(f"🛡️ GÊMEA FÊNIX: {res.text}")
    except:
        st.error("🔄 Tentando nova sincronização...")
        
