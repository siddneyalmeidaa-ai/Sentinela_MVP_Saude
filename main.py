import streamlit as st
import urllib.parse

# --- NÚCLEO DE INTELIGÊNCIA GF-17 ---
class ProjetoFrajolaBrain:
    def __init__(self):
        # Definição das Personas Criadas pelo Bigode
        self.personas = {
            "IA-SENTINELA": "Rastreador de Vácuo (1.00x).",
            "ADVOGADA_CABELUDA": "Blindagem Jurídica e ROI.",
            "MALUQUINHA_DOS_CODIGOS": "Engenharia de Prompt e Mobile Fix.",
            "CFO_VISION": "Cálculo de Margem e Lucro Líquido."
        }

    def processar_interacao(self, prompt):
        # Lógica RAG: O sistema 'pensa' com base nas 17 IAs
        if "1.00" in prompt or "vácuo" in prompt.lower():
            return "🚨 IA-SENTINELA: Bloqueio ativado. Risco de vácuo identificado."
        if "boa noite" in prompt.lower():
            return "✨ GÊMEA FÊNIX: Sincronizando dados para o Projeto Frajola..."
        return "🔥 SISTEMA ATIVO: Aguardando comando tático."

    def calcular_acao(self, projecao):
        # Lógica da Tabela da Favelinha (conforme print: 1.85x)
        if projecao <= 1.05: return "PULA (Vácuo)"
        if projecao >= 1.80: return "ENTRA (Padrão Ouro)"
        return "AGUARDAR"

# --- INTERFACE (SIMULANDO O SEU APP) ---
brain = ProjetoFrajolaBrain()

# Métricas do Print
st.title("85% LIBERADO")
st.caption("EM AUDITORIA")
st.subheader("15% PENDENTE")

# Interação RAG
user_input = st.text_input("Interação com as 17 Inteligências (RAG Mode):", value="Boa noite")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    resposta = brain.processar_interacao(user_input)
    st.info(f"🧐 GÊMEA FÊNIX: {resposta}")

# Tabela da Favelinha
projecao = 1.85
status = brain.calcular_acao(projecao)
# Exibição dos dados do Doutor ANIMA COSTA conforme o print

# Botão WhatsApp com Mobile Fix (UTF-8)
msg = f"Doutor ANIMA COSTA, ação para {projecao}x: {status}"
url_whatsapp = f"https://wa.me/?text={urllib.parse.quote(msg)}"
st.link_button("🚀 ENVIAR PARA WHATSAPP", url_whatsapp)
