import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE ESTILO (PAPEL BRANCO) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* DOCUMENTO BRANCO SEM CÓDIGO APARECENDO */
    .papel-timbrado {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 25px !important;
        border-radius: 8px;
        border-top: 15px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .tabela-doc { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .tabela-doc th { background: #f2f2f2; color: black; padding: 10px; border-bottom: 2px solid #333; text-align: left; }
    .tabela-doc td { padding: 10px; border-bottom: 1px solid #ddd; color: #333; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS ATUALIZADO ---
dados_medicos = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "list": [{"PAC": "JOAO SILVA", "PROC": "RAIO-X", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "list": [{"PAC": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "list": [{"PAC": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOT": "LAUDO AUSENTE"}]}
}

# Identificação Superior Sidney Almeida
st.markdown(f"<div style='background:#1c232d; padding:
