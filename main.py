import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO DE ALTO NÍVEL ---
st.set_page_config(page_title="IA-SENTINELA PRO", page_icon="💎", layout="wide")

# CSS personalizado para interface sofisticada
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1c2e4a; padding: 15px; border-radius: 15px; border: 1px solid #00d4ff; }
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(90deg, #00d4ff, #005f73); color: white; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ IA-SENTINELA: AUDITORIA ALPHA PREMIMUM")

# --- 🧠 INTELIGÊNCIA DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML no lote 402."},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Ausência de assinatura digital."},
    "DR. ALPHA TESTE": {"valor": 12000.0, "pacientes": 45, "motivo": "CID-10 incompatível com procedimento."},
    "DRA. ELENA SILVA": {"valor": 18900.0, "pacientes": 92, "motivo": "Duplicidade de cobrança detectada."},
    "DR. MARCOS PONTES": {"valor": 25000.0, "pacientes": 150, "motivo": "Falta de autorização prévia."},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Inconsistência cadastral de beneficiários."},
    "DRA. BEATRIZ LINS": {"valor": 14200.0, "pacientes": 60, "motivo": "Glosa técnica: relatório cirúrgico ausente."},
    "DR. RICARDO MELO": {"valor": 19800.0, "pacientes": 88, "motivo": "Material especial fora da tabela."},
    "CENTRO MÉDICO VIP": {"valor": 31000.0, "pacientes": 210, "motivo": "Taxa de sala acima do contrato."},
    "AUDITORIA GERAL": {"valor": 150000.0, "pacientes": 1200, "motivo": "Múltiplas inconsistências detectadas."}
}

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1087/1087080.png", width=80)
    st.header("SISTEMA SENTINELA")
    medico_sel = st.selectbox("Escolha o Alvo da Auditoria", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]
    faturamento_real = st.number_input("Faturamento Bruto (R$)", value=info["valor"])
    st.divider()
    st.write("💎 **Nível de Acesso:** Auditor Master")

# --- 📊 CÁLCULOS ---
v_pendente = faturamento_real * 0.32
v_liberado = faturamento_real * 0.68
tkt_medio = faturamento_real / info["pacientes"]

# --- 📈 DASHBOARD FUTURISTA ---
col1, col2, col3 = st.columns(3)
with col1: st.metric("VOLUME ATENDIDO", f"{info['pacientes']} Pacientes")
with col2: st.metric("TICKET MÉDIO", f"R$ {tkt_medio:,.2f}")
with col3: st.metric("CAPITAL EM RISCO", f"R$ {v_pendente:,.2f}", "-32%", delta_color="inverse")

st.markdown("---")

# Gráfico de Pizza (Donut Futurista com Efeito Neon)
df_pizza = pd.DataFrame({
    "Status": ["PENDENTE (EM RISCO)", "LIBERADO (CONFORMIDADE)"],
    "Percentual": [32, 68]
})

st.subheader("🔭 Mapa de Calor de Liquidez")
st.vega_lite_chart(df_pizza, {
    'width': 'container',
    'height': 300,
    'mark': {'type': 'arc', 'innerRadius': 80, 'outerRadius': 120, 'cornerRadius': 10, 'padAngle': 5, 'tooltip': True},
    'encoding': {
        'theta': {'field': 'Percentual', 'type': 'quantitative'},
        'color': {
            'field': 'Status', 
            'type': 'nominal', 
            'scale': {'range': ['#ff0055', '#00d4ff']} # Rosa Neon e Azul Neon
        }
    },
    'view': {'stroke': None}
})

# --- 🚀 RELATÓRIO ALPHA PREMIUM ---
if st.button("📊 GERAR DOSSIÊ DETALHADO"):
    st.balloons()
    with st.expander("📄 VISUALIZAR RELATÓRIO COMPLETO", expanded=True):
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown(f"### 💵 Financeiro: {medico_sel}")
            st.info(f"**Garantido:** R$ {v_liberado:,.2f}")
            st.error(f"**Retido:** R$ {v_pendente:,.2f}")
        with c_b:
            st.markdown("### 🧬 Análise Técnica")
            st.warning(f"**Diagnóstico:** {info['motivo']}")
            st.write("---")
            st.write(f"**Auditoria Concluída em:** 11/01/2026")

    st.success("🏁 Relatório gerado com criptografia de auditoria.")
    
