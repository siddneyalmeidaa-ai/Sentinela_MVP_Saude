import streamlit as st
import pd

# --- 🏛️ CONFIGURAÇÃO DE ALTO NÍVEL ---
st.set_page_config(page_title="IA-SENTINELA PRO", page_icon="💎", layout="wide")

# CSS para compactar o cabeçalho e métricas no celular
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    /* Diminui o Título Principal */
    h1 { font-size: 1.4rem !important; margin-bottom: 0.5rem !important; padding-top: 0px !important; }
    /* Compacta as Métricas */
    [data-testid="stMetricValue"] { font-size: 1.0rem !important; line-height: 1 !important; }
    [data-testid="stMetricLabel"] { font-size: 0.6rem !important; }
    /* Ajusta o espaçamento geral */
    .block-container { padding-top: 0.5rem !important; padding-bottom: 0px !important; }
    /* Tabela compacta */
    .stTable { font-size: 0.7rem !important; }
    </style>
    """, unsafe_allow_html=True)

# Título Curto para não ocupar a tela inteira
st.title("🏛️ IA-SENTINELA: AUDITORIA")

# --- 🧠 INTELIGÊNCIA DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Erro XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Cadastro"}
}

# Sidebar discreta
with st.sidebar:
    medico_sel = st.selectbox("Alvo:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento_real = st.number_input("Valor:", value=info["valor"])

# --- 📈 CÁLCULOS ---
v_pendente = faturamento_real * 0.32
v_liberado = faturamento_real * 0.68
tkt_medio = faturamento_real / info["pacientes"]

# --- 📊 MÉTRICAS EM LINHA (SUPER COMPACTAS) ---
c1, c2, c3 = st.columns(3)
c1.metric("PACIENTES", f"{info['pacientes']}")
c2.metric("TKT MÉDIO", f"R${tkt_medio:,.0f}")
c3.metric("RETIDO", f"R${v_pendente:,.0f}", "-32%")

# --- 🍕 PIZZA COMPACTA (TAMANHO FIXO PARA NÃO QUEBRAR) ---
df_pizza = pd.DataFrame({"Status": ["RISCO (32%)", "LIBERADO (68%)"], "Valor": [32, 68]})

st.vega_lite_chart(df_pizza, {
    'width': 280, 'height': 150, # Tamanho forçado para mobile
    'mark': {'type': 'arc', 'innerRadius': 35, 'outerRadius': 60, 'cornerRadius': 4},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#ff0055', '#00d4ff']}}
    },
    'config': {'legend': {'labelFontSize': 8, 'symbolSize': 50}}
})

# --- 🚨 LISTA DE PACIENTES (AÇÃO RÁPIDA) ---
st.markdown(f"**📋 Pendências: {medico_sel}**")
df_p = pd.DataFrame({
    "Paciente": info["pendentes"],
    "Motivo": [info["motivo"]] * len(info["pendentes"])
})
st.table(df_p)

# --- 🚀 BOTÃO ---
if st.button("📊 RELATÓRIO FINAL"):
    st.write(f"**Garantido:** R$ {v_liberado:,.2f}")
    st.error(f"Bloqueio: {info['motivo']}")
    
