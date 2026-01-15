import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    .header-box { 
        background: #1c232d; padding: 20px; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #1c2e4a; border-radius: 10px; padding: 5px; }
    .stTabs [data-baseweb="tab"] { color: #8899A6; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #2c3e50 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }
    
    /* ESTILO PAPEL TIMBRADO */
    .timbrado { 
        background: white; color: black; padding: 40px; 
        border-radius: 5px; border-top: 15px solid #00d4ff;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }
    
