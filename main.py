import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MOBILE MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    /* Título Justificado e Compacto */
    .header-box { display: flex; justify-content: space-between; align-items: center; padding: 0px 10px; color: #00d4ff; font-weight: bold; font-size: 1rem; }
    /* Métricas na Horizontal em uma única linha */
    .metric-row { display: flex; justify-content: space-around; background: #1c2e4a; border-radius: 8px; padding: 5px; margin: 5px 0px; }
    .metric-item { text-align: center; color: white; flex: 1; border-right: 1px solid #2c3e50; }
    .metric-item:last-child { border-right: none; }
    .m-label { font-size: 0.55rem; color: #8899A6; text-transform: uppercase; }
    .m-value { font-size: 0.85rem; font-weight: bold; }
    /* Ajuste do container */
    .block-container { padding-top: 0.2rem !important; padding-left: 0.5rem !important; padding-right: 0.5rem !important; }
    /* Esconder elementos padrão do Streamlit para ganhar espaço */
    header {visibility: hidden;}
    </style>
    <div class="header-box"><span>🏛️ IA-SENTINELA PRO</span> <span>VIP</span></div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Erro XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Cadastro"}
}

with st.sidebar:
    medico_sel = st.selectbox("Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento = st.number_input("R$", value=info["valor"])

# --- 📈 CÁLCULOS ---
v_pendente = faturamento * 0.32
v_liberado = faturamento * 0.68
tkt_medio = faturamento / info["pacientes"]

# --- 📊 MÉTRICAS NA HORIZONTAL (HTML PURO PARA JUSTIFICAR) ---
st.markdown(f"""
    <div class="metric-row">
        <div class="metric-item"><div class="m-label">Vol</div><div class="m-value">{info['pacientes']}</div></div>
        <div class="metric-item"><div class="m-label">Ticket</div><div class="m-value">R${tkt_medio:,.0f}</div></div>
        <div class="metric-item" style="color:#ff0055;"><div class="m-label">Risco</div><div class="m-value">R${v_pendente:,.0f}</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- 🍕 PIZZA DONUT ---
df_p = pd.DataFrame({"S": ["RISCO", "OK"], "V": [32, 68]})
st.vega_lite_chart(df_p, {
    'width': 'container', 'height': 150,
    'mark': {'type': 'arc', 'innerRadius': 35, 'outerRadius': 60, 'cornerRadius': 4},
    'encoding': {
        'theta': {'field': 'V', 'type': 'quantitative'},
        'color': {'field': 'S', 'type': 'nominal', 'scale': {'range': ['#ff0055', '#00d4ff']}}
    },
    'config': {'legend': {'orient': 'right', 'labelFontSize': 10}}
})

# --- 🚨 PENDÊNCIAS JUSTIFICADAS ---
st.markdown(f"**📋 Pendentes: {medico_sel}**")
df_p_table = pd.DataFrame({"Paciente": info["pendentes"], "Motivo": [info["motivo"]] * 2})
st.table(df_p_table)

# --- 🚀 BOTÃO ---
if st.button("📊 GERAR DOSSIÊ"):
    st.success(f"Liberado: R$ {v_liberado:,.2f}")
    st.error(f"Bloqueio: {info['motivo']}")
