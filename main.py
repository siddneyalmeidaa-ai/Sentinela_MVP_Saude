import streamlit as st
import urllib.parse
import pandas as pd

# --- 1. CORE DE INTELIGÊNCIA GF-17 (O CÉREBRO) ---
class CoreGF17:
    def __init__(self, doutor="ANIMA COSTA"):
        self.doutor = doutor
        self.liberado = "85%"
        self.pendente = "15%"
        
    def processar_rag(self, prompt):
        prompt_limpo = prompt.lower()
        # Regra IA-SENTINELA: Bloqueio de Vácuo (1.00x)
        if "1.00" in prompt_limpo or "vácuo" in prompt_limpo:
            return "🚨 IA-SENTINELA: Bloqueio detectado! Zona de Vácuo (1.00x) identificada. Operação abortada para proteção do ROI."
        
        # Regra Advogada Cabeluda: Blindagem e Auditoria
        if "auditoria" in prompt_limpo or "liberado" in prompt_limpo:
            return f"⚖️ ADVOGADA CABELUDA: Blindagem Padrão Ouro ativa para {self.doutor}. ROI protegido e auditado."
            
        # Resposta de Sincronização Padrão
        return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {self.doutor}. Todas as 17 IAs estão em standby tático."

    def decisao_sts(self, projecao):
        # Lógica de decisão conforme o Padrão Ouro
        if projecao == 1.00:
            return "VÁCUO (PULA)"
        elif projecao >= 1.80:
            return "ENTRA"
        else:
            return "PULA"

# --- 2. CONFIGURAÇÃO DA INTERFACE (STREAMLIT) ---
st.set_page_config(page_title="GF-17 - Projeto Frajola", layout="centered")
brain = CoreGF17()

# --- 3. MÉTRICAS DINÂMICAS (Sincronizadas com os Prints) ---
st.title(f"{brain.liberado} LIBERADO")
st.caption("EM AUDITORIA")
st.subheader(f"{brain.pendente} PENDENTE")

st.divider()

# --- 4. CAMPO DE INTERAÇÃO RAG ---
st.write("### 🧠 Interação com as 17 Inteligências (RAG Mode):")
user_input = st.text_input("Digite sua mensagem para o sistema:", value="Boa noite")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if user_input:
        resposta = brain.processar_rag(user_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta}")
    else:
        st.warning("Maluquinha dos Códigos: Digite um comando para ativar o cérebro!")

st.divider()

# --- 5. TABELA DA FAVELINHA (Lógica de Rodada 1.85x) ---
st.write("### 📋 TABELA DA FAVELINHA")
proj_rodada = 1.85
acao_imediata = brain.decisao_sts(proj_rodada)

df_favelinha = pd.DataFrame({
    "Doutor": [brain.doutor],
    "Projeção Rodada": [f"{proj_rodada}x"],
    "Ação Imediata": [acao_imediata]
})

st.table(df_favelinha)
st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para {brain.doutor} ({proj_rodada}x).")

# --- 6. BOTÃO WHATSAPP (MOBILE FIX - SEM ERRO DE ACENTO) ---
def gerar_link_wa(doutor, proj, acao):
    texto = f"🚀 PROJETO FRAJOLA\n\nDoutor: {doutor}\nProjeção: {proj}x\nAção: {acao}\n\nStatus: PADRÃO OURO ATIVADO"
    return f"https://wa.me/?text={urllib.parse.quote(texto)}"

link = gerar_link_wa(brain.doutor, proj_rodada, acao_imediata)
st.link_button("🚀 ENVIAR PARA WHATSAPP", link, use_container_width=True)

# Rodapé de Auditoria
st.divider()
st.caption("© 2026 Gêmea Fênix Bonde - Proteção Advogada Cabeluda")
