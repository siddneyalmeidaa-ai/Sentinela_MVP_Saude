import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL E BLINDAGEM DE CABEÇALHO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

# Oculta menus de sistema e mantém apenas o essencial operacional
st.markdown("""
    <style>
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
    [data-testid="stMetricValue"] { color: #00d4ff; font-weight: bold; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.3rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V20 - BLINDADO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS SINCRONIZADA (SEM ERROS DE SINTAXE) ---
# Corrigido: Todas as aspas e colchetes fechados corretamente
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

# --- 3. BARRA LATERAL (CENTRO DE COMANDO) ---
with st.sidebar:
    st.header("⚙️ Configurações Alpha")
    # Seletor de unidade/médico
    medico_sel = st.selectbox("Selecione a Unidade:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    
    # Slider dinâmico que comanda todo o sistema
    p_ok = st.slider("Porcentagem Liberada (%)", 0, 100, 85)
    p_risco = 100 - p_ok

# --- 4. MOTOR DE CÁLCULO FINANCEIRO ---
v_total = info["faturamento"]
v_liberado = v_total * (p_ok / 100)
v_pendente = v_total * (p_risco / 100)

# Cálculo dinâmico do prejuízo por paciente
num_pacientes = len(info["pacientes"])
valor_por_paciente = v_pendente / num_pacientes if num_pacientes > 0 else 0

# --- 5. INTERFACE OPERACIONAL (ABAS) ---
tab1, tab2, tab3 = st.tabs(["🏥 AUDITORIA", "📈 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"### Unidade em Análise: {medico_sel}")
    col_m1, col_m2 = st.columns(2)
    # Métricas sincronizadas com o slider
    col_m1.metric(f"{p_ok}% LIBERADO", f"R$ {v_liberado:,.2f}")
    col_m2.metric(f"{p_risco}% PENDENTE", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.markdown("---")
    st.subheader("📌 Detalhamento Financeiro por Paciente")
    
    # Tabela dinâmica que mostra os gatos das pendências
    tabela_financeira = []
    for p in info["pacientes"]:
        tabela_financeira.append({
            "Paciente": p["nome"],
            "Motivo da Glosa": p["glosa"],
            "Valor Pendente": f"R$ {valor_por_paciente:,.2f}"
        })
    st.table(tabela_financeira)

with tab2:
    st.write("**Composição de Faturamento (%)**")
    # Gráfico que responde instantaneamente ao slider
    df_pizza = pd.DataFrame({'Status': ['Liberado', 'Pendente'], 'Valor': [p_ok, p_risco]})
    st.vega_lite_chart(df_pizza, {
        'mark': {'type': 'arc', 'innerRadius': 60, 'outerRadius': 100},
        'encoding': {
            'theta': {'field': 'Valor', 'type': 'quantitative'},
            'color': {'field': 'Status', 'scale': {'range': ['#228B22', '#8B0000']}}
        }
    })

with tab3:
    if st.button("🚀 GERAR DOSSIÊ PADRÃO OURO"):
        txt_pacientes = "".join([f"- {p['nome']} ({p['glosa']}): R$ {valor_por_paciente:,.2f}\n" for p in info["pacientes"]])
        
        dossie = f"""
==========================================
   DOSSIÊ DE AUDITORIA - IA-SENTINELA 
==========================================
UNIDADE/MÉDICO : {medico_sel}
DATA EMISSÃO   : 14/01/2026
------------------------------------------
TOTAL LIBERADO : R$ {v_liberado:,.2f} ({p_ok}%)
TOTAL PENDENTE : R$ {v_pendente:,.2f} ({p_risco}%)
------------------------------------------
LISTA DE PENDÊNCIAS POR PACIENTE:
{txt_pacientes}
=========================================="""
        st.code(dossie)
        st.download_button("⬇️ BAIXAR RELATÓRIO (.TXT)", dossie.encode('utf-8-sig'), f"Auditoria_{medico_sel}.txt")
    
