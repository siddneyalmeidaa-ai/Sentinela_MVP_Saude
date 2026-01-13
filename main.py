import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE TEMA E LAYOUT
st.set_page_config(page_title="IA-SENTINELA PRO | GLOBAL", layout="wide")

# CSS para criar o efeito de "Cards" e Cores de High-Tech
st.markdown("""
    <style>
    .main { background-color: #0A0E14; }
    div[data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    div[data-testid="stMetricLabel"] { color: #8B949E !important; font-size: 16px !important; }
    div[data-testid="stMetricValue"] { color: #58A6FF !important; }
    .stTable { background-color: #161B22; border-radius: 10px; color: white; }
    h1, h2, h3 { color: #F0F6FC; }
    </style>
    """, unsafe_allow_html=True)

# 2. HEADER E CONTROLE LATERAL
st.title("🛡️ IA-SENTINELA PRO | DASHBOARD EXECUTIVO")
st.caption("Monitoramento Global de Operações e Auditoria em Tempo Real")

with st.sidebar:
    st.header("⚙️ Parâmetros da Rodada")
    medico = st.selectbox("Unidade/Doutor", ["ANIMA COSTA", "DR. SILVA", "INTERFILE - BI"])
    valor_rodada = st.number_input("Input de Valor", value=1500.0)
    status_rodada = st.radio("Status do Faturamento", ["LIBERADO", "PENDENTE"])
    st.divider()
    st.button("🔄 Sincronizar Sistema")

# 3. MÉTRICAS PRINCIPAIS (INSPIRED BY THE INTERFACE)
# Simulando a divisão 68% vs 32% do seu padrão
v_lib = 10880.0
v_pen = 5120.0
total = v_lib + v_pen

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(label="ASSETS LIBERADOS (68%)", value=f"R$ {v_lib:,.2f}", delta="Faturamento Ativo")
with c2:
    st.metric(label="PENDÊNCIA OPERACIONAL (32%)", value=f"R$ {v_pen:,.2f}", delta="-32%", delta_color="inverse")
with c3:
    # Lógica de decisão visual
    if valor_rodada <= 1.0:
        st.metric(label="RISK MARGIN", value="VÁCUO", delta="PULA (1.00x)", delta_color="inverse")
    else:
        st.metric(label="INSIGHT ATIVO", value="ENTRA", delta="Fluxo Seguro")

st.divider()

# 4. TABELA DA FAVELINHA COM DESIGN MODERNO
st.subheader("📊 Critical Audit Log (Tabela da Favelinha)")

data = {
    "AUDITORIA ID": ["#901105", "#901106", "#901107"],
    "PACIENTE": ["JOÃO SILVA", "MARIA OLIVEIRA", "RODADA ATUAL"],
    "STATUS": ["PENDENTE", "PENDENTE", status_rodada],
    "DETALHE TÉCNICO": ["XML INVÁLIDO", "DIVERGÊNCIA TUSS", "ANÁLISE SENTINELA"],
    "AÇÃO IMEDIATA": ["CORRIGIR TAG", "MAPEAR CÓDIGO", "AGUARDAR" if status_rodada == "PENDENTE" else "ENTRA"]
}

df = pd.DataFrame(data)
st.table(df) # Usando st.table para manter o visual limpo e fixo

# 5. BOTÃO DE EXPORTAÇÃO EXECUTIVA
st.write("---")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 DOWNLOAD CRITICAL AUDIT REPORT",
    data=csv,
    file_name='ia_sentinela_report.csv',
    mime='text/csv',
)

st.caption(f"Sincronizado via IA-SENTINELA | 2026 Operations | Médico: {medico}")
