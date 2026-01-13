import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE TEMA (PADRÃO OURO - DARK MODE)
st.set_page_config(page_title="IA-SENTINELA PRO | DASHBOARD", layout="wide")

# Estilização CSS para cartões sofisticados (idêntico ao seu print 15:24)
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stMetric {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 12px;
    }
    div[data-testid="stMetricValue"] { color: #58A6FF; font-family: 'Courier New', monospace; }
    .status-card {
        padding: 20px;
        border-radius: 12px;
        background-color: #161B22;
        border-left: 5px solid #00FFCC;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. TÍTULO E IDENTIDADE
st.title("🛡️ IA-SENTINELA PRO")
st.subheader("Dashboard Executivo | Monitoramento em Tempo Real")

# Sidebar - Sincronização de Dados
with st.sidebar:
    st.header("⚙️ Controle Operacional")
    medico = st.selectbox("Selecione a Clínica", ["ANIMA COSTA", "DR. SILVA", "INTERFILE"])
    valor_atual = st.number_input("Valor da Rodada", value=2500.0)
    status_auditoria = st.radio("Status Atual", ["LIBERADO", "PENDENTE"])
    st.divider()
    st.info("Sistema Sincronizado com Q2-2026")

# 3. BLOCO DE MÉTRICAS (VISUAL DO PRINT 15:24)
v_liberado = 10880.0
v_pendente = 5120.0
total = v_liberado + v_pendente
p_lib = int((v_liberado / total) * 100)
p_pen = int((v_pendente / total) * 100)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label=f"ASSETS LIBERADOS ({p_lib}%)", value=f"R$ {v_liberado:,.2f}")
    st.caption("🟢 Faturamento Ativo")

with col2:
    st.metric(label=f"PENDÊNCIA OPERACIONAL ({p_pen}%)", value=f"R$ {v_pendente:,.2f}", delta=f"-{p_pen}%", delta_color="inverse")
    st.caption("🔴 Risco de Glosa")

with col3:
    # Lógica de Decisão (Entra/Pula)
    if valor_atual <= 1.0:
        st.error("### DECISÃO: PULA")
        st.caption("⚠️ Zona de Vácuo Detectada (1.00x)")
    else:
        st.success("### DECISÃO: ENTRA")
        st.caption("✅ Fluxo Seguro para Auditoria")

st.divider()

# 4. TABELA DA FAVELINHA (CRITICAL AUDIT LOG)
st.markdown("### 📊 Critical Audit Log (Tabela da Favelinha)")

data = {
    "ID": ["#901", "#902", "#903"],
    "PACIENTE": ["JOÃO SILVA", "MARIA OLIVEIRA", "ANÁLISE ATUAL"],
    "STATUS": ["PENDENTE", "PENDENTE", status_auditoria],
    "INSIGHT ATIVO (Q2)": ["Erro XML - Corrigir Tag", "Divergência Tuss - Mapear", "Ação Sincronizada"]
}
df_favelinha = pd.DataFrame(data)

st.dataframe(df_favelinha, use_container_width=True)

# 5. EXPORTAÇÃO E RODAPÉ
st.write("---")
csv = df_favelinha.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📦 Exportar Relatório de Auditoria",
    data=csv,
    file_name='ia_sentinela_executivo.csv',
    mime='text/csv',
)

st.caption(f"Unidade: {medico} | IA-SENTINELA Operacional")
