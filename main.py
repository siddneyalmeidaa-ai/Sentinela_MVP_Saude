import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MOBILE MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { display: flex; justify-content: space-between; align-items: center; padding: 5px 10px; color: #00d4ff; font-weight: bold; font-size: 1.0rem; border-bottom: 1px solid #1c2e4a; margin-bottom: 10px; }
    .pro-tag { background-color: #00d4ff; color: #0e1117; font-size: 0.7rem; padding: 2px 6px; border-radius: 4px; font-weight: 900; }
    
    .metric-row { display: flex; justify-content: space-between; background: #1c2e4a; border-radius: 8px; padding: 8px 5px; margin: 10px 0px; }
    .metric-item { text-align: center; flex: 1; border-right: 1px solid #2c3e50; }
    .metric-item:last-child { border-right: none; }
    .m-label { font-size: 0.5rem; color: #8899A6; text-transform: uppercase; }
    .m-value { font-size: 0.8rem; font-weight: bold; color: white; }
    .m-risk { color: #ff4b4b !important; }

    .block-container { padding: 0.5rem 0.5rem !important; }
    header {visibility: hidden;}
    
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

# --- 🧠 BASE DE DADOS DINÂMICA ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML", "perc_risco": 32},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Assinatura Digital", "perc_risco": 32},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Erro Cadastral", "perc_risco": 15}
}

# --- 🔍 SELETOR DINÂMICO ---
medico_sel = st.selectbox("Selecione o Médico para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS EM TEMPO REAL ---
risco_p = info["perc_risco"]
ok_p = 100 - risco_p

v_faturamento = info["valor"]
v_pendente = v_faturamento * (risco_p / 100)
v_liberado = v_faturamento * (ok_p / 100)
tkt_medio = v_faturamento / info["pacientes"]

# --- 📊 MÉTRICAS SUPERIORES ---
st.markdown(f"""
    <div class="metric-row">
        <div class="metric-item"><div class="m-label">VOL. PACIENTES</div><div class="m-value">{info['pacientes']}</div></div>
        <div class="metric-item"><div class="m-label">TICKET</div><div class="m-value">R${tkt_medio:,.0f}</div></div>
        <div class="metric-item"><div class="m-label">PENDENTE</div><div class="m-value m-risk">R${v_pendente:,.0f}</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- 🍕 PIZZA DINÂMICA (NÚMEROS FORA PARA NÃO DESALINHAR) ---
df_p = pd.DataFrame({
    "Status": [f"LIBERADO ({ok_p}%)", f"RISCO ({risco_p}%)"], 
    "Valor": [ok_p, risco_p]
})

st.vega_lite_chart(df_p, {
    'width': 'container',
    'height': 220,
    'mark': {'type': 'arc', 'innerRadius': 50, 'outerRadius': 90, 'cornerRadius': 5},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {
            'field': 'Status', 
            'type': 'nominal', 
            'scale': {'range': ['#00d4ff', '#ff4b4b']},
            'legend': {'orient': 'bottom', 'labelColor': 'white', 'labelFontSize': 12}
        }
    }
})

# --- 🚀 RELATÓRIO FINAL DE AUDITORIA ---
st.markdown(f"**📋 Auditoria: {medico_sel}**")
st.markdown(f'<div class="status-box status-ok">LIBERADO: R$ {v_liberado:,.2f} ({ok_p}%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box status-error">PENDENTE: R$ {v_pendente:,.2f} ({risco_p}%)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="status-box status-info">MOTIVO: {info["motivo"]}</div>', unsafe_allow_html=True)
