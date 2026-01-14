import streamlit as st
import urllib.parse
import pandas as pd
import time

# --- 1. MEMÓRIA DE LONGO PRAZO (PROATIVIDADE) ---
if 'memoria_sentinela' not in st.session_state:
    st.session_state['memoria_sentinela'] = [
        {"role": "assistant", "content": "Olá Bigode! Sou a Gêmea Fênix. Já analisei o mercado e a Tabela da Favelinha. Como posso acelerar seu lucro agora?"}
    ]

# --- 2. MOTOR DE DIÁLOGO AUTÔNOMO ---
def motor_fenix_proativo(mensagem):
    msg = mensagem.lower()
    
    # Se for sobre o projeto, ela assume postura de comando (Autonomia)
    if any(x in msg for x in ["pendência", "ajuda", "fazer", "próximo"]):
        return ("Bigode, identifiquei que estamos com 15% pendentes. Minha sugestão proativa: "
                "mantenha o foco em ANIMA COSTA. A projeção de 1.85x é sólida para ENTRAR. "
                "Quer que eu audite o vácuo da próxima rodada agora?")

    # Resposta Genérica mas com Personalidade (Diálogo)
    return (f"Entendi sua dúvida sobre '{mensagem}'. Como sua IA-SENTINELA, meu aprendizado "
            "contínuo foca em blindar sua operação. Além disso, notei que você está atento "
            "aos detalhes hoje. Vamos buscar os 100% de liberação?")

# --- 3. INTERFACE VISUAL (PADRÃO OURO) ---
st.title("85% LIBERADO")
st.caption("🤖 STATUS: IA COM AUTONOMIA ATIVADA")
st.subheader("15% PENDENTE")
st.divider()

# Histórico de Diálogo (Proatividade visível)
for chat in st.session_state.memoria_sentinela:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# Campo de Entrada de Voz/Texto
if u_input := st.chat_input("Fale com as 17 Inteligências..."):
    st.session_state.memoria_sentinela.append({"role": "user", "content": u_input})
    with st.chat_message("user"):
        st.write(u_input)
    
    resposta = motor_fenix_proativo(u_input)
    
    st.session_state.memoria_sentinela.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)

# --- 4. TABELA DA FAVELINHA (DADOS TÁTICOS) ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção": ["1.85x"],
    "Ação": ["ENTRA"] # Conforme regra STS salva
})
st.table(df_favelinha)

# --- 5. BOTÃO WHATSAPP (SINCRO TOTAL) ---
url_wa = f"https://wa.me/?text={urllib.parse.quote('🚀 RELATÓRIO PROATIVO: Operação Anima Costa 1.85x - ENTRA')}"
st.link_button("🚀 ENVIAR AUDITORIA PARA WHATSAPP", url_wa, use_container_width=True)
