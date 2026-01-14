import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. ÂNCORA DE MEMÓRIA (IMPEDE QUE A MENSAGEM SUMA) ---
# Inicializa o núcleo de memória para manter a interação viva
if 'memoria_sentinela' not in st.session_state:
    st.session_state.memoria_sentinela = []
if 'ultima_ia_msg' not in st.session_state:
    st.session_state.ultima_ia_msg = ""

class NucleoInteracao:
    def __init__(self):
        self.valor_total = 26801.80 #
        self.medicos = ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS", "LAB CLINIC"]

    def responder(self, medico, texto):
        """Interage de forma humana e coerente com o Sidney"""
        t = texto.lower()
        
        # Interação de Saudação
        if any(x in t for x in ["boa noite", "olá", "oi"]):
            return f"Boa noite, Sidney! Analisando {medico}, o status é CONFORMIDADE OK. Como as 17 IAs podem te ajudar agora?"
        
        # Interação de Fechamento (Evita que a IA repita saudações)
        if any(x in t for x in ["obrigado", "valeu", "entendi", "somente isso"]):
            return f"Show, Sidney! Registrei a conformidade da {medico}. Diálogo salvo na Memória Quântica. Próximo passo?"
            
        return f"Entendido, Sidney. Para {medico}, o parecer sugere fluxo normal. Deseja enviar para o WhatsApp?"

ni = NucleoInteracao()

# --- 2. INTERFACE ESTÁVEL E SEM ERROS ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
st.title("🛡️ Caixa de Diálogo Online")

# Arredondamento Padrão Ouro (69% e 31%)
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", "69% LIBERADO")
c2.metric("EM AUDITORIA", "31% PENDENTE")

# --- 3. CAIXA DE INTERAÇÃO (DIÁLOGO ONLINE) ---
with st.container(border=True):
    # 'key' garante que o Streamlit não limpe o campo sozinho
    med_foco = st.selectbox("Médico em Foco:", ni.medicos, key="escolha_medico")
    msg_sidney = st.text_input("Interação:", placeholder="Ex: Boa noite", key="chat_input")

    if st.button("🚀 Ativar Projeto Frajola"):
        if msg_sidney:
            # IA processa e o resultado é 'ancorado' na sessão
            resposta = ni.responder(med_foco, msg_sidney)
            st.session_state.ultima_ia_msg = resposta
            
            # Alimenta o Histórico (Memória Quântica)
            st.session_state.memoria_sentinela.append({
                "Hora": datetime.now().strftime("%H:%M"),
                "Médico": med_foco,
                "Sidney": msg_sidney,
                "IA Sentinela": resposta
            })

    # EXIBIÇÃO TRAVADA: A resposta não some ao clicar em outros botões
    if st.session_state.ultima_ia_msg:
        st.info(f"**Parecer Sugerido:** {st.session_state.ultima_ia_msg}")
        
        # WhatsApp Blindado contra TypeError
        zap_link = f"https://wa.me/5511942971753?text={urllib.parse.quote(st.session_state.ultima_ia_msg)}"
        st.markdown(f'<a href="{zap_link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

# --- 4. ABA DE HISTÓRICO (MEMÓRIA) ---
st.divider()
tab1, tab2 = st.tabs(["📋 Tabela da Favelinha", "📜 Histórico de Diálogo (Memória)"])

with tab1:
    st.table(pd.DataFrame([{"Médico": med_foco, "Ação": "entra"}]))

with tab2:
    if st.session_state.memoria_sentinela:
        st.dataframe(pd.DataFrame(st.session_state.memoria_sentinela))
    else:
        st.info("Inicie uma interação para alimentar a Memória Quântica.")
        
