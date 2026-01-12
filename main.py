import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MOBILE MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    /* Cabeçalho de Controle Justificado */
    .header-box { 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        padding: 5px 10px; 
        color: #00d4ff; 
        font-weight: bold; 
        font-size: 1.0rem;
    }
    .pro-tag { background-color: #00d4ff; color: #0e1117; font-size: 0.7rem; padding: 2px 6px; border-radius: 4px; font-weight: 900; }
    
    /* Faixa de Métricas Horizontal */
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
    .m-label { font-size: 0.5rem; color: #8899A6; text-transform: uppercase; }
    .m-value { font-size: 0.8rem; font-weight: bold; color: white; }
    .m-risk { color: #ff4b4b !important; }

    .block-container { padding: 0.5rem 0.5rem !important; }
    header {visibility: hidden;}
    
    /* Tabelas e Caixas de Status */
    .stTable { width: 100% !important; margin-top: 5px; }
    .status-box { padding: 10px; border-radius: 5px; margin-top: 5px; font-weight: bold; font-size: 0.9rem; text-align: center; }
    .status-ok { background-color: #15572422; color: #28a745; border: 1px solid #28a745; }
    .status-error { background-color: #721c2422; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
    
    <div class="header-box">
        <span>🏛️ CONTROLE: IA-SENTINELA</span> 
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ALPHA ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Divergência de XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura Digital"},
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

# --- 📊 MÉTRICAS NA HORIZONTAL ---
st.markdown(f"""
    <div class="metric-row">
        <div class="metric-item"><div class="m-label">VOL. PACIENTES</div><div class="m-value">{info['pacientes']}</div></div>
        <div class="metric-item"><div class="m-label">TICKET</div><div class="m-value">R${tkt_medio:,.0f}</div></div>
        <div class="metric-item"><div class="m-label">PENDENTE</div><div class="m-value m-risk">R${v_pendente:,.0f}</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- 🍕 GRÁFICO COM PORCENTAGEM NO LUGAR CORRETO ---
df_p = pd.DataFrame({
    "Status": ["PENDENTE", "LIBERADO"], 
    "Valor": [32, 68]
})

st.vega_lite_chart(df_p, {
    'width': 'container',
    'height': 190,
    'layer': [
        {
            'mark': {'type': 'arc', 'innerRadius': 45, 'outerRadius': 85, 'cornerRadius': 4},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative'},
                'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#ff4b4b', '#00d4ff']}, 'legend': None}
            }
        },
        {
            'mark': {'type': 'text', 'radius': 65, 'fill': 'white', 'fontWeight': 'bold', 'fontSize': 13},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative', 'stack': True},
                'text': {'field': 'Valor', 'type': 'quantitative', 'format': '.0f', 'suffix': '%'}
            }
        }
    ]
})

# --- 🚨 LISTA DE PENDÊNCIAS ---
st.markdown(f"**📋 Lista de Pendências: {medico_sel}**")
st.table(pd.DataFrame({"Paciente": info["pendentes"], "Motivo": [info["motivo"]] * 2}))

# --- 🚀 RELATÓRIO FINAL DE AUDITORIA ---
st.markdown(f'<div class="status-box status-ok">LIBERADO: R$ {v_liberado:,.2f} (68%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box status-error">PENDENTE: R$ {v_pendente:,.2f} (32%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box" style="border: 1px solid #00d4ff; color: #00d4ff;">MOTIVO: {info["motivo"]}</div>', unsafe_allow_html=True)
