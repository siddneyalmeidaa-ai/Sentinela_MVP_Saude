import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E DESIGN ULTRA-CLEAN ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}

    /* HEADER MINIMALISTA: SPA + LOGO PEQUENO */
    .mini-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 15px;
        background: #1c232d;
        border-radius: 8px;
        border-bottom: 2px solid #00d4ff;
        margin-bottom: 15px;
    }
    .spa-tag {
        color: white;
        font-weight: 900;
        font-size: 1.1rem;
        letter-spacing: 2px;
    }
    .mini-logo {
        width: 25px;
        filter: drop-shadow(0px 0px 5px #00d4ff);
    }

    /* CARDS DE PERFORMANCE IDENTICOS À REFERÊNCIA */
    .perf-card {
        background: #1c232d;
        padding: 12px;
        border-radius: 10px;
        border: 1px solid #262730;
        text-align: center;
    }
    </style>
    
    <div class="mini-header">
        <div>
            <img src="https://cdn-icons-png.flaticon.com/512/3914/3914404.png" class="mini-logo">
            <span style="color: #00d4ff; font-size: 0.7rem; font-weight: 800; margin-left: 5px;">IA-SENTINELA</span>
        </div>
        <div class="spa-tag">SPA</div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

# --- 3. SELEÇÃO ---
medico_sel = st.selectbox("Selecione a Unidade:", list(dados.keys()))
info = dados[medico_sel]

tab1, tab2, tab3 = st.tabs(["📋 AUDITORIA", "📊 GRÁFICOS", "📩 EXPORTAR"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='perf-card'><p style='color:grey;font-size:0.75rem;margin:0;'>OK</p><h4 style='color:#00d4ff;margin:0;'>R$ {info['lib']:,.2f}</h4></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='perf-card'><p style='color:grey;font-size:0.75rem;margin:0;'>PEND</p><h4 style='color:#ff4b4b;margin:0;'>R$ {info['pen']:,.2f}</h4></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.table(pd.DataFrame({"Paciente": ["João Silva", "Maria Oliveira"], "Status": ["OK", "PENDENTE"], "Valor": ["R$ 1.200", "R$ 1.200"]}))

with tab2:
    # GRÁFICOS EM DUPLA (Lado a Lado)
    st.markdown("#### Performance Operacional")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("<p style='font-size:0.7rem; color:grey; text-align:center;'>Pizza (%)</p>", unsafe_allow_html=True)
        st.vega_lite_chart(pd.DataFrame({"C": ["OK", "PEN"], "V": [info['p_ok'], info['p_pen']]}), {
            "width": "container", "height": 160,
            "mark": {"type": "arc", "innerRadius": 35, "outerRadius": 55},
            "encoding": {"theta": {"field": "V", "type": "quantitative"}, "color": {"field": "C", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": None}}
        })

    with col_b:
        st.markdown("<p style='font-size:0.7rem; color:grey; text-align:center;'>Barras (R$)</p>", unsafe_allow_html=True)
        st.vega_lite_chart(pd.DataFrame({"C": ["L", "P"], "V": [info['lib'], info['pen']]}), {
            "width": "container", "height": 160,
            "mark": {"type": "bar", "color": "#00d4ff", "cornerRadius": 4},
            "encoding": {"x": {"field": "C", "type": "nominal", "axis": {"labelAngle": 0}}, "y": {"field": "V", "type": "quantitative", "axis": None}}
        })

with tab3:
    st.button("🚀 EXPORTAR RELATÓRIO SPA")
        
