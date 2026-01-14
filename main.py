import streamlit as st
import google.generativeai as genai

# --- 1. COMANDO DE LIMPEZA DE EMERGÊNCIA ---
st.cache_data.clear()
st.cache_resource.clear()

# --- 2. CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="centered")
st.markdown("<style>.main {background-color: #0e1117; color: #00ffcc;}</style>", unsafe_allow_html=True)

# --- 3. CÉREBRO DA IA (COLE SUA NOVA CHAVE AQUI) ---
# Lembre-se: Coloque a chave entre as aspas " "
API_KEY ="gen-lang-client-0387384358" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Teste de conexão silencioso
    model.generate_content("oi")
    status_msg = "✅ SISTEMA 100% LIBERADO"
except:
    status_msg = "❌ Erro: Verifique a Chave e as Aspas"

# --- 4. INTERFACE OPERACIONAL ---
st.title("🛡️ IA-SENTINELA")
st.subheader(f"STATUS: {status_msg}")

if prompt := st.chat_input("Dê sua ordem operacional..."):
    try:
        # Regra de Python para as rodadas
        regra = "Responda apenas com ENTRA, NÃO ENTRA ou PULA. Use a lógica de projeção de rodada."
        res = model.generate_content(f"{regra}: {prompt}")
        st.write(f"🛡️ GÊMEA FÊNIX: {res.text}")
    except:
        st.error("Erro técnico na rodada. Reinicie o App.")

# Botão de download sem erro de acento para celular
st.download_button(
    label="Baixar Relatório Operacional",
    data="Relatorio de Atividades - Sidney Pereira",
    file_name="relatorio_sentinela.txt"
)
