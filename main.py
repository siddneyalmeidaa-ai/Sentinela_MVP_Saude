import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Esconde o menu original para não comer espaço */
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}

    /* HEADER SPA MINIMALISTA */
    .header-spa {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 15px;
        background: #1c232d;
        border-radius: 8px;
        border-bottom: 2px solid #00d4ff;
        margin-bottom: 15px;
    }
    .spa-text { color: white; font-weight: 900; font-size: 1.1rem; letter-spacing: 2px; }

    /* CARD DE MÉTRICAS COMPACTO */
    .m-card {
        background: #1c232d;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #262730;
        text-align: center;
    }
    </style>
    
    <div class="header-spa">
        <span style="color: #00d4ff; font-weight: 800; font-size: 0.8rem;">🏛️ IA-SENTINELA</span>
        <span class="spa-text">SPA</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. DADOS SINCRONIZADOS ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

# --- 3. SELEÇÃO ---
medico_sel = st.selectbox("Unidade:", list(dados.keys()))
info = dados[medico_sel]

# --- 4. PAINEL PRINCIPAL ---
t1, t2 = st.tabs(["📋 DADOS", "📊 GRÁFICOS"])

with t1:
    # Cards de valores imediatos
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='m-card'><p style='color:grey;font-size:0.7rem;margin:0;'>{info['p_ok']}% OK</p><h4 style='color:#00d4ff;margin:0;'>R$ {info['lib']:,.0f}</h4></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='m-card'><p style='color:grey;font-size:0.7rem;margin:0;'>{info['p_pen']}% PEN</p><h4 style='color:#ff4b4b;margin:0;'>R$ {info['pen']:,.0f}</h4></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.table(pd.DataFrame({"Item": ["Liberado", "Pendente"], "Total": [f"R$ {info['lib']:,.2f}", f"R$ {info['pen']:,.2f}"]}))

with t2:
    st.markdown("#### Performance SPA")
    # CRIAÇÃO DE COLUNAS PARA EVITAR O EMPILHAMENTO NO CELULAR
    g1, g2 = st.columns(2)
    
    with g1:
        # Gráfico de Pizza com legendas embutidas
        df_p = pd.DataFrame({"Status": ["LIB", "PEN"], "Val": [info['p_ok'], info['p_pen']]})
        st.vega_lite_chart(df_p, {
            "width": "container", "height": 180,
            "mark": {"type": "arc", "innerRadius": 35, "outerRadius": 60},
            "encoding": {
                "theta": {"field": "Val", "type": "quantitative"},
                "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom"}}
            }
        })

    with g2:
        # Gráfico de Barras com as mesmas cores do de pizza
        df_b = pd.DataFrame({"Status": ["LIB", "PEN"], "Val": [info['lib'], info['pen']]})
        st.vega_lite_chart(df_b, {
            "width": "container", "height": 180,
            "mark": {"type": "bar", "cornerRadius": 4},
            "encoding": {
                "x": {"field": "Status", "type": "nominal", "axis": {"labelAngle": 0}},
                "y": {"field": "Val", "type": "quantitative", "axis": None},
                "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": None}
            }
        })

# --- 5. RODAPÉ FIXO ---
st.button("🚀 EXPORTAR RELATÓRIO SPA")
