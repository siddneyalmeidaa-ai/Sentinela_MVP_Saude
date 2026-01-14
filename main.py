import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DE SEGURANÇA ---
# Sua chave vai aqui entre as aspas
API_KEY = "COLOQUE_SUA_CHAVE_AQUI"

# --- CONFIGURAÇÃO DA RODADA (PRINT 14 DE JAN) ---
doutor = "ANIMA COSTA"
porcentagem = 85
projecao = "1.85x"
acao = "ENTRA"
sentinela_msg = "Monitorando o vácuo"

# --- ESTILIZAÇÃO DA INTERFACE ---
st.set_page_config(page_title="Gêmea Fênix", layout="centered")

# Título Principal
st.markdown(f"<h1 style='text-align: center; color: white;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- ÁREA DE STATUS DA IA ---
if API_KEY == "COLOQUE_SUA_CHAVE_AQUI":
    # Alerta de processamento
    st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem}% LIBERADO. Projeção {projecao} para {doutor}. {sentinela_msg}.")
    st.info("🔄 O servidor da IA está processando sua nova chave. Tente novamente em um instante.")
else:
    st.success(f"✅ SISTEMA SINCRONIZADO: {porcentagem}% LIBERADO")

# Exemplo de Balão de Chat
with st.chat_message("user", avatar="🔴"):
    st.write("Bom dia")

# --- TABELA DA FAVELINHA (VISUAL INTERFACE) ---
st.markdown("### 📋 TABELA DA FAVELINHA")

df_favelinha = pd.DataFrame({
    "Doutor": [doutor],
    "Projeção": [projecao],
    "Ação": [acao],
    "IA-SENTINELA": [sentinela_msg]
})

# Exibe a tabela sem o índice para ficar igual ao print
st.table(df_favelinha)

# --- COMANDO OPERACIONAL (CHAT NO RODAPÉ) ---
# Simula a barra de digitação do print
st.chat_input("Fale com a Gêmea Fênix...")

# --- BOTÃO DE DOWNLOAD (CONFIGURADO PARA CELULAR) ---
st.download_button(
    label="📥 Baixar Relatorio Operacional",
    data=f"Relatorio: {porcentagem}% LIBERADO para {doutor}",
    file_name="relatorio_sentinela.txt"
)
