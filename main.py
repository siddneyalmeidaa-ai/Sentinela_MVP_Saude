import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE TELA E TOPO COMPACTO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}
    
    /* HEADER ULTRA COMPACTO */
    .header-compacto {
        display: flex; justify-content: space-between; align-items: center;
        padding: 8px 15px; background: #1c232d; border-radius: 5px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 10px;
    }
    .logo-area { color: #00d4ff; font-weight: 800; font-size: 0.9rem; }
    .iniciais-spa { color: white; font-weight: 900; font-size: 1rem; letter-spacing: 1px; }
    </style>
    
    <div class="header-compacto">
        <div class="logo-area">💠 IA-SENTINELA PRO</div>
        <div class="iniciais-spa">SPA</div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

# Filtro de Unidade (Ocupando pouco espaço)
medico_sel = st.selectbox("Unidade para Auditoria:", list(dados.keys()))
info = dados[medico_sel]

# --- 3. CADA UM EM UMA ABA (Sincronizado) ---
tab_pizza, tab_barras, tab_relatorio = st.tabs(["⭕ PIZZA (%)", "📊 BARRAS (R$)", "📄 RELATÓRIO"])

with tab_pizza:
    st.markdown("<h4 style='text-align: center;'>Distribuição Auditada</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({
        "Status": [f"LIBERADO ({info['p_ok']}%)", f"PENDENTE ({info['p_pen']}%)"],
        "Valor": [info['p_ok'], info['p_pen']]
    })
    st.vega_lite_chart(df_p, {
        "width": "container", "height": 380,
        "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 110},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {
                "field": "Status", 
                "scale": {"range": ["#00d4ff", "#ff4b4b"]},
                "legend": {"orient": "bottom", "labelColor": "white", "fontSize": 14}
            }
        }
    })

with tab_barras:
    st.markdown("<h4 style='text-align: center;'>Volume Financeiro (R$)</h4>", unsafe_allow_html=True)
    df_b = pd.DataFrame({
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [info['lib'], info['pen']],
        "Texto": [f"R$ {info['lib']:,.0f}", f"R$ {info['pen']:,.0f}"]
    })
    st.vega_lite_chart(df_b, {
        "width": "container", "height": 350,
        "layer": [
            {"mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTop": 8},
             "encoding": {
                 "x": {"field": "Status", "type": "nominal", "axis": {"labelAngle": 0}},
                 "y": {"field": "Valor", "type": "quantitative", "axis": None}}},
            {"mark": {"type": "text", "baseline": "bottom", "dy": -10, "fontSize": 16, "fill": "white"},
             "encoding": {
                 "x": {"field": "Status", "type": "nominal"},
                 "y": {"field": "Valor", "type": "quantitative"},
                 "text": {"field": "Texto"}}}
        ]
    })

with tab_relatorio:
    # Relatório Visual SPA
    st.markdown(f"""
    <div style="background: #1c232d; padding: 15px; border-radius: 8px; border-left: 4px solid #00d4ff; color: white;">
        <h4 style="color: #00d4ff; margin-top:0;">CERTIFICADO SPA</h4>
        <p style="font-size: 0.9rem;"><b>UNIDADE:</b> {medico_sel}</p>
        <hr style="border-color: #262730; margin: 10px 0;">
        <p>✅ <b>LIBERADO:</b> {info['p_ok']}% (R$ {info['lib']:,.2f}) -> <b>ENTRA</b></p>
        <p>❌ <b>PENDENTE:</b> {info['p_pen']}% (R$ {info['pen']:,.2f}) -> <b>PULA</b></p>
        <p>🕳️ <b>VÁCUO:</b> 0% -> <b>NÃO ENTRA</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    rel_txt = f"AUDITORIA SPA\nUNIDADE: {medico_sel}\nLIB: {info['p_ok']}%\nPEN: {info['p_pen']}%"
    st.download_button(
        label="⬇️ BAIXAR RELATÓRIO (.TXT)",
        data=rel_txt.encode('utf-8-sig'),
        file_name=f"Relatorio_{medico_sel}.txt",
        mime="text/plain"
    )

st.caption("IA-SENTINELA PRO | Sistema de Gestão SPA")
