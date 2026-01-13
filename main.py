import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE TEMA (MODERNO E COMPACTO PARA CELULAR)
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    /* Estilização dos Cards para ficarem idênticos ao print */
    div[data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: -10px;
    }
    /* Ajuste da cor dos títulos e valores */
    div[data-testid="stMetricLabel"] { color: #8B949E !important; }
    div[data-testid="stMetricValue"] { color: #58A6FF !important; font-weight: bold; }
    
    /* Personalização do Bloco de Decisão */
    .decisao-box {
        background-color: #1a2a1d;
        border: 1px solid #2ea043;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 10px;
    }
    .decisao-texto { color: #39d353; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. IDENTIDADE DO SISTEMA
st.title("🛡️ IA-SENTINELA PRO")
st.caption("Dashboard Executivo | Monitoramento em Tempo Real")

# Sidebar compacta
with st.sidebar:
    st.header("⚙️ Configuração")
    medico = st.selectbox("Clínica", ["ANIMA COSTA", "DR. SILVA", "INTERFILE"])
    valor_input = st.number_input("Valor Rodada", value=2500.0)
    status_input = st.radio("Status", ["LIBERADO", "PENDENTE"])

# 3. MÉTRICAS SINCRONIZADAS (68% vs 32%)
# Valores baseados no seu print real
v_lib = 10880.0
v_pen = 5120.0

st.metric(label="ASSETS LIBERADOS (68%)", value=f"R$ {v_lib:,.2f}")
st.markdown("🟢 <span style='color:#8B949E; font-size:14px;'>Faturamento Ativo</span>", unsafe_allow_html=True)

st.metric(label="PENDÊNCIA OPERACIONAL (32%)", value=f"R$ {v_pen:,.2f}", delta="-32%", delta_color="inverse")
st.markdown("🔴 <span style='color:#8B949E; font-size:14px;'>Risco de Glosa</span>", unsafe_allow_html=True)

# 4. BLOCO DE DECISÃO REFINADO (Q2-2026)
if valor_input <= 1.0:
    st.error("### 🚫 DECISÃO: PULA")
    st.write("⚠️ Vácuo Operacional detectado (1.00x)")
else:
    st.markdown(f"""
        <div class="decisao-box">
            <div class="decisao-texto">DECISÃO: {'ENTRA' if status_input == 'LIBERADO' else 'AGUARDAR'}</div>
            <span style='color:#8B949E;'>✅ Fluxo Seguro para Auditoria</span>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 5. TABELA DA FAVELINHA (CRITICAL AUDIT LOG)
st.subheader("📊 Critical Audit Log (Tabela da Favelinha)")

df = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Analise Atual"],
    "Status": ["PENDENTE", "PENDENTE", status_input],
    "Insight Ativo (Q2)": ["Erro XML - Corrigir", "Divergência TUSS", "Auditoria Sincronizada"]
})

st.dataframe(df, use_container_width=True)

# 6. RODAPÉ EXECUTIVO
st.write("---")
st.caption(f"Operação: {medico} | Criador: Sidney Pereira de Almeida")
