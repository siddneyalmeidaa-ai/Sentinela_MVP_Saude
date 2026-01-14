import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. MEMÓRIA DE DIÁLOGO (GARANTE A COERÊNCIA) ---
# Inicializa o estado para que a IA não esqueça o que foi dito
if 'historico_viva' not in st.session_state:
    st.session_state.historico_viva = []
if 'conversa_ativa' not in st.session_state:
    st.session_state.conversa_ativa = []

class MotorAuditoria:
    def __init__(self):
        self.total = 26801.80 #
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"}
        ]

    def responder_conforme_dialogo(self, unidade, texto):
        """Analisa o texto e interage conforme o contexto"""
        med = next(item for item in self.db if item["unidade"] == unidade)
        t = texto.lower()
        
        # Identificação de encerramento ou agradecimento
        if any(x in t for x in ["obrigado", "valeu", "tá bom", "entendi"]):
            return f"Show, Sidney! Registrei a conformidade da {unidade}. O histórico está salvo para auditoria. Próximo passo?"
        
        # Identificação de dúvida sobre pendências
        if any(x in t for x in ["pendente", "resolver", "certeza"]):
            if med['status'] == "RESTRIÇÃO":
                return f"Sidney, identifiquei que o valor de R$ {med['valor']:,.2f} está retido por falta de arquivos XML. Vamos destravar agora?"
            return f"Confirmado: a {unidade} está em CONFORMIDADE OK para o valor de R$ {med['valor']:,.2f}."

        return f"Olá Sidney! Analisando a {unidade}, o status é {med['status']}. Como posso agilizar isso agora?"

ma = MotorAuditoria()

# --- 2. INTERFACE (RESTAURAÇÃO E ARREDONDAMENTO) ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
st.title("🛡️ Sentinela: Governança & Mediação")

# Arredondamento para visual limpo
p_lib = round((ma.liberado / ma.total) * 100)
p_pen = round((ma.pendente / ma.total) * 100)

c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", f"{p_lib}% LIBERADO")
c2.metric("EM AUDITORIA", f"{p_pen}% PENDENTE")

# Gráfico Nativo (Resolve erro de Plotly das imagens)
st.subheader(f"📊 Performance por Unidade (Total: R$ {ma.total:,.2f})")
st.bar_chart(pd.DataFrame(ma.db).set_index("unidade")["valor"])

tab1, tab2 = st.tabs(["💬 Canal de Comunicação Viva", "📜 Histórico de Diálogo"])

with tab1:
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in ma.db])
    entrada = st.text_input("Sua mensagem:", placeholder="Ex: Tá bom, obrigado")
    
    if st.button("🚀 Ativar Projeto Frajola"):
        resposta = ma.responder_conforme_dialogo(u_sel, entrada)
        
        # Salva no histórico persistente
        st.session_state.conversa_ativa.append({
            "Momento": datetime.now().strftime("%H:%M"),
            "Unidade": u_sel,
            "Você": entrada,
            "IA": resposta
        })
        st.success(resposta)
        
        # Link WhatsApp Seguro
        url = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta)}"
        st.markdown(f'<a href="{url}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

with tab2:
    if st.session_state.conversa_ativa:
        st.table(pd.DataFrame(st.session_state.conversa_ativa))
    else:
        st.info("Inicie um diálogo para registrar o histórico.")

st.caption(f"Sidney Pereira de Almeida | {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')} | Sincronizado")
