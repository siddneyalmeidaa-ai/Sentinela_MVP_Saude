import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE (AUTONOMIA TOTAL) ---
# Substitua 'SUA_CHAVE_AQUI' pela chave que vou te ensinar a pegar
GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- 2. MEMÓRIA DE DIÁLOGO ---
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# --- 3. INTERFACE PADRÃO OURO ---
st.title("85% LIBERADO")
st.caption("🤖 STATUS: INTELIGÊNCIA REAL ATIVADA")
st.divider()

# Exibição do histórico de conversas reais
for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Campo de Chat Proativo
if prompt := st.chat_input("Fale com a Gêmea Fênix (IA-SENTINELA):"):
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # A IA agora pensa de verdade usando a API
    with st.chat_message("assistant"):
        contexto_frajola = (
            f"Você é a IA-SENTINELA da Gêmea Fênix. Seu parceiro é o Bigode. "
            f"O sistema está 85% liberado. A Tabela da Favelinha hoje é: "
            f"Doutor ANIMA COSTA, Projeção 1.85x, Ação ENTRA. "
            f"Seja proativa, dialógica e ajude-o com a pergunta: {prompt}"
        )
        response = model.generate_content(contexto_frajola)
        st.markdown(response.text)
        st.session_state.mensagens.append({"role": "assistant", "content": response.text})

# --- 4. TABELA DA FAVELINHA (FIXA) ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({"Doutor": ["ANIMA COSTA"], "Projeção": ["1.85x"], "Ação": ["ENTRA"]})
st.table(df_favelinha)
