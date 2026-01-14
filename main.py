import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    /* Oculta apenas elementos de sistema do topo direito */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header .st-emotion-cache-15ec66s {display:none;}
    footer {visibility: hidden;}

    /* Design VIP Sentinela */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 15px; background: linear-gradient(90deg, #1c232d, #0e1117); 
        border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 25px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 3px 10px; border-radius: 4px; font-weight: 900; font-size: 0.8rem; }
    [data-testid="stMetricValue"] { color: #00d4ff !important; font-size: 1.8rem !important; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.2rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V24 - TOTAL</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (REVISADA) ---
dados_medicos = {
    "ANIMA COSTA": {
        "faturamento": 16000.0,
        "pacientes": [
            {"nome": "João Silva", "glosa": "XML Inválido"},
            {"nome": "Maria Oliveira", "glosa": "Divergência Tuss"}
        ]
    },
    "DMMIGINIO GUERRA": {
        "faturamento": 22500.0,
        "pacientes": [
            {"nome": "João Souza", "glosa": "Assinatura Digital"},
            {"nome": "Ana Costa", "glosa": "Falta Assinatura"}
        ]
    }
}

# --- 3. ÁREA DE TRABALHO E ABAS ---
tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA / AUDITORIA", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    # SELEÇÃO INTERNA: Agora dentro da interface para não sumir ao ocultar cabeçalho
    st.subheader("🕵️ Seleção de Auditoria")
    col_sel1, col_sel2 = st.columns([1, 1])
    
    with col_sel1:
        medico_sel = st.selectbox("Médico/Unidade:", list(dados_medicos.keys()))
        info = dados_medicos[medico_sel]
    
    with col_sel2:
        p_ok = st.slider("Porcentagem Liberada (%):", 0, 100, 85)
        p_risco = 100 - p_ok

    st.markdown("---")
    
    # Cálculos Sincronizados
    v_total = info["faturamento"]
    v_liberado = v_total * (p_ok / 100)
    v_pendente = v_total * (p_risco / 100)
    valor_individual = v_pendente / len(info["pacientes"]) if info["pacientes"] else 0

    c1, c2 = st.columns(2)
    c1.metric(f"{p_ok}% LIBERADO", f"R$ {v_liberado:,.2f}")
    c2.metric(f"{p_risco}% PENDENTE", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.markdown("#### 📌 Detalhamento por Paciente")
    tabela_resumo = []
    for p in info["pacientes"]:
        tabela_resumo.append({
            "Paciente": p["nome"],
            "Motivo": p["glosa"],
            "Glosa Indiv.": f"R$ {valor_individual:,.2f}"
        })
    st.table(tabela_resumo)

with tab2:
    st.write("**Composição de Auditoria**")
    df_pizza = pd.DataFrame({'Status': ['Liberado', 'Pendente'], 'Valor': [p_ok, p_risco]})
    st.vega_lite_chart(df_pizza, {
        'mark': {'type': 'arc', 'innerRadius': 50, 'outerRadius': 90},
        'encoding': {
            'theta': {'field': 'Valor', 'type': 'quantitative'},
            'color': {'field': 'Status', 'scale': {'range': ['#228B22', '#8B0000']}}
        }
    })

with tab3:
    if st.button("🚀 GERAR RELATÓRIO FINAL"):
        detalhes = "".join([f"- {p['nome']} ({p['glosa']}): R$ {valor_individual:,.2f}\n" for p in info["pacientes"]])
        relatorio = f"""
==========================================
   DOSSIÊ DE AUDITORIA - IA-SENTINELA 
==========================================
MÉDICO   : {medico_sel}
DATA     : 14/01/2026
------------------------------------------
LIBERADO : R$ {v_liberado:,.2f} ({p_ok}%)
PENDENTE : R$ {v_pendente:,.2f} ({p_risco}%)

PENDÊNCIAS DETALHADAS:
{detalhes}
=========================================="""
        st.code(relatorio)
        st.download_button("⬇️ BAIXAR (.TXT)", relatorio.encode('utf-8-sig'), f"Auditoria_{medico_sel}.txt")
    
