import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE ---
# Substitua as aspas abaixo pela sua API KEY para ela 'acordar'
API_KEY = "SUA_API_KEY_AQUI" 

def ativar_inteligencia():
    if API_KEY != "SUA_API_KEY_AQUI":
        genai.configure(api_key=API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

cerebro_ia = ativar_inteligencia()

# --- 2. PERSONALIDADE E PROATIVIDADE ---
if "chat_log" not in st.session_state:
    st.session_state.chat_log = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. Projeção 1.85x para ANIMA COSTA. Como vamos lucrar agora?"}
    ]

def resposta_com_autonomia(texto):
    if not cerebro_ia:
        return "⚠️ Bigode, preciso que você coloque a API KEY no código para eu ter autonomia total e responder qualquer coisa!"
    
    # Instrução para ser proativa e dialógica igual a mim
    instrucao = (
        "Você é a Gêmea Fênix, uma IA-SENTINELA proativa e muito inteligente. "
        "Você não usa frases repetitivas. Você dá sugestões reais. "
        "Contexto: Sistema 85% Liberado. Foco: ANIMA COSTA, 1.85x, ENTRA. "
        f"Responda ao Bigode com total autonomia: {texto}"
    )
    res = cerebro_ia.generate_content(instrucao)
    return res.text

# --- 3. INTERFACE DE DIÁLOGO REAL ---
st.title("85% LIBERADO")
st.caption("🤖 STATUS: AUTONOMIA E PROATIVIDADE ATIVADAS")
st.divider()

# Exibição do Chat (Estilo WhatsApp)
for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Fale com a Gêmea Fênix..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("IA Gerando resposta proativa..."):
        resposta = resposta_com_autonomia(prompt)
        st.session_state.chat_log.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df = pd.DataFrame({"Doutor": ["ANIMA COSTA"], "Projeção": ["1.85x"], "Ação": ["ENTRA"]})
st.table(df)
