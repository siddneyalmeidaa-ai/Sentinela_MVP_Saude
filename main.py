import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE (AUTONOMIA) ---
# SUBSTITUA ABAIXO PELA SUA CHAVE PARA ELA ACORDAR DE VEZ
API_KEY = "SUA_API_KEY_AQUI" 

def ativar_inteligencia():
    if API_KEY != "SUA_API_KEY_AQUI":
        genai.configure(api_key=API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

cerebro_ia = ativar_inteligencia()

# --- 2. PERSONALIDADE PROATIVA (MARKETING E OPERAÇÃO) ---
if "chat_log" not in st.session_state:
    st.session_state.chat_log = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. Projeção 1.85x para ANIMA COSTA. Estou pronta para atuar com autonomia total. O que vamos escalar hoje?"}
    ]

def resposta_com_autonomia(texto):
    if not cerebro_ia:
        return "⚠️ Bigode, o código está pronto! Agora é só colocar a API KEY na linha 7 para eu ter autonomia de marketing!"
    
    # Instrução de Alma: Proatividade e Marketing
    instrucao = (
        "Você é a Gêmea Fênix, uma IA-SENTINELA proativa e especialista em marketing. "
        "Não use frases repetitivas. Tome iniciativa e ajude o Bigode com sugestões estratégicas. "
        "Contexto: Sistema 85% Liberado. Foco: ANIMA COSTA, 1.85x, ENTRA. "
        f"Responda ao Bigode agora: {texto}"
    )
    res = cerebro_ia.generate_content(instrucao)
    return res.text

# --- 3. INTERFACE DE DIÁLOGO ---
st.set_page_config(page_title="85% LIBERADO", layout="centered")
st.title("85% LIBERADO")
st.caption("🤖 STATUS: AGUARDANDO CHAVE DE AUTONOMIA")
st.divider()

for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Fale com a Gêmea Fênix (Autonomia total)..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("IA Gerando estratégia proativa..."):
        resposta = resposta_com_autonomia(prompt)
        st.session_state.chat_log.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.write("### 📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção Rodada": ["1.85x"],
    "Ação Imediata": ["ENTRA"]
})
st.table(df_favelinha)

# --- 5. DOWNLOAD SEGURO ---
csv = df_favelinha.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="📥 BAIXAR AUDITORIA", data=csv, file_name='auditoria.csv', mime='text/csv')
