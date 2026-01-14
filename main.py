import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE ALTO IMPACTO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}
    
    /* BANNER SIDNEY */
    .banner-sidney {
        background: #1c232d; padding: 15px; border-radius: 10px; 
        border-bottom: 3px solid #00d4ff; text-align: center; margin-bottom: 20px;
    }
    .nome-auditor { color: white; font-size: 1.5rem; font-weight: 900; margin: 0; }
    .cargo { color: #00d4ff; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; }
    </style>
    
    <div class="banner-sidney">
        <p class="nome-auditor">SIDNEY PEREIRA DE ALMEIDA</p>
        <p class="cargo">DIRETOR OPERACIONAL | IA-SENTINELA</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS E FILTRO ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

st.markdown("🎯 **Selecione a Unidade:**")
medico_sel = st.selectbox("", list(dados.keys()), label_visibility="collapsed")
info = dados[medico_sel]

# --- 3. ORGANIZAÇÃO EM ABAS (Cada um na sua água) ---
tab_pizza, tab_barras, tab_relatorio = st.tabs(["⭕ PIZZA (%)", "📊 BARRAS (R$)", "📄 RELATÓRIO"])

with tab_pizza:
    st.markdown("<h4 style='text-align: center;'>Distribuição Percentual</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({
        "Status": [f"LIB ({info['p_ok']}%)", f"PEN ({info['p_pen']}%)"],
        "Val": [info['p_ok'], info['p_pen']]
    })
    st.vega_lite_chart(df_p, {
        "width": "container", "height": 350,
        "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 110},
        "encoding": {
            "theta": {"field": "Val", "type": "quantitative"},
            "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
        }
    })

with tab_barras:
    st.markdown("<h4 style='text-align: center;'>Volume Financeiro (R$)</h4>", unsafe_allow_html=True)
    df_b = pd.DataFrame({
        "S": ["LIBERADO", "PENDENTE"], 
        "V": [info['lib'], info['pen']], 
        "T": [f"R${info['lib']:,.0f}", f"R${info['pen']:,.0f}"]
    })
    st.vega_lite_chart(df_b, {
        "width": "container", "height": 350,
        "layer": [
            {"mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTop": 8}, 
             "encoding": {"x": {"field": "S", "axis": {"labelAngle": 0}}, "y": {"field": "V", "axis": None}}},
            {"mark": {"type": "text", "baseline": "bottom", "dy": -10, "fill": "white", "fontSize": 14}, 
             "encoding": {"x": {"field": "S"}, "y": {"field": "V"}, "text": {"field": "T"}}}
        ]
    })

with tab_relatorio:
    # Relatório Visual Bonitinho que funciona
    st.markdown(f"""
    <div style="background: #1c232d; padding: 20px; border-radius: 10px; border-left: 5px solid #00d4ff; color: white;">
        <h3 style="color: #00d4ff; margin-top:0;">CERTIFICADO DE AUDITORIA</h3>
        <p><b>UNIDADE:</b> {medico_sel}</p>
        <hr style="border-color: #262730;">
        <p>✅ <b>LIBERADO:</b> {info['p_ok']}% (R$ {info['lib']:,.2f}) -> <b>ENTRA</b></p>
        <p>❌ <b>PENDENTE:</b> {info['p_pen']}% (R$ {info['pen']:,.2f}) -> <b>PULA</b></p>
        <p>🕳️ <b>VÁCUO:</b> 0% -> <b>NÃO ENTRA</b></p>
        <hr style="border-color: #262730;">
        <p style="text-align: right; font-size: 0.8rem;">AUDITOR RESPONSÁVEL: <b>SPA</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    rel_txt = f"SISTEMA IA-SENTINELA\nUNIDADE: {medico_sel}\nLIB: {info['p_ok']}%\nPEN: {info['p_pen']}%"
    st.download_button("🚀 EXPORTAR DOSSIÊ", rel_txt.encode('utf-8-sig'), f"Auditoria_{medico_sel}.txt")

st.markdown("---")
st.caption("IA-SENTINELA PRO | Sistema de Gestão Operacional")
