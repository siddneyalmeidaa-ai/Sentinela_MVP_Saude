import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL & SEGURANÇA MÁXIMA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

# CSS para ocultar botões da direita e estilizar abas e métricas
st.markdown("""
    <style>
    /* Blindagem: Oculta menus de desenvolvedor (direita) */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header .st-emotion-cache-15ec66s {display:none;}
    footer {visibility: hidden;}

    /* Design VIP */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 15px; background: linear-gradient(90deg, #1c232d, #0e1117); 
        border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 25px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 3px 10px; border-radius: 4px; font-weight: 900; font-size: 0.8rem; }
    [data-testid="stMetricValue"] { color: #00d4ff !important; font-size: 1.8rem !important; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.2rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V21 - BLINDADO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS SINCRONIZADA ---
dados_medicos = {
    "ANIMA COSTA": {
        "total": 16000.0,
        "pacientes": [
            {"nome": "João Silva", "motivo": "XML Inválido"},
            {"nome": "Maria Oliveira", "motivo": "Divergência Tuss"}
        ]
        
