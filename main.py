import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. MEMÓRIA QUÂNTICA ---
if "historico_militar" not in st.session_state:
    st.session_state.historico_militar = [
        {"role": "assistant", "content": "Bom dia, Sidney! Ecossistema militar 17 IA calibrado.", "avatar": "🤖"}
    ]

# --- 2. VARIÁVEIS PADRÃO OURO ---
doutor = "ANIMA COSTA"
porcentagem = 85
projecao = "1.85x"

# --- 3. DESIGN DA INTERFACE (GÊMEA FÊNIX) ---
st.markdown("<br>", unsafe_allow_html=True) # Respiro no topo
st.markdown(f"<h1 style='text-align: center;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)

# Alerta de Status
st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem}% LIBERADO. Projeção {projecao} para {doutor}.")

# --- 4. GRÁFICO AJUSTADO (SEM SOBREPOSIÇÃO) ---
fig = go.Figure(data=[go.Pie(
    labels=['LIBERADO', 'PENDENTE'],
    values=[porcentagem, 100-porcentagem],
    hole=.7,
    marker_colors=['#556b2f', '#8b0000'],
    textinfo='percent'
)])
# Ajuste de margens para não cortar a legenda
fig.update_layout(
    showlegend=True, 
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
    height=350, 
    margin=dict(t=20, b=50, l=20, r=20)
)
st.plotly_chart(fig, use_container_width=True)

# --- 5. TABELA DA FAVELINHA (FIXA E VISÍVEL) [cite: 2025-12-29] ---
st.markdown("### 📋 TABELA DA FAVELINHA")
st.table({"Doutor": [doutor], "Ação": ["ENTRA"], "IA-SENTINELA": ["Monitorando vácuo"]})

# --- 6. HISTÓRICO DE CONVERSAS (NAVEGAÇÃO) ---
for msg in st.session_state.historico_militar:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.write(msg["content"])

# --- 7. RODAPÉ REATIVO ---
prompt = st.chat_input("Dê sua ordem militar...")
if prompt:
    st.session_state.historico_militar.append({"role": "user", "content": prompt, "avatar": "🔴"})
    st.session_state.historico_militar.append({"role": "assistant", "content": f"Ordem '{prompt}' recebida pelas 17 IAs.", "avatar": "🤖"})
    st.rerun()

# --- 8. BOTÃO DE DOWNLOAD (BLINDADO) [cite: 2026-01-12] ---
st.download_button("📥 Baixar Relatorio Operacional", "Log de Auditoria", "relatorio.txt")
