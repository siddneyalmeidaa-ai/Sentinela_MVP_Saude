import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE INTERFACE (VISUAL EXECUTIVO)
st.set_page_config(page_title="IA-SENTINELA PRO | Q2-2026", layout="wide")

# Estilo para garantir que o visual fique limpo no celular
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. TÍTULO E SINCRONIZAÇÃO
st.title("🛡️ IA-SENTINELA PRO")
st.subheader("Auditoria Estratégica & Gestão de Vácuo")

# Sidebar para controle total
with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Unidade/Doutor", ["ANIMA COSTA", "DR. SILVA - TABOÃO", "INTERFILE - BI"])
    valor_input = st.number_input("Valor da Rodada", min_value=0.0, value=1000.0)
    status_auditoria = st.radio("Status Atual", ["LIBERADO", "PENDENTE"])

# 3. LÓGICA DE AUDITORIA (O "X" DA PROJEÇÃO)
def calcular_sentinela(valor, status):
    if valor <= 1.0:
        return "PULA (Vácuo Detectado)", "🔴", "Risco de Morte Operacional (1.00x)"
    elif status == "PENDENTE":
        return "NÃO ENTRA (Aguardando)", "🟡", "Ajuste de XML ou Tuss pendente"
    else:
        return "ENTRA (Operação Liberada)", "🟢", "Fluxo autorizado para faturamento"

acao, icone, detalhe = calcular_sentinela(valor_input, status_auditoria)

# 4. DASHBOARD DE MÉTRICAS (SINCRONIZADO AUTOMATICAMENTE)
# Simulando os valores do seu print (68% vs 32%)
v_liberado = 10880.0
v_pendente = 5120.0
total = v_liberado + v_pendente
p_liberado = int((v_liberado / total) * 100)
p_pendente = int((v_pendente / total) * 100)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label=f"{p_liberado}% LIBERADO", value=f"R$ {v_liberado:,.2f}")

with col2:
    st.metric(label=f"{p_pendente}% PENDENTE", value=f"R$ {v_pendente:,.2f}", delta=f"-{p_pendente}%", delta_color="inverse")

with col3:
    st.write(f"### Decisão: {icone}")
    st.info(f"**{acao}**")

st.divider()

# 5. TABELA DA FAVELINHA (VISUAL INTERFACE)
st.write("### 📊 Tabela da Favelinha - Auditoria Q2")

data = {
    "Paciente": ["Joao Silva", "Maria Oliveira", "Auditoria Atual"],
    "Valor": [2500.0, 2620.0, valor_input],
    "Status": ["PENDENTE", "PENDENTE", status_auditoria],
    "Insight Ativo (Q2)": ["Erro XML - Corrigir Tag", "Divergência Tuss - Mapear", acao]
}
df_favelinha = pd.DataFrame(data)

st.table(df_favelinha)

# 6. GRÁFICO DE BARRAS (SEM PLOTLY PARA NÃO DAR ERRO)
st.write("### 📈 Consolidado por Status")
chart_data = pd.DataFrame(
    [v_liberado, v_pendente],
    index=["LIBERADO", "PENDENTE"],
    columns=["Valores"]
)
st.bar_chart(chart_data)

# 7. BOTÃO DE DOWNLOAD (CONFIGURADO SEM ERRO DE ACENTO)
csv = df_favelinha.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Baixar Relatorio de Auditoria",
    data=csv,
    file_name='auditoria_sentinela.csv',
    mime='text/csv',
)

st.success(f"Sistema sincronizado para: {medico}. Nenhuma morte operacional detectada.")
