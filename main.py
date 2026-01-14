import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER & BLINDAGEM ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

# Oculta menus de sistema para segurança
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header .st-emotion-cache-15ec66s {display:none;}
    footer {visibility: hidden;}

    /* Design Premium */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 15px; background: linear-gradient(90deg, #1c232d, #0e1117); 
        border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 25px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 3px 10px; border-radius: 4px; font-weight: 900; font-size: 0.8rem; }
    </style>
    <div class="header-box">
        <span style="color: white; font-size: 1.3rem;">🏛️ SISTEMA: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V18 - PREMIUM</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS INTELIGENTE ---
dados_medicos = {
    "ANIMA COSTA": {
        "valor_total": 16000.0,
        "pacientes": [
            {"nome": "João Silva", "erro": "XML Inválido", "peso": 0.5},
            {"nome": "Maria Oliveira", "erro": "Divergência Tuss", "peso": 0.5}
        ]
    },
    "DMMIGINIO GUERRA": {
        "valor_total": 22500.0,
        "pacientes": [
            {"nome": "João Souza", "erro": "Falta Assinatura", "peso": 0.5},
            {"nome": "Ana Costa", "erro": "Falta Assinatura", "peso": 0.5}
        ]
    }
}

# --- 3. BARRA LATERAL (CENTRO DE COMANDO) ---
with st.sidebar:
    st.header("⚙️ Configurações Alpha")
    medico_sel = st.selectbox("Selecione o Médico
    
