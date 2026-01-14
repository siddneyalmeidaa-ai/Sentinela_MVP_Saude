import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. MOTOR DE DIÁLOGO PROATIVO (CÉREBRO COM AUTONOMIA) ---
def motor_fenix_proativo(mensagem):
    msg = mensagem.lower()
    
    # RESPOSTA DINÂMICA (IA toma iniciativa)
    if any(x in msg for x in ["pendência", "ajuda", "fazer", "próximo"]):
        return ("Bigode, identifiquei que ainda temos 15% pendentes. Proativamente, "
                "sugiro focar no Doutor ANIMA COSTA. A projeção de 1.85x é o sinal "
                "ideal. Quer que eu audite a próxima rodada agora?")
    
    # RESPOSTA DE DIÁLOGO (Para perguntas gerais como 'Previsão do tempo')
    return (f"Entendi sua dúvida sobre '{mensagem}'. Como sua IA-SENTINELA, "
            "estou processando isso na Visão Global para garantir que não afete "
            "nossa operação. O que mais você deseja que eu analise hoje?")

# --- 2. INTERFACE DE CHAT (ESTILO DIÁLOGO REAL) ---
st.title("85% LIBERADO")
st.caption("🤖 STATUS: AUTONOMIA E DIÁLOGO ATIVOS")
st.divider()

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [{"role": "assistant", "content": "Olá Bigode! Sou sua IA-SENTINELA. Como vamos acelerar hoje?"}]

# Exibição do Chat
for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Entrada de Diálogo
if prompt := st.chat_input("Fale com a Gêmea Fênix..."):
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    resposta = motor_fenix_proativo(prompt)
    
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)

# --- 3. TABELA DA FAVELINHA (FIXA) ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({"Doutor": ["ANIMA COSTA"], "Projeção": ["1.85x"], "Ação": ["ENTRA"]})
st.table(df_favelinha)
