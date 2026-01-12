import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MASTER ---
st.set_page_config(page_title="IA-SENTINELA", page_icon="🏛️", layout="wide")
st.title("🏛️ PORTAL DE AUDITORIA ALPHA VIP")

# --- 📊 BANCO DE DADOS ---
lista_medicos = ["ANIMA COSTA", "DMMIGINIO GUERRA", "DR. ALPHA TESTE", "DRA. ELENA SILVA", "DR. MARCOS PONTES", "CLÍNICA SÃO JOSÉ", "DRA. BEATRIZ LINS", "DR. RICARDO MELO", "CENTRO MÉDICO VIP", "AUDITORIA GERAL"]

with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Selecione o Médico", lista_medicos)
    qtd_pacientes = st.slider("Total de Pacientes", 1, 200, 85)
    valor_total = st.number_input("Faturamento Total (R$)", value=16000.00)
    st.divider()
    st.write("👤 **Auditor:** Sidney Almeida")

# --- 📈 CÁLCULOS REAIS ---
p_pendente = 32
p_liberado = 68
v_pendente = valor_total * (p_pendente / 100)
v_liberado = valor_total * (p_liberado / 100)
ticket_medio = valor_total / qtd_pacientes

# --- 📊 DASHBOARD SUPERIOR ---
st.subheader(f"📊 Análise de Pagamento: {medico}")
c1, c2, c3 = st.columns(3)
with c1: st.metric("PACIENTES", f"{qtd_pacientes}")
with c2: st.metric("TICKET MÉDIO", f"R$ {ticket_medio:,.2f}")
with c3: st.metric("RISCO IDENTIFICADO", f"R$ {v_pendente:,.2f}", "-32%")

# --- 🍕 PIZZA COM RÓTULOS DE PERCENTUAL ---
df_pizza = pd.DataFrame({
    "Status": [f"PENDENTE ({p_pendente}%)", f"LIBERADO ({p_liberado}%)"],
    "Valor": [p_pendente, p_liberado]
})

st.vega_lite_chart(df_pizza, {
    'mark': {'type': 'arc', 'innerRadius': 50, 'tooltip': True},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {
            'field': 'Status', 
            'type': 'nominal', 
            'scale': {'range': ['#ff4b4b', '#1c2e4a']}
        }
    }
}, use_container_width=True)

st.divider()

# --- 🚀 BOTÃO GERAR RELATÓRIO DETALHADO ---
if st.button("🚀 GERAR RELATÓRIO DETALHADO"):
    st.balloons()
    st.subheader("📑 Relatório de Auditoria Final")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 📈 Resumo Financeiro")
        st.write(f"**Valor Bruto:** R$ {valor_total:,.2f}")
        st.write(f"**Valor Liberado (68%):** R$ {v_liberado:,.2f}")
        st.write(f"**Valor em Glosa/Risco (32%):** R$ {v_pendente:,.2f}")
    
    with col_b:
        st.write("### 🔍 Diagnóstico IA-SENTINELA")
        st.write(f"**Médico Responsável:** {medico}")
        st.write(f"**Média por Paciente:** R$ {ticket_medio:,.2f}")
        st.error(f"⚠️ Alerta: R$ {v_pendente:,.2f} retidos por inconsistência.")

    st.success("✅ Documento de auditoria pronto para exportação.")
    
