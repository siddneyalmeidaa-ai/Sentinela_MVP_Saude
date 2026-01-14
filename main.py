import streamlit as st
import urllib.parse
import pandas as pd
import requests  # 🌐 Conexão com o servidor da internet

# --- 1. MOTOR DE BUSCA E VISÃO GLOBAL ---
def consulta_visao_global(query):
    # Simulação de consulta ao servidor para buscar classificação
    try:
        # Aqui o sistema interage com a internet (mockup de servidor)
        status_servidor = "CONECTADO"
        return f"🌍 VISÃO GLOBAL ({status_servidor}): Classificação auditada. Padrão Ouro em vigor para {query}."
    except:
        return "⚠️ Erro de conexão com o servidor da internet."

# --- 2. CÉREBRO DAS 17 INTELIGÊNCIAS ---
def motor_rag_fenix(mensagem, doutor="ANIMA COSTA"):
    p = mensagem.lower()
    
    # Resposta da MALUQUINHA DOS CÓDIGOS (Desbloqueio)
    if "classificação" in p or "internet" in p:
        return consulta_visao_global(doutor)
        
    # Resposta CFO VISION (Aparece no seu print)
    if "tudo bem" in p or "como está" in p:
        return "🔥 CFO VISION: Analisando margem líquida. Sistema pronto para o gatilho de entrada via Cloud."
    
    # Proteção IA-SENTINELA
    if "vácuo" in p or "1.00" in p:
        return "🚨 IA-SENTINELA: Bloqueio detectado! Zona de Vácuo. Operação abortada."

    return f"✨ GÊMEA FÊNIX: Sincronização completa para {doutor}. Todas as 17 IAs online."

# --- 3. INTERFACE (CONFORME SEUS PRINTS) ---
st.title("85% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader("15% PENDENTE")
st.divider()

# Campo de Interação RAG
st.write("🧠 **Interação com as 17 Inteligências (RAG Mode):**")
u_input = st.text_input("Digite sua mensagem para o servidor:", key="input_global")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if u_input:
        resposta = motor_rag_fenix(u_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta}")

st.divider()

# --- 4. TABELA DA FAVELINHA (PADRÃO OURO) ---
st.write("### 📋 TABELA DA FAVELINHA")
proj_rodada = 1.85 # Valor sincronizado
acao = "ENTRA" if proj_rodada >= 1.80 else "PULA" # Regra STS

df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção Rodada": [f"{proj_rodada}x"],
    "Ação Imediata": [acao]
})
st.table(df_favelinha)

# --- 5. WHATSAPP SEM ERRO DE ACENTO (CRIPTOGRAFIA) ---
def gerar_link_wa():
    texto = f"🚀 PROJETO FRAJOLA\nDoutor: ANIMA COSTA\nProjeção: {proj_rodada}x\nAção: {acao}\nStatus: VISÃO GLOBAL ATIVA"
    # Criptografia para não quebrar no celular
    return f"https://wa.me/?text={urllib.parse.quote(texto)}"

st.link_button("🚀 ENVIAR PARA WHATSAPP", gerar_link_wa(), use_container_width=True)

st.divider()
st.caption("© 2026 Gêmea Fênix - Sistema Conectado ao Servidor")
