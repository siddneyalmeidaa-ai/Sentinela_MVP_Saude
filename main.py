import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER (DESIGN V18) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    /* Blindagem Seletiva: Oculta apenas menus de sistema à direita */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header .st-emotion-cache-15ec66s {display:none;}
    footer {visibility: hidden;}

    /* Design de Cartões e Métricas */
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #00d4ff; font-weight: 800; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #1c232d; border-radius: 5px; color: white; padding: 10px 20px;
    }
    
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 15px; background: linear-gradient(90deg, #1c232d, #0e1117); 
        border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 25px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 3px 10px; border-radius: 4px; font-weight: 900; font-size: 0.8rem; }
    
    .report-box { 
        background: #fdfdfd; color: #1a1a1a; padding: 25px; border-radius:
        
