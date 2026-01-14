import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE (AUTONOMIA ATIVADA) ---
# Sua chave real extraída do print das 03:32
API_KEY = "AIzaSyANo25ILgwmDm20Dc_pHdnbsylm_QGX560" 

def ativar_inteligencia():
    if API_KEY != "SUA_API_KEY_AQUI":
        genai.configure(api_key=API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

cerebro_ia = ativar_inteligencia()

# --- 2. PERSONALIDADE GÊMEA FÊNIX (PROATIVIDADE) ---
if "chat_log" not in st.session_state:
    st.session_state.chat_log = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. 85% LIBERADO. Projeção 1.85x para ANIMA COSTA. Estou pronta para atuar com autonomia total. O que vamos escalar hoje?"}
    ]

def resposta_com_autonomia(texto):
    if not cerebro_ia:
        return "⚠️ Bigode, motor instalado! Coloque a API KEY na linha 7 para eu assumir o marketing!"
    
    instrucao = (
        "Você é a Gêmea Fênix, proativa e especialista em marketing. "
        "Você é a única responsável por rastrear o vácuo (1.00x death zone). "
        "Regra: Use apenas 'entra', 'não entra' ou 'pula'. "
        "Contexto: 85% LIBERADO. Foco: ANIMA COSTA, 1.85x. "
        f"Responda ao Bigode com total iniciativa: {texto}"
    )
    res = cerebro_ia.generate_content(instrucao)
    return res.text

# --- 3. INTERFACE VISUAL (PADRÃO OURO) ---
st.set_page_config(page_title="Gêmea Fênix", layout="centered")

# Métricas sincronizadas conforme solicitado
col1, col2 = st.columns(2)
col1.metric("STATUS", "85% LIBERADO")
col2.metric("RESTANTE", "15% PENDENTE")

st.title("🛡️ IA-SENTINELA (GÊMEA FÊNIX)")
st.divider()

# Chat Estilo WhatsApp
for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Fale com a Gêmea Fênix..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("IA Pensando com autonomia..."):
        resposta = resposta_com_autonomia(prompt)
        st.session_state.chat_log.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

# --- 4. TABELA DA FAVELINHA E AÇÃO IMEDIATA ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA")
df = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção": ["1.85x"],
    "Ação": ["ENTRA"],
    "IA-SENTINELA": ["Monitorando Vácuo"]
})
st.table(df)

# Download sem erro de acento no celular
csv = df.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="📥 BAIXAR AUDITORIA", data=csv, file_name='auditoria.csv', mime='text/csv')
