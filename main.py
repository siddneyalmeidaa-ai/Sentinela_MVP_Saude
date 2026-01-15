import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE ESTILO BLINDADO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* RELATÓRIO TIMBRADO LIMPO - SEM VAZAMENTO DE CÓDIGO */
    .papel-timbrado {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 30px !important;
        border-radius: 8px;
        border-top: 15px solid #00d4ff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .tabela-fav { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .tabela-fav th { background: #f2f2f2; color: black; padding: 10px; border-bottom: 2px solid #333; text-align: left; }
    .tabela-fav td { padding: 10px; border-bottom: 1px solid #ddd; color: #333; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS (CONSOLIDADO) ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "p_pula": 15, "pacientes": [{"PACIENTE": "JOAO SILVA", "PROC": "RAIO-X", "MOTIVO": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "p_pula": 22, "pacientes": [{"PACIENTE": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOTIVO": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "p_pula": 18, "pacientes": [{"PACIENTE": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOTIVO": "LAUDO AUSENTE"}]}
}

# Cabeçalho Sidney Almeida
st.markdown("<div style='background:#1c232d; padding:15px; border-radius:10px; border-left:5px solid #00d4ff; color:white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL | IA-SENTINELA</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[unidade]
v_entra = info["valor"] * ((100 - info["p_pula"]) / 100)
v_pula = info["
