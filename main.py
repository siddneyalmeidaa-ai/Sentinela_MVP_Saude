import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E DESIGN IDENTICO À IMAGEM ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0rem; background-color: #0e1117;}

    /* BANNER SUPERIOR IDENTICO */
    .brand-banner {
        background: linear-gradient(90deg, #1c232d 0%, #0e1117 100%);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #262730;
        border-left: 5px solid #00d4ff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .user-info { text-align: right; }
    .user-name { color: white; font-size: 1.6rem; font-weight: 800; margin: 0; }
    .user-sub { color: #00d4ff; font-size: 0.8rem; font-weight: 900; letter-spacing: 2px; }

    /* ESTILO DOS CARDS (AUDITORIA E GRAFICOS) */
    .st-card {
        background: #1c232d;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #262730;
        margin-bottom: 15px;
    }
    
    /* ABAS CUSTOMIZADAS */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1c232d;
        border-radius: 8px 8px 0px 0px;
        color: white;
        padding: 10px 20px;
    }
    </style>

    <div class="brand-banner">
        <div>
            <span style="color: #00d4ff; font-weight: 900; font-size: 1.2rem;">🏛️ IA-SENTINELA PRO V31</span><br>
            <span style="color: white; font-size: 0.8rem;">DIRETOR OPERACIONAL</span>
        </div>
        <div class="user-info">
            <p class="user-name">SIDNEY PEREIRA DE ALMEIDA</p>
            <p class="user-sub">DIRETOR OPERACIONAL</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"liberado": 13600.0, "pendente": 2400.0, "p_ok": 85, "p_pend": 15},
    "DMMIGINIO GUERRA": {"liberado": 17550.0, "pendente": 4950.0, "p_ok": 78, "p_pend": 22}
}

# --- 3. SELEÇÃO ---
medico_sel = st.selectbox("🕵️ Selecione o Doutor para Analise:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 4. TABS ---
tab1, tab2, tab3 = st.tabs(["📋 AUDITORIA", "📊 PERFORMANCE", "📩 EXPORTAR"])

with tab1:
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown(f"""<div class='st-card'>
            <p style='color:grey; font-size:0.9rem;'>{info['p_ok']}% LIBERADO</p>
            <h2 style='color:#00d4ff;'>R$ {info['liberado']:,.2f}</h2>
        </div>""", unsafe_allow_html=True)
        
    with col_right:
        st.markdown(f"""<div class='st-card'>
            <p style='color:grey; font-size:0.9rem;'>{info['p_pend']}% PENDENTE</p>
            <h2 style='color:#ff4b4b;'>R$ {info['pendente']:,.2f}</h2>
        </div>""", unsafe_allow_html
                    
