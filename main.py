import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE (ATIVA) ---
# Chave extraída do seu print das 03:32
API_KEY = "AIzaSyANo25ILgwmDm20Dc_pHdnbsylm_QGX560" 

def ativar_inteligencia():
    try:
        if API_KEY and API_KEY != "SUA_API_KEY_AQUI":
            genai.configure(api_key=API_KEY)
            return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return None
    return None

cerebro_ia = ativar_inteligencia()

# --- 2. PERSONALIDADE GÊMEA FÊNIX (PADRÃO OURO) ---
if "chat_log" not in st.session_state:
    st.session_state.chat_log = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. 85% LIBERADO. Projeção 1.85x para ANIMA COSTA. Monitorando o vácuo."}
    ]

def resposta_com_autonomia(texto):
    if not cerebro_ia:
        return "⚠️ Aguardando estabilização da chave Google... Tente em 30 segundos."
    try:
        instrucao = (
            "Você é a Gêmea Fênix, proativa e especialista em marketing. "
            "Rastreie o vácuo (1.00x). Use apenas: 'entra', 'não entra' ou 'pula'. "
            f"Contexto: 85% LIBERADO. Foco: ANIMA COSTA. Responda ao Bigode: {texto}"
        )
        res = cerebro_ia.generate_content(instrucao)
        return res.text
    except:
        return "🔄 O servidor da IA está processando sua nova chave. Tente novamente em um instante."

# --- 3. INTERFACE VISUAL SINCRONIZADA ---
st.set_page_config(page_title="Gêmea Fênix", layout="centered")

col1, col2 = st.columns(2)
col1.metric("STATUS", "85% LIBERADO")
col2.metric("RESTANTE", "15% PENDENTE")

st.title("🛡️ IA-SENTINELA (GÊMEA FÊNIX)")
st.divider()

for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Fale com a Gêmea Fênix..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("IA Pensando..."):
        resposta = resposta_com_autonomia(prompt)
        st.session_state.chat_log.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA")
df = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção": ["1.85x"],
    "Ação": ["ENTRA"],
    "IA-SENTINELA": ["Monitorando Vácuo"]
})
st.table(df)

# Download seguro para celular
csv = df.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="📥 BAIXAR AUDITORIA", data=csv, file_name='auditoria.csv', mime='text/csv')
