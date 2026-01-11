import streamlit as st

# 🏛️ CONFIGURAÇÃO ALPHA VIP
st.set_page_config(page_title="ALPHA VIP - SENTINELA", page_icon="🏛️")

st.title("🏛️ PAINEL DE AUDITORIA ALPHA VIP")
st.markdown("---")

# ⚙️ SIDEBAR DE CONTROLE
with st.sidebar:
    st.header("⚙️ Configurações")
    medico = st.selectbox("Médico", ["ANIMA COSTA", "DMMIGINIO GUERRA"])
    valor = st.text_input("Valor da Guia", "R$ 16.000,00")
    status = st.radio("Status", ["AUTORIZADO", "PENDENTE"])

# 🔥 BOTÃO DE EXECUÇÃO
if st.button("🚀 GERAR RELATÓRIO PADRÃO OURO"):
    st.balloons()
    st.success(f"🔱 Auditoria de {medico} concluída com sucesso!")
    
    # INTERFACE DO RELATÓRIO
    st.markdown(f"""
    <div style="background:#fff; padding:30px; border:3px solid #1a237e; border-radius:10px; color:black;">
        <h2 style="color:#1a237e;">RELATÓRIO DE FATURAMENTO</h2>
        <p><b>AUDITOR:</b> Sidney Almeida</p>
        <p><b>MÉDICO:</b> {medico}</p>
        <hr>
        <h3 style="text-align:center;">VALOR LIBERADO: {valor}</h3>
    </div>
    """, unsafe_allow_html=True)
  
