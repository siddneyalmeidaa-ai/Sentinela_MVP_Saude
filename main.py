import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE TELA (PADRÃO OURO) ---
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

# --- 2. DADOS (Sincronizados) ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}
medico_sel = st.selectbox("Unidade:", list(dados.keys()))
info = dados[medico_sel]

# --- 3. NAVEGAÇÃO POR ABAS (GRÁFICOS E RELATÓRIO) ---
tab_pizza, tab_barras, tab_relatorio = st.tabs(["⭕ PIZZA (%)", "📊 BARRAS (R$)", "📄 RELATÓRIO"])

with tab_pizza:
    st.markdown("<h4 style='text-align: center;'>Distribuição Percentual</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({
        "Status": [f"LIBERADO ({info['p_ok']}%)", f"PENDENTE ({info['p_pen']}%)"],
        "Valor": [info['p_ok'], info['p_pen']]
    })
    st.vega_lite_chart(df_p, {
        "width": "container", "height": 400,
        "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 110},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white", "fontSize": 16}}
        }
    })

with tab_barras:
    st.markdown("<h4 style='text-align: center;'>Volume em Reais (R$)</h4>", unsafe_allow_html=True)
    df_b = pd.DataFrame({
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [info['lib'], info['pen']],
        "Txt": [f"R$ {info['lib']:,.0f}", f"R$ {info['pen']:,.0f}"]
    })
    st.vega_lite_chart(df_b, {
        "width": "container", "height": 350,
        "layer": [
            {"mark": {"type": "bar", "color": "#00d4ff", "cornerRadiusTop": 8},
             "encoding": {"x": {"field": "Status", "axis": {"labelAngle": 0}}, "y": {"field": "Valor", "axis": None}}},
            {"mark": {"type": "text", "baseline": "bottom", "dy": -10, "fontSize": 16, "fill": "white"},
             "encoding": {"x": {"field": "Status"}, "y": {"field": "Valor"}, "text": {"field": "Txt"}}}
        ]
    })

with tab_relatorio:
    st.markdown("### 📝 Dossiê de Auditoria Final")
    # Texto limpo para garantir abertura imediata no celular [cite: 01-12-2026]
    relat_txt = (
        f"CERTIFICADO DE AUDITORIA SPA\n"
        f"UNIDADE: {medico_sel}\n"
        f"---------------------------\n"
        f"LIBERADO: {info['p_ok']}% (R$ {info['lib']:,.2f}) -> ENTRA\n"
        f"PENDENTE: {info['p_pen']}% (R$ {info['pen']:,.2f}) -> PULA\n"
        f"VÁCUO: 0% -> NÃO ENTRA\n"
        f"---------------------------\n"
        f"RESPONSÁVEL: SPA"
    )
    st.text_area(label="Conteúdo do Relatório", value=relat_txt, height=250)
    
    # Botão de Download sem erro de acento [cite: 01-12-2026]
    st.download_button(
        label="⬇️ BAIXAR RELATÓRIO OFICIAL",
        data=relat_txt.encode('utf-8-sig'),
        file_name=f"Relatorio_{medico_sel}.txt",
        mime="text/plain"
    )
    
