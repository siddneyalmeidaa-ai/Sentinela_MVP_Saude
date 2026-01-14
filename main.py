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
medico_sel = st.selectbox("Selecione a Unidade:", list(dados.keys()))
info = dados[medico_sel]

# --- 3. GRÁFICOS LADO A LADO COM PERCENTUAL ---
st.markdown("#### 📊 Performance de Auditoria")
col1, col2 = st.columns(2)

with col1:
    # PIZZA COM PERCENTUAL
    df_p = pd.DataFrame({
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [info['p_ok'], info['p_pen']],
        "Lab": [f"{info['p_ok']}%", f"{info['p_pen']}%"]
    })
    st.vega_lite_chart(df_p, {
        "width": "container", "height": 300,
        "layer": [
            {"mark": {"type": "arc", "innerRadius": 50, "outerRadius": 90},
             "encoding": {"theta": {"field": "Valor", "type": "quantitative"},
                          "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom"}}}},
            {"mark": {"type": "text", "radius": 70, "fontSize": 16, "fontWeight": "bold", "fill": "white"},
             "encoding": {"theta": {"field": "Valor", "type": "quantitative"}, "text": {"field": "Lab"}}}
        ]
    })

with col2:
    # BARRAS COM VALORES
    df_b = pd.DataFrame({
        "Status": ["LIB", "PEN"],
        "Valor": [info['lib'], info['pen']],
        "Txt": [f"R${info['lib']:,.0f}", f"R${info['pen']:,.0f}"]
    })
    st.vega_lite_chart(df_b, {
        "width": "container", "height": 300,
        "layer": [
            {"mark": {"type": "bar", "cornerRadiusTop": 5, "color": "#00d4ff"},
             "encoding": {"x": {"field": "Status", "type": "nominal", "axis": {"labelAngle": 0}},
                          "y": {"field": "Valor", "type": "quantitative", "axis": None}}},
            {"mark": {"type": "text", "baseline": "bottom", "dy": -5, "fill": "white", "fontWeight": "bold"},
             "encoding": {"x": {"field": "Status", "type": "nominal"}, "y": {"field": "Valor", "type": "quantitative"}, "text": {"field": "Txt"}}}
        ]
    })

# --- 4. TABELA DA FAVELINHA E AÇÃO IMEDIATA ---
st.markdown("---")
st.markdown("### 🏘️ Tabela da Favelinha")
st.table(pd.DataFrame({
    "Métrica": ["LIBERADO", "PENDENTE", "VÁCUO"],
    "Percentual": [f"{info['p_ok']}%", f"{info['p_pen']}%", "0%"],
    "Ação": ["ENTRA", "PULA", "NÃO ENTRA"]
}))

st.button("🚀 EXPORTAR DOSSIÊ SPA")
