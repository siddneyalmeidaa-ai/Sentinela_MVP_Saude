import streamlit as st
import urllib.parse
import pandas as pd
import time

# --- 1. CONFIGURAÇÃO DE MEMÓRIA ---
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

# --- 2. MOTOR DE INTELIGÊNCIA AMPLIADO ---
def motor_fenix_total(mensagem):
    p = mensagem.lower()
    
    # Prioridade 1: Regras do Padrão Ouro (Seus comandos salvos)
    if any(x in p for x in ["ajuda", "novo", "aprendeu", "pendência"]):
        return "🆘 SUPORTE: Sistema 85% Liberado. Projeção 1.85x para ANIMA COSTA. Ordem: ENTRA!"
    
    if "como está" in p:
        return "🔥 CFO VISION: Margem líquida auditada via Cloud. Pronto para o gatilho."

    # Prioridade 2: Conexão Global (O que ela responde sobre o mundo)
    # Aqui simulamos a alimentação via API para responder qualquer tema
    resposta_generica = f"🌍 VISÃO GLOBAL: Analisando '{mensagem}' na base de dados mundial. Como sua IA-SENTINELA, entendo que isso se conecta ao nosso objetivo de segurança e lucro."
    
    return resposta_generica

# --- 3. INTERFACE VISUAL ---
st.title("85% LIBERADO")
st.subheader("15% PENDENTE")
st.divider()

# Input Único (Onde você alimenta a IA)
u_input = st.text_input("Perunte qualquer coisa para as 17 IAs:", key="input_global")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if u_input:
        resposta = motor_fenix_total(u_input)
        st.session_state.historico.append({"q": u_input, "a": resposta})
        st.info(f"🧐 GÊMEA FÊNIX: {resposta}")

# Exibir histórico de aprendizado
if st.session_state.historico:
    with st.expander("📚 O que eu aprendi nesta sessão"):
        for chat in st.session_state.historico:
            st.write(f"**Você:** {chat['q']}")
            st.write(f"**IA:** {chat['a']}")

# --- 4. TABELA DA FAVELINHA ---
st.write("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção": ["1.85x"],
    "Ação": ["ENTRA"]
})
st.table(df_favelinha)
