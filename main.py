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
        padding: 5px 10px; 
        color: #00d4ff; 
        font-weight: bold; 
        font-size: 1.1rem;
        border-bottom: 1px solid #1c2e4a;
    }
    .vip-tag { color: #00d4ff; font-size: 0.9rem; border: 1px solid #00d4ff; padding: 2px 8px; border-radius: 5px; }
    
    /* Faixa de Métricas Horizontal Justificada */
    .metric-row { 
        display: flex; 
        justify-content: space-around; 
        background: #1c2e4a; 
        border-radius: 8px; 
        padding: 8px 0px; 
        margin: 10px 0px; 
    }
    .metric-item { text-align: center; flex: 1; border-right: 1px solid #2c3e50; }
    .metric-item:last-child { border-right: none; }
    .m-label { font-size: 0.6rem; color: #8899A6; text-transform: uppercase; margin-bottom: 2px; }
    .m-value { font-size: 0.9rem; font-weight: bold; color: white; }
    .m-risk { color: #ff0055 !important; }

    /* Ajuste Geral de Tela */
    .block-container { padding: 0.5rem 0.7rem !important; }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Ajuste da Tabela para ocupar largura total */
    .stTable { width: 100% !important; font-size: 0.75rem !important; }
    </style>
    <div class="header-box">
        <span>🏛️ IA-SENTINELA PRO</span> 
        <span class="vip-tag">VIP</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ALPHA ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Divergência de XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Erro Cadastral"}
}

with st.sidebar:
    st.title("SISTEMA")
    medico_sel = st.selectbox("Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento = st.number_input("Valor Bruto:", value=info["valor"])

# --- 📈 CÁLCULOS ---
v_pendente = faturamento * 0.32
v_liberado = faturamento * 0.68
tkt_medio = faturamento / info["pacientes"]

# --- 📊 MÉTRICAS NA HORIZONTAL ---
st.markdown(f"""
    <div class="metric-row">
        <div class="metric-item"><div class="m-label">Vol</div><div class="m-value">{info['pacientes']}</div></div>
        <div class="metric-item"><div class="m-label">Ticket</div><div class="m-value">R${tkt_medio:,.0f}</div></div>
        <div class="metric-item"><div class="m-label">Risco</div><div class="m-value m-risk">R${v_pendente:,.0f}</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- 🍕 GRÁFICO DE PIZZA (AJUSTE FINO) ---
df_p = pd.DataFrame({"Status": ["RISCO", "OK"], "Valor": [32, 68]})
st.vega_lite_chart(df_p, {
    'width': 'container', 'height': 160,
    'mark': {'type': 'arc', 'innerRadius': 38, 'outerRadius': 65, 'cornerRadius': 4, 'padAngle': 2},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#ff0055', '#00d4ff']}}
    },
    'config': {'legend': {'orient': 'right', 'labelFontSize': 10, 'symbolSize': 40}}
})

# --- 🚨 LISTA DE PENDÊNCIAS JUSTIFICADA ---
st.markdown(f"**📋 Pendências: {medico_sel}**")
df_final = pd.DataFrame({
    "Paciente": info["pendentes"],
    "Motivo": [info["motivo"]] * len(info["pendentes"])
})
st.table(df_final)

# --- 🚀 AÇÃO FINAL ---
if st.button("📊 GERAR DOSSIÊ ALPHA"):
    st.success(f"Liberado: R$ {v_liberado:,.2f}")
    st.error(f"Bloqueio: {info['motivo']}")
    
