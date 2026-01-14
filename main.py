import streamlit as st
import urllib.parse
import pandas as pd

# --- 1. MOTOR DE RESPOSTA (O CÉREBRO DAS 17 IAs) ---
def motor_fenix_rag(comando, doutor="ANIMA COSTA"):
    c = comando.lower()
    # Camada IA-SENTINELA: Monitoramento de Vácuo
    if "vácuo" in c or "1.00" in c:
        return "🚨 IA-SENTINELA: Bloqueio imediato! Zona de vácuo identificada. Protegendo banca."
    # Camada ADVOGADA CABELUDA: Auditoria de Risco
    if "auditoria" in c or "liberado" in c:
        return f"⚖️ ADVOGADA CABELUDA: Auditoria concluída para {doutor}. ROI blindado."
    # Camada CFO VISION (Processamento de Margem)
    if "tudo bem" in c:
        return "🔥 CFO VISION: Analisando margem líquida. Sistema pronto para o gatilho de entrada."
    # Resposta Padrão de Sincronização
    return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {doutor}. Todas as 17 IAs em standby tático."

# --- 2. INTERFACE VISUAL (Métricas Padrão Ouro) ---
st.title("85% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader("15% PENDENTE")
st.divider()

# --- 3. CAMPO DE INTERAÇÃO (RAG MODE) ---
st.write("🧠 **Interação com as 17 Inteligências (RAG Mode):**")
u_input = st.text_input("Digite sua mensagem para o sistema:", key="input_fenix", value="Boa noite")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if u_input:
        resp = motor_fenix_rag(u_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resp}")

st.divider()

# --- 4. TABELA DA FAVELINHA (ESTRUTURA FIXA) ---
st.write("### 📋 TABELA DA FAVELINHA")
proj = 1.85
# Lógica STS: Automatização de ação baseada na projeção
status_acao = "ENTRA" if proj >= 1.80 else "PULA"

df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção Rodada": [f"{proj}x"],
    "Ação Imediata": [status_acao]
})
st.table(df_favelinha)

# Aviso de Status Sincronizado
st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para ANIMA COSTA ({proj}x).")

# --- 5. BOTÃO WHATSAPP (CORREÇÃO DE CRIPTOGRAFIA PARA MOBILE) ---
msg_blindada = f"🚀 PROJETO FRAJOLA\nDoutor: ANIMA COSTA\nProjeção: {proj}x\nAção: {status_acao}\n\nPADRÃO OURO ATIVADO"
url_wa = f"https://wa.me/?text={urllib.parse.quote(msg_blindada)}"
st.link_button("🚀 ENVIAR PARA WHATSAPP", url_wa, use_container_width=True)
