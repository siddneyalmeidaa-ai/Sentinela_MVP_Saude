import streamlit as st
import pandas as pd

# CONFIGURAÇÃO MASTER ALPHA
st.set_page_config(page_title="IA-SENTINELA", layout="wide")
st.title("🏛️ PORTAL DE AUDITORIA ALPHA VIP")

# LISTA DE 10 MÉDICOS (PADRÃO OURO)
lista_medicos = ["ANIMA COSTA", "DMMIGINIO GUERRA", "DR. ALPHA TESTE", "DRA. ELENA SILVA", "DR. MARCOS PONTES", "CLÍNICA SÃO JOSÉ", "DRA. BEATRIZ LINS", "DR. RICARDO MELO", "CENTRO MÉDICO VIP", "AUDITORIA GERAL"]

with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Selecione o Médico", lista_medicos)
    valor = st.number_input("Valor da Guia (R$)", value=16000.00)
    status = st.radio("Status", ["AUTORIZADO", "PENDENTE"])

# DASHBOARD (MAR DE ÓLEO)
c1, c2 = st.columns(2)
with c1: st.metric("Faturamento", f"R$ {valor:,.2f}")
with c2: st.metric("Status IA", status)

st.subheader("📊 Performance de Faturamento")
df = pd.DataFrame({'Médico': [medico], 'Valor': [valor]})
st.bar_chart(data=df, x='Médico', y='Valor', color="#1c2e4a")

if st.button("🚀 GERAR RELATÓRIO PADRÃO OURO"):
    st.balloons()
    st.success(f"Relatório de {medico} concluído com sucesso!")
    
