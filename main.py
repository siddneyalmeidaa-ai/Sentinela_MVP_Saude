import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA QUÂNTICA (ESTADO DA SESSÃO) ---
# Inicializa as variáveis para que nada suma ao clicar nos botões
if 'historico_viva' not in st.session_state:
    st.session_state.historico_viva = []
if 'ultima_resposta' not in st.session_state:
    st.session_state.ultima_resposta = ""

class MotorSentinela:
    def __init__(self):
        self.total = 26801.80
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.medicos = ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS"]

    def interpretar(self, medico, texto):
        """Interpreta a intenção do diálogo sem perder a coerência"""
        t = texto.lower()
        if any(x in t for x in ["obrigado", "valeu", "show", "entendi"]):
            return f"Show, Sidney! Registrei a conformidade da {medico}. Próximo passo?"
        if "pendente" in t:
            return f"Sidney, identifiquei que {medico} tem R$ 5.400,00 pendentes por falta de XML."
        return f"Olá Sidney! No contexto da {medico}, o status é CONFORMIDADE OK. Como posso ajudar?"

ms = MotorSentinela()

# --- 2. INTERFACE ESTÁVEL ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
st.title("🛡️ Caixa de Diálogo Online")

# Arredondamento Padrão Ouro
p_lib = round((ms.liberado / ms.total) * 100)
p_pen = round((ms.pendente / ms.total) * 100)

c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", f"{p_lib}% LIBERADO")
c2.metric("EM AUDITORIA", f"{p_pen}% PENDENTE")

# --- 3. CAIXA DE DIÁLOGO BLINDADA ---
with st.container(border=True):
    medico_foco = st.selectbox("Médico em Foco:", ms.medicos)
    
    # Usamos o parâmetro 'key' para manter o texto na memória
    msg_input = st.text_input("Interação:", key="input_dialogo", placeholder="Digite e clique em Ativar...")

    if st.button("🚀 Ativar Projeto Frajola"):
        if msg_input:
            # IA interpreta e gera a resposta
            resposta = ms.interpretar(medico_foco, msg_input)
            st.session_state.ultima_resposta = resposta
            
            # Salva no histórico para não sumir
            st.session_state.historico_viva.append({
                "Hora": datetime.now().strftime("%H:%M"),
                "Médico": medico_foco,
                "Você": msg_input,
                "IA Sentinela": resposta
            })

    # Exibe a resposta travada na tela (não some ao clicar em outros botões)
    if st.session_state.ultima_resposta:
        st.info(f"**Parecer Sugerido:** {st.session_state.ultima_resposta}")
        
        # Link WhatsApp Seguro (Resolve o TypeError dos prints)
        url_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(st.session_state.ultima_resposta)}"
        st.markdown(f'<a href="{url_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

# --- 4. ABA DE HISTÓRICO (MEMÓRIA QUÂNTICA) ---
st.divider()
tab1, tab2 = st.tabs(["📋 Tabela da Favelinha", "📜 Histórico de Diálogo (Memória)"])

with tab1:
    st.table(pd.DataFrame([{"Médico": "ANIMA COSTA", "Ação": "entra"}, {"Médico": "INTERFILE - BI", "Ação": "pula"}]))

with tab2:
    if st.session_state.historico_viva:
        st.dataframe(pd.DataFrame(st.session_state.historico_viva))
    else:
        st.info("Aguardando interações...")
        
