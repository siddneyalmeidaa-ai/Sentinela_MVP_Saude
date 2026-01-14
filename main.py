import streamlit as st
import google.generativeai as genai

# --- 1. COMANDO DE LIMPEZA DE CACHE ---
# Isso força o sistema a esquecer erros anteriores toda vez que carregar
st.cache_data.clear()
st.cache_resource.clear()

# --- 2. VISUAL IA-SENTINELA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="centered")
st.markdown("<style>.main {background-color: #0e1117; color: #00ffcc;}</style>", unsafe_allow_html=True)

# --- 3. CÉREBRO DA IA (COLE SUA NOVA CHAVE ABAIXO) ---
# Use aspas retas: "CHAVE"
API_KEY = "gen-lang-client-0213547701" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Teste de pulso (vácuo)
    model.generate_content("ping")
    st.success("✅ SISTEMA 100% SINCRONIZADO")
except:
    st.error("🔄 Erro técnico: Reinicie o App no menu lateral.")

# --- 4. PAINEL DE COMANDO ---
st.title("🛡️ IA-SENTINELA")

if prompt := st.chat_input("Dê sua ordem operacional..."):
    try:
        res = model.generate_content(f"Responda com ENTRA, NÃO ENTRA ou PULA: {prompt}")
        st.write(f"🛡️ GÊMEA FÊNIX: {res.text}")
    except:
        st.error("Erro na rodada. Verifique a conexão.")

# Botão de download configurado para celular
st.download_button(label="Baixar Relatório", data="Relatorio Operacional", file_name="sentinela.txt")
