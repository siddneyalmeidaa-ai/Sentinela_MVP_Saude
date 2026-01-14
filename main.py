import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E DESIGN REFINADO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}

    /* HEADER SPA ULTRA-CLEAN */
    .mini-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 18px;
        background: #1c232d;
        border-radius: 10px;
        border-bottom: 3px solid #00d4ff;
        margin-bottom: 20px;
    }
    .spa-tag {
        color: white;
        font-weight: 900;
        font-size: 1.2rem;
        letter-spacing: 3px;
    }
    .system-title {
        color: #00d4ff;
        font-size: 0.8rem;
        font-weight: 800;
        text-transform: uppercase;
    }

    /* CARDS DE MÉTRICAS */
    .metric-card {
        background: #1c232d;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #262730;
        text-align: center;
    }
    </style>
    
    <div class="mini-header">
        <div>
            <span class="system-title">🏛️ IA-SENTINELA</span>
        </div>
        <div class="spa-tag">SPA</div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS SINCRONIZADO ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

# --- 3. SELEÇÃO DE UNIDADE ---
medico_sel = st.selectbox("Selecione a Unidade para Auditoria:", list(dados.keys()))
info = dados[medico_sel]

tab1, tab2, tab3 = st.tabs(["📋 PAINEL", "📊 PERFORMANCE", "📩 EXPORTAR"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='metric-card'><p style='color:grey;font-size:0.8rem;margin:0;'>{info['p_ok']}% LIBERADO</p><h3 style='color:#00d4ff;margin:0;'>R$ {info['lib']:,.2f}</h3></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><p style='color:grey;font-size:0.8rem;margin:0;'>{info['p_pen']}% PENDENTE</p><h3 style='color:#ff4b4b;margin:0;'>R$ {info['pen']:,.2f}</h3></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 📌 Detalhamento por Paciente")
    df_pacientes = pd.DataFrame({
        "Paciente": ["João Silva", "Maria Oliveira"],
        "Motivo": ["Glosado", "Pendente"],
        "Valor": [f"R$ {info['pen']/2:,.2f}", f"R$ {info['pen']/2:,.2f}"]
    })
    st.table(df_pacientes)

with tab2:
    st.markdown("#### 📊 Análise de Performance")
    # COLUNAS PARA OS GRÁFICOS FICAREM LADO A LADO
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        st.markdown("<p style='text-align:center; font-size:0.8rem; color:grey;'>Distribuição (%)</p>", unsafe_allow_html=True)
        chart_pizza = pd.DataFrame({"Status": ["LIBERADO", "PENDENTE"], "Valor": [info['p_ok'], info['p_pen']]})
        st.vega_lite_chart(chart_pizza, {
            "width": "container", "height": 200,
            "mark": {"type": "arc", "innerRadius": 45, "outerRadius": 75, "tooltip": True},
            "encoding": {
                "theta": {"field": "Valor", "type": "quantitative"},
                "color": {"field": "Status", "type": "nominal", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
            }
        })

    with g_col2:
        st.markdown("<p style='text-align:center; font-size:0.8rem; color:grey;'>Volume (R$)</p>", unsafe_allow_html=True)
        chart_barras = pd.DataFrame({"Status": ["OK", "PEN"], "Total": [info['lib'], info['pen']]})
        st.vega_lite_chart(chart_barras, {
            "width": "container", "height": 200,
            "mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTopLeft": 5, "cornerRadiusTopRight": 5},
            "encoding": {
                "x": {"field": "Status", "type": "nominal", "axis": {"labelAngle": 0, "labelColor": "white"}},
                "y": {"field": "Total", "type": "quantitative", "axis": None}
            }
        })

with tab3:
    st.markdown("#### 📄 Dossiê SPA")
    relatorio = f"IA-SENTINELA - RESPONSÁVEL: SPA\nUNIDADE: {medico_sel}\n------------------\nLIBERADO: {info['p_ok']}%\nPENDENTE: {info['p_pen']}%"
    st.code(relatorio)
    st.download_button("⬇️ BAIXAR RELATORIO", relatorio.encode('utf-8-sig'), "Auditoria_SPA.txt")
    
