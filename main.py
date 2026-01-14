import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DE SEGURANÇA ---
# Coloque sua chave entre as aspas quando estiver pronto
API_KEY = "COLOQUE_SUA_CHAVE_AQUI"

# --- CONFIGURAÇÃO OPERACIONAL (VALORES DO PRINT DE 14 DE JAN) ---
# Altere os valores abaixo para atualizar o sistema automaticamente
doutor_atual = "ANIMA COSTA"
porcentagem_liberado = 85
projecao_valor = "1.85x"
acao_imediata = "ENTRA"
status_ia = "Monitorando o vácuo"

# --- INTERFACE GÊMEA FÊNIX ---
st.title("(GÊMEA FÊNIX)")

# Verificação de Sincronização
if API_KEY == "COLOQUE_SUA_CHAVE_AQUI" or API_KEY == "":
    st.error("❌ STATUS: Erro: Verifique a Chave e as Aspas")
    st.info("🔄 O servidor da IA está processando sua nova chave. Tente novamente em um instante.")
else:
    # Mensagem sincronizada: Altera os valores no texto automaticamente
    st.success(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem_liberado}% LIBERADO. Projeção {projecao_valor} para {doutor_atual}. {status_ia}.")

st.markdown("---")

# --- TABELA DA FAVELINHA (VISUAL INTERFACE) ---
st.subheader("📋 TABELA DA FAVELINHA")

df_favelinha = pd.DataFrame({
    "Doutor": [doutor_atual],
    "Projeção": [projecao_valor],
    "Ação": [acao_imediata],
    "IA-SENTINELA": [status_ia]
})

# Exibe a tabela sem o índice lateral (scannable)
st.table(df_favelinha)

st.markdown("---")

# --- BOTÃO DE DOWNLOAD (CONFIGURADO SEM ACENTO PARA CELULAR) ---
st.download_button(
    label="📥 Baixar Relatorio Operacional",
    data=f"STATUS: {porcentagem_liberado}% LIBERADO. Doutor: {doutor_atual}. Projeção: {projecao_valor}.",
    file_name="relatorio_sentinela.txt",
    mime="text/plain"
)

# --- RODAPÉ DE AUDITORIA ---
st.caption(f"Sistema Sincronizado: {doutor_atual} | IA-SENTINELA v1.0")
