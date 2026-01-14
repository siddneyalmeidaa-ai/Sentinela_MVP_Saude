import streamlit as st
import pandas as pd

# --- SEGURANÇA E CHAVE API ---
# Substitua pela sua chave quando for rodar no motor real
API_KEY = "COLOQUE_SUA_CHAVE_AQUI"

# --- CONFIGURAÇÃO PADRÃO OURO (ANIMA COSTA) ---
doutor = "ANIMA COSTA"
porcentagem_liberado = 85
porcentagem_pendente = 15
projecao = "1.85x"
acao_imediata = "ENTRA"
sentinela_status = "Monitorando o vácuo"

# --- INTERFACE VISUAL GÊMEA FÊNIX ---
st.set_page_config(page_title="Gêmea Fênix", layout="centered")

# Título Estilizado
st.markdown("<h1 style='text-align: center; color: white;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)
st.markdown("---")

# Verificação de Motor (API)
if API_KEY == "COLOQUE_SUA_CHAVE_AQUI" or API_KEY == "":
    # Alerta de Processamento
    st.error("❌ STATUS: Erro: Verifique a Chave e as Aspas")
    st.info("🔄 O servidor da IA está processando sua nova chave. Tente novamente em um instante.")
else:
    # Interface Liberada
    st.success(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem_liberado}% LIBERADO. Projeção {projecao} para {doutor}. {sentinela_status}.")

# Balão de Chat de Apoio
with st.chat_message("user", avatar="🔴"):
    st.write("Bom dia")

# --- TABELA DA FAVELINHA (VISUAL INTERFACE) ---
st.markdown("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": [doutor],
    "Projeção": [projecao],
    "Ação": [acao_imediata],
    "IA-SENTINELA": [sentinela_status]
})
st.table(df_favelinha)

# --- CAMPO DE COMANDO OPERACIONAL ---
st.chat_input("Fale com a Gêmea Fênix...")

# --- BOTÃO DE DOWNLOAD (CONFIGURADO PARA CELULAR) ---
st.download_button(
    label="📥 Baixar Relatorio Operacional",
    data=f"STATUS: {porcentagem_liberado}% LIBERADO / {porcentagem_pendente}% PENDENTE. Doutor: {doutor}.",
    file_name="relatorio_sentinela.txt"
)
