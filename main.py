import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    .header-box { 
        background: #1c232d; padding: 15px; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    
    .stTabs [data-baseweb="tab-list"] { background-color: #1c2e4a; border-radius: 10px; padding: 5px; }
    .stTabs [data-baseweb="tab"] { color: #8899A6; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #2c3e50 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }

    .report-preview { 
        background: #f8f9fa; color: #1a1a1a; padding: 20px; 
        border-radius: 8px; font-family: 'Courier New', monospace; 
        font-size: 1.1rem; border: 1px solid #dee2e6; white-space: pre-wrap;
    }
    </style>
    
    <div class="header-box">
        <div style="color: white; font-size: 1.1rem;">
            <b>SIDNEY PEREIRA DE ALMEIDA</b><br>
            <span style="color: #00d4ff; font-size: 0.9rem;">DIRETOR OPERACIONAL | IA-SENTINELA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "p_pen": 15, "motivo": "Divergência de XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "p_pen": 22, "motivo": "Assinatura Digital"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "p_pen": 18, "motivo": "Erro Cadastral"}
}

unidade = st.selectbox("Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[unidade]

p_risco = info["p_pen"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

# --- 3. DADOS NO TOPO (Métricas SPA) ---
st.markdown(f"### 📍 Unidade: {unidade}")
c1, c2 = st.columns(2)
c1.metric("CONFORMIDADE OPERACIONAL", f"R$ {v_liberado:,.2f}")
c2.metric("PROJEÇÃO DE GLOSA", f"R$ {v_pendente:,.2f}")

# --- 4. ABAS COM TERMINOLOGIA TÉCNICA ---
tab_conformidade, tab_analise, tab_favelinha, tab_dossie = st.tabs([
    "🎯 CONFORMIDADE (%)", "📊 ANÁLISE DE GLOSA (H)", "🏘️ FAVELINHA", "📄 DOSSIÊ FINAL"
])

with tab_conformidade:
    st.markdown("<h4 style='text-align: center; color: white;'>Distribuição de Conformidade Operacional</h4>", unsafe_allow_html=True)
    df_pizza = pd.DataFrame({'Status': [f'LIBERADO ({p_ok}%)', f'PENDENTE ({p_risco}%)'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_pizza, {
        'width': 'container', 'height': 350,
        'mark': {'type': 'arc', '
    
