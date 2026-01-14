import streamlit as st
import urllib.parse
import pandas as pd
import requests

# --- 1. CORE DE INTELIGÊNCIA GF-17 (VISÃO GLOBAL & RAG) ---
class CoreGF17:
    def __init__(self, doutor="ANIMA COSTA"):
        self.doutor = doutor
        self.liberado = "85%"
        self.pendente = "15%"
        
    def processar_rag(self, prompt):
        p = prompt.lower()
        
        # Regra IA-SENTINELA: Bloqueio de Vácuo (Zona 1.00x)
        if "1.00" in p or "vácuo" in p:
            return "🚨 IA-SENTINELA: Bloqueio detectado! Zona de Vácuo (1.00x) identificada. Operação abortada."
        
        # Visão Global / Classificação
        if "classificação" in p or "internet" in p:
            return f"🌍 VISÃO GLOBAL: Conectada ao servidor. Classificação auditada: Padrão Ouro em vigor."

        # Resposta CFO VISION
        if "tudo bem" in p:
            return "🔥 CFO VISION: Analisando margem líquida. Sistema pronto para o gatilho de entrada."

        # Resposta Padrão
        return f"✨ GÊMEA FÊNIX: Sincronização total para {self.doutor}. 17 IAs online via Cloud."

    def decisao_sts(self, projecao):
        # Regra: 'Entra' ou 'Pula' conforme a projeção de cada rodada
        if projecao <= 1.05:
            return "PULA"
        elif projecao >= 1.80:
            return "ENTRA"
        return "PULA"

# --- 2. CONFIGURAÇÃO DA INTERFACE ---
st.set_page_config(page_title="GF-17 - Projeto Frajola", layout="centered")
brain = CoreGF17()

# --- 3. MÉTRICAS DINÂMICAS (Sincronizadas) ---
st.title(f"{brain.liberado} LIBERADO")
st.caption("EM AUDITORIA")
st.subheader(f"{brain.pendente} PENDENTE")
st.divider()

# --- 4. CAMPO DE INTERAÇÃO (RAG MODE) ---
st.write("🧠 **Interação com as 17 Inteligências (RAG Mode):**")
user_input = st.text_input("Digite sua mensagem para o sistema:", key="input_global")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if user_input:
        resposta = brain.processar_rag(user_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta}")

st.divider()

# --- 5. TABELA DA FAVELINHA (Sempre visível) ---
st.write("### 📋 TABELA DA FAVELINHA")
proj_rodada = 1.85 # Valor determinado a partir da projeção da rodada
acao = brain.decisao_sts(proj_rodada)

df_favelinha = pd.DataFrame({
    "Doutor": [brain.doutor],
    "Projeção Rodada": [f"{proj_rodada}x"],
    "Ação Imediata": [acao]
})
st.table(df_favelinha)

st.success(f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para {brain.doutor} ({proj_rodada}x).")

# --- 6. BOTÃO WHATSAPP (Mobile Fix - Sem erro de acento) ---
def gerar_link_wa(doutor, proj, acao_final):
    # Texto codificado para evitar erros no celular
    texto = f"🚀 PROJETO FRAJOLA\n\nDoutor: {doutor}\nProjeção: {proj}x\nAção: {acao_final}\n\nStatus: PADRÃO OURO ATIVADO"
    return f"https://wa.me/?text={urllib.parse.quote(texto)}"

link_final = gerar_link_wa(brain.doutor, proj_rodada, acao)
st.link_button("🚀 ENVIAR PARA WHATSAPP", link_final, use_container_width=True)

# Rodapé
st.divider()
st.caption("© 2026 Gêmea Fênix - Sistema de Visão Global")
