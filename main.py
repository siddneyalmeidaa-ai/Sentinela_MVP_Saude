import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MOBILE MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { display: flex; justify-content: space-between; align-items: center; padding: 5px 10px; color: #00d4ff; font-weight: bold; font-size: 1.0rem; border-bottom: 1px solid #1c2e4a; margin-bottom: 10px; }
    .pro-tag { background-color: #00d4ff; color: #0e1117; font-size: 0.7rem; padding: 2px 6px; border-radius: 4px; font-weight: 900; }
    
    /* Faixa de Métricas Horizontal */
    .metric-row { display: flex; justify-content: space-between; background: #1c2e4a; border-radius: 8px; padding: 8px 5px; margin: 10px 0px; }
    .metric-item { text-align: center; flex: 1; border-right: 1px solid #2c3e50; }
    .metric-item:last-child { border-right: none; }
    .m-label { font-size: 0.5rem; color: #8899A6; text-transform: uppercase; }
    .m-value { font-size: 0.8rem; font-weight: bold; color: white; }
    .m-risk { color: #ff4b4b !important; }

    .block-container { padding: 0.5rem 0.5rem !important; }
    header {visibility: hidden;}
    
    /* Caixas de Relatório Final */
    .status-box { padding: 12px; border-radius: 5px; margin-top: 6px; font-weight: bold; font-size: 0.9rem; text-align: center; }
    .status-ok { background-color: #15572422; color: #28a745; border: 1px solid #28a745; }
    .status-error { background-color: #721c2422; color: #ff4b4b; border: 1px solid #ff4b4b; }
    .status-info { background-color: #0c546022; color: #00d4ff; border: 1px solid #00d4ff; }
    </style>
    
    <div class="header-box">
        <span>🏛️ CONTROLE: IA-SENTINELA</span> 
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS SINCRONIZADA ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Divergência de XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura Digital"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Erro Cadastral"}
}

# --- 🔍 BUSCA DE MÉDICOS (RESTAURADA) ---
medico_sel = st.selectbox("Selecione o Médico para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS ---
v_pendente = info["valor"] * 0.32
v_liberado = info["valor"] * 0.68
tkt_medio = info["valor"] / info["pacientes"]

# --- 📊 MÉTRICAS JUSTIFICADAS ---
st.markdown(f"""
    <div class="metric-row">
        <div class="metric-item"><div class="m-label">VOL. PACIENTES</div><div class="m-value">{info['pacientes']}</div></div>
        <div class="metric-item"><div class="m-label">TICKET</div><div class="m-value">R${tkt_medio:,.0f}</div></div>
        <div class="metric-item"><div class="m-label">PENDENTE</div><div class="m-value m-risk">R${v_pendente:,.0f}</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- 🍕 PIZZA COM % SINCRONIZADO ---
df_p = pd.DataFrame({
    "Status": ["LIBERADO", "PENDENTE"], 
    "Valor": [68, 32],
    "Label": ["68%", "32%"]
})

st.vega_lite_chart(df_p, {
    'width': 'container',
    'height': 200,
    'layer': [
        {
            'mark': {'type': 'arc', 'innerRadius': 45, 'outerRadius': 85},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative', 'stack': True},
                'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}, 'legend': None}
            }
        },
        {
            'mark': {'type': 'text', 'radius': 65, 'fill': 'white', 'fontWeight': 'bold', 'fontSize': 14},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative', 'stack': True},
                'text': {'field': 'Label', 'type': 'nominal'}
            }
        }
    ]
})

# --- 🚨 LISTA DE PENDÊNCIAS ---
st.markdown(f"**📋 Pendências: {medico_sel}**")
st.table(pd.DataFrame({"Paciente": info["pendentes"], "Motivo": [info["motivo"]] * 2}))

# --- 🚀 RELATÓRIO DE SINCRONIZAÇÃO (PADRÃO INICIAL) ---
st.markdown(f'<div class="status-box status-ok">LIBERADO: R$ {v_liberado:,.2f} (68%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box status-error">PENDENTE: R$ {v_pendente:,.2f} (32%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box status-info">MOTIVO: {info["motivo"]}</div>', unsafe_allow_html=True)
