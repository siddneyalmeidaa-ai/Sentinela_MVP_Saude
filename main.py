import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIGURAÇÃO ALPHA VIP ---
st.set_page_config(page_title="ALPHA VIP - Gêmea Fênix", layout="wide")

# --- 2. BARRA LATERAL (ENTRADAS DINÂMICAS) ---
with st.sidebar:
    st.header("⚙️ Configurações Alpha VIP")
    medico = st.selectbox("Selecione o Médico", ["ANIMA COSTA", "DMMIGINIO GUERRA", "OUTRO"])
    if medico == "OUTRO": medico = st.text_input("Nome do Médico")
    
    # Captura o valor e limpa para formato numérico
    valor_texto = st.text_input("Valor Total da Guia (R$)", "2.250,00")
    valor_limpo = valor_texto.replace("R$", "").replace(".", "").replace(",", ".")
    valor_total = float(valor_limpo)
    
    # O SLIDER QUE COMANDA OS GRÁFICOS
    porcentagem = st.slider("Porcentagem Liberada", 0, 100, 85)

# --- 3. MOTOR PANDAS (AUTOMAÇÃO DE VALORES) ---
# Aqui a mágica acontece: os cálculos mudam conforme você mexe no slider
v_liberado = valor_total * (porcentagem / 100)
v_pendente = valor_total - v_liberado

df_faturamento = pd.DataFrame({
    "MÉTRICA": ["LIBERADO", "PENDENTE"],
    "VALOR (R$)": [v_liberado, v_pendente],
    "PERCENTUAL": [porcentagem, 100 - porcentagem]
})

# --- 4. INTERFACE VISUAL (GÊMEA FÊNIX) ---
st.markdown(f"<h1 style='text-align: center;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)
st.warning(f"🤖 IA-SENTINELA: {porcentagem}% LIBERADO para {medico}. Projeção ativa.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Status de Liberação (%)")
    # Gráfico de Pizza que responde ao slider
    fig_pizza = px.pie(df_faturamento, values='PERCENTUAL', names='MÉTRICA', 
                       color='MÉTRICA', color_discrete_map={'LIBERADO':'#556b2f', 'PENDENTE':'#8b0000'},
                       hole=.6)
    fig_pizza.update_layout(showlegend=True, legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.markdown("### 💰 Faturamento Auditado (R$)")
    # Gráfico de Barras que responde ao valor total e slider
    fig_barra = px.bar(df_faturamento, x='MÉTRICA', y='VALOR (R$)', 
                       color='MÉTRICA', color_discrete_map={'LIBERADO':'#556b2f', 'PENDENTE':'#8b0000'},
                       text_auto='.2s')
    st.plotly_chart(fig_barra, use_container_width=True)

# --- 5. TABELA DA FAVELINHA (PADRÃO OURO) ---
st.markdown("### 📋 TABELA DA FAVELINHA")
st.table({
    "Médico": [medico],
    "Total Liberado": [f"R$ {v_liberado:,.2f}"],
    "Status": ["ENTRA" if porcentagem >= 85 else "PULA"],
    "IA-SENTINELA": ["VÁCUO DETECTADO" if porcentagem < 10 else "Monitorando vácuo"]
})

# --- 6. RELATÓRIO PADRÃO OURO ---
if st.button("🚀 GERAR RELATÓRIO FINAL"):
    st.balloons()
    st.success(f"🔱 Auditoria de {medico} concluída: R$ {v_liberado:,.2f} liberados.")
    
