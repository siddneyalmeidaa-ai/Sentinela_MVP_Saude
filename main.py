import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL & BLINDAGEM SELETIVA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    /* 🛡️ BLINDAGEM: OCULTA APENAS O QUE É PERIGOSO (DIREITA) */
    #MainMenu {visibility: hidden;}          /* Oculta Menu hambúrguer */
    header .stDeployButton {display:none;}   /* Oculta botão de Deploy */
    header .st-emotion-cache-15ec66s {display:none;} /* Oculta GitHub e Lápis */
    footer {visibility: hidden;}             /* Oculta rodapé */

    /* ✅ OPERACIONAL: MANTÉM AS ABAS E CABEÇALHO VISÍVEIS */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 10px; background: #1c232d; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.1rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V17 - PROTEGIDO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS PADRÃO OURO (CORRIGIDA) ---
dados_medicos = {
    "ANIMA COSTA": {
        "valor": 16000.0, "motivo": "Divergência de XML", "risco": 15,
        "detalhes": [["João Silva", "XML Inválido"], ["Maria Oliveira", "Divergência Tuss"]]
    },
    "DMMIGINIO GUERRA": {
        "valor": 22500.0, "motivo": "Assinatura Digital", "risco": 45,
        "detalhes": [["João Souza", "Falta Assinatura"], ["Ana Costa", "Falta Assinatura"]]
    },
    "CLÍNICA SÃO JOSÉ": {
        "valor": 45000.0, "motivo": "Erro Cadastral", "risco": 18,
        "detalhes": [["Carlos Luz", "CPF Inválido"], ["Bia Rosa", "Guia Ausente"]]
    }
}

# --- 3. BARRA LATERAL (FILTROS) ---
with st.sidebar:
    st.header("⚙️ Filtros Alpha")
    medico_sel = st.selectbox("Selecione o Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    p_risco = st.slider("Ajustar Risco (%)", 0, 100, info["risco"])
    p_ok = 100 - p_risco

# --- 4. CÁLCULOS DINÂMICOS ---
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

# --- 5. INTERFACE DE TRABALHO (ABAS VOLTARAM) ---
tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"### Análise: {medico_sel}")
    col_a, col_b = st.columns(2)
    # Sincronização automática de títulos
    col_a.metric(f"{p_ok}% LIBERADO", f"R$ {v_liberado:,.2f}")
    col_b.metric(f"{p_risco}% PENDENTE", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.markdown("#### 📋 LISTA DE PACIENTES")
    st.dataframe(pd.DataFrame(info["detalhes"], columns=["Paciente", "Motivo"]), use_container_width=True)

with tab2:
    st.markdown("#### Distribuição de Auditoria")
    df_p = pd.DataFrame({'Status': [f'{p_ok}% LIBERADO', f'{p_risco}% PENDENTE'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_p, {
        'width': 'container', 'height': 300,
        'mark': {'type': 'arc', 'innerRadius': 70, 'outerRadius': 110},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}}
        }
    })

with tab3:
    if st.button("🔄 GERAR DOSSIÊ DETALHADO"):
        pendencias = "".join([f"- {p[0]}: {p[1]}\n" for p in info["detalhes"]])
        relatorio = f"MÉDICO: {medico_sel}\nLIBERADO: {p_ok}%\nPENDENTE: {p_risco}%\n\nDETALHES:\n{pendencias}"
        st.code(relatorio)
        st.download_button("⬇️ BAIXAR (.TXT)", relatorio.encode('utf-8-sig'), f"Dossie_{medico_sel}.txt")
    
