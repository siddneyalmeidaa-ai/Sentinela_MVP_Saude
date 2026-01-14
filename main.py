import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}
    
    /* CABEÇALHO SPA */
    .header-spa {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px; background: #1c232d; border-radius: 8px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .spa-text { color: white; font-weight: 900; font-size: 1.1rem; letter-spacing: 2px; }

    /* ESTILO DO RELATÓRIO BONITINHO */
    .report-box {
        background-color: #1c232d;
        border-left: 5px solid #00d4ff;
        padding: 20px;
        border-radius: 10px;
        color: white;
        font-family: 'Courier New', Courier, monospace;
    }
    .status-entra { color: #00d4ff; font-weight: bold; }
    .status-pula { color: #ff4b4b; font-weight: bold; }
    </style>
    
    <div class="header-spa">
        <span style="color: #00d4ff; font-weight: 800; font-size: 0.8rem;">🏛️ IA-SENTINELA PRO</span>
        <span class="spa-text">SPA</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}
medico_sel = st.selectbox("Unidade:", list(dados.keys()))
info = dados[medico_sel]

# --- 3. SISTEMA DE ABAS ---
tab_pizza, tab_barras, tab_relatorio, tab_favelinha = st.tabs([
    "⭕ PIZZA (%)", "📊 BARRAS (R$)", "📄 RELATÓRIO", "🏘️ FAVELINHA"
])

with tab_pizza:
    st.markdown("<h4 style='text-align: center;'>Distribuição Auditada</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({
        "Status": [f"LIBERADO ({info['p_ok']}%)", f"PENDENTE ({info['p_pen']}%)"],
        "Valor": [info['p_ok'], info['p_pen']]
    })
    st.vega_lite_chart(df_p, {
        "width": "container", "height": 350,
        "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 110},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
        }
    })

with tab_barras:
    st.markdown("<h4 style='text-align: center;'>Volume Financeiro</h4>", unsafe_allow_html=True)
    df_b = pd.DataFrame({"Cat": ["LIB", "PEN"], "Val": [info['lib'], info['pen']], "Txt": [f"R${info['lib']:,.0f}", f"R${info['pen']:,.0f}"]})
    st.vega_lite_chart(df_b, {
        "width": "container", "height": 300,
        "layer": [
            {"mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTop": 8}, "encoding": {"x": {"field": "Cat", "axis": {"labelAngle": 0}}, "y": {"field": "Val", "axis": None}}},
            {"mark": {"type": "text", "baseline": "bottom", "dy": -10, "fill": "white"}, "encoding": {"x": {"field": "Cat"}, "y": {"field": "Val"}, "text": {"field": "Txt"}}}
        ]
    })

with tab_relatorio:
    st.markdown("### 📋 Dossiê de Auditoria Final")
    # Versão Visual do Relatório (Bonitinho)
    st.markdown(f"""
    <div class="report-box">
        <h2 style="color: #00d4ff; margin-top:0;">CERTIFICADO DE AUDITORIA</h2>
        <p><b>UNIDADE:</b> {medico_sel}</p>
        <hr style="border-color: #262730;">
        <p>✅ <b>LIBERADO:</b> {info['p_ok']}% (R$ {info['lib']:,.2f}) -> <span class="status-entra">ENTRA</span></p>
        <p>❌ <b>PENDENTE:</b> {info['p_pen']}% (R$ {info['pen']:,.2f}) -> <span class="status-pula">PULA</span></p>
        <p>🕳️ <b>VÁCUO:</b> 0% -> <b>NÃO ENTRA</b></p>
        <hr style="border-color: #262730;">
        <p style="font-size: 0.8rem; text-align: right;">RESPONSÁVEL OPERACIONAL: <b>SPA</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão de exportação funcional [cite: 01-12-2026]
    rel_txt = f"AUDITORIA SPA\nUNIDADE: {medico_sel}\nLIB: {info['p_ok']}%\nPEN: {info['p_pen']}%"
    st.download_button("⬇️ SALVAR ARQUIVO OFICIAL", rel_txt.encode('utf-8-sig'), f"Auditoria_{medico_sel}.txt")

with tab_favelinha:
    st.markdown("### 🏘️ Tabela da Favelinha")
    st.table(pd.DataFrame({
        "Métrica": ["LIBERADO", "PENDENTE", "VÁCUO"],
        "Percentual": [f"{info['p_ok']}%", f"{info['p_pen']}%", "0%"],
        "Ação": ["ENTRA", "PULA", "NÃO ENTRA"]
    }))
    
