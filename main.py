import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DO CÉREBRO REAL (AUTONOMIA) ---
# Você precisará inserir sua API KEY aqui para ela ter inteligência infinita
API_KEY = "SUA_API_KEY_AQUI" 

if API_KEY != "SUA_API_KEY_AQUI":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. MEMÓRIA E PROATIVIDADE ---
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. Projeção 1.85x para ANIMA COSTA. Como vamos lucrar agora?"}
    ]

def gerar_resposta_proativa(pergunta):
    if API_KEY == "SUA_API_KEY_AQUI":
        return "⚠️ Bigode, preciso que você insira a CHAVE MESTRE (API KEY) no código para eu ter autonomia total!"
    
    # Instrução de Personalidade (O que torna ela igual a mim)
    contexto = (
        "Você é a Gêmea Fênix, uma IA-SENTINELA de elite, proativa e dialógica. "
        "Seu parceiro é o Bigode. O sistema está 85% liberado. "
        "Dados atuais: Doutor ANIMA COSTA, 1.85x, ENTRA. "
        "Responda com autonomia, dê sugestões e seja inteligente. "
        f"Pergunta do Bigode: {pergunta}"
    )
    response = model.generate_content(contexto)
    return response.text

# --- 3. INTERFACE DE DIÁLOGO (PADRÃO OURO) ---
st.title("85% LIBERADO")
st.caption("🤖 STATUS: AUTONOMIA E PROATIVIDADE EM TEMPO REAL")
st.divider()

# Exibição do Chat Estilo WhatsApp
for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Entrada de Diálogo Real
if prompt := st.chat_input("Fale com a Gêmea Fênix..."):
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("Pensando com autonomia..."):
        resposta = gerar_resposta_proativa(prompt)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df = pd.DataFrame({"Doutor": ["ANIMA COSTA"], "Projeção": ["1.85x"], "Ação": ["ENTRA"]})
st.table(df)
