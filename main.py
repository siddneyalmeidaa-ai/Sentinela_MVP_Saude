import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. SETUP ---
st.set_page_config(page_title="IA-SENTINELA | Interação", layout="wide")

# --- 2. BASE DE DADOS ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. INTERFACE ---
st.title("🛡️ Sistema de Governança & Resposta IA")
st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Status de Auditoria")
    st.table(df)

with col2:
    st.subheader("🤖 IA de Resposta Diplomática")
    msg_cliente = st.text_area("Cole aqui a mensagem recebida do cliente:")
    
    if msg_cliente:
        st.info("🔄 IA Processando tom diplomático...")
        # Simulação de Resposta Inteligente baseada no seu Padrão Ouro
        resposta_sugerida = (
            "Prezado, analisamos sua solicitação. No momento, a unidade encontra-se em "
            "status de RESTRIÇÃO técnica devido à inconsistência de ativos. "
            "Para evoluirmos para CONFORMIDADE OK, solicitamos o envio do XML pendente."
        )
        st.success("**Sugestão Executiva:**")
        st.write(resposta_sugerida)
        
        if st.button("Copiar para WhatsApp"):
            st.session_state.copy_text = resposta_sugerida
            st.toast("Resposta pronta para envio!")

# --- 4. DISPARO DE COMPLIANCE ---
st.divider()
st.subheader("📲 Canal Oficial de Comunicação")
unidade = st.selectbox("Unidade Destino:", df["unidade"].tolist())
link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote('🛡️ Relatório de Governança atualizado.')}"

st.markdown(f"""
    <a href="{link_zap}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
            🚀 ENVIAR RESPOSTA VIA WHATSAPP
        </div>
    </a>
""", unsafe_allow_html=True)
