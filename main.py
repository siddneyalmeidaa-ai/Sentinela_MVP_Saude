import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. VISUAL (FUNDO ESCURO PADRÃO - SEM IMAGEM) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown(
    """
    <style>
    .main .block-container {
        background-color: #0e1117 !important;
        border-radius: 15px;
        padding: 30px;
        color: #00ffcc !important;
        border: 1px solid #00ffcc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 2. CÉREBRO DA IA (CHAVE VALIDADA) ---
# Sincronizado com a chave final 4_p0 do seu print
API_KEY = "AIzaSyDY_J0MUpYJw_70qBIx8t25KwyW46Y4_p0"

def inicializar_ia():
    try:
        genai.configure(api_key=API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception:
        return None

cerebro_ia = inicializar_ia()

# --- 3. PAINEL OPERACIONAL ---
st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")

col1, col2 = st.columns(2)
col1.metric("STATUS", "100% LIBERADO")
col2.metric("ALVO", "ANIMA COSTA")

if prompt := st.chat_input("Dê sua ordem operacional..."):
    if cerebro_ia:
        try:
            # Protocolo Sidney: Resposta Curta
            instrucao = "Responda apenas com: ENTRA, NÃO ENTRA ou PULA."
            res = cerebro_ia.generate_content(f"{instrucao} Pergunta: {prompt}")
            st.write(f"🛡️ GÊMEA FÊNIX: {res.text}")
        except Exception:
            st.error("🔄 Erro técnico: Tente reiniciar o App no menu lateral.")
    else:
        st.error("⚠️ IA não inicializada. Verifique a chave no GitHub.")
        
