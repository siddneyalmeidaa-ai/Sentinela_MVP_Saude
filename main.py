import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE DESIGN SPA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    .header-box { 
        background: #1c232d; padding: 20px; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    
    /* ESTILO PAPEL TIMBRADO PARA PRINT */
    .timbrado-container {
        background-color: white;
        color: #1a1a1a;
        padding: 45px;
        border-radius: 4px;
        border-top: 20px solid #00d4ff;
        font-family: 'Helvetica', Arial, sans-serif;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin: 10px 0;
    }
    .topo-doc { text-align: center; border-bottom: 2px solid #333; padding-bottom: 15px; margin-bottom: 25px; }
    .linha-dados { border-bottom: 1px solid #eee; padding: 8px 0; display: flex; justify-content: space-between; }
    .secao-titulo { background: #f4f4f4; padding: 5px 10px; margin-top: 20px; font-weight: bold; border-left: 5px solid #00d4ff; }
    .rodape-doc { text-align: center; margin-top: 50px; font-size: 0.7rem; color: #777; border-top: 1px solid #eee; padding-top: 10px; }
    </style>
    
    <div class="header-box">
        <div style="color: white; font-size: 1.1rem;">
            <b>SIDNEY PEREIRA DE ALMEIDA</b><br>
            <span style="color: #00d4ff; font-size: 0.9rem;">DIRETOR OPERACIONAL | IA-SENTINELA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS ATUALIZADA ---
dados_medicos = {
    
