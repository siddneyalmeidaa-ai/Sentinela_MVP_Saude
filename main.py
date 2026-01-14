import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE TELA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}

    /* HEADER SPA */
    .header-spa {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px; background: #1c232d; border-radius: 8px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 10px;
    }
    .spa-text { color: white; font-weight: 900; font-size: 1rem; letter-spacing: 2px; }
    </style>
    
    <div class="header-spa">
        <span style="color: #00d4ff; font-weight: 800; font-size: 0.7rem;">🏛️ IA-SENTINELA PRO</span>
        <span class="spa-text">SPA</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. DADOS (Sincronizados Automaticamente) ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}

# --- 3. SELEÇÃO DE UNIDADE ---
medico_sel = st.selectbox("Unidade:", list(dados.keys()))
info = dados[medico_sel]

# --- 4. NAVEGAÇÃO POR CHIPS (Abas Separadas para não amassar) ---
# Aqui separamos cada gráfico em uma "chip" diferente
tab_dados, tab_pizza, tab_barras, tab_relatorio = st.tabs([
    "📋 DADOS", "⭕ PIZZA (%)", "📊 BARRAS (R$)", "📩 EXPORTAR"
])

with tab_dados:
    st.markdown(f"### Unidade: {medico_sel}")
    st.write(f"**Liberado:** {info['p_ok']}% — R$ {info['lib']:,.2f}")
    st.write(f"**Pendente:** {info['p_pen']}% — R$ {info['pen']:,.2f}")
    st.markdown("---")
    st.table(pd.DataFrame({
        "Paciente": ["João Silva", "Maria Oliveira"],
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [f"R$ {info['lib']/10:,.2f}", f"R$ {info['pen']/2:,.2f}"]
    }))

with tab_pizza:
    st.markdown("<h4 style='text-align: center;'>Distribuição Percentual</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({"Status": ["LIBERADO", "PENDENTE"], "Valor": [info['p_ok'], info['p_pen']]})
    st.vega_lite_chart(df_p, {
        "width": "container", "height": 350,
        "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 110},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {"field": "Status", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
        }
    })

with tab_barras:
    st.markdown("<h4 style='text-align: center;'>Valores em Reais (R$)</h4>", unsafe_allow_html=True)
    df_b = pd.DataFrame({"Cat": ["LIBERADO", "PENDENTE"], "Valor": [info['lib'], info['pen']]})
    st.vega_lite_chart(df_b, {
        "width": "container", "height": 350,
        "mark": {"type": "bar", "cornerRadiusTopLeft": 8, "cornerRadiusTopRight": 8},
        "encoding": {
            "x": {"field": "Cat", "type": "nominal", "axis": {"labelAngle": 0, "title": None}},
            "y": {"field": "Valor", "type": "quantitative", "axis": {"title": "Valor R$"}},
            "color": {"field": "Cat", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": None}
        }
    })

with tab_relatorio:
    st.markdown("### 📄 Dossiê SPA")
    relat = f"SISTEMA IA-SENTINELA\nRESPONSÁVEL: SPA\nUNIDADE: {medico_sel}\nOK: {info['p_ok']}%\nPEN: {info['p_pen']}%"
    st.code(relat)
    st.download_button("⬇️ BAIXAR RELATÓRIO (.TXT)", relat.encode('utf-8-sig'), "Auditoria_SPA.txt")
    
