import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. MOTOR DE MEMÓRIA VIVA (SESSÃO PERSISTENTE) ---
# Garante que a IA identifique o fluxo do diálogo e não esqueça o histórico
if 'historico_chat' not in st.session_state:
    st.session_state.historico_chat = []

class MotorSentinela:
    def __init__(self):
        self.total = 26801.80 #
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"}
        ]

    def processar_interacao(self, unidade, texto):
        """Identifica a intenção e interage conforme o diálogo"""
        med = next(item for item in self.db if item["unidade"] == unidade)
        t = texto.lower()
        
        # Lógica de Diálogo: Identifica agradecimentos ou conclusões
        if any(x in t for x in ["obrigado", "entendi", "valeu", "somente isso"]):
            return f"Show, Sidney! Registrei a conformidade da {unidade}. O histórico está salvo para auditoria. Próximo passo?"
        
        # Lógica de Diálogo: Identifica cobranças ou dúvidas técnicas
        if any(x in t for x in ["pendente", "resolver", "certeza", "andando"]):
            if med['status'] == "RESTRIÇÃO":
                return f"Análise Sugerida: Sidney, identifiquei que R$ {med['valor']:,.2f} da {unidade} está retido por falta de XML. Vamos destravar?"
            return f"Confirmado: a unidade {unidade} está em CONFORMIDADE OK com R$ {med['valor']:,.2f} no fluxo oficial."

        return f"Boa noite, Sidney! No contexto da {unidade}, o status é {med['status']}. Como posso agilizar isso agora?"

ms = MotorSentinela()

# --- 2. INTERFACE E ARREDONDAMENTO (PADRÃO OURO) ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
st.title("🛡️ Sentinela: Governança & Mediação")

# Arredondamento Sincronizado para 69% e 31%
p_lib = round((ms.liberado / ms.total) * 100)
p_pen = round((ms.pendente / ms.total) * 100)

c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", f"{p_lib}% LIBERADO")
c2.metric("EM AUDITORIA", f"{p_pen}% PENDENTE")

# Gráfico Nativo: Resolve erro de Plotly visto nas imagens
st.subheader(f"📊 Performance por Unidade (Total: R$ {ms.total:,.2f})")
st.bar_chart(pd.DataFrame(ms.db).set_index("unidade")["valor"])

tab1, tab2 = st.tabs(["💬 Canal de Comunicação Viva", "📜 Histórico de Diálogo"])

with tab1:
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in ms.db])
    entrada = st.text_input("Sua mensagem:", placeholder="Ex: Somente isso obrigado")
    
    if st.button("🚀 Ativar Projeto Frajola"):
        resposta = ms.processar_interacao(u_sel, entrada)
        
        # Salva para manter a coerência e histórico
        st.session_state.historico_chat.append({
            "Hora": datetime.now().strftime("%H:%M"), 
            "Unidade": u_sel, 
            "Sua Mensagem": entrada, 
            "Resposta IA": resposta
        })
        st.success(resposta)
        
        # Link WhatsApp Seguro (Resolve o TypeError)
        zap_url = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta)}"
        st.markdown(f'<a href="{zap_url}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

with tab2:
    if st.session_state.historico_chat:
        st.table(pd.DataFrame(st.session_state.historico_chat))
    else:
        st.info("Inicie uma interação para registrar o histórico.")

st.caption(f"Sidney Pereira de Almeida | {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')} | Sincronizado")
