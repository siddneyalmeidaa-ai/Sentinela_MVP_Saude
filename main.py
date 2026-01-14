import streamlit as st
import pandas as pd
import json

# --- 1. PERSONA 17: BLINDAGEM CONTRA KEYERROR ---
# Resolve o erro do print 01:37 garantindo que a memória exista sempre
if 'memoria_rag' not in st.session_state:
    st.session_state.memoria_rag = {"acao": "Pula", "status": "Auditando..."}

# --- 2. BASE DE CONHECIMENTO (Onde ela tira a informação) ---
# Aqui simulamos o RAG: a IA lendo seus dados de 69% e 31%
DATA_AUDITORIA = {
    "ANIMA COSTA": {"liberado": "85%", "pendente": "15%", "projecao": 1.85},
    "INTERFILE - BI": {"liberado": "40%", "pendente": "60%", "projecao": 1.00},
}

# --- 3. CORE DAS 17 INTELIGÊNCIAS (PROATIVIDADE) ---
def motor_de_decisao(medico, comando):
    dados = DATA_AUDITORIA.get(medico, {"liberado": "0%", "pendente": "100%", "projecao": 0})
    c = comando.lower()
    
    # REGRA DO VÁCUO (Persona 12):
    if dados["projecao"] <= 1.00:
        return "Pula", f"⚠️ IA-SENTINELA: Vácuo detectado ({dados['projecao']}x). Risco de perda total. Ação: PULA."

    # LÓGICA DE APRENDIZADO (Persona 5): Se você autoriza, ela aprende
    if any(x in c for x in ["pode", "liberar", "pagar", "agendar"]):
        return "Entra", f"✅ CFO VISION: Analisado {medico}. Projeção favorável de {dados['projecao']}x. Efetuando ENTRA."

    return "Não Entra", "🧐 GÊMEA FÊNIX: Contexto insuficiente. Aguardando instrução de fluxo."

# --- 4. INTERFACE PADRÃO OURO ---
st.title("🛡️ GÊMEA FÊNIX BONDE | RAG 2.0")

# Sincronização Automática
dr = st.selectbox("Doutor Responsável:", list(DATA_AUDITORIA.keys()))
dados_dr = DATA_AUDITORIA[dr]

col1, col2 = st.columns(2)
col1.metric(f"ESTATUTO {dr}", f"{dados_dr['liberado']} LIBERADO")
col2.metric("EM AUDITORIA", f"{dados_dr['pendente']} PENDENTE")

interacao = st.text_input("Comando para as 17 Inteligências:")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    acao, parecer = motor_de_decisao(dr, interacao)
    st.session_state.memoria_rag = {"acao": acao, "status": parecer}

# TABELA DA FAVELINHA (AÇÃO IMEDIATA)
st.subheader("📋 Tabela da Favelinha")
df_fav = pd.DataFrame([{"Doutor": dr, "Ação": st.session_state.memoria_rag["acao"], "Parecer": st.session_state.memoria_rag["status"]}])
st.table(df_fav)
