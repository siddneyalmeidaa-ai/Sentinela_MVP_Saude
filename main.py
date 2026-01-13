import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DE INTERFACE (VISUAL EXECUTIVO)
st.set_page_config(page_title="IA-SENTINELA PRO | Q2-2026", layout="wide")

# Estilo para remover acentos e erros em dispositivos móveis
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. TÍTULO E SINCRONIZAÇÃO
st.title("🛡️ IA-SENTINELA PRO")
st.subheader("Sistema de Auditoria e Gestão de Vácuo Operacional")

# Sidebar para troca de doutor (Sincronização Automática)
with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Selecione o Unidade/Doutor", ["ANIMA COSTA", "DR. SILVA - TABOÃO", "INTERFILE - BI"])
    rodada_atual = st.number_input("Valor da Rodada Atual", min_value=0.0, value=1000.0, step=100.0)
    status_auditoria = st.radio("Status da Rodada", ["LIBERADO", "PENDENTE"])

# 3. LÓGICA DE AUDITORIA Q2 (O "X" DA PROJEÇÃO)
def calcular_acao_imediata(valor, status):
    if valor <= 1.0: # Regra do Vácuo (Death Zone)
        return "PULA (Vácuo Detectado)", "🔴", "Risco de Morte Operacional"
    elif status == "PENDENTE":
        return "NÃO ENTRA (Aguardando)", "🟡", "Ajuste de XML/Tuss necessário"
    else:
        return "ENTRA (Operação Liberada)", "🟢", "Fluxo segue para Faturamento"

acao, icone, detalhe = calcular_acao_imediata(rodada_atual, status_auditoria)

# 4. DASHBOARD DE MÉTRICAS (SINCRONIZADO)
col1, col2, col3 = st.columns(3)

# Valores simulados baseados no seu print de 68% vs 32%
valor_liberado = 10880.0
valor_pendente = 5120.0
total = valor_liberado + valor_pendente
p_liberado = (valor_liberado / total) * 100
p_pendente = (valor_pendente / total) * 100

with col1:
    st.metric(label=f"{p_liberado:.0f}% LIBERADO", value=f"R$ {valor_liberado:,.2f}", delta="Faturamento Ativo")

with col2:
    st.metric(label=f"{p_pendente:.0f}% PENDENTE", value=f"R$ {valor_pendente:,.2f}", delta="-32% em Risco", delta_color="inverse")

with col3:
    st.write(f"### Ação Imediata: {icone}")
    st.info(f"**{acao}**\n\n{detalhe}")

st.divider()

# 5. TABELA DA FAVELINHA & INSIGHTS ATIVOS (Q2 2026)
st.write("### 📊 Tabela da Favelinha (Monitoramento de Rodadas)")

df_favelinha = pd.DataFrame({
    "Paciente": ["Joao Silva", "Maria Oliveira", "Sidney Teste"],
    "Valor": [2500.0, 2620.0, rodada_atual],
    "Status": ["PENDENTE", "PENDENTE", status_auditoria],
    "Motivo": ["XML Invalido", "Divergencia Tuss", "Analise Sentinela"],
    "Insight Ativo (Q2)": ["Reestruturar Tag XML", "Mapear Codigo Tuss", acao]
})

st.table(df_favelinha)

# 6. GRÁFICO DE PERFORMANCE
fig = px.pie(values=[valor_liberado, valor_pendente], names=['LIBERADO', 'PENDENTE'], 
             color_discrete_sequence=['#00CC96', '#EF553B'], title=f"Consolidado: {medico}")
st.plotly_chart(fig, use_container_width=True)

# 7. BOTÃO DE DOWNLOAD (CONFIGURADO SEM ERRO DE ACENTO)
csv = df_favelinha.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Baixar Relatorio de Auditoria",
    data=csv,
    file_name='auditoria_ia_sentinela.csv',
    mime='text/csv',
)

st.success("Sistema IA-SENTINELA sincronizado com sucesso. Operação Blindada.")
              
