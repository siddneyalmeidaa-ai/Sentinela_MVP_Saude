import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- MEMÓRIA QUÂNTICA: SALVAMENTO AUTOMÁTICO ---
if "historico_militar" not in st.session_state:
    st.session_state.historico_militar = [
        {"role": "assistant", "content": "Bom dia, Sidney! Ecossistema militar de 17 IAs ativo.", "avatar": "🤖"}
    ]

# --- VARIÁVEIS DO PROJETO (PADRÃO OURO) ---
doutor = "ANIMA COSTA"
porcentagem = 85
projecao = "1.85x"

# --- INTERFACE VISUAL (GÊMEA FÊNIX) ---
st.markdown("<h1 style='text-align: center;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)

# Alerta de Status Militar
st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem}% LIBERADO. Projeção {projecao} para {doutor}.")

# --- GRÁFICO DE SINCRONIA ---
fig = go.Figure(data=[go.Pie(
    labels=['LIBERADO', 'PENDENTE'],
    values=[porcentagem, 100-porcentagem],
    hole=.7,
    marker_colors=['#556b2f', '#8b0000']
)])
fig.update_layout(showlegend=True, height=300, margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=True)

# --- EXIBIÇÃO DO HISTÓRICO VIVO ---
for msg in st.session_state.historico_militar:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.write(msg["content"])

# --- TABELA DA FAVELINHA ---
st.markdown("### 📋 TABELA DA FAVELINHA")
st.table({"Doutor": [doutor], "Ação": ["ENTRA"], "IA-SENTINELA": ["Monitorando vácuo"]})

# --- CAMPO DE COMANDO OPERACIONAL ---
prompt = st.chat_input("Dê sua ordem militar...")

if prompt:
    st.session_state.historico_militar.append({"role": "user", "content": prompt, "avatar": "🔴"})
    resposta = f"Recebi sua ordem: '{prompt}'. O motor das 17 IAs está pronto, aguardando chave."
    st.session_state.historico_militar.append({"role": "assistant", "content": resposta, "avatar": "🤖"})
    st.rerun()

# --- BOTÃO DE DOWNLOAD ---
st.download_button("📥 Baixar Relatorio Operacional", "Log de Auditoria", "relatorio.txt")
