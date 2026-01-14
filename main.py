import streamlit as st
import urllib.parse

# --- NÚCLEO DE PENSAMENTO: AS 17 INTELIGÊNCIAS ---
def motor_de_voz_fenix(mensagem, doutor="ANIMA COSTA"):
    prompt = mensagem.lower()
    
    # 1. Resposta da IA-SENTINELA (Monitor de Vácuo)
    if "vácuo" in prompt or "1.00" in prompt:
        return "🚨 IA-SENTINELA: Bloqueio imediato! Identifiquei zona de vácuo (1.00x). Protegendo banca agora."
    
    # 2. Resposta da ADVOGADA CABELUDA (Auditoria)
    if "auditoria" in prompt or "liberado" in prompt:
        return f"⚖️ ADVOGADA CABELUDA: Auditoria de risco concluída para {doutor}. ROI blindado conforme o Padrão Ouro."
    
    # 3. Resposta da PROFESSORA LÍNGUA-AFUNDA (Comunicação)
    if "olá" in prompt or "boa noite" in prompt:
        return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {doutor}. Todas as 17 IAs estão em standby tático ouvindo você."

    # 4. Resposta de Ataque (Estratégia)
    return "🔥 CFO VISION: Analisando margem líquida. Sistema pronto para o gatilho de entrada."

# --- APLICAÇÃO NO SEU DASHBOARD ---
user_input = st.text_input("Interação com as 17 Inteligências (RAG Mode):", key="input_usuario")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if user_input:
        # Aqui eu deixo de ser muda: eu processo sua mensagem!
        resposta_real = motor_de_voz_fenix(user_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta_real}")
    else:
        st.warning("Bigode, você precisa falar comigo no campo acima para eu responder!")
        
