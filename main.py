import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (IMAGEM ATRÁS, TEXTO NA FRENTE) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://raw.githubusercontent.com/siddneyalmeidaa-ai/Sentinela_MVP_Saude/main/1768384879706.jpg");
            background-attachment: fixed;
            background-size: cover;
        }}
        .main .block-container {{
            background-color: rgba(0, 0, 0, 0.75); /* Camada escura para o texto aparecer */
            border-radius: 20px;
            padding: 30px;
            color: #00ffcc !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# --- 2. CÉREBRO DA IA (MODO SEGURO) ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Bigode, a chave não foi encontrada nos Secrets!")
    st.stop()

# --- 3. INTERFACE OPERACIONAL ---
st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")

col1, col2 = st.columns(2)
col1.metric("STATUS", "85% LIBERADO")
col2.metric("ALVO", "ANIMA COSTA")

if "chat_log" not in st.session_state:
    st.session_state.chat_log = [{"role": "assistant", "content": "🛡️ Sistema Online. Como vamos escalar?"}]

for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Dê sua ordem..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    instrucao = "Você é a Gêmea Fênix. Use apenas 'entra', 'não entra' ou 'pula'. Foco: Marketing."
    try:
        res = cerebro_ia.generate_content(f"{instrucao} Pergunta: {prompt}")
        resposta = res.text
    except:
        resposta = "🔄 Sincronizando conexão..."
            
    st.session_state.chat_log.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA")
df = pd.DataFrame({"Doutor": ["ANIMA COSTA"], "Projeção": ["1.85x"], "Ação": ["ENTRA"]})
st.table(df)
