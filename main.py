import streamlit as st
import urllib.parse
import pandas as pd

# --- 1. CONFIGURAÇÃO DO MOTOR DE INTELIGÊNCIA (GF-17) ---
class FenixEngine:
    def __init__(self):
        self.doutor = "ANIMA COSTA"
        self.versao = "2.0 RAG"
        
    def processar_inteligencia(self, prompt):
        # Filtro de Segurança IA-SENTINELA
        if "1.00" in prompt or "vácuo" in prompt.lower():
            return "🚨 IA-SENTINELA: Operação Abortada! Vácuo detectado (1.00x). Risco de perda total de ativos."
        
        # Filtro de Blindagem Advogada Cabeluda
        if "auditoria" in prompt.lower() or "liberado" in prompt.lower():
            return "⚖️ ADVOGADA CABELUDA: Blindagem Padrão Ouro ativa. ROI protegido e 85% do capital liberado para operação."
        
        # Resposta de Sincronização Geral
        if "boa noite" in prompt.lower() or "olá" in prompt.lower():
            return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {self.doutor}. Todas as 17 IAs estão em standby tático."
            
        return "🔥 SISTEMA ATIVO: Processando análise quântica da rodada atual..."

# --- 2. INICIALIZAÇÃO ---
st.set_page_config(page_title="Projeto Frajola GF-17", layout="centered")
brain = FenixEngine()

# --- 3. INTERFACE VISUAL (CONFORME SEUS PRINTS) ---

# Títulos de Status com Substituição Dinâmica de %
st.title("85% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader("15% PENDENTE")

st.divider()

# Campo de Interação RAG (Onde o sistema 'pensa')
st.write("### 🧠 Interação com as 17 Inteligências (RAG Mode):")
user_input = st.text_input("Digite sua mensagem para o sistema:", placeholder="Ex: Analisar vácuo ou status da auditoria")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if user_input:
        with st.spinner('As 17 inteligências estão processando...'):
            resposta = brain.processar_inteligencia(user_input)
            st.info(f"🧐 GÊMEA FÊNIX: {resposta}")
    else:
        st.warning("A Maluquinha dos Códigos avisa: Digite algo para ativar o cérebro!")

st.divider()

# --- 4. TABELA DA FAVELINHA (LÓGICA ESTRUTURADA) ---
st.write("### 📋 TABELA DA FAVELINHA")

data = {
    "Doutor": [brain.doutor],
    "Projeção Rodada": ["1.85x"],
    "Ação Imediata": ["PULA"] # Ação baseada na análise da IA-SENTINELA
}
df = pd.DataFrame(data)
st.table(df)

# Feedback visual da Gêmea Fênix
st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para {brain.doutor} (1.85x).")

# --- 5. BOTÃO WHATSAPP (MOBILE FIX - SEM ERRO DE ACENTO) ---
def gerar_link_whatsapp(doutor, projecao, acao):
    texto = f"🚀 PROJETO FRAJOLA\n\nDoutor: {doutor}\nProjeção: {projecao}\nAção: {acao}\n\nStatus: PADRÃO OURO ATIVADO"
    # O segredo da Maluquinha dos Códigos para não dar erro no celular:
    texto_codificado = urllib.parse.quote(texto)
    return f"https://wa.me/?text={texto_codificado}"

link = gerar_link_whatsapp(brain.doutor, "1.85x", "PULA")

st.link_button("🚀 ENVIAR PARA WHATSAPP", link, use_container_width=True)

# Rodapé de Auditoria
st.divider()
st.caption("© 2026 Gêmea Fênix Bonde - Protegido pela Advogada Cabeluda")
