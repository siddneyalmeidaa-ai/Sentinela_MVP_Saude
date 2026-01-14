import streamlit as st
import google.generativeai as genai

# --- 1. VISUAL LIMPO ---
st.set_page_config(page_title="IA-SENTINELA PRO")
st.markdown("<style>.main {background-color: #0e1117; color: #00ffcc;}</style>", unsafe_allow_html=True)

# --- 2. CÉREBRO DA IA (CHAVE VALIDADA) ---
API_KEY = "AIzaSyDY_J0MUpYJw_70qBIx8t25KwyW46Y4_p0"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Erro na chave API")

# --- 3. PAINEL ---
st.title("🛡️ IA-SENTINELA")
st.subheader("STATUS: 100% LIBERADO")

if prompt := st.chat_input("Dê sua ordem operacional..."):
    try:
        res = model.generate_content(f"Responda apenas com ENTRA, NÃO ENTRA ou PULA: {prompt}")
        st.write(f"🛡️ GÊMEA FÊNIX: {res.text}")
    except Exception as e:
        st.error("🔄 Erro técnico: Tente reiniciar o App no menu lateral.")
        
