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

# --- 2. BASE DE DADOS INTEGRADA ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "p_pen": 15, "motivo": "Divergência de XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "p_pen": 22, "motivo": "Assinatura Digital"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "p_pen": 18, "motivo": "Erro Cadastral"}
}

medico_sel = st.selectbox("Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

p_risco = info["p_pen"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

# --- 3. DADOS PRINCIPAIS NO TOPO (Padrão Sidney) ---
st.markdown(f"### 📍 Auditoria: {medico_sel}")
col1, col2 = st.columns(2)
col1.metric(f"LIBERADO ({p_ok}%)", f"R$ {v_liberado:,.2f}")
col2.metric(f"PENDENTE ({p_risco}%)", f"R$ {v_pendente:,.2f}")

# --- 4. ABAS COM GRÁFICOS SEPARADOS ---
tab_pizza, tab_barras, tab_fav, tab_rel = st.tabs([
    "⭕ PIZZA (%)", "📊 BARRAS (H)", "🏘️ FAVELINHA", "📄 RELATÓRIO"
])

with tab_pizza:
    df_pizza = pd.DataFrame({'Status': [f'LIBERADO ({p_ok}%)', f'PENDENTE ({p_risco}%)'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_pizza, {
        'width': 'container', 'height': 350,
        'mark': {'type': 'arc', 'innerRadius': 80, 'outerRadius': 120, 'cornerRadius': 10},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'scale': {'range': ['#00d4ff', '#ff4b4b']}, 'legend': {'orient': 'bottom', 'labelColor': 'white'}}
        }
    })

with tab_barras:
    st.markdown("<h4 style='text-align: center; color: white;'>Volume Financeiro (Barras Horizontais)</h4>", unsafe_allow_html=True)
    df_bar = pd.DataFrame({
        'Métrica': ['LIBERADO', 'PENDENTE'],
        'Valor': [v_liberado, v_pendente],
        'Cor': ['#00d4ff', '#ff4b4b']
    })
    
    # GRÁFICO HORIZONTAL: Métrica no eixo Y e Valor no eixo X
    st.vega_lite_chart(df_bar, {
        'width': 'container', 'height': 250,
        'mark': {'type': 'bar', 'cornerRadiusEnd': 10, 'size': 50},
        'encoding': {
            'y': {'field': 'Métrica', 'type': 'nominal', 'axis': {'title': None, 'labelColor': 'white', 'labelFontSize': 14}},
            'x': {'field': 'Valor', 'type': 'quantitative', 'axis': {'title': 'Valor R$', 'grid': False}},
            'color': {'field': 'Cor', 'type': 'nominal', 'scale': None}
        }
    })

with tab_fav:
    st.markdown("### 🏘️ Tabela da Favelinha")
    df_fav = pd.DataFrame({
        "Métrica": ["LIBERADO", "PENDENTE"],
        "Percentual": [f"{p_ok}%", f"{p_risco}%"],
        "Ação Imediata": ["ENTRA", "NÃO ENTRA"]
    })
    st.table(df_fav)

with tab_rel:
    # RELATÓRIO NO FORMATO DOSSIÊ (LETRA AMPLIADA)
    relatorio_txt = (
        "==========================================\n"
        "   DOSSIÊ DE AUDITORIA - IA-SENTINELA PRO \n"
        "==========================================\n"
        f"MÉDICO/UNIDADE : {medico_sel}\n"
        f"DATA EMISSÃO   : 14/01/2026\n"
        "------------------------------------------\n"
        f"Faturamento Total  : R$ {info['valor']:,.2f}\n"
        f"Percentual Correto : {p_ok}% (R$ {v_liberado:,.2f})\n"
        f"Percentual Risco   : {p_risco}% (R$ {v_pendente:,.2f})\n"
        "------------------------------------------\n"
        f"MOTIVO PRINCIPAL   : {info['motivo']}\n"
        "==========================================\n"
        "STATUS FINAL: ENTRA\n"
        "RESPONSÁVEL : DIRETORIA OPERACIONAL"
    )
    
    st.markdown(f'<div class="report-preview">{relatorio_txt}</div>', unsafe_allow_html=True)
    
    st.download_button(
        label="⬇️ BAIXAR RELATÓRIO OFICIAL (.TXT)",
        data=relatorio_txt.encode('utf-8-sig'),
        file_name=f"Dossie_{medico_sel.replace(' ', '_')}.txt",
        mime="text/plain"
    )

st.caption("IA-SENTINELA PRO | Padrão Ouro SPA")
