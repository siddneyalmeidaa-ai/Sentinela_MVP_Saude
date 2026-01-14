import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO PREMIUM ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}
    .header-spa {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px; background: #1c232d; border-radius: 8px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .spa-text { color: white; font-weight: 900; font-size: 1.1rem; letter-spacing: 2px; }
    </style>
    <div class="header-spa">
        <span style="color: #00d4ff; font-weight: 800; font-size: 0.8rem;">🏛️ IA-SENTINELA PRO</span>
        <span class="spa-text">SPA</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. DADOS SINCRONIZADOS ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}
medico_sel = st.selectbox("Unidade para Auditoria:", list(dados.keys()))
info = dados[medico_sel]

# --- 3. ORGANIZAÇÃO EM ABAS SEPARADAS ---
tab1, tab2, tab3 = st.tabs(["📊 PIZZA (%)", "📈 BARRAS (R$)", "🏘️ FAVELINHA"])

with tab1:
    st.markdown("<h4 style='text-align: center;'>Distribuição Percentual</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({
        "Status": [f"LIBERADO ({info['p_ok']}%)", f"PENDENTE ({info['p_pen']}%)"],
        "Valor": [info['p_ok'], info['p_pen']]
    })
    # Gráfico limpo com percentual na legenda para não errar no mobile
    st.vega_lite_chart(df_p, {
        "width": "container", "height": 350,
        "mark": {"type": "arc", "innerRadius": 60, "outerRadius": 100},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {
                "field": "Status", 
                "scale": {"range": ["#00d4ff", "#ff4b4b"]},
                "legend": {"orient": "bottom", "labelColor": "white", "fontSize": 15}
            }
        }
    })
    st.info(f"💡 Faturamento Auditado: {info['p_ok']}% Liberado.")

with tab2:
    st.markdown("<h4 style='text-align: center;'>Volume Financeiro</h4>", unsafe_allow_html=True)
    df_b = pd.DataFrame({
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [info['lib'], info['pen']],
        "Label": [f"R$ {info['lib']:,.0f}", f"R$ {info['pen']:,.0f}"]
    })
    st.vega_lite_chart(df_b, {
        "width": "container", "height": 350,
        "layer": [
            {"mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTop": 8},
             "encoding": {
                 "x": {"field": "Status", "type": "nominal", "axis": {"labelAngle": 0, "labelColor": "white"}},
                 "y": {"field": "Valor", "type": "quantitative", "axis": None}}},
            {"mark": {"type": "text", "baseline": "bottom", "dy": -10, "fontSize": 16, "fill": "white"},
             "encoding": {
                 "x": {"field": "Status", "type": "nominal"},
                 "y": {"field": "Valor", "type": "quantitative"},
                 "text": {"field": "Label"}}}
        ]
    })

with tab3:
    # Tabela da Favelinha
    st.markdown("### Ação Imediata")
    st.table(pd.DataFrame({
        "Métrica": ["LIBERADO", "PENDENTE", "VÁCUO"],
        "Percentual": [f"{info['p_ok']}%", f"{info['p_pen']}%", "0%"],
        "Regra": ["ENTRA", "PULA", "NÃO ENTRA"]
    }))

# --- 4. EXPORTAÇÃO ---
st.markdown("---")
st.button("🚀 EXPORTAR DOSSIÊ COMPLETO SPA")
