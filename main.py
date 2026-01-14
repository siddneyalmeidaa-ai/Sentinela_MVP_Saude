import streamlit as st
import pandas as pd

# --- MEMÓRIA QUÂNTICA: SALVAMENTO AUTOMÁTICO DO HISTÓRICO ---
if "historico_militar" not in st.session_state:
    # Inicializa com a estrutura que já testamos e funcionou
    st.session_state.historico_militar = [
        {"role": "assistant", "content": "Bom dia, Sidney! O ecossistema está em modo de espera. Aguardando ignição da chave para análise em tempo real.", "avatar": "🤖"}
    ]

# --- CONFIGURAÇÃO PADRÃO OURO ---
API_KEY = "COLOQUE_SUA_CHAVE_AQUI"
doutor = "ANIMA COSTA"
porcentagem = 85
projecao = "1.85x"

# --- INTERFACE VISUAL (GÊMEA FÊNIX) ---
st.markdown("<h1 style='text-align: center;'>(GÊMEA FÊNIX)</h1>", unsafe_allow_html=True)

# Alerta de Status Sincronizado
st.warning(f"🤖 Olá Bigode! IA-SENTINELA ativa. {porcentagem}% LIBERADO. Projeção {projecao} para {doutor}.")

# Exibição do Histórico Salvo (Memória Quântica)
for msg in st.session_state.historico_militar:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.write(msg["content"])

# --- TABELA DA FAVELINHA ---
st.markdown("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": [doutor],
    "Ação": ["ENTRA"],
    "IA-SENTINELA": ["Monitorando vácuo"]
})
st.table(df_favelinha)

# --- CAMPO DE COMANDO MILITAR (REATIVO) ---
prompt = st.chat_input("Dê sua ordem militar...")

if prompt:
    # Registra a ordem do usuário no histórico
    st.session_state.historico_militar.append({"role": "user", "content": prompt, "avatar": "🔴"})
    
    # Resposta Automática das 17 IAs
    resposta = f"Recebi sua ordem: '{prompt}'. O motor das 17 IAs está pronto, aguardando a chave para executar."
    st.session_state.historico_militar.append({"role": "assistant", "content": resposta, "avatar": "🤖"})
    
    # Força a atualização para salvar e mostrar na tela imediatamente
    st.rerun()

# --- BOTÃO DE DOWNLOAD (LOG DE AUDITORIA) ---
st.download_button(
    label="📥 Baixar Relatorio Operacional",
    data=str(st.session_state.historico_militar),
    file_name="historico_militar_fenix.txt"
)
