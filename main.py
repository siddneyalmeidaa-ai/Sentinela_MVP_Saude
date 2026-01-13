import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE TEMA PROFISSIONAL (PADRÃO OURO Q2)
st.set_page_config(page_title="IA-SENTINELA PRO | STANDBY", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 15px;
        border-radius: 12px;
    }
    .decisao-container {
        background-color: #1a2a1d;
        border: 1px solid #2ea043;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. IDENTIDADE
st.title("🛡️ IA-SENTINELA PRO")
st.caption("Modo de Segurança Ativado | Sincronização WhatsApp em Standby")

# Sidebar
with st.sidebar:
    st.header("⚙️ Controle")
    medico = st.selectbox("Unidade", ["ANIMA COSTA", "DR. SILVA", "INTERFILE"])
    valor_rodada = st.number_input("Valor da Rodada", value=2500.0)
    status_rodada = st.radio("Status", ["LIBERADO", "PENDENTE"])

# 3. MÉTRICAS SINCRONIZADAS (68% vs 32%)
v_lib = 10880.0
v_pen = 5120.0
total = v_lib + v_pen
p_lib = int((v_lib / total) * 100)
p_pen = int((v_pen / total) * 100)

col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"ASSETS LIBERADOS ({p_lib}%)", value=f"R$ {v_lib:,.2f}")
with col2:
    st.metric(label=f"PENDÊNCIA OPERACIONAL ({p_pen}%)", value=f"R$ {v_pen:,.2f}", delta=f"-{p_pen}%", delta_color="inverse")

# Lógica de Decisão
acao = "PULA" if valor_rodada <= 1.0 else ("ENTRA" if status_rodada == "LIBERADO" else "AGUARDAR")

st.markdown(f"""
    <div class="decisao-container">
        <h2 style="color: #39d353; margin:0;">DECISÃO: {acao}</h2>
        <span style='color:#8B949E;'>Auditoria de Q2 Sincronizada</span>
    </div>
""", unsafe_allow_html=True)

# 4. TABELA DA FAVELINHA
st.subheader("📊 Critical Audit Log")
df = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Analise"],
    "Insight Ativo (Q2)": ["Erro XML", "Divergência TUSS", f"Ação: {acao}"]
})
st.table(df)

st.success(f"Sistema Operacional para {medico}. Erro de módulo Flask contornado.")
