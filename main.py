import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E OCULTAÇÃO DO CABEÇALHO DIREITO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    /* Oculta apenas os itens do sistema no canto superior direito */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header .st-emotion-cache-15ec66s {display:none;}
    footer {visibility: hidden;}

    /* Design VIP do Cabeçalho Principal */
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
        <span class="pro-tag">PRO V23 - ESTÁVEL</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (CORREÇÃO DE SINTAXE) ---
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

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.header("⚙️ Configurações Alpha")
    medico_sel = st.selectbox("Selecione a Unidade:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    
    # Controle central de porcentagem
    p_ok = st.slider("Porcentagem Liberada (%)", 0, 100, 85)
    p_risco = 100 - p_ok

# --- 4. MOTOR DE CÁLCULO SINCRONIZADO ---
v_total = info["faturamento"]
v_liberado = v_total * (p_ok / 100)
v_pendente = v_total * (p_risco / 100)

# Cálculo do gasto individual por paciente
num_pacientes = len(info["pacientes"])
valor_por_paciente = v_pendente / num_pacientes if num_pacientes > 0 else 0

# --- 5. INTERFACE OPERACIONAL (ABAS) ---
tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"### Auditoria Ativa: {medico_sel}")
    col1, col2 = st.columns(2)
    col1.metric(f"{p_ok}% LIBERADO", f"R$ {v_liberado:,.2f}")
    col2.metric(f"{p_risco}% PENDENTE", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.markdown("---")
    st.subheader("📌 Gasto Detalhado por Paciente")
    
    # Tabela dinâmica com os valores atualizados pelo slider
    lista_detalhada = []
    for p in info["pacientes"]:
        lista_detalhada.append({
            "Paciente": p["nome"],
            "Motivo da Pendência": p["glosa"],
            "Valor da Glosa": f"R$ {valor_por_paciente:,.2f}"
        })
    st.table(lista_detalhada)

with tab2:
    st.write("**Composição de Auditoria**")
    # Gráfico que responde ao slider
    df_grafico = pd.DataFrame({'Status': ['Liberado', 'Pendente'], 'Valor': [p_ok, p_risco]})
    st.vega_lite_chart(df_grafico, {
        'mark': {'type': 'arc', 'innerRadius': 50, 'outerRadius': 90},
        'encoding': {
            'theta': {'field': 'Valor', 'type': 'quantitative'},
            'color': {'field': 'Status', 'scale': {'range': ['#228B22', '#8B0000']}}
        }
    })

with tab3:
    if st.button("🚀 GERAR RELATÓRIO DETALHADO"):
        detalhes_rel = "".join([f"- {p['nome']} ({p['glosa']}): R$ {valor_por_paciente:,.2f}\n" for p in info["pacientes"]])
        txt = f"""
==========================================
   DOSSIÊ DE AUDITORIA - IA-SENTINELA 
==========================================
UNIDADE  : {medico_sel}
DATA     : 14/01/2026
------------------------------------------
TOTAL LIBERADO : R$ {v_liberado:,.2f}
TOTAL PENDENTE : R$ {v_pendente:,.2f}

DETALHAMENTO POR PACIENTE:
{detalhes_rel}
=========================================="""
        st.code(txt)
        st.download_button("⬇️ BAIXAR (.TXT)", txt.encode('utf-8-sig'), f"Relatorio_{medico_sel}.txt")
                                                                    
