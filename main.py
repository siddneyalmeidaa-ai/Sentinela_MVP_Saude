import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURAÇÃO MASTER ALPHA
st.set_page_config(page_title="IA-SENTINELA", layout="wide")
st.title("🏛️ PORTAL DE AUDITORIA ALPHA VIP")

# LISTA DE 10 MÉDICOS
lista_medicos = ["ANIMA COSTA", "DMMIGINIO GUERRA", "DR. ALPHA TESTE", "DRA. ELENA SILVA", "DR. MARCOS PONTES", "CLÍNICA SÃO JOSÉ", "DRA. BEATRIZ LINS", "DR. RICARDO MELO", "CENTRO MÉDICO VIP", "AUDITORIA GERAL"]

with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Selecione o Médico", lista_medicos)
    valor = st.number_input("Valor da Guia (R$)", value=16000.00)
    status = st.radio("Status Atual", ["AUTORIZADO", "PENDENTE"])

# LÓGICA DA PIZZA (Simulação de Auditoria)
# Se um está autorizado, o sistema assume o restante como análise
dados_pizza = pd.DataFrame({
    "Status": ["AUTORIZADO", "EM ANÁLISE/PENDENTE"],
    "Valores": [valor if status == "AUTORIZADO" else 0, 16000 - (valor if status == "AUTORIZADO" else 0) + 1000]
})

# DASHBOARD
c1, c2 = st.columns(2)
with c1: st.metric("Faturamento Identificado", f"R$ {valor:,.2f}")
with c2: st.metric("Status IA-SENTINELA", status)

st.subheader("📊 Distribuição de Status (Auditoria)")
fig = px.pie(dados_pizza, values='Valores', names='Status', 
             color='Status', color_discrete_map={'AUTORIZADO':'#1c2e4a', 'EM ANÁLISE/PENDENTE':'#ff4b4b'})
st.plotly_chart(fig, use_container_width=True)

if st.button("🚀 GERAR RELATÓRIO FINAL"):
    st.balloons()
    st.success(f"Auditoria de {medico} concluída!")
    
