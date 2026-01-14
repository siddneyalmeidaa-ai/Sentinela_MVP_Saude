import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER & CSS ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 10px; background: #1c232d; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    .report-preview { 
        background: #f8f9fa; color: #1a1a1a; padding: 20px; 
        border-radius: 8px; font-family: 'Courier New', monospace; 
        font-size: 0.85rem; border: 1px solid #dee2e6; white-space: pre-wrap;
    }
    </style>
    <div class="header-box">
        <span style="color: white; font-size: 1.1rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V17</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (PANDAS/SISTEMA) ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "motivo": "Divergência de XML", "risco": 15},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "motivo": "Assinatura Digital", "risco": 45},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "motivo": "Erro Cadastral", "risco": 18}
}

# --- 3. BARRA LATERAL & AUTOMAÇÃO ---
with st.sidebar:
    st.header("⚙️ Configurações Alpha")
    medico_sel = st.selectbox("Selecione o Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    
    # Slider que permite ajuste manual além do pré-determinado
    p_risco = st.slider("Percentual de Risco (%)", 0, 100, info["risco"])
    p_ok = 100 - p_risco

# --- 4. CÁLCULOS DINÂMICOS (PANDAS) ---
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

# --- 5. INTERFACE DE ABAS ---
tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"**Análise de Dados: {medico_sel}**")
    col_a, col_b = st.columns(2)
    # Títulos agora são as porcentagens dinâmicas [cite: 2026-01-12]
    col_a.metric(f"{p_ok}% LIBERADO", f"R$ {v_liberado:,.2f}")
    col_b.metric(f"{p_risco}% PENDENTE", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.markdown("### 📋 TABELA DA FAVELINHA")
    st.table({
        "Doutor": [medico_sel],
        "Ação": ["ENTRA" if p_ok >= 85 else "PULA"], # Regra do Vácuo [cite: 2025-12-29]
        "IA-SENTINELA": ["Monitorando vácuo" if p_ok >= 85 else "VÁCUO DETECTADO"]
    })

with tab2:
    # Gráfico de Pizza com legenda de porcentagem sincronizada [cite: 2026-01-12]
    df_p = pd.DataFrame({'Status': [f'{p_ok}% LIBERADO', f'{p_risco}% PENDENTE'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_p, {
        'width': 'container', 'height': 300,
        'mark': {'type': 'arc', 'innerRadius': 70, 'outerRadius': 110},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}}
        }
    })
    
    # Gráfico de Barras de Faturamento
    st.markdown("#### 💰 Faturamento Auditado (R$)")
    df_v = pd.DataFrame({'Métrica': ['Liberado', 'Pendente'], 'Valor': [v_liberado, v_pendente]})
    st.bar_chart(df_v.set_index('Métrica'), color="#00d4ff")

with tab3:
    if st.button("🔄 GERAR DOSSIÊ CONSOLIDADO"):
        relatorio = f"""
==========================================
   DOSSIÊ DE AUDITORIA - IA-SENTINELA PRO 
==========================================
MÉDICO/UNIDADE : {medico_sel}
DATA EMISSÃO   : 14/01/2026
------------------------------------------
Faturamento Total  : R$ {info['valor']:,.2f}
PERCENTUAL LIBERADO: {p_ok}% (R$ {v_liberado:,.2f})
PERCENTUAL PENDENTE: {p_risco}% (R$ {v_pendente:,.2f})
------------------------------------------
MOTIVO PRINCIPAL   : {info['motivo']}
=========================================="""
        st.markdown(f'<div class="report-preview">{relatorio}</div>', unsafe_allow_html=True)
        
        # Download blindado contra erros de acento no celular [cite: 2026-01-12]
        st.download_button(
            label="⬇️ BAIXAR RELATÓRIO (.TXT)",
            data=relatorio.encode('utf-8-sig'),
            file_name=f"Dossie_{medico_sel}.txt",
            mime="text/plain"
        )
        
