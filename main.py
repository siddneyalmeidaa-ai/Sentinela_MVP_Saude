import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. MOTOR DE INTELIGÊNCIA Q2-2026 ---
def processar_auditoria(valor, status):
    if valor <= 1.0:
        return "PULA", "🔴 VÁCUO OPERACIONAL (1.00x)", "#ff7b72"
    elif status == "PENDENTE":
        return "AGUARDAR", "🟡 PENDÊNCIA TÉCNICA (XML/TUSS)", "#f1e05a"
    else:
        return "ENTRA", "🟢 FLUXO SEGURO - LIBERADO", "#39d353"

# --- 2. CONFIGURAÇÃO DA INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO | WHATSAPP", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] {
        background-color: #161B22; border: 1px solid #30363D;
        border-radius: 12px; padding: 15px;
    }
    .decisao-box {
        padding: 20px; border-radius: 12px;
        text-align: center; margin: 15px 0; border: 2px solid;
    }
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3em;
        background-color: #25D366; color: white; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO")
st.caption("Dashboard de Auditoria | Envio de Insight Ativo")

# Painel Lateral
with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("
    
