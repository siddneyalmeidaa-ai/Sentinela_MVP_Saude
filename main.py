import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DE ALTO IMPACTO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main .block-container {padding-top: 0.5rem; background-color: #0e1117;}
    
    /* Header SPA com Sombra 3D */
    .header-spa {
        display: flex; justify-content: space-between; align-items: center;
        padding: 12px; background: #1c232d; border-radius: 10px;
        border-bottom: 4px solid #00d4ff; 
        box-shadow: 0px 4px 15px rgba(0, 212, 255, 0.3);
        margin-bottom: 15px;
    }
    .spa-text { color: white; font-weight: 900; font-size: 1.2rem; letter-spacing: 3px; }
    </style>
    
    <div class="header-spa">
        <span style="color: #00d4ff; font-weight: 800; font-size: 0.8rem;">🏛️ IA-SENTINELA PRO</span>
        <span class="spa-text">SPA</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. DADOS E SINCRONIZAÇÃO ---
dados = {
    "ANIMA COSTA": {"lib": 13600.0, "pen": 2400.0, "p_ok": 85, "p_pen": 15},
    "DMMIGINIO GUERRA": {"lib": 17550.0, "pen": 4950.0, "p_ok": 78, "p_pen": 22}
}
medico_sel = st.selectbox("Unidade:", list(dados.keys()))
info = dados[medico_sel]

# --- 3. GRÁFICO DE PIZZA COM EFEITO DE PROFUNDIDADE (3D VISUAL) ---
st.markdown("<h4 style='text-align: center; color: #00d4ff;'>📊 Visão de Auditoria 3D</h4>", unsafe_allow_html=True)

df_pizza = pd.DataFrame({
    "Status": ["LIBERADO", "PENDENTE"],
    "Valor": [info['p_ok'], info['p_pen']],
    "Porcentagem": [f"{info['p_ok']}%", f"{info['p_pen']}%"]
})

st.vega_lite_chart(df_pizza, {
    "width": "container", "height": 450,
    "layer": [
        # Camada 1: Sombra Inferior (Dá o efeito de profundidade 3D)
        {
            "mark": {"type": "arc", "innerRadius": 75, "outerRadius": 125, "fill": "black", "opacity": 0.5},
            "encoding": {"theta": {"field": "Valor", "type": "quantitative"}}
        },
        # Camada 2: Gráfico Principal
        {
            "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 120, "stroke": "#0e1117", "strokeWidth": 3},
            "encoding": {
                "theta": {"field": "Valor", "type": "quantitative"},
                "color": {
                    "field": "Status", 
                    "scale": {"range": ["#00d4ff", "#ff4b4b"]}, 
                    "legend": {"orient": "bottom", "labelColor": "white", "fontSize": 14}
                }
            }
        },
        # Camada 3: PERCENTUAIS EM DESTAQUE (SPA Ouro)
        {
            "mark": {"type": "text", "radius": 95, "fontSize": 24, "fontWeight": "bold", "fill": "white", "stroke": "black", "strokeWidth": 1},
            "encoding": {
                "theta": {"field": "Valor", "type": "quantitative"},
                "text": {"field": "Porcentagem", "type": "nominal"}
            }
        }
    ]
})

# --- 4. TABELA DA FAVELINHA ---
st.markdown("---")
st.markdown("### 🏘️ Tabela da Favelinha")
st.markdown(f"""
| Métrica | Percentual | Ação Imediata |
| :--- | :--- | :--- |
| **LIBERADO** | <span style="color:#00d4ff">{info['p_ok']}%</span> | **ENTRA** |
| **PENDENTE** | <span style="color:#ff4b4b">{info['p_pen']}%</span> | **PULA** |
| **VÁCUO** | 0% | **NÃO ENTRA** |
""", unsafe_allow_html=True)

st.button("🚀 EXPORTAR RELATÓRIO SPA (.TXT)")
