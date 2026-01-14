import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO PREMIUM (Mobile First) ---
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

# --- 2. BANCO DE DADOS (Sincronizado) ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

medico_sel = st.selectbox("Unidade para Auditoria:", list(dados.keys()))
info = dados[medico_sel]

# --- 3. SISTEMA DE ABAS UNIFICADO (Todas as funções de volta) ---
tab_dados, tab_pizza, tab_barras, tab_relatorio = st.tabs([
    "📋 DADOS", "⭕ PIZZA (%)", "📊 BARRAS (R$)", "📩 RELATÓRIO"
])

with tab_dados:
    st.markdown(f"### 🏘️ Tabela da Favelinha - {medico_sel}")
    df_fav = pd.DataFrame({
        "Métrica": ["LIBERADO", "PENDENTE", "VÁCUO"],
        "Percentual": [f"{info['p_ok']}%", f"{info['p_pen']}%", "0%"],
        "Ação": ["ENTRA", "PULA", "NÃO ENTRA"]
    })
    st.table(df_fav) # Entrega visual direta conforme solicitado [cite: 12-28-2025]
    
    st.markdown("---")
    st.markdown("#### Detalhamento Financeiro")
    st.metric("Total Liberado", f"R$ {info['lib']:,.2f}", f"{info['p_ok']}%")
    st.metric("Total Pendente", f"R$ {info['pen']:,.2f}", f"-{info['p_pen']}%", delta_color="inverse")

with tab_pizza:
    st.markdown("<h4 style='text-align: center;'>Distribuição Auditada</h4>", unsafe_allow_html=True)
    # Correção: Percentual direto na legenda para leitura rápida no celular
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
    st.markdown("<h4 style='text-align: center;'>Volume em Reais (R$)</h4>", unsafe_allow_html=True)
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
            {"mark": {"type": "text", "baseline": "bottom", "dy": -10, "fontSize": 15, "fill": "white"},
             "encoding": {
                 "x": {"field": "Status", "type": "nominal"},
                 "y": {"field": "Valor", "type": "quantitative"},
                 "text": {"field": "Texto"}}}
        ]
    })

with tab_relatorio:
    st.markdown("### 📄 Dossiê de Auditoria SPA")
    relatorio_txt = (
        f"SISTEMA IA-SENTINELA - DOSSIÊ OFICIAL\n"
        f"UNIDADE: {medico_sel}\n"
        f"-----------------------------------\n"
        f"LIBERADO: {info['p_ok']}% (R$ {info['lib']:,.2f}) -> ENTRA\n"
        f"PENDENTE: {info['p_pen']}% (R$ {info['pen']:,.2f}) -> PULA\n"
        f"VÁCUO: 0% -> NÃO ENTRA\n"
        f"-----------------------------------\n"
        f"AUDITORIA CONCLUÍDA POR: SPA"
    )
    st.code(relatorio_txt)
    # Download configurado sem erro de acento no celular [cite: 01-12-2026]
    st.download_button(
        label="⬇️ BAIXAR RELATÓRIO (.TXT)",
        data=relatorio_txt.encode('utf-8-sig'),
        file_name=f"Auditoria_{medico_sel}.txt",
        mime="text/plain"
    )

st.markdown("---")
st.caption("IA-SENTINELA PRO - Sistema de Gestão Operacional")
    
