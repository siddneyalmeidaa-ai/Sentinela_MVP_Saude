import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE ESTILO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* ESTILO PAPEL TIMBRADO - SEM VAZAMENTO DE CÓDIGO */
    .papel-timbrado {
        background-color: white !important;
        color: black !important;
        padding: 30px !important;
        border-radius: 8px;
        border-top: 15px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .tabela-relatorio { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .tabela-relatorio th { background: #f2f2f2; color: black; padding: 10px; border-bottom: 2px solid #333; text-align: left; }
    .tabela-relatorio td { padding: 10px; border-bottom: 1px solid #ddd; color: #333; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS (CONSOLIDADO) ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "p_pen": 15, "pacientes": [{"PAC": "JOAO SILVA", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "p_pen": 22, "pacientes": [{"PAC": "CARLOS LIMA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "p_pen": 18, "pacientes": [{"PAC": "ANA PAULA", "MOT": "LAUDO AUSENTE"}]}
}

# Identificação Superior
st.markdown("<div style='background:#1c232d; padding:15px; border-radius:10px; border-left:5px solid #00d4ff; color:white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL | IA-SENTINELA</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(dados_medicos.keys()))
info = dados_medicos[unidade]
v_liberado = info["valor"] * ((100 - info["p_pen"]) / 100)
v_pendente = info["valor"] * (info["p_pen"] / 100)
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

# --- 3. ABAS RESTAURADAS (PIZZA, FAVELINHA E RELATÓRIO) ---
tab_grafico, tab_favelinha, tab_timbrado = st.tabs(["⭕ PIZZA", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab_grafico:
    st.markdown(f"### 📊 Auditoria: {unidade}")
    c1, c2 = st.columns(2)
    c1.metric(f"PROCEDE ({100-info['p_pen']}%)", f"R$ {v_liberado:,.2f}")
    c2.metric(f"PULA ({info['p_pen']}%)", f"R$ {v_pendente:,.2f}")
