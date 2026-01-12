import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO DE ALTO NÍVEL ---
st.set_page_config(page_title="IA-SENTINELA PRO", page_icon="💎", layout="wide")

# CSS para interface compacta e profissional
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 1.1rem !important; color: #00d4ff; }
    [data-testid="stMetricLabel"] { font-size: 0.7rem !important; }
    .main { background-color: #0e1117; }
    div.block-container { padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ IA-SENTINELA PRO")

# --- 🧠 INTELIGÊNCIA DE DADOS (SIMULANDO PACIENTES POR MÉDICO) ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "pendentes": ["Carlos Silva", "Maria Oliveira"], "motivo": "Divergência de XML"},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "pendentes": ["João Souza", "Ana Costa"], "motivo": "Assinatura Digital"},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "pendentes": ["Pedro Santos", "Luana Vaz"], "motivo": "Erro Cadastral"}
}

with st.sidebar:
    st.header("CONTROLE")
    medico_sel = st.selectbox("Médico", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento_real = st.number_input("Valor Bruto", value=info["valor"])

# --- 📈 CÁLCULOS ---
v_pendente = faturamento_real * 0.32
v_liberado = faturamento_real * 0.68
tkt_medio = faturamento_real / info["pacientes"]

# --- 📊 CARDS COMPACTOS ---
c1, c2, c3 = st.columns(3)
c1.metric("VOL. TOTAL", f"{info['pacientes']}")
c2.metric("TKT MÉDIO", f"R${tkt_medio:,.0f}")
c3.metric("RETIDO", f"R${v_pendente:,.0f}", "-32%")

# --- 🍕 PIZZA AJUSTADA PARA MOBILE ---
df_pizza = pd.DataFrame({"Status": ["RISCO (32%)", "LIBERADO (68%)"], "Valor": [32, 68]})
st.vega_lite_chart(df_pizza, {
    'width': 'container', 'height': 180,
    'mark': {'type': 'arc', 'innerRadius': 40, 'cornerRadius': 5, 'padAngle': 2},
    'encoding': {'theta': {'field': 'Valor', 'type': 'quantitative'},
                 'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#ff0055', '#00d4ff']}}}
})

# --- 🚨 LISTA DE PACIENTES PENDENTES (AÇÃO IMEDIATA) ---
st.markdown(f"### 📋 Pendências: {medico_sel}")
df_pendentes = pd.DataFrame({
    "Paciente": info["pendentes"],
    "Status": ["PENDENTE 🔴"] * len(info["pendentes"]),
    "Motivo": [info["motivo"]] * len(info["pendentes"])
})
st.table(df_pendentes) # Tabela simples e rápida de ler no celular

# --- 🚀 DOSSIÊ DETALHADO ---
if st.button("📊 GERAR RELATÓRIO"):
    with st.expander("📄 DETALHAMENTO FINAL", expanded=True):
        st.write(f"**Garantido:** R$ {v_liberado:,.2f}")
        st.error(f"**Motivo Principal:** {info['motivo']}")
        st.success("✅ Auditoria pronta para correção.")
        
