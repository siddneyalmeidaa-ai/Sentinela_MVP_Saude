import streamlit as st
import pandas as pd
import random

# --- 🏛️ CONFIGURAÇÃO MOBILE MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { display: flex; justify-content: space-between; align-items: center; padding: 5px 10px; color: #00d4ff; font-weight: bold; font-size: 0.9rem; border-bottom: 1px solid #1c2e4a; }
    .pro-tag { background-color: #00d4ff; color: #0e1117; font-size: 0.6rem; padding: 2px 5px; border-radius: 4px; font-weight: 900; }
    
    /* Menu de Navegação Horizontal */
    .stTabs [data-baseweb="tab-list"] { gap: 5px; }
    .stTabs [data-baseweb="tab"] { 
        height: 35px; background-color: #1c2e4a; border-radius: 5px; color: white; font-size: 0.7rem;
    }
    .stTabs [aria-selected="true"] { background-color: #00d4ff !important; color: #0e1117 !important; }

    .block-container { padding: 0.5rem 0.5rem !important; }
    header {visibility: hidden;}
    
    .status-box { padding: 12px; border-radius: 5px; margin-top: 8px; font-weight: bold; font-size: 0.85rem; text-align: center; }
    .status-ok { background-color: #15572422; color: #28a745; border: 1px solid #28a745; }
    .status-error { background-color: #721c2422; color: #ff4b4b; border: 1px solid #ff4b4b; }
    
    /* Botão de Gerar Relatório Online */
    .stButton>button { width: 100%; background-color: #00d4ff; color: #0e1117; font-weight: 900; border-radius: 8px; height: 50px; border: none; }
    </style>
    
    <div class="header-box">
        <span>🏛️ CONTROLE: IA-SENTINELA</span> 
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML", "risco": 32},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Assinatura Digital", "risco": 68},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Erro Cadastral", "risco": 15}
}

# --- 🔍 SELETOR PRINCIPAL ---
medico_sel = st.selectbox("Auditar Médico:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS ---
p_risco = info["risco"]
p_ok = 100 - p_risco
v_faturamento = info["valor"]
v_pendente = v_faturamento * (p_risco / 100)
v_liberado = v_faturamento * (p_ok / 100)

# --- 🕹️ NAVEGAÇÃO POR ETAPAS (TABS) ---
tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICO", "📋 RELATÓRIO"])

with tab1:
    st.write(f"**Dados da Unidade: {medico_sel}**")
    st.write(f"Volume: {info['pacientes']} pacientes")
    st.write(f"Faturamento: R$ {v_faturamento:,.2f}")
    st.info("Selecione a próxima aba para ver a análise visual.")

with tab2:
    st.write("**Análise de Risco Operacional**")
    df_p = pd.DataFrame({'Status': ['OK', 'RISCO'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_p, {
        'width': 'container', 'height': 250,
        'mark': {'type': 'arc', 'innerRadius': 60, 'outerRadius': 100},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}, 'legend': {'orient': 'bottom'}}
        }
    }, key=f"pizza_{medico_sel}")

with tab3:
    st.subheader("📑 Menu de Relatórios")
    st.write("Clique abaixo para processar a auditoria final.")
    
    if st.button("📊 GERAR RELATÓRIO ONLINE"):
        st.markdown("---")
        st.markdown(f"### 📄 DOSSIÊ FINAL: {medico_sel}")
        st.markdown(f'<div class="status-box status-ok">LIBERADO: R$ {v_liberado:,.2f} ({p_ok}%)</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="status-box status-error">PENDENTE: R$ {v_pendente:,.2f} ({p_risco}%)</div>', unsafe_allow_html=True)
        st.error(f"MOTIVO DO BLOQUEIO: {info['motivo']}")
        st.success("✅ Relatório gerado com sucesso para auditoria.")
    else:
        st.warning("Aguardando comando de geração...")
    
