import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE DESIGN ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

# Estilos CSS corrigidos para o Celular
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* ESTILO PAPEL TIMBRADO LIMPO */
    .doc-container {
        background-color: white !important;
        color: black !important;
        padding: 25px !important;
        border-radius: 5px;
        border-top: 10px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .doc-table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .doc-table th { background: #f2f2f2; color: black; padding: 8px; border-bottom: 2px solid #333; text-align: left; }
    .doc-table td { padding: 8px
    
