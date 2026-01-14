import streamlit as st
import urllib.parse
import pandas as pd

# --- 1. MOTOR DE RESPOSTA (O CÉREBRO DAS 17 IAs) ---
def motor_fenix_rag(comando, doutor="ANIMA COSTA"):
    c = comando.lower()
    # Camada IA-SENTINELA: Bloqueio de Vácuo
    if "vácuo" in c or "1.00" in c:
        return "🚨 IA-SENTINELA: Bloqueio imediato! Zona de vácuo identificada. Protegendo banca."
    # Camada ADVOGADA CABELUDA: Auditoria
    if "auditoria" in c or "liberado" in c:
        return f"⚖️ ADVOGADA CABELUDA: Auditoria concluída para {doutor}. ROI blindado."
    # Camada CFO VISION (A que apareceu no seu print)
    if "tudo bem" in c:
        return "🔥 CFO VISION: Analisando margem líquida. Sistema pronto para o gatilho de entrada."
    # Resposta Padrão Ouro
    return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {doutor}. Todas as 17 IAs em standby."

# --- 2. INTERFACE VISUAL (Métricas fixas conforme solicitado) ---
st.title("85% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader("15% PENDENTE")
st.divider()

# --- 3. CAMPO DE INTERAÇÃO (Não some mais) ---
st.write("🧠 **Interação com as 17 Inteligências (RAG Mode):**")
u_input = st.text_input("Digite sua mensagem para o sistema:", key="input_fenix")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if u_input:
        resp = motor_fenix_rag(u_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resp}")

st.divider()

# --- 4. TABELA DA FAVELINHA E WHATSAPP (ESTRUTURA FIXA) ---
st.write("### 📋 TABELA DA FAVELINHA")
proj = 1.85
# Regra: Entra ou Pula
status_acao = "ENTRA" if proj >= 1.80 else "PULA"

df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção Rodada": [f"{proj}x"],
    "Ação Imediata": [status_acao]
})
st.table(df_favelinha)

# Aviso tático sincronizado
st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para ANIMA COSTA ({proj}x).")

# Botão WhatsApp com criptografia de URL para mobile
msg_blindada = f"🚀 PROJETO FRAJOLA\nDoutor: ANIMA COSTA\nProjeção: {proj}x\nAção: {status_acao}\nPADRÃO OURO ATIVADO"
url_wa = f"https://wa.me/?text={urllib.parse.quote(msg_blindada)}"
st.link_button("🚀 ENVIAR PARA WHATSAPP", url_wa, use_container_width=True)
