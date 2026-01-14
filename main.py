import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MOTOR DE MEMÓRIA QUÂNTICA (LLM CONTEXT) ---
# Garante que a IA não "se perca" ao clicar nos botões
if 'historico_llm' not in st.session_state:
    st.session_state.historico_llm = []
if 'resposta_ativa' not in st.session_state:
    st.session_state.resposta_ativa = ""

class MotorLLM:
    def __init__(self):
        self.total = 26801.80 #
        self.medicos = ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS", "LAB CLINIC"]

    def processar_linguagem(self, medico, prompt):
        """Simula a lógica de um LLM para interagir com o Sidney"""
        p = prompt.lower()
        
        # Lógica de Contexto: Identifica saudações ou agradecimentos
        if any(x in p for x in ["boa noite", "olá", "oi"]):
            return f"Boa noite, Sidney! Analisando a unidade {medico}, o status atual é CONFORMIDADE OK. Como as 17 IAs podem acelerar seu processo?"
        
        if any(x in p for x in ["obrigado", "valeu", "entendi", "somente isso"]):
            return f"Perfeito, Sidney! Registrei a conformidade da unidade {medico}. Diálogo salvo na Memória Quântica para auditoria."
        
        return f"Parecer Técnico: Sidney, verifiquei que {medico} opera com fluxo normal sob o Estatuto Atual (69% Liberado). Alguma outra dúvida?"

ai_nucleo = MotorLLM()

# --- 2. INTERFACE PADRÃO OURO (ESTÁVEL) ---
st.set_page_config(page_title="Sentinela LLM | GF-17", layout="wide")
st.title("🛡️ Sentinela: Inteligência de Dados")

# Arredondamento Sincronizado (69% e 31%)
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", "69% LIBERADO")
c2.metric("EM AUDITORIA", "31% PENDENTE")

# --- 3. CAIXA DE DIÁLOGO ONLINE (PROJETO FRAJOLA) ---
st.subheader("💬 Caixa de Diálogo Online (IA Viva)")
with st.container(border=True):
    col_med, col_msg = st.columns([1, 2])
    with col_med:
        u_sel = st.selectbox("Médico em Foco:", ai_nucleo.medicos, key="med_llm")
    with col_msg:
        entrada = st.text_input("Interação:", placeholder="Ex: Boa noite, tudo bem?", key="input_llm")

    if st.button("🚀 Ativar Projeto Frajola"):
        if entrada:
            # IA processa e a resposta fica 'travada' na memória
            resposta_ia = ai_nucleo.processar_linguagem(u_sel, entrada)
            st.session_state.resposta_ativa = resposta_ia
            
            # Alimenta a Memória Quântica (Histórico)
            st.session_state.historico_llm.append({
                "Data": datetime.now().strftime("%d/%m %H:%M"),
                "Unidade": u_sel,
                "Sidney": entrada,
                "IA Sentinela": resposta_ia
            })

    # Exibição do Parecer (Não some ao clicar)
    if st.session_state.resposta_ativa:
        st.info(f"**Análise da IA:** {st.session_state.resposta_ativa}")
        
        # Link WhatsApp Blindado (Resolve o TypeError dos seus prints)
        texto_zap = urllib.parse.quote(st.session_state.resposta_ativa)
        url_zap = f"https://wa.me/5511942971753?text={texto_zap}"
        st.markdown(f'<a href="{url_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

# --- 4. ABA DE SALVAMENTO (MEMÓRIA) ---
st.divider()
t1, t2 = st.tabs(["📋 Tabela da Favelinha", "📜 Histórico de Diálogo (Memória)"])

with t1:
    st.table(pd.DataFrame([{"Médico": u_sel, "Ação": "entra"}])) # Regras salvas

with t2:
    if st.session_state.historico_llm:
        st.dataframe(pd.DataFrame(st.session_state.historico_llm))
    else:
        st.info("Aguardando interações para alimentar a memória.")

st.caption(f"Sidney Pereira de Almeida | {datetime.now().strftime('%d/%m/%Y %H:%M')} | Sincronizado")
