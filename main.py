import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL E SEGURANÇA (BLINDAGEM) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    /* Oculta menus de edição e botões de sistema à direita */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header .st-emotion-cache-15ec66s {display:none;}
    footer {visibility: hidden;}

    /* Design Premium do Cabeçalho */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 15px; background: linear-gradient(90deg, #1c232d, #0e1117); 
        border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 25px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 3px 10px; border-radius: 4px; font-weight: 900; font-size: 0.8rem; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.3rem;">🏛️ SISTEMA: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V18 - PREMIUM</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS SINCRONIZADA ---
dados_medicos = {
    "ANIMA COSTA": {
        "faturamento": 16000.0,
        "pacientes": [
            {"nome": "João Silva", "erro": "XML Inválido"},
            {"nome": "Maria Oliveira", "erro": "Divergência Tuss"}
        ]
    },
    "DMMIGINIO GUERRA": {
        "faturamento": 22500.0,
        "pacientes": [
            {"nome": "João Souza", "erro": "Falta Assinatura"},
            {"nome": "Ana Costa", "erro": "Falta Assinatura"}
        ]
    }
}

# --- 3. CONTROLES LATERAIS ---
with st.sidebar:
    st.header("⚙️ Filtros Alpha")
    medico_sel = st.selectbox("Selecione o Médico:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    
    # Slider que comanda os valores em tempo real
    p_ok = st.slider("Liberação (%)", 0, 100, 85)
    p_risco = 100 - p_ok

# --- 4. CÁLCULOS FINANCEIROS ---
v_total = info["faturamento"]
v_liberado = v_total * (p_ok / 100)
v_pendente = v_total * (p_risco / 100)
# Rateio do prejuízo por paciente
valor_por_glosa = v_pendente / len(info["pacientes"])

# --- 5. INTERFACE OPERACIONAL (ABAS RESTAURADAS) ---
tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"### Análise de Dados: {medico_sel}")
    col1, col2 = st.columns(2)
    col1.metric(f"{p_ok}% LIBERADO", f"R$ {v_liberado:,.2f}")
    col2.metric(f"{p_risco}% PENDENTE", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.markdown("#### 📋 Gastos por Pendência")
    # Tabela detalhada com valores por paciente
    lista_pacientes = []
    for p in info["pacientes"]:
        lista_pacientes.append({
            "Paciente": p["nome"],
            "Motivo": p["erro"],
            "Valor da Glosa": f"R$ {valor_por_glosa:,.2f}"
        })
    st.table(lista_pacientes)

with tab2:
    st.write("**Status de Liberação (%)**")
    df_pizza = pd.DataFrame({'Status': ['Liberado', 'Pendente'], 'Valor': [p_ok, p_risco]})
    st.vega_lite_chart(df_pizza, {
        'mark': {'type': 'arc', 'innerRadius': 60, 'outerRadius': 100},
        'encoding': {
            'theta': {'field': 'Valor', 'type': 'quantitative'},
            'color': {'field': 'Status', 'scale': {'range': ['#228B22', '#8B0000']}}
        }
    })

with tab3:
    if st.button("🚀 GERAR DOSSIÊ DETALHADO"):
        detalhes_txt = "".join([f"- {p['nome']} ({p['erro']}): R$ {valor_por_glosa:,.2f}\n" for p in info["pacientes"]])
        relatorio = f"""
==========================================
   DOSSIÊ DE AUDITORIA - IA-SENTINELA 
==========================================
UNIDADE: {medico_sel}
STATUS: {p_ok}% LIBERADO / {p_risco}% PENDENTE
------------------------------------------
VALOR LIBERADO: R$ {v_liberado:,.2f}
VALOR PENDENTE: R$ {v_pendente:,.2f}

DETALHAMENTO POR PACIENTE:
{detalhes_txt}
=========================================="""
        st.code(relatorio)
        st.download_button("⬇️ BAIXAR RELATÓRIO (.TXT)", relatorio.encode('utf-8-sig'), f"Auditoria_{medico_sel}.txt")
        
