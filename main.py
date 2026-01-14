import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. CONFIGURAÇÃO DA MEMÓRIA QUÂNTICA ---
# Garante que o histórico não fique oculto e salve tudo
if "historico_militar" not in st.session_state:
    st.session_state.historico_militar = [
        {"role": "assistant", "content": "Bom dia, Sidney! Ecossistema militar de 17 IAs ativo e homologado.", "avatar": "🤖"}
    ]

# --- 2. PADRÃO OURO: VARIÁVEIS DO PROJETO ---
# Sincroniza o gráfico e a tabela automaticamente
doutor = "ANIMA COSTA"
porcentagem_liberado = 85
porcentagem_pendente = 15
projecao = "1.85x"

# --- 3. INTERFACE VISUAL (GÊMEA FÊNIX) ---
st.markdown("<h1 style='text-align: center;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)
st.markdown("---")

# Alerta de Status Militar
st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem_liberado}% LIBERADO. Projeção {projecao} para {doutor}.")

# --- 4. GRÁFICO DE SINCRONIA (LIBERADO VS PENDENTE) ---
# Cria o visual profissional que separa o sucesso do pendente
fig = go.Figure(data=[go.Pie(
    labels=['LIBERADO', 'PENDENTE'],
    values=[porcentagem_liberado, porcentagem_pendente],
    hole=.7,
    marker_colors=['#556b2f', '#8b0000'] # Verde Oliva e Vermelho Escuro
)])
fig.update_layout(showlegend=True, height=300, margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=True)

# --- 5. EXIBIÇÃO DO HISTÓRICO DE CONVERSAS ---
# Mostra as mensagens empilhadas na tela
for msg in st.session_state.historico_militar:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.write(msg["content"])

# --- 6. TABELA DA FAVELINHA (VISUAL HOMOLOGADO) ---
st.markdown("### 📋 TABELA DA FAVELINHA")
st.table({
    "Doutor": [doutor],
    "Projeção": [projecao],
    "Ação": ["ENTRA"],
    "IA-SENTINELA": ["Monitorando vácuo"]
})

# --- 7. COMANDO OPERACIONAL REATIVO ---
# Responde confirmando o recebimento da ordem
prompt = st.chat_input("Dê sua ordem militar...")

if prompt:
    st.session_state.historico_militar.append({"role": "user", "content": prompt, "avatar": "🔴"})
    resposta = f"Recebi sua ordem: '{prompt}'. O motor das 17 IAs está processando. Aguardando chave para execução real."
    st.session_state.historico_militar.append({"role": "assistant", "content": resposta, "avatar": "🤖"})
    st.rerun()

# --- 8. BOTÃO DE DOWNLOAD (LOG DE AUDITORIA) ---
st.download_button("📥 Baixar Relatorio Operacional", "Log de Auditoria Militar", "relatorio.txt")
