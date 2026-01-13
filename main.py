import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE TEMA (MODERNO, DARK E EXECUTIVO)
st.set_page_config(page_title="IA-SENTINELA PRO | Q2-2026", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    /* Estilização dos Cards de Métricas */
    div[data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 5px;
    }
    div[data-testid="stMetricLabel"] { color: #8B949E !important; font-size: 14px !important; }
    div[data-testid="stMetricValue"] { color: #58A6FF !important; font-weight: bold; font-size: 28px !important; }
    
    /* Caixa de Decisão Centralizada */
    .decisao-container {
        background-color: #1a2a1d;
        border: 1px solid #2ea043;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
    }
    .decisao-texto { color: #39d353; font-size: 26px; font-weight: bold; letter-spacing: 1px; }
    .vácuo-texto { color: #ff7b72; font-size: 26px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. IDENTIDADE E CONTROLE
st.title("🛡️ IA-SENTINELA PRO")
st.caption("Monitoramento e Observabilidade | Criador: Sidney Pereira de Almeida")

with st.sidebar:
    st.header("⚙️ Painel de Auditoria")
    medico = st.selectbox("Unidade Atual", ["ANIMA COSTA", "DR. SILVA", "INTERFILE - BI"])
    valor_rodada = st.number_input("Valor da Rodada Atual", value=2500.0)
    status_rodada = st.radio("Status do Faturamento", ["LIBERADO", "PENDENTE"])
    st.divider()
    st.info("Sincronizado: Q2-2026")

# 3. MOTOR DE INSIGHTS ATIVOS (LOGICA Q2)
def motor_decisao(valor, status):
    if valor <= 1.0:
        return "PULA", "vácuo-texto", "🔴 Risco de Vácuo Operacional (1.00x)"
    elif status == "PENDENTE":
        return "AGUARDAR", "decisao-texto", "🟡 Aguardando Correção de Lote"
    else:
        return "ENTRA", "decisao-texto", "🟢 Fluxo Autorizado para Faturamento"

acao, classe_estilo, sub_texto = motor_decisao(valor_rodada, status_rodada)

# 4. DASHBOARD DE KPIs (68% vs 32%)
v_lib = 10880.0
v_pen = 5120.0
total = v_lib + v_pen
p_lib = int((v_lib / total) * 100)
p_pen = int((v_pen / total) * 100)

col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"ASSETS LIBERADOS ({p_lib}%)", value=f"R$ {v_lib:,.2f}")
    st.markdown("🟢 <span style='color:#8B949E;'>Faturamento Ativo</span>", unsafe_allow_html=True)
with col2:
    st.metric(label=f"PENDÊNCIA OPERACIONAL ({p_pen}%)", value=f"R$ {v_pen:,.2f}", delta=f"-{p_pen}%", delta_color="inverse")
    st.markdown("🔴 <span style='color:#8B949E;'>Risco de Glosa</span>", unsafe_allow_html=True)

# Bloco de Ação Imediata
st.markdown(f"""
    <div class="decisao-container" style="background-color: {'#2a1a1a' if acao == 'PULA' else '#1a2a1d'}; border-color: {'#ff7b72' if acao == 'PULA' else '#2ea043'};">
        <div class="{classe_estilo}">DECISÃO: {acao}</div>
        <span style='color:#8B949E;'>{sub_texto}</span>
    </div>
""", unsafe_allow_html=True)

st.divider()

# 5. TABELA DA FAVELINHA COM INSIGHTS DE AUDITORIA
st.subheader("📊 Critical Audit Log (Tabela da Favelinha)")

tabela_dados = {
    "ID": ["#901", "#902", "ATUAL"],
    "PACIENTE": ["JOÃO SILVA", "MARIA OLIVEIRA", "RODADA ANALISADA"],
    "ERRO": ["XML INVÁLIDO", "DIVERGÊNCIA TUSS", "-"],
    "INSIGHT ATIVO (Q2)": [
        "Reestruturar tag do lote e reenviar.",
        "Validar código TUSS na tabela 2026.",
        f"Ação: {acao}"
    ]
}

df = pd.DataFrame(tabela_dados)
st.table(df)

# 6. EXPORTAÇÃO EXECUTIVA (SEM ACENTO NO ARQUIVO)
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Exportar Relatório de Auditoria",
    data=csv,
    file_name='auditoria_sentinela_q2.csv',
    mime='text/csv',
)

st.caption(f"Operação: {medico} | Sistema IA-SENTINELA Blindado")
