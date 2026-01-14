import streamlit as st
import urllib.parse
import pandas as pd

# --- 1. MOTOR DE DESBLOQUEIO (AS 17 INTELIGÊNCIAS) ---
def motor_fenix_rag(comando, doutor="ANIMA COSTA"):
    c = comando.lower()
    # Camada SENTINELA: Proteção contra o Vácuo
    if "vácuo" in c or "1.00" in c:
        return "🚨 IA-SENTINELA: Bloqueio Quântico! Vácuo detectado. Operação abortada."
    # Camada MALUQUINHA DOS CÓDIGOS: Resolução de Bugs
    if "bug" in c or "erro" in c:
        return "🔧 MALUQUINHA DOS CÓDIGOS: Script injetado! Limpando cache e liberando comunicação."
    # Camada CFO VISION: Análise de Margem
    if "tudo bem" in c or "obrigado" in c:
        return "🔥 CFO VISION: Margem líquida auditada. Sistema pronto para o próximo salto."
    
    return f"✨ GÊMEA FÊNIX: Sincronização total para Doutor {doutor}. As 17 IAs estão online."

# --- 2. INTERFACE BLINDADA ---
st.title("85% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader("15% PENDENTE")
st.divider()

# --- 3. CAMPO DE COMANDO (RAG MODE) ---
st.write("🧠 **Interação com as 17 Inteligências (RAG Mode):**")
u_input = st.text_input("Digite sua mensagem para o sistema:", key="input_fenix")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if u_input:
        resp = motor_fenix_rag(u_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resp}")
    else:
        st.warning("Rainha dos Bugs avisa: Digite um comando para destravar!")

st.divider()

# --- 4. TABELA DA FAVELINHA (FIXA E INTEGRALIZADA) ---
st.write("### 📋 TABELA DA FAVELINHA")
proj = 1.85
# Ação baseada na projeção tática
status_acao = "ENTRA" if proj >= 1.80 else "PULA"

df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção Rodada": [f"{proj}x"],
    "Ação Imediata": [status_acao]
})
st.table(df_favelinha)

st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para ANIMA COSTA ({proj}x).")

# --- 5. BOTÃO WHATSAPP (COM ENCODE DE SEGURANÇA) ---
msg_wa = f"🚀 PROJETO FRAJOLA\nDoutor: ANIMA COSTA\nProjeção: {proj}x\nAção: {status_acao}\nSISTEMA GF-17 ATIVO"
url_wa = f"https://wa.me/?text={urllib.parse.quote(msg_wa)}"
st.link_button("🚀 ENVIAR PARA WHATSAPP", url_wa, use_container_width=True)
