import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (BACKGROUND GLOBAL OPERATIONS) ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            /* Link atualizado com o nome real do arquivo que você subiu */
            background-image: url("https://raw.githubusercontent.com/siddneyalmeidaa-ai/Sentinela_MVP_Saude/main/1768384879706.jpg");
            background-attachment: fixed;
            background-size: cover;
        }}
        /* Deixa o conteúdo visível sobre a imagem */
        .stMarkdown, .stTable, .stChatMessage, [data-testid="stMetricValue"] {{
            background-color: rgba(0, 0, 0, 0.8) !important;
            border-radius: 15px;
            padding: 15px;
            color: #00ffcc !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# --- 2. CONFIGURAÇÃO SEGURA (BUSCA NOS SECRETS) ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    cerebro_ia = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Bigode, a chave não foi encontrada nos Secrets do Streamlit!")
    st.stop()

# --- 3. INTERFACE DE OPERAÇÕES GLOBAIS ---
col1, col2 = st.columns(2)
col1.metric("STATUS OPERACIONAL", "85% LIBERADO")
col2.metric("ALVO (DOUTOR)", "ANIMA COSTA")

st.title("🛡️ IA-SENTINELA | GLOBAL OPERATIONS")
st.divider()

if "chat_log" not in st.session_state:
    st.session_state.chat_log = [{"role": "assistant", "content": "🛡️ Operações Globais Online. Sistema Blindado. Como vamos escalar hoje?"}]

for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Comando para a Gêmea Fênix..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("Analisando vácuo..."):
        try:
            instrucao = "Você é a Gêmea Fênix. Use apenas 'entra', 'não entra' ou 'pula'. Foco: Marketing e Vácuo."
            res = cerebro_ia.generate_content(f"{instrucao} Pergunta: {prompt}")
            resposta_texto = res.text
        except:
            resposta_texto = "🔄 Sincronizando com o servidor... Tente novamente em 10 segundos."
            
        st.session_state.chat_log.append({"role": "assistant", "content": resposta_texto})
        with st.chat_message("assistant"):
            st.write(resposta_texto)

# --- 4. TABELA DA FAVELINHA ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA")
df = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção": ["1.85x"],
    "Ação": ["ENTRA"],
    "IA-SENTINELA": ["Sincronizada"]
})
st.table(df)

# Download sem erro para celular
csv = df.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="📥 BAIXAR AUDITORIA", data=csv, file_name='auditoria.csv', mime='text/csv')
