import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER ---
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

    .report-preview { 
        background: #1c232d; color: white; padding: 25px; 
        border-radius: 10px; border: 2px solid #00d4ff;
        font-family: 'Segoe UI', sans-serif; line-height: 1.6;
    }
    </style>
    
    <div class="header-box">
        <div style="color: white; font-size: 1.1rem;">
            <b>SIDNEY PEREIRA DE ALMEIDA</b><br>
            <span style="color: #00d4ff; font-size: 0.9rem;">DIRETOR OPERACIONAL | IA-SENTINELA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. MOTOR DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "p_pen": 15},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "p_pen": 22},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "p_pen": 18}
}

unidade = st.selectbox("Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[unidade]

p_risco = info["p_pen"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

# --- 3. INDICADORES ---
st.markdown(f"### 📍 Auditoria: {unidade}")
c1, c2 = st.columns(2)
c1.metric("CONFORMIDADE OPERACIONAL", f"R$ {v_liberado:,.2f}")
c2.metric("PROJEÇÃO DE GLOSA", f"R$ {v_pendente:,.2f}")

# --- 4. FLUXO DE ABAS ---
# Aba Favelinha renomeada para Parecer Operacional
tab_perfil, tab_fluxo, tab_parecer, tab_cert = st.tabs([
    "🎯 PERFIL DE RISCO", "📊 ANÁLISE DE GLOSA (H)", "📋 PARECER OPERACIONAL", "📄 CERTIFICADO SPA"
])

with tab_perfil:
    df_donut = pd.DataFrame({'Status': [f'LIBERADO ({p_ok}%)', f'PENDENTE ({p_risco}%)'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_donut, {
        'width': 'container', 'height': 350,
        'mark': {'type': 'arc', 'innerRadius': 85, 'outerRadius': 125, 'cornerRadius': 10},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'scale': {'range': ['#00d4ff', '#ff4b4b']}, 'legend': {'orient': 'bottom', 'labelColor': 'white'}}
        }
    })

with tab_fluxo:
    df_bar = pd.DataFrame({
        'Status': ['LIBERADO', 'PENDENTE'],
        'Valor': [v_liberado, v_pendente],
        'Cor': ['#00d4ff', '#ff4b4b']
    })
    st.vega_lite_chart(df_bar, {
        'width': 'container', 'height': 250,
        'mark': {'type': 'bar', 'cornerRadiusEnd': 10, 'size': 50},
        'encoding': {
            'y': {'field': 'Status', 'type': 'nominal', 'axis': {'title': None, 'labelColor': 'white'}},
            'x': {'field': 'Valor', 'type': 'quantitative', 'axis': {'title': 'R$', 'grid': False}},
            'color': {'field': 'Cor', 'type': 'nominal', 'scale': None}
        }
    })

with tab_parecer:
    st.markdown("### 🏘️ Tabela de Parecer Técnico")
    # Colunas alteradas para Procede / Não Procede
    df_parecer = pd.DataFrame({
        "Métrica": ["CONFORMIDADE", "GLOSA"],
        "Eficiência": [f"{p_ok}%", f"{p_risco}%"],
        "Análise SPA": ["PROCEDE", "NÃO PROCEDE"]
    })
    st.table(df_parecer)

with tab_cert:
    # Retornando ao layout de certificado padrão original
    cert_html = f"""
    <div class="report-preview">
        <h2 style="color: #00d4ff; margin-top:0;">CERTIFICADO SPA</h2>
        <b>UNIDADE:</b> {unidade}<br><br>
        ✅ <b>LIBERADO:</b> {p_ok}% (R$ {v_liberado:,.2f}) -> <b>PROCEDE</b><br>
        ❌ <b>PENDENTE:</b> {p_risco}% (R$ {v_pendente:,.2f}) -> <b>NÃO PROCEDE</b><br>
        🕳️ <b>VÁCUO:</b> 0% -> <b>NÃO ENTRA</b>
    </div>
    """
    st.markdown(cert_html, unsafe_allow_html=True)
    
    # Configuração de download sem erro de acento
    relatorio_txt = (
        f"CERTIFICADO SPA\\nUNIDADE: {unidade}\\n"
        f"LIBERADO: {p_ok}% (R$ {v_liberado:,.2f}) -> PROCEDE\\n"
        f"PENDENTE: {p_risco}% (R$ {v_pendente:,.2f}) -> NAO PROCEDE\\n"
        "STATUS FINAL: AUDITADO POR SPA"
    )
    st.download_button("⬇️ BAIXAR CERTIFICADO (.TXT)", relatorio_txt.encode('utf-8'), f"Certificado_{unidade}.txt")

st.caption("IA-SENTINELA PRO | Sistema de Gestão SPA")
    
