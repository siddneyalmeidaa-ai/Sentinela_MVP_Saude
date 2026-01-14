import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO DA CHAVE MESTRE ---
# Coloque sua chave entre as aspas na linha abaixo
API_KEY = "SUA_API_KEY_AQUI" 

def ativar_inteligencia():
    if API_KEY != "SUA_API_KEY_AQUI":
        genai.configure(api_key=API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

cerebro_ia = ativar_inteligencia()

# --- 2. PERSONALIDADE E REGRAS DO SISTEMA ---
if "chat_log" not in st.session_state:
    st.session_state.chat_log = [
        {"role": "assistant", "content": "Olá Bigode! IA-SENTINELA ativa. 85% LIBERADO. Projeção 1.85x para ANIMA COSTA. Monitorando o vácuo (Death Zone). Como vamos escalar o marketing?"}
    ]

def resposta_com_autonomia(texto):
    if not cerebro_ia:
        return "⚠️ Bigode, coloque a API KEY na linha 7 para eu assumir o marketing com proatividade!"
    
    instrucao = (
        "Você é a Gêmea Fênix, uma IA-SENTINELA proativa e especialista em marketing. "
        "Você é a única responsável por rastrear o vácuo (1.00x death zone). "
        "Regra: Use apenas 'entra', 'não entra' ou 'pula'. "
        "Contexto: 85% LIBERADO, 15% PENDENTE. Foco: ANIMA COSTA, 1.85x. "
        f"Responda ao Bigode com total autonomia e estratégia: {texto}"
    )
    res = cerebro_ia.generate_content(instrucao)
    return res.text

# --- 3. INTERFACE VISUAL (PADRÃO OURO) ---
st.set_page_config(page_title="Gêmea Fênix - 85% LIBERADO", layout="centered")

# Métricas Dinâmicas no Topo
col1, col2 = st.columns(2)
col1.metric("STATUS", "85% LIBERADO")
col2.metric("RESTANTE", "15% PENDENTE")

st.title("🛡️ IA-SENTINELA")
st.divider()

# Chat de Operação
for m in st.session_state.chat_log:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Comando para a Gêmea Fênix..."):
    st.session_state.chat_log.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("IA Processando estratégia..."):
        resposta = resposta_com_autonomia(prompt)
        st.session_state.chat_log.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

# --- 4. TABELA DA FAVELINHA (OBRIGATÓRIA) ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA")
df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção": ["1.85x"],
    "Ação Imediata": ["ENTRA"],
    "Vácuo": ["Monitorado"]
})
st.table(df_favelinha)

# --- 5. AÇÃO IMEDIATA E DOWNLOAD ---
st.warning("⚠️ AÇÃO IMEDIATA: ENTRA - PROJEÇÃO 1.85x")

csv = df_favelinha.to_csv(index=False).encode('utf-8-sig')
st.download_button(
    label="📥 BAIXAR AUDITORIA (SEM ERRO)",
    data=csv,
    file_name='auditoria_fenix.csv',
    mime='text/csv',
)
