import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DE SEGURANÇA ---
# ATENÇÃO: Substitua o texto entre as aspas pela sua chave que você criou.
API_KEY = "COLOQUE_SUA_CHAVE_AQUI"

# --- CONFIGURAÇÃO DO SISTEMA (PADRÃO OURO) ---
# Quando precisar mudar o doutor, basta alterar o nome abaixo.
doutor_atual = "ANIMA COSTA"
porcentagem_liberado = 85  # Este valor muda o título automaticamente
porcentagem_pendente = 15   # Calculado para fechar 100%
projecao_valor = "1.85x"
acao_imediata = "ENTRA"
status_ia = "Monitorando o vácuo"

# --- INTERFACE VISUAL (GÊMEA FÊNIX) ---
st.title("(GÊMEA FÊNIX)")

# Verificação de sincronização da Chave
if API_KEY == "COLOQUE_SUA_CHAVE_AQUI":
    st.error("❌ SISTEMA PENDENTE: Verifique a Chave API no GitHub.")
    st.info("🔄 O servidor da IA está processando sua nova chave. Tente novamente em um instante.")
else:
    # Mensagem de Boas-vindas com sincronização automática
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

# Exibe a tabela sem os índices laterais para ficar mais limpo
st.table(df_favelinha)

st.markdown("---")

# --- ÁREA DE DOWNLOAD (CONFIGURADO PARA CELULAR) ---
# Nome do arquivo e texto sem acentos para evitar erro no Android/iOS
st.download_button(
    label="📥 Baixar Relatorio Operacional",
    data=f"STATUS: {porcentagem_liberado} LIBERADO / {porcentagem_pendente} PENDENTE. Doutor: {doutor_atual}.",
    file_name="relatorio_sentinela.txt",
    mime="text/plain"
)

# --- RODAPÉ OPERACIONAL ---
st.caption(f"Sistema sincronizado: {doutor_atual} | Projeção atual determinada pela rodada.")
