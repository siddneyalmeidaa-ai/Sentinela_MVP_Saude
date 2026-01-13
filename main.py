import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE INTERFACE (ESTILO DARK MODE EXECUTIVO)
st.set_page_config(page_title="IA-SENTINELA | EXECUTIVE", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    div[data-testid="stMetricValue"] { font-size: 32px; font-weight: bold; color: #00FFCC; }
    .stTable { background-color: #161B22; border-radius: 10px; }
    .css-1544893 { background-image: linear-gradient(to right, #00C9FF, #92FE9D); }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO E CONTROLE SINCRONIZADO
st.title("🛡️ IA-SENTINELA PRO")
st.caption("Módulo de Auditoria Estratégica & Insights Ativos (Q2-2026)")

with st.sidebar:
    st.header("🎛️ Gestão de Operação")
    medico = st.selectbox("Unidade Selecionada", ["ANIMA COSTA", "DR. SILVA - TABOÃO", "INTERFILE - BI"])
    valor_input = st.number_input("Valor da Rodada", min_value=0.0, value=2500.0)
    status_input = st.radio("Status da Auditoria", ["LIBERADO", "PENDENTE"])
    st.divider()
    st.info("Sistema operando em modo de Observabilidade Total.")

# 3. LÓGICA DE AUDITORIA (PROJEÇÃO DE RODADA)
def calcular_decisao_q2(valor, status):
    if valor <= 1.0:
        return "PULA", "🔴", "ZONA DE VÁCUO (1.00X)"
    elif status == "PENDENTE":
        return "NÃO ENTRA", "🟡", "AGUARDANDO XML/TUSS"
    else:
        return "ENTRA", "🟢", "FLUXO AUTORIZADO"

acao, icone, detalhe = calcular_decisao_q2(valor_input, status_input)

# 4. DASHBOARD DE PERFORMANCE (KPIs SINCRONIZADOS)
v_liberado = 10880.0
v_pendente = 5120.0
total = v_liberado + v_pendente
p_lib = int((v_liberado / total) * 100)
p_pen = int((v_pendente / total) * 100)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label=f"{p_lib}% LIBERADO", value=f"R$ {v_liberado:,.2f}")
    st.write("✅ Faturamento Seguro")

with col2:
    st.metric(label=f"{p_pen}% PENDENTE", value=f"R$ {v_pendente:,.2f}", delta=f"-{p_pen}%", delta_color="inverse")
    st.write("⚠️ Risco de Glosa")

with col3:
    st.markdown(f"### Decisão: {icone} {acao}")
    st.success(f"**Insight Ativo:** {detalhe}")

st.divider()

# 5. TABELA DA FAVELINHA (VISUAL PROFISSIONAL)
st.subheader("📊 Tabela da Favelinha - Auditoria em Tempo Real")

dados_auditoria = {
    "Paciente": ["João Silva", "Maria Oliveira", "Rodada Atual"],
    "Valor (R$)": [2500.0, 2620.0, valor_input],
    "Status": ["PENDENTE", "PENDENTE", status_input],
    "Ação Q2 (IA)": ["Corrigir Tag XML", "Mapear TUSS", acao]
}

df = pd.DataFrame(dados_auditoria)
st.dataframe(df, use_container_width=True)

# 6. RELATÓRIO DE SAÍDA (SEM ERRO DE ACENTO)
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📦 Exportar Relatorio de Auditoria",
    data=csv,
    file_name='auditoria_executiva_sentinela.csv',
    mime='text/csv',
)

st.write("---")
st.caption(f"Operação: {medico} | Sincronizado com IA-SENTINELA")
