import streamlit as st
import urllib.parse
import pandas as pd

# --- 1. CORE DE INTELIGÊNCIA GF-17 ---
def motor_de_voz_fenix(mensagem, doutor="ANIMA COSTA"):
    prompt = mensagem.lower()
    if "vácuo" in prompt or "1.00" in prompt:
        return "🚨 IA-SENTINELA: Bloqueio imediato! Identifiquei zona de vácuo (1.00x)."
    if "auditoria" in prompt or "liberado" in prompt:
        return f"⚖️ ADVOGADA CABELUDA: Auditoria concluída para {doutor}. ROI blindado."
    if "olá" in prompt or "boa noite" in prompt:
        return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {doutor}. Em standby tático."
    return "🔥 CFO VISION: Analisando margem líquida. Sistema pronto para o gatilho de entrada."

# --- 2. INTERFACE E MÉTRICAS ---
st.title("85% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader("15% PENDENTE")

st.divider()

# --- 3. CAMPO DE INTERAÇÃO (RAG MODE) ---
st.write("🧠 **Interação com as 17 Inteligências (RAG Mode):**")
user_input = st.text_input("Digite sua mensagem:", key="input_frajola")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if user_input:
        resposta = motor_de_voz_fenix(user_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta}")

st.divider()

# --- 4. TABELA DA FAVELINHA (FIXA NO RODAPÉ) ---
st.write("### 📋 TABELA DA FAVELINHA")

proj_atual = 1.85
# Lógica STS do Bigode: Se >= 1.80x então ENTRA
acao = "ENTRA" if proj_atual >= 1.80 else "PULA"

df = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção Rodada": [f"{proj_atual}x"],
    "Ação Imediata": [acao]
})

st.table(df)

# Notificação de status fixa
st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para ANIMA COSTA ({proj_atual}x).")

# --- 5. BOTÃO WHATSAPP (FIXO E SEM ERRO DE ACENTO) ---
msg_wa = f"🚀 PROJETO FRAJOLA\nDoutor: ANIMA COSTA\nProjeção: {proj_atual}x\nAção: {acao}"
link_wa = f"https://wa.me/?text={urllib.parse.quote(msg_wa)}"

st.link_button("🚀 ENVIAR PARA WHATSAPP", link_wa, use_container_width=True)
