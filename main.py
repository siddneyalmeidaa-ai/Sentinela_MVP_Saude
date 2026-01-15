import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# --- 1. CONFIGURAÇÃO DE AMBIENTE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

# Estilos unificados para evitar "vazamento" de código
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1c232d; border-radius: 5px; color: white; padding: 10px; }
    
    /* ESTILO PAPEL TIMBRADO - BRANCO REAL */
    .papel-branco {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 30px !important;
        border-radius: 8px;
        border-top: 15px solid #00d4ff;
        font-family: sans-serif;
    }
    .tabela-doc { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .tabela-doc th { background: #f0f0f0; padding: 10px; text
    
