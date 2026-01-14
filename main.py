import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- 1. CONFIGURAÇÃO DA INTERFACE ---
st.set_page_config(page_title="ALPHA VIP - Gêmea Fênix", layout="wide")

# --- 2. BARRA LATERAL (MOTOR DE AUTOMAÇÃO) ---
with st.sidebar:
    st.header("⚙️ Configurações Alpha VIP")
    medico = st.selectbox("Selecione o Médico", ["ANIMA COSTA", "DMMIGINIO GUERRA", "OUTRO"])
    if medico == "OUTRO": medico = st.text_input("Nome do Médico")
    
    # Transformamos o valor de texto para número para o gráfico de barras
    valor_input = st.text_input("Valor Total da Guia", "2250.00")
    valor_float = float(valor_input.replace("R$", "").replace(".", "").replace(",", "."))
    
    porcentagem = st.slider("Porcentagem Liberada", 0, 100, 85)

# --- 3. LOGICA PANDAS (DADOS AUTOMATIZADOS) ---
# Criamos o DataFrame que alimenta tudo no sistema
dados_operacao = pd.DataFrame({
    "MÉTRICA": ["LIBERADO", "PENDENTE"],
    "VALOR (R$)": [valor_float * (porcentagem/100), valor_float * ((100-porcentagem)/100)],
    "PERCENTUAL": [porcentagem, 100-porcentagem]
})

# --- 4. TÍTULO E ALERTAS ---
st.markdown(f"<h1 style='text-align: center;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)
st.warning(f"🤖 IA-SENTINELA: {porcentagem}% LIBERADO para {medico}. Projeção ativa.")

# --- 5. ÁREA DE GRÁFICOS (LADO A LADO) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Status de Liberação (%)")
    fig_pizza = px.pie(dados_operacao, values='PERCENTUAL', names='MÉTRICA', 
                       color='MÉTRICA', color_discrete_map={'LIBERADO':'#556b2f', 'PENDENTE':'#8b0000'},
                       hole=.6)
    fig_pizza.update_layout(showlegend=True, legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.markdown("### 💰 Faturamento Auditado (R$)")
    fig_barra = px.bar(dados_operacao, x='MÉTRICA', y='VALOR (R$)', 
                       color='MÉTRICA', color_discrete_map={'LIBERADO':'#556b2f', 'PENDENTE':'#8b0000'})
    st.plotly_chart(fig_barra, use_container_width=True)

# --- 6. TABELA DA FAVELINHA AUTOMATIZADA ---
st.markdown("### 📋 TABELA DA FAVELINHA")
st.table({
    "Médico": [medico],
    "Valor Total": [f"R$ {valor_float:,.2f}"],
    "Ação": ["ENTRA" if porcentagem >= 85 else "PULA"],
    "IA-SENTINELA": ["Monitorando vácuo" if porcentagem >= 85 else "VÁCUO DETECTADO"]
})

# --- 7. BOTÃO DE RELATÓRIO PADRÃO OURO ---
if st.button("🚀 GERAR RELATÓRIO PADRÃO OURO"):
    st.balloons()
    st.success(f"🔱 Auditoria de {medico} integrada com sucesso!")
