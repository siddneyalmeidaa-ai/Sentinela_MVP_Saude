import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER (SENTINELA PRO) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 10px; background: #1c232d; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1c2e4a; border-radius: 10px; padding: 5px; }
    .report-preview { 
        background: #f8f9fa; color: #1a1a1a; padding: 20px; 
        border-radius: 8px; font-family: 'Courier New', monospace; 
        font-size: 0.85rem; border: 1px solid #dee2e6; white-space: pre-wrap;
    }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.1rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V17</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS INTELIGENTE (PANDAS) ---
dados_medicos = {
    "ANIMA COSTA": {
        "valor": 16000.0, "motivo": "Divergência de XML", "risco": 15,
        "detalhes": [["João Silva", "XML Inválido"], ["Maria Oliveira", "Divergência Tuss"]]
    },
    "DMMIGINIO GUERRA": {
        "valor": 22500.0, "motivo": "Assinatura Digital", "risco": 45,
        "detalhes": [["João Souza", "Falta Assinatura"], ["Ana Costa", "Falta Assinatura"]]
    },
    "CLÍNICA SÃO JOSÉ": {
        "valor": 45000.0, "motivo": "Erro Cadastral", "risco": 18,
        "detalhes": [["Carlos Luz", "CPF
                      
