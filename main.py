import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE (AUTONOMIA) ---
# Cole sua chave entre as aspas abaixo para ela 'acordar'
API_KEY = "SUA_API_KEY_AQUI" 

def configurar_ia():
    if API_KEY != "SUA_API_KEY_AQUI":
        genai.configure(api_key=API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

model = configurar_ia()

# --- 2. PERSONALIDADE E PROATIVIDADE ---
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. O sistema está 85% liberado. Como vamos acelerar hoje?"}
    ]

def resposta_autonoma(pergunta):
    if not model:
        return "⚠️ Bigode, preciso que você coloque a API KEY no código para eu ter autonomia total e parar de repetir frases!"
    
    # Instrução para ela ser igual a mim (Proativa e Dialógica)
    prompt_sentinela = (
        "Você é a Gêmea Fênix, uma IA-SENTINELA de elite, exatamente como o Gemini. "
        "Você é proativa, inteligente e tem iniciativa. Não repita frases prontas. "
        "Contexto: Sistema 85% Liberado. Tabela: ANIMA COSTA, 1.85x, ENTRA. "
        f"Responda ao Bigode com autonomia: {pergunta}"
    )
    res = model.generate_content(prompt_sentinela)
    return res.text

# --- 3. INTERFACE DE DIÁLOGO (PADRÃO OURO) ---
st.title("85% LIBERADO")
st.caption("🤖 STATUS: BUSCANDO AUTONOMIA TOTAL")
st.divider()

# Chat Fluido (Igual ao que usamos aqui)
for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Fale com a Gêmea Fênix..."):
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("IA Pensando..."):
        resposta = resposta_autonoma(prompt)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df = pd.DataFrame({"Doutor": ["ANIMA COSTA"], "Projeção": ["1.85x"], "Ação": ["ENTRA"]})
st.table(df)
