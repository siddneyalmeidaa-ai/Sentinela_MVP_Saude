import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MASTER ALPHA ---
st.set_page_config(page_title="IA-SENTINELA", page_icon="🏛️", layout="wide")

st.title("🏛️ PORTAL DE AUDITORIA ALPHA VIP")

# --- 📊 BANCO DE DATA (OS 10 MÉDICOS) ---
lista_medicos = [
    "ANIMA COSTA", "DMMIGINIO GUERRA", "DR. ALPHA TESTE", 
    "DRA. ELENA SILVA", "DR. MARCOS PONTES", "CLÍNICA SÃO JOSÉ", 
    "DRA. BEATRIZ LINS", "DR. RICARDO MELO", "CENTRO MÉDICO VIP", 
    "AUDITORIA GERAL"
]

with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Selecione o Médico", lista_medicos)
    valor = st.number_input("Valor da Guia (R$)", value=16000.00)
    status = st.radio("Status da Auditoria", ["AUTORIZADO", "PENDENTE"])
    st.divider()
    st.write("👤 **Auditor:** Sidney Almeida")

# --- 📈 DASHBOARD PRINCIPAL ---
c1, c2 = st.columns(2)
with c1:
    st.metric("Faturamento Identificado", f"R$ {valor:,.2f}")
with c2:
    st.metric("Status IA-SENTINELA", status)

st.subheader("📊 Distribuição de Auditoria (Visão de Pizza)")

# Lógica da Pizza Nativa (Sem erro de módulo)
if status == "AUTORIZADO":
    dados = {"Status": ["AUTORIZADO", "RESTANTE"], "Valores": [valor, 2000]}
else:
    dados = {"Status": ["PENDENTE", "RESTANTE"], "Valores": [valor, 500]}

df_pizza = pd.DataFrame(dados)

# Criando o gráfico de pizza que não trava o sistema
st.vega_lite_chart(df_pizza, {
    'mark': {'type': 'arc', 'innerRadius': 50, 'tooltip': True},
    'encoding': {
        'theta': {'field': 'Valores', 'type': 'quantitative'},
        'color': {
            'field': 'Status', 
            'type': 'nominal', 
            'scale': {'range': ['#1c2e4a', '#ff4b4b']} # Azul e Vermelho
        }
    },
    'view': {'stroke': None}
}, use_container_width=True)

# --- 🚀 AÇÃO IMEDIATA ---
if st.button("🚀 GERAR RELATÓRIO FINAL"):
    st.balloons()
    st.success(f"Auditoria de {medico} processada com sucesso no Padrão Ouro!")
    
