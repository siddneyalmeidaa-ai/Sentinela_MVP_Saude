import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (IMAGEM NO FUNDO, TEXTO NA FRENTE) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

def add_bg():
    st.markdown(
        f"""
        <style>
        /* Define a imagem como fundo fixo e atrás de tudo */
        .stApp {{
            background-image: url("https://raw.githubusercontent.com/siddneyalmeidaa-ai/Sentinela_MVP_Saude/main/1768384879706.jpg");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        /* Garante que o conteúdo (escritos) tenha contraste e fique na frente */
        .main .block-container {{
            background-color: rgba(0, 0, 0, 0.7); /* Fundo escuro semi-transparente para o texto brilhar */
            border-radius: 20px;
            padding: 30px;
            margin-top: 20px;
        }}
        /* Estilo para os cards e chat */
        .stChatMessage, .stTable, [data-testid="stMetricValue"] {{
            background-color: rgba(20, 20, 20, 0.9) !important;
            color: #00ffcc !important;
            border: 1px solid #00ffcc;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# --- 2. CÉREBRO DA IA (MODO SEGURO) ---
try:
    # O sistema busca a chave no cofre (Secrets) que você configurou no Manage App
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Bigode, a chave ainda não foi salva nos Secrets do Streamlit!")
    st.stop()

# --- 3. INTERFACE DE OPERAÇÕES ---
st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")

col1, col2, col3 = st.columns(3)
col1.metric("STATUS", "85% LIBERADO")
col2.metric("PENDENTE", "15%")
col3.metric("ALVO", "ANIMA COSTA")

if "chat_log" not in st.session_state:
    st.session_state.chat_log = [{"role": "assistant", "content": "🛡️ Operação Online. Escritos na frente, imagem no fundo. Como vamos escalar?"}]

for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Dê sua ordem operacional..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    instrucao = "Você é a Gêmea Fênix. Use apenas 'entra', 'não entra' ou 'pula'. Foco: Marketing e Vácuo."
    try:
        res = cerebro_ia.generate_content(f"{instrucao} Pergunta: {prompt}")
        resposta = res.text
    except:
        resposta = "🔄 Sincronizando com o servidor..."
            
    st.session_state.chat_log.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA")
df = pd.DataFrame({"Doutor": ["ANIMA COSTA"], "Projeção": ["1.85x"], "Ação": ["ENTRA"]})
st.table(df)
    
