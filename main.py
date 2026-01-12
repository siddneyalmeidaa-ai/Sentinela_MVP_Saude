import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO ULTRA-SLIM ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    /* Título Minimalista */
    .topo-premium { font-size: 1.1rem; font-weight: bold; color: #00d4ff; text-align: center; margin-bottom: 10px; }
    /* Ajuste de métricas para não ocupar espaço vertical */
    [data-testid="stMetricValue"] { font-size: 0.85rem !important; }
    [data-testid="stMetricLabel"] { font-size: 0.55rem !important; }
    div[data-testid="column"] { background: #1c2e4a; border-radius: 8px; padding: 2px !important; text-align: center; }
    /* Zerar paddings que empurram o gráfico para baixo */
    .block-container { padding-top: 0.5rem !important; padding-bottom: 0px !important; }
    /* Tabela compacta para mobile */
    .stTable { font-size: 0.65rem !important; }
    </style>
    <div class="topo-premium">🏛️ IA-SENTINELA: AUDITORIA PRO</div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ALPHA ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Erro XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Cadastro"}
}

with st.sidebar:
    medico_sel = st.selectbox("Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento = st.number_input("R$", value=info["valor"])

# --- 📈 CÁLCULOS DINÂMICOS ---
v_pendente = faturamento * 0.32
v_liberado = faturamento * 0.68
tkt_medio = faturamento / info["pacientes"]

# --- 📊 MÉTRICAS EM LINHA ÚNICA (SLIM) ---
c1, c2, c3 = st.columns(3)
c1.metric("VOL", f"{info['pacientes']}")
c2.metric("TKT", f"R${tkt_medio:,.0f}")
c3.metric("RISCO", f"R${v_pendente:,.0f}")

# --- 🍕 PIZZA DONUT (CENTRALIZADA E SEM CORTES) ---
df_p = pd.DataFrame({"Status": ["RISCO (32%)", "OK (68%)"], "V": [32, 68]})

st.vega_lite_chart(df_p, {
    'width': 'container', 'height': 140,
    'mark': {'type': 'arc', 'innerRadius': 35, 'outerRadius': 55, 'cornerRadius': 3},
    'encoding': {
        'theta': {'field': 'V', 'type': 'quantitative'},
        'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#ff0055', '#00d4ff']}}
    },
    'config': {'legend': {'orient': 'bottom', 'labelFontSize': 8, 'symbolSize': 30}}
})

# --- 🚨 FOCO EM AÇÃO: LISTA DE PENDÊNCIAS ---
st.markdown(f"**📋 Pendências: {medico_sel}**")
st.table(pd.DataFrame({"Paciente": info["pendentes"], "Motivo": [info["motivo"]] * 2}))

# --- 🚀 RELATÓRIO EXPRESSO ---
if st.button("📊 GERAR DOSSIÊ"):
    st.success(f"Liberado: R$ {v_liberado:,.2f}")
    st.error(f"Bloqueio: {info['motivo']}")
