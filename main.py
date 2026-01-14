import streamlit as st
import google.generativeai as genai

# --- 1. VISUAL IA-SENTINELA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="centered")
st.markdown("<style>.main {background-color: #0e1117; color: #00ffcc;}</style>", unsafe_allow_html=True)

# --- 2. CÉREBRO DA IA ---
# IMPORTANTE: Coloque a chave entre as aspas ""
API_KEY = "AIzaSyAneNQauwI1niX1KRk4TVOW1mRH1NSrLyk" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Erro na chave API: Verifique as aspas e o código.")

# --- 3. PAINEL DE COMANDO ---
st.title("🛡️ IA-SENTINELA")
st.subheader("STATUS: 100% LIBERADO")

if prompt := st.chat_input("Dê sua ordem operacional..."):
    try:
        regra = "Responda apenas com ENTRA, NÃO ENTRA ou PULA. Use a lógica de projeção de rodada."
        res = model.generate_content(f"{regra}: {prompt}")
        st.write(f"🛡️ GÊMEA FÊNIX: {res.text}")
    except Exception as e:
        st.error("🔄 Erro técnico: Reinicie o App no menu lateral.")

st.download_button(
    label="Baixar Relatório Operacional",
    data="Relatorio de Atividades - Sidney Pereira",
    file_name="relatorio_sentinela.txt",
    mime="text/plain"
)
