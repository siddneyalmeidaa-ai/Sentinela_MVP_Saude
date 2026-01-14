import streamlit as st
import google.generativeai as genai

# --- 1. VISUAL IA-SENTINELA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="centered")
st.markdown("<style>.main {background-color: #0e1117; color: #00ffcc;}</style>", unsafe_allow_html=True)

# --- 2. CÉREBRO DA IA (COLE SUA NOVA CHAVE ABAIXO) ---
# Substitua o texto entre as aspas pela chave que você criou agora pouco
API_KEY = AIzaSyBpojt9HBHKtXV7iEMENlrRDV_aJljs38c
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Erro na chave API: Verifique se colou corretamente.")

# --- 3. PAINEL DE COMANDO ---
st.title("🛡️ IA-SENTINELA")
st.subheader("STATUS: 100% LIBERADO")

# --- 4. LÓGICA DE DECISÃO (ENTRA / NÃO ENTRA / PULA) ---
if prompt := st.chat_input("Dê sua ordem operacional..."):
    try:
        # Comando configurado conforme sua regra de Python salva
        regra = "Responda apenas com ENTRA, NÃO ENTRA ou PULA. Use a lógica de projeção de rodada."
        res = model.generate_content(f"{regra}: {prompt}")
        st.write(f"🛡️ GÊMEA FÊNIX: {res.text}")
    except Exception as e:
        st.error("🔄 Erro técnico: Tente reiniciar o App no menu lateral.")

# --- 5. DOWNLOAD SEM ERRO DE ACENTO (PARA CELULAR) ---
# Configurado para não dar erro de codificação no Android
st.download_button(
    label="Baixar Relatório Operacional",
    data="Relatorio de Atividades - Sidney Pereira",
    file_name="relatorio_sentinela.txt",
    mime="text/plain"
)
