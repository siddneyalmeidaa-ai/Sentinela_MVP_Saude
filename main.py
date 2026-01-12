import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MOBILE MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { display: flex; justify-content: space-between; align-items: center; padding: 5px 10px; color: #00d4ff; font-weight: bold; font-size: 0.9rem; border-bottom: 1px solid #1c2e4a; }
    .pro-tag { background-color: #00d4ff; color: #0e1117; font-size: 0.6rem; padding: 2px 5px; border-radius: 4px; font-weight: 900; }
    
    .metric-row { display: flex; justify-content: space-between; background: #1c2e4a; border-radius: 8px; padding: 5px; margin: 8px 0px; }
    .metric-item { text-align: center; flex: 1; border-right: 1px solid #2c3e50; }
    .metric-item:last-child { border-right: none; }
    .m-label { font-size: 0.45rem; color: #8899A6; text-transform: uppercase; }
    .m-value { font-size: 0.75rem; font-weight: bold; color: white; }
    .m-risk { color: #ff4b4b !important; }

    .block-container { padding: 0.3rem 0.5rem !important; }
    header {visibility: hidden;}
    
    .status-box { padding: 10px; border-radius: 5px; margin-top: 5px; font-weight: bold; font-size: 0.8rem; text-align: center; }
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
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML", "risco": 32},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Assinatura Digital", "risco": 45},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Erro Cadastral", "risco": 18}
}

# --- 🔍 SELETOR ---
medico_sel = st.selectbox("Selecione o Médico:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS TÉCNICOS ---
perc_risco = info["risco"]
perc_ok = 100 - perc_risco
v_pendente = info["valor"] * (perc_risco / 100)
v_liberado = info["valor"] * (perc_ok / 100)
tkt_medio = info["valor"] / info["pacientes"]

# --- 📊 MÉTRICAS ---
st.markdown(f"""
    <div class="metric-row">
        <div class="metric-item"><div class="m-label">VOL. PACIENTES</div><div class="m-value">{info['pacientes']}</div></div>
        <div class="metric-item"><div class="m-label">TICKET</div><div class="m-value">R${tkt_medio:,.0f}</div></div>
        <div class="metric-item"><div class="m-label">PENDENTE</div><div class="m-value m-risk">R${v_pendente:,.0f}</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- 🍕 PIZZA DINÂMICA (COMPACTA) ---
df_p = pd.DataFrame({
    "Status": [f"LIBERADO ({perc_ok}%)", f"PENDENTE ({perc_risco}%)"], 
    "Valor": [perc_ok, perc_risco]
})

st.vega_lite_chart(df_p, {
    'width': 'container',
    'height': 180,
    'mark': {'type': 'arc', 'innerRadius': 40, 'outerRadius': 75},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {
            'field': 'Status', 
            'type': 'nominal', 
            'scale': {'range': ['#00d4ff', '#ff4b4b']},
            'legend': {'orient': 'bottom', 'labelColor': 'white', 'labelFontSize': 11}
        }
    }
}, use_container_width=True)

# --- 🚀 RELATÓRIO FINAL ---
st.markdown(f"**📋 Auditoria: {medico_sel}**")
st.markdown(f'<div class="status-box status-ok">LIBERADO: R$ {v_liberado:,.2f} ({perc_ok}%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box status-error">PENDENTE: R$ {v_pendente:,.2f} ({perc_risco}%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box status-info">MOTIVO: {info["motivo"]}</div>', unsafe_allow_html=True)
