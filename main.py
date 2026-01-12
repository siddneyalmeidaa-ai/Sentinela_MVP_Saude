import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MOBILE DEFINITIVA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    /* Cabeçalho Justificado Horizontal */
    .header-box { 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        padding: 5px 5px; 
        color: #00d4ff; 
        font-weight: bold; 
        font-size: 1.0rem;
    }
    .vip-tag { 
        background-color: #00d4ff; 
        color: #0e1117; 
        font-size: 0.7rem; 
        padding: 2px 6px; 
        border-radius: 4px; 
        font-weight: 900;
    }
    
    /* Faixa de Métricas Horizontal Justificada */
    .metric-row { 
        display: flex; 
        justify-content: space-between; 
        background: #1c2e4a; 
        border-radius: 8px; 
        padding: 8px 5px; 
        margin: 5px 0px; 
    }
    .metric-item { text-align: center; flex: 1; border-right: 1px solid #2c3e50; }
    .metric-item:last-child { border-right: none; }
    .m-label { font-size: 0.55rem; color: #8899A6; text-transform: uppercase; }
    .m-value { font-size: 0.85rem; font-weight: bold; color: white; }
    .m-risk { color: #ff4b4b !important; }

    /* Ajuste de Margens para eliminar cortes */
    .block-container { padding: 0.5rem 0.5rem !important; }
    header {visibility: hidden;}
    
    /* Tabela Justificada */
    .stTable { width: 100% !important; margin-top: 10px; }
    thead tr th { font-size: 0.7rem !important; color: #00d4ff !important; }
    tbody tr td { font-size: 0.75rem !important; }
    </style>
    
    <div class="header-box">
        <span>🏛️ IA-SENTINELA PRO</span> 
        <span class="vip-tag">VIP</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Divergência de XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Erro Cadastral"}
}

with st.sidebar:
    medico_sel = st.selectbox("Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento = st.number_input("R$", value=info["valor"])

# --- 📈 CÁLCULOS ---
v_pendente = faturamento * 0.32
v_liberado = faturamento * 0.68
tkt_medio = faturamento / info["pacientes"]

# --- 📊 MÉTRICAS NA HORIZONTAL (JUSTIFICADAS) ---
st.markdown(f"""
    <div class="metric-row">
        <div class="metric-item"><div class="m-label">Vol</div><div class="m-value">{info['pacientes']}</div></div>
        <div class="metric-item"><div class="m-label">Ticket</div><div class="m-value">R${tkt_medio:,.0f}</div></div>
        <div class="metric-item"><div class="m-label">Risco</div><div class="m-value m-risk">R${v_pendente:,.0f}</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- 🍕 GRÁFICO DE PIZZA (CENTRALIZAÇÃO TOTAL) ---
df_p = pd.DataFrame({"Status": ["RISCO", "OK"], "Valor": [32, 68]})
st.vega_lite_chart(df_p, {
    'width': 'container', 'height': 170,
    'mark': {'type': 'arc', 'innerRadius': 40, 'outerRadius': 70, 'cornerRadius': 4},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#ff4b4b', '#00d4ff']}}
    },
    'config': {'legend': {'orient': 'right', 'labelFontSize': 10}}
})

# --- 🚨 LISTA DE PENDÊNCIAS ---
st.markdown(f"**📋 Pendências: {medico_sel}**")
st.table(pd.DataFrame({"Paciente": info["pendentes"], "Motivo": [info["motivo"]] * 2}))

# --- 🚀 BOTÃO DE AÇÃO ---
if st.button("📊 GERAR DOSSIÊ ALPHA"):
    st.success(f"Liberado: R$ {v_liberado:,.2f}")
    st.error(f"Bloqueio: {info['motivo']}")
    
