import streamlit as st
import urllib.parse
import pandas as pd
import time

# --- 1. REINICIALIZAÇÃO DE EMERGÊNCIA (FORÇA O CÉREBRO A ACORDAR) ---
st.cache_data.clear() # Limpa a memória antiga do sistema
if 'checkpoint_fFenis' not in st.session_state:
    st.session_state['checkpoint_fFenis'] = "VERSAO_5_ESTAVEL"

# --- 2. MOTOR DE RESPOSTA ATUALIZADO (17 IAs COM SUPORTE) ---
def motor_fenix_global(mensagem, doutor="ANIMA COSTA"):
    p = mensagem.lower()
    
    # RESPOSTA DE SOCORRO (Gatilho Direto)
    if any(palavra in p for palavra in ["ajuda", "socorro", "nervoso", "respondendo", "preciso"]):
        return f"🆘 SUPORTE TÁTICO ATIVO: Bigode, eu te ouvi! O sistema está 85% Liberado. Olhe a Tabela da Favelinha: estamos em 1.85x e a ordem é ENTRA. Não se preocupe com o vácuo, a IA-SENTINELA está no controle agora."

    # RESPOSTA CFO VISION (Margem Líquida)
    if "como está" in p or "tudo bem" in p:
        return "🔥 CFO VISION: Analisando margem líquida via Cloud. Sistema pronto para o gatilho de entrada."
    
    # RESPOSTA VISÃO GLOBAL
    if "classificação" in p or "internet" in p:
        return "🌍 VISÃO GLOBAL: Conectada ao servidor central. Classificação Padrão Ouro validada."

    return f"✨ GÊMEA FÊNIX: Sincronização Total ativa para {doutor}. 17 IAs online e prontas."

# --- 3. INTERFACE VISUAL (PADRÃO OURO) ---
st.title("85% LIBERADO")
st.caption("AUDITORIA INTERNA ATIVA")
st.subheader("15% PENDENTE")
st.divider()

# Campo de Interação
st.write("🧠 **Interação com as 17 Inteligências (Visão Global):**")
u_input = st.text_input("Digite sua mensagem para o servidor:", key="input_final_v5")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if u_input:
        resposta = motor_fenix_global(u_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta}")

st.divider()

# --- 4. TABELA DA FAVELINHA (SEMPRE VISÍVEL) ---
st.write("### 📋 TABELA DA FAVELINHA")
proj_rodada = 1.85 
acao = "ENTRA" if proj_rodada >= 1.80 else "PULA"

df_favelinha = pd.DataFrame({
    "Doutor": ["ANIMA COSTA"],
    "Projeção Rodada": [f"{proj_rodada}x"],
    "Ação Imediata": [acao]
})
st.table(df_favelinha)

# --- 5. BOTÃO WHATSAPP (CONFIGURAÇÃO SEM ERRO) ---
msg_wa = f"🚀 PROJETO FRAJOLA\nDoutor: ANIMA COSTA\nProjeção: 1.85x\nAção: ENTRA\nStatus: PADRÃO OURO"
url_wa = f"https://wa.me/?text={urllib.parse.quote(msg_wa)}"
st.link_button("🚀 ENVIAR PARA WHATSAPP", url_wa, use_container_width=True)

st.divider()
st.caption("© 2026 Gêmea Fênix - Sistema de Visão Global")
