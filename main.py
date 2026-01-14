import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA DE DIÁLOGO (ESTADO DA SESSÃO) ---
# Impede que a IA se perca ou apague a mensagem ao clicar
if 'historico_viva' not in st.session_state:
    st.session_state.historico_viva = []
if 'resposta_travada' not in st.session_state:
    st.session_state.resposta_travada = ""

class MotorInteracao:
    def __init__(self):
        self.valor_consolidado = 26801.80 #
        self.medicos = ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS", "LAB CLINIC"]

    def processar_conversa(self, medico, texto):
        """Interage conforme o diálogo (ex: Boa noite) e mantém coerência"""
        t = texto.lower()
        
        # Interação Natural (Saudação e Conclusão)
        if any(x in t for x in ["boa noite", "olá", "oi"]):
            return f"Boa noite, Sidney! Analisando a unidade {medico}, verifiquei que o status está em CONFORMIDADE OK. Como as 17 IAs podem agilizar seu processo agora?"
        
        if any(x in t for x in ["obrigado", "valeu", "entendi", "somente isso"]):
            return f"Show, Sidney! Registrei a conformidade da {medico}. Diálogo salvo na Memória Quântica. Próximo passo?"
        
        return f"Entendido, Sidney. Para a unidade {medico}, o parecer sugere fluxo normal de processamento. Deseja enviar para o WhatsApp?"

mi = MotorInteracao()

# --- 2. INTERFACE ESTÁVEL (CORREÇÃO DE ERROS DOS PRINTS) ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
st.title("🛡️ Caixa de Diálogo Online")

# Arredondamento Padrão Ouro
st.write(f"**VALOR TOTAL CONSOLIDADO: R$ {mi.valor_consolidado:,.2f}**")
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", "69% LIBERADO")
c2.metric("EM AUDITORIA", "31% PENDENTE")

# --- 3. CANAL DE COMUNICAÇÃO VIVA (SEM PERDA DE DADOS) ---
with st.container(border=True):
    # Selectbox e Input com 'key' para travar na memória
    medico_sel = st.selectbox("Selecione o Médico:", mi.medicos, key="sel_medico")
    msg_user = st.text_input("Sua mensagem:", placeholder="Ex: Boa noite", key="input_usuario")

    if st.button("🚀 Ativar Projeto Frajola"):
        if msg_user:
            # IA processa e a resposta é salva no estado da sessão
            resultado = mi.processar_conversa(medico_sel, msg_user)
            st.session_state.resposta_travada = resultado
            
            # Alimenta o Histórico (Memória Quântica)
            st.session_state.historico_viva.append({
                "Data": datetime.now().strftime("%H:%M"),
                "Médico": medico_sel,
                "Interação": msg_user,
                "Parecer IA": resultado
            })

    # Exibição do Parecer (SÓ APARECE E TRAVA SE HOUVER RESPOSTA)
    if st.session_state.resposta_travada:
        st.info(f"**Parecer das 17 IAs:** {st.session_state.resposta_travada}")
        
        # Link WhatsApp Blindado contra TypeError
        zap_msg = urllib.parse.quote(st.session_state.resposta_travada)
        url_zap = f"https://wa.me/5511942971753?text={zap_msg}"
        st.markdown(f'<a href="{url_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

# --- 4. ABA DE SALVAMENTO (MEMÓRIA) ---
st.divider()
tab1, tab2 = st.tabs(["📋 Tabela da Favelinha", "📜 Histórico de Diálogo (Memória)"])

with tab1:
    st.table(pd.DataFrame([{"Médico": medico_sel, "Ação": "entra"}])) # Regra salva

with tab2:
    if st.session_state.historico_viva:
        st.dataframe(pd.DataFrame(st.session_state.historico_viva))
    else:
        st.info("Aguardando interações para alimentar a memória.")
        
