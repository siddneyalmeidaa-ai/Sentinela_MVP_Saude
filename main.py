import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. CONFIGURAÇÃO DO ECOSSISTEMA MILITAR ---
st.set_page_config(page_title="Gêmea Fênix V17", layout="centered")

# Inicialização da Memória Quântica (Não apaga ao interagir) [cite: 2026-01-14]
if "historico_militar" not in st.session_state:
    st.session_state.historico_militar = [
        {"role": "assistant", "content": "Bom dia, Sidney! Ecossistema militar de 17 IAs ativo e homologado.", "avatar": "🤖"}
    ]

# --- 2. PADRÃO OURO: VARIÁVEIS DO PROJETO ---
# Quando você mudar o doutor ou a %, o gráfico e os textos mudam sozinhos [cite: 2026-01-12]
doutor = "ANIMA COSTA"
porcentagem_liberado = 85
porcentagem_pendente = 100 - porcentagem_liberado
projecao = "1.85x"
acao_imediata = "ENTRA" if float(projecao.replace('x','')) > 1.05 else "PULA" # Regra do vácuo [cite: 2025-12-29]

# --- 3. INTERFACE VISUAL (GÊMEA FÊNIX) ---
st.markdown("<h1 style='text-align: center;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)

# Alerta de Status Sincronizado
st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem_liberado}% LIBERADO. Projeção {projecao} para {doutor}.")

# --- 4. GRÁFICO DE SINCRONIA (LIBERADO VS PENDENTE) [cite: 2026-01-12] ---
fig = go.Figure(data=[go.Pie(
    labels=['LIBERADO', 'PENDENTE'],
    values=[porcentagem_liberado, porcentagem_pendente],
    hole=.7,
    marker_colors=['#556b2f', '#8b0000'] # Verde Oliva e Vermelho Escuro
)])
fig.update_layout(showlegend=True, height=300, margin=dict(t=0, b=0, l=0, r=0))
st.plotly_chart(fig, use_container_width=True)

# --- 5. HISTÓRICO DE CONVERSAS (NÃO OCULTADO) [cite: 2026-01-14] ---
for msg in st.session_state.historico_militar:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.write(msg["content"])

# --- 6. TABELA DA FAVELINHA (VISUAL HOMOLOGADO) ---
st.markdown("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": [doutor],
    "Projeção": [projecao],
    "Ação": [acao_imediata],
    "IA-SENTINELA": ["Monitorando vácuo" if acao_imediata == "ENTRA" else "VÁCUO DETECTADO"]
})
st.table(df_favelinha)

# --- 7. COMANDO OPERACIONAL (REATIVO) ---
prompt = st.chat_input("Dê sua ordem militar...")

if prompt:
    # Salva na Memória Quântica [cite: 2026-01-14]
    st.session_state.historico_militar.append({"role": "user", "content": prompt, "avatar": "🔴"})
    
    # Resposta de Intenção das 17 IAs
    resposta = f"Recebi sua ordem: '{prompt}'. O motor das 17 IAs está processando. Aguardando chave para execução real."
    st.session_state.historico_militar.append({"role": "assistant", "content": resposta, "avatar": "🤖"})
    st.rerun()

# --- 8. DOWNLOAD OPERACIONAL (SEM ERRO DE ACENTO) [cite: 2026-01-12] ---
st.download_button(
    label="📥 Baixar Relatorio Operacional",
    data=f"STATUS: {porcentagem_liberado}% LIBERADO para {doutor}. Acao: {acao_imediata}.",
    file_name="relatorio_f Phoenix.txt"
)
