import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE TELA E ESTILO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

# Estilo para remover o topo do sistema e criar o layout de cartões
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0rem; background-color: #0e1117;}
    
    /* Banner do Sidney */
    .brand-banner {
        background: linear-gradient(90deg, #1c232d 0%, #0e1117 100%);
        padding: 15px;
        border-radius: 12px;
        border-left: 6px solid #00d4ff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .user-name { color: white; font-size: 1.2rem; font-weight: 800; margin: 0; }
    .user-sub { color: #00d4ff; font-size: 0.7rem; font-weight: 900; letter-spacing: 1px; }

    /* Estilo dos Cards de Métricas */
    .st-card {
        background: #1c232d;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #262730;
        text-align: center;
    }
    </style>

    <div class="brand-banner">
        <div>
            <span style="color: #00d4ff; font-weight: 900; font-size: 1rem;">🏛️ IA-SENTINELA PRO</span><br>
            <span style="color: white; font-size: 0.7rem;">SISTEMA DE AUDITORIA</span>
        </div>
        <div style="text-align: right;">
            <p class="user-name">SIDNEY PEREIRA DE ALMEIDA</p>
            <p class="user-sub">DIRETOR OPERACIONAL</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS (Sincronizado) ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

# --- 3. SELEÇÃO E NAVEGAÇÃO ---
medico_sel = st.selectbox("🎯 Selecione a Unidade:", list(dados.keys()))
info = dados[medico_sel]

tab1, tab2, tab3 = st.tabs(["📋 PAINEL", "📊 PERFORMANCE", "📩 EXPORTAR"])

with tab1:
    # Métricas em Cards Lado a Lado
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='st-card'><p style='color:grey;font-size:0.8rem;'>{info['p_ok']}% LIBERADO</p><h3 style='color:#00d4ff;margin:0;'>R$ {info['lib']:,.2f}</h3></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='st-card'><p style='color:grey;font-size:0.8rem;'>{info['p_pen']}% PENDENTE</p><h3 style='color:#ff4b4b;margin:0;'>R$ {info['pen']:,.2f}</h3></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 📌 Lista de Auditoria")
    st.table(pd.DataFrame({"Paciente": ["João Silva", "Maria Oliveira"], "Status": ["OK", "PENDENTE"], "Valor": ["R$ 1.200", "R$ 1.200"]}))

with tab2:
    # GRÁFICOS LADO A LADO (Pizza e Barras)
    st.markdown("#### 📊 Análise Comparativa")
    col_graph1, col_graph2 = st.columns(2)
    
    with col_graph1:
        st.write("Pizza (%)")
        df_p = pd.DataFrame({"Cat": ["OK", "PEN"], "Val": [info['p_ok'], info['p_pen']]})
        st.vega_lite_chart(df_p, {
            "width": "container", "height": 180,
            "mark": {"type": "arc", "innerRadius": 40, "outerRadius": 65},
            "encoding": {
                "theta": {"field": "Val", "type": "quantitative"},
                "color": {"field": "Cat", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": None}
            }
        })

    with col_graph2:
        st.write("Barras (R$)")
        df_b = pd.DataFrame({"Cat": ["LIB", "PEN"], "Val": [info['lib'], info['pen']]})
        st.vega_lite_chart(df_b, {
            "width": "container", "height": 180,
            "mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTopLeft": 5, "cornerRadiusTopRight": 5},
            "encoding": {
                "x": {"field": "Cat", "type": "nominal", "axis": {"labelAngle": 0}},
                "y": {"field": "Val", "type": "quantitative", "axis": None}
            }
        })

with tab3:
    st.markdown("#### 📄 Gerar Relatório")
    st.button("🚀 EXPORTAR DOSSIÊ COMPLETO")
    
