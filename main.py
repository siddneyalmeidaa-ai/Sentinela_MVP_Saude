import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE ALTO IMPACTO (Fiel ao seu print 19:46) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}
    
    /* BANNER COM SEU NOME */
    .banner-sidney {
        background: linear-gradient(90deg, #1c232d 0%, #0e1117 100%);
        padding: 20px; border-radius: 10px; border-left: 5px solid #00d4ff;
        text-align: center; margin-bottom: 20px;
        box-shadow: 0px 4px 15px rgba(0, 212, 255, 0.2);
    }
    .nome-auditor { color: white; font-size: 1.8rem; font-weight: 900; margin: 0; }
    .cargo { color: #00d4ff; font-size: 0.9rem; font-weight: 700; letter-spacing: 2px; }
    </style>
    
    <div class="banner-sidney">
        <p class="nome-auditor">SIDNEY PEREIRA DE ALMEIDA</p>
        <p class="cargo">DIRETOR OPERACIONAL | IA-SENTINELA</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. DADOS E FILTRO ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

st.markdown("🎯 **Selecione o Doutor para Análise:**")
medico_sel = st.selectbox("", list(dados.keys()), label_visibility="collapsed")
info = dados[medico_sel]

# --- 3. VALORES FINANCEIROS (Métricas no topo como você gosta) ---
col_m1, col_m2 = st.columns(2)
with col_m1:
    st.metric("LIBERADO (R$)", f"R$ {info['lib']:,.2f}", f"{info['p_ok']}% ENTRA")
with col_m2:
    st.metric("PENDENTE (R$)", f"R$ {info['pen']:,.2f}", f"{info['p_pen']}% PULA", delta_color="inverse")

st.markdown("---")

# --- 4. PERFORMANCE VISUAL (Tudo em uma tela para o Print) ---
tab_perf, tab_relat = st.tabs(["📊 PERFORMANCE", "📄 EXPORTAR"])

with tab_perf:
    st.markdown("### Visão Geral do Faturamento")
    c1, c2 = st.columns(2)
    
    with c1:
        # Pizza com Percentual Travado na Legenda
        df_p = pd.DataFrame({
            "Status": [f"LIB ({info['p_ok']}%)", f"PEN ({info['p_pen']}%)"],
            "Val": [info['p_ok'], info['p_pen']]
        })
        st.vega_lite_chart(df_p, {
            "width": "container", "height": 300,
            "mark": {"type": "arc", "innerRadius": 50, "outerRadius": 90},
            "encoding": {
                "theta": {"field": "Val", "type": "quantitative"},
                "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
            }
        })

    with c2:
        # Barras com Valor em Real no Topo
        df_b = pd.DataFrame({"S": ["LIB", "PEN"], "V": [info['lib'], info['pen']], "T": [f"R${info['lib']:,.0f}", f"R${info['pen']:,.0f}"]})
        st.vega_lite_chart(df_b, {
            "width": "container", "height": 300,
            "layer": [
                {"mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTop": 5}, "encoding": {"x": {"field": "S", "axis": {"labelAngle": 0}}, "y": {"field": "V", "axis": None}}},
                {"mark": {"type": "text", "baseline": "bottom", "dy": -5, "fill": "white"}, "encoding": {"x": {"field": "S"}, "y": {"field": "V"}, "text": {"field": "T"}}}
            ]
        })

with tab_relat:
    st.markdown("### Gerar Dossiê Oficial")
    rel_txt = f"SISTEMA IA-SENTINELA\nRESPONSÁVEL: SIDNEY ALMEIDA\nUNIDADE: {medico_sel}\nLIB: {info['p_ok']}%\nPEN: {info['p_pen']}%"
    st.download_button("🚀 EXPORTAR DOSSIÊ COMPLETO", rel_txt.encode('utf-8-sig'), f"Auditoria_{medico_sel}.txt")
    
