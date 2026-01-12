import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO VISUAL MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 10px; background: #1c232d; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    
    .stTabs [data-baseweb="tab-list"] { background-color: #1c2e4a; border-radius: 10px; padding: 5px; }
    .stTabs [data-baseweb="tab"] { color: #8899A6; font-weight: bold; border: none !important; }
    .stTabs [aria-selected="true"] { background-color: #2c3e50 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }

    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #00d4ff, #008fb3);
        color: #12171d; font-weight: 900; border: none; height: 50px; border-radius: 10px;
    }
    
    .report-preview { 
        background: #f8f9fa; color: #1a1a1a; padding: 20px; 
        border-radius: 8px; font-family: 'Courier New', monospace; 
        font-size: 0.85rem; border: 1px solid #dee2e6; white-space: pre-wrap;
    }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.1rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "motivo": "Divergência de XML", "risco": 32},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "motivo": "Assinatura Digital", "risco": 45},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "motivo": "Erro Cadastral", "risco": 18}
}

medico_sel = st.selectbox("Selecione o Médico:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS DINÂMICOS ---
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICO", "📄 RELATÓRIO"])

with tab1:
    col_a, col_b = st.columns(2)
    # AJUSTE SOLICITADO: Substituição do texto pelo percentual correto
    col_a.metric(f"{p_ok}%", f"R$ {v_liberado:,.2f}")
    col_b.metric(f"{p_risco}%", f"R$ {v_pendente:,.2f}")

with tab2:
    # AJUSTE SOLICITADO: Legenda do gráfico com os percentuais
    df_p = pd.DataFrame({'Status': [f'{p_ok}%', f'{p_risco}%'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_p, {
        'width': 'container', 'height': 300,
        'mark': {'type': 'arc', 'innerRadius': 80, 'outerRadius': 120, 'cornerRadius': 10},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}, 'legend': {'orient': 'bottom', 'labelColor': 'white'}}
        }
    })

with tab3:
    if st.button("🔄 GERAR DOSSIÊ CONSOLIDADO"):
        relatorio = [
            "==========================================",
            f"MÉDICO/UNIDADE : {medico_sel}",
            "------------------------------------------",
            f"Percentual Correto : {p_ok}%",
            f"Percentual Pendente: {p_risco}%",
            "=========================================="
        ]
        texto_final = "\n".join(relatorio)
        st.markdown(f'<div class="report-preview">{texto_final}</div>', unsafe_allow_html=True)
        # Download corrigido para não dar erro de acento no celular
        st.download_button("⬇️ BAIXAR RELATÓRIO", texto_final.encode('utf-8-sig'), file_name="Dossie.txt")
        
