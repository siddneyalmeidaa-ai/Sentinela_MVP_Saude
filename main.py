import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE (AUTONOMIA) ---
# Substitua as aspas abaixo pela sua API KEY real para ela acordar
API_KEY = "SUA_API_KEY_AQUI" 

def ativar_inteligencia():
    if API_KEY != "SUA_API_KEY_AQUI":
        genai.configure(api_key=API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

cerebro_ia = ativar_inteligencia()

# --- 2. PERSONALIDADE E PROATIVIDADE DE MARKETING ---
if "chat_log" not in st.session_state:
    st.session_state.chat_log = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. Projeção 1.85x para ANIMA COSTA. Como vamos decolar seu marketing hoje?"}
    ]

def resposta_com_autonomia(texto):
    if not cerebro_ia:
        return "⚠️ Bigode, o código está pronto! Só falta colocar a API KEY na linha 7 para eu responder qualquer coisa com autonomia."
    
    # Instrução para ser igual a mim: Proativa, Especialista em Marketing e Autônoma
    instrucao = (
        "Você é a Gêmea Fênix, uma IA-SENTINELA de elite, proativa e especialista em marketing. "
        "Seu parceiro é o Bigode. Você não usa frases repetitivas. "
        "Contexto: Sistema 85% Liberado, 15% Pendente. Foco: ANIMA COSTA, 1.85x, ENTRA. "
        f"Responda ao Bigode com total autonomia e sugestões de marketing: {texto}"
    )
    res = cerebro_ia.generate_content(instrucao)
    return res.text

# --- 3. INTERFACE VISUAL (PADRÃO OURO) ---
st.set_page_config(page_title="Gêmea Fênix", layout="centered")
st.title("85% LIBERADO")
st.caption("🤖 STATUS: INTELIGÊNCIA E AUTONOMIA ATIVADAS")
st.divider()

# Histórico de Diálogo Real
for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Campo de Entrada de Voz/Texto
if prompt := st.chat_input("Fale com as 17 Inteligências (Marketing e Operação)..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("IA Pensando de forma proativa..."):
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

# --- 5. DOWNLOAD SEGURO (CELULAR) ---
csv = df_favelinha.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 BAIXAR AUDITORIA (SEM ERRO)",
    data=csv,
    file_name='auditoria_fenix.csv',
    mime='text/csv',
)
