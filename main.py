import streamlit as st
import urllib.parse
import pandas as pd

# --- 1. CORE DE INTELIGÊNCIA (As 17 Personas do Projeto Frajola) ---
class CoreGF17:
    def __init__(self, doutor="ANIMA COSTA"):
        self.doutor = doutor
        self.liberado = 85
        self.pendente = 15
        
    def processar_rag(self, prompt):
        # Lógica IA-SENTINELA: Rastreio de Vácuo (1.00x)
        if "1.00" in prompt or "vácuo" in prompt.lower():
            return "🚨 IA-SENTINELA: Bloqueio detectado! Zona de Vácuo (1.00x) identificada. Operação abortada."
        
        # Lógica Advogada Cabeluda: Blindagem e Auditoria
        if "auditoria" in prompt.lower():
            return f"⚖️ ADVOGADA CABELUDA: Iniciando blindagem para {self.doutor}. ROI protegido pelo Padrão Ouro."
            
        # Resposta de Sincronização
        return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {self.doutor}. Todas as 17 IAs em standby."

    def decisao_sts(self, projecao):
        # Regra: 'Entra' ou 'Pula' conforme a projeção
        if projecao <= 1.05:
            return "PULA"
        elif projecao >= 1.80:
            return "ENTRA"
        return "PULA"

# --- 2. CONFIGURAÇÃO DA INTERFACE (STREAMLIT) ---
st.set_page_config(page_title="GF-17 - Projeto Frajola", layout="centered")
if 'brain' not in st.session_state:
    st.session_state.brain = CoreGF17()

brain = st.session_state.brain

# --- 3. MÉTRICAS DINÂMICAS (Sincronização Padrão Ouro) ---
# Substitui palavras por porcentagens reais conforme sua regra
st.title(f"{brain.liberado}% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader(f"{brain.pendente}% PENDENTE")

st.divider()

# --- 4. CAMPO DE INTERAÇÃO RAG ---
st.write("### 🧠 Interação com as 17 Inteligências (RAG Mode):")
user_input = st.text_input("Digite sua mensagem:", value="Boa noite", key="input_rag")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if user_input:
        resposta = brain.processar_rag(user_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta}")

st.divider()

# --- 5. TABELA DA FAVELINHA (Visual Interface) ---
st.write("### 📋 TABELA DA FAVELINHA")

# Projeção atual conforme seu print
proj_atual = 1.85
acao = brain.decisao_sts(proj_atual)

df_favelinha = pd.DataFrame({
    "Doutor": [brain.doutor],
    "Projeção Rodada": [f"{proj_atual}x"],
    "Ação Imediata": [acao]
})

st.table(df_favelinha)

# Notificação visual sincronizada
st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para {brain.doutor} ({proj_atual}x).")

# --- 6. BOTÃO WHATSAPP (Mobile Fix - Sem erro de acento) ---
def gerar_link(doutor, proj, acao):
    texto = f"🚀 PROJETO FRAJOLA\nDoutor: {doutor}\nProjeção: {proj}x\nAção: {acao}\n\nStatus: PADRÃO OURO"
    # Codificação para evitar erro no celular
    return f"https://wa.me/?text={urllib.parse.quote(texto)}"

link_wa = gerar_link(brain.doutor, proj_atual, acao)
st.link_button("🚀 ENVIAR PARA WHATSAPP", link_wa, use_container_width=True)

# Rodapé de Auditoria
st.divider()
st.caption("© 2026 Gêmea Fênix Bonde - Sistema Blindado")
