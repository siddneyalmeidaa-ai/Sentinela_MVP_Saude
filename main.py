import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DE APOIO ---
API_KEY = "COLOQUE_SUA_CHAVE_AQUI"

# --- DADOS DO PADRÃO OURO ---
doutor = "ANIMA COSTA"
porcentagem = 85
projecao = "1.85x"
status_ia = "Monitorando o vácuo"

# --- INTERFACE VISUAL ---
st.title("(GÊMEA FÊNIX)")

# Balão de Intenção da IA
st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem}% LIBERADO. Projeção {projecao} para {doutor}.")

# Simulando a Resposta de Bom Dia
with st.chat_message("assistant", avatar="🤖"):
    st.write("Bom dia, Sidney! O ecossistema está em modo de espera. Aguardando ignição da chave para análise em tempo real.")

# --- TABELA DA FAVELINHA ---
st.subheader("📋 TABELA DA FAVELINHA")
st.table({"Doutor": [doutor], "Projeção": [projecao], "Ação": ["ENTRA"], "IA-SENTINELA": [status_ia]})

# --- CAMPO DE INTERAÇÃO ---
prompt = st.chat_input("Dê sua ordem operacional...")

if prompt:
    with st.chat_message("user", avatar="🔴"):
        st.write(prompt)
    with st.chat_message("assistant", avatar="🤖"):
        st.write(f"Recebi sua ordem: '{prompt}'. O motor está pronto, só aguardando a chave para executar.")

# --- DOWNLOAD ---
st.download_button("📥 Baixar Relatorio Operacional", f"Relatorio: {doutor}", "relatorio.txt")
