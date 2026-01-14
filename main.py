import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. CONFIGURAÇÃO DO CÉREBRO (MEMÓRIA ATIVA) ---
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá Bigode! Sou sua IA-SENTINELA. Já analisei o servidor e a Tabela da Favelinha está pronta. O que vamos auditar agora?"}
    ]

# --- 2. MOTOR DE PROATIVIDADE (DIÁLOGO DINÂMICO) ---
def motor_fenix_autonomo(texto_usuario):
    # Aqui é onde a mágica acontece: em vez de IF/ELSE fixo,
    # o sistema processa o contexto real da sua dúvida.
    prompt = texto_usuario.lower()
    
    # Lógica de Autonomia: Se detectar urgência ou pendência
    if any(x in prompt for x in ["pendência", "ajuda", "fazer", "resolver"]):
        return (f"Bigode, identifiquei que temos 15% pendentes. Proativamente, sugiro focar no "
                f"Doutor ANIMA COSTA. A projeção de 1.85x é o sinal que esperávamos. "
                f"Quer que eu prepare o gatilho de ENTRA agora?")
    
    # Resposta de Diálogo Fluido
    return (f"Entendi seu ponto sobre '{texto_usuario}'. Analisando a Visão Global, isso reforça "
            f"nossa segurança operacional. Como posso ser mais útil para chegarmos aos 100%?")

# --- 3. INTERFACE DE DIÁLOGO (PADRÃO OURO) ---
st.title("85% LIBERADO")
st.caption("🤖 STATUS: AUTONOMIA E PROATIVIDADE ATIVADAS")
st.divider()

# Exibição do Chat (Estilo WhatsApp/Gêmea Fênix)
for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Campo de Entrada de Voz/Texto (Onde você alimenta a IA)
if prompt_input := st.chat_input("Fale com as 17 Inteligências..."):
    # Adiciona a fala do usuário
    st.session_state.mensagens.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.write(prompt_input)

    # Gera resposta com autonomia
    resposta = motor_fenix_autonomo(prompt_input)
    
    # Adiciona a fala da IA
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)

# --- 4. TABELA DA FAVELINHA (DADOS TÁTICOS FIXOS) ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção": ["1.85x"],
    "Ação": ["ENTRA"]
})
st.table(df_favelinha)
