import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO DE ALTO NÍVEL ---
st.set_page_config(page_title="IA-SENTINELA PRO", page_icon="💎", layout="wide")

# CSS para interface ULTRA-COMPACTA (Mobile First)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    /* Título em linha única e pequeno */
    .topo { font-size: 1.2rem; font-weight: bold; color: #00d4ff; margin-bottom: 5px; }
    /* Métricas Minificadas */
    [data-testid="stMetricValue"] { font-size: 0.9rem !important; color: #ffffff !important; }
    [data-testid="stMetricLabel"] { font-size: 0.6rem !important; }
    [data-testid="stMetric"] { background: #1c2e4a; padding: 5px; border-radius: 10px; }
    /* Remove espaços inúteis */
    .block-container { padding-top: 0.5rem !important; padding-bottom: 0px !important; }
    </style>
    <div class="topo">🏛️ IA-SENTINELA PRO</div>
    """, unsafe_allow_html=True)

# --- 🧠 INTELIGÊNCIA DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Erro XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Cadastro"}
}

# Seleção rápida na barra lateral
with st.sidebar:
    medico_sel = st.selectbox("Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento_real = st.number_input("Valor:", value=info["valor"])

# --- 📈 CÁLCULOS ---
v_pendente = faturamento_real * 0.32
v_liberado = faturamento_real * 0.68
tkt_medio = faturamento_real / info["pacientes"]

# --- 📊 MÉTRICAS EM LINHA ÚNICA ---
c1, c2, c3 = st.columns(3)
c1.metric("PACIENTES", f"{info['pacientes']}")
c2.metric("TKT MÉDIO", f"R${tkt_medio:,.0f}")
c3.metric("RETIDO", f"R${v_pendente:,.0f}", "-32%")

# --- 🍕 PIZZA COMPACTA (POSICIONAMENTO CENTRAL) ---
df_pizza = pd.DataFrame({"Status": ["RISCO (32%)", "LIBERADO (68%)"], "Valor": [32, 68]})

st.vega_lite_chart(df_pizza, {
    'width': 'container', 'height': 150,
    'mark': {'type': 'arc', 'innerRadius': 35, 'outerRadius': 60, 'cornerRadius': 4},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#ff0055', '#00d4ff']}}
    },
    'config': {'legend': {'orient': 'right', 'labelFontSize': 9}}
})

# --- 🚨 LISTA DE PACIENTES (AÇÃO RÁPIDA) ---
st.markdown(f"**📋 Pendentes: {medico_sel}**")
df_p = pd.DataFrame({
    "Paciente": info["pendentes"],
    "Motivo": [info["motivo"]] * len(info["pendentes"])
})
st.table(df_p)

# --- 🚀 BOTÃO ---
if st.button("📊 GERAR DOSSIÊ"):
    st.info(f"Fatia Garantida: R$ {v_liberado:,.2f}")
    st.error(f"Bloqueio Técnico: {info['motivo']}")
    
