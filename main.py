import streamlit as st
import pandas as pd

# --- ESQUELETO MILITAR: MEMÓRIA DE SESSÃO ---
if "historico" not in st.session_state:
    st.session_state.historico = [
        {"role": "assistant", "content": "Bom dia, Sidney! O ecossistema está em modo de espera. Aguardando ignição da chave."}
    ]

# --- CONFIGURAÇÃO OPERACIONAL ---
API_KEY = "COLOQUE_SUA_CHAVE_AQUI"
doutor = "ANIMA COSTA"
porcentagem = 85
projecao = "1.85x"

# --- INTERFACE VISUAL (GÊMEA FÊNIX) ---
st.title("(GÊMEA FÊNIX)")

# Alerta de Status Militar
st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem}% LIBERADO. Projeção {projecao} para {doutor}.")

# Exibição do Histórico de Mensagens
for mensagem in st.session_state.historico:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# --- TABELA DA FAVELINHA ---
st.subheader("📋 TABELA DA FAVELINHA")
st.table({"Doutor": [doutor], "Projeção": [projecao], "Ação": ["ENTRA"], "IA-SENTINELA": ["Monitorando o vácuo"]})

# --- INPUT DE COMANDO COM REAÇÃO ---
prompt = st.chat_input("Dê sua ordem operacional...")

if prompt:
    # Salva e exibe a mensagem do usuário
    st.session_state.historico.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Resposta de Intenção do Sistema
    resposta = f"Recebi sua ordem: '{prompt}'. O motor está pronto, só aguardando a chave para executar."
    st.session_state.historico.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)

# --- BOTÃO DE DOWNLOAD SEM ACENTO ---
st.download_button("Baixar Relatorio Operacional", f"Relatorio: {doutor} - {porcentagem}%", "relatorio.txt")
