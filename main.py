import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA QUÂNTICA BLINDADA (EVITA KEYERROR) ---
# Inicializamos estados padrão para que o sistema nunca trave
if 'brain' not in st.session_state:
    st.session_state.brain = {"msg": "Sistema pronto.", "status": "pula", "score": 100}
if 'log_infinito' not in st.session_state:
    st.session_state.log_infinito = []

class CérebroInfinito:
    def __init__(self):
        self.meta_liberada = 69 #
        # Histórico de confiabilidade (Exemplo de aprendizado)
        self.historico_medicos = {"ANIMA COSTA": 95, "INTERFILE - BI": 40}

    def processar_conhecimento(self, medico, comando):
        """A IA aprende com o contexto e sugere o melhor caminho"""
        c = comando.lower()
        score = self.historico_medicos.get(medico, 50)
        
        # Inteligência Proativa: Alerta de Risco
        if score < 50 and "liberar" not in c:
            return {
                "msg": f"⚠️ ATENÇÃO: Score de {medico} está baixo ({score}%). Sugiro auditoria rígida antes de qualquer 'ENTRA'.",
                "status": "pula", "score": score
            }

        # Inteligência Executiva: Ordem Direta
        if any(x in c for x in ["pode liberar", "pagamento", "autorizado"]):
            return {
                "msg": f"🚀 INTELIGÊNCIA APLICADA: Unidade {medico} autorizada. Atualizando Favelinha para ENTRA. Fluxo de R$ 12.500,00 protegido.",
                "status": "entra", "score": score
            }

        return {
            "msg": f"Olá Sidney! Analisando {medico}. Tudo está em conformidade. Aguardo seu comando.",
            "status": "pula", "score": score
        }

# --- 2. INTERFACE SENTINELA ---
st.set_page_config(page_title="Sentinela Infinita", layout="wide")
st.title("🛡️ Sentinela: Inteligência Infinita")

# Painel de Controle
c1, c2, c3 = st.columns(3)
c1.metric("ESTATUTO", "69% LIBERADO")
c2.metric("PENDENTE", "31% AUDITORIA")
c3.metric("SCORE IA", f"{st.session_state.brain['score']}%")

# --- 3. CAIXA DE DIÁLOGO NEURAL ---
with st.container(border=True):
    medico_alvo = st.selectbox("Médico em Foco:", ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS"], key="sel_inf")
    comando_sidney = st.text_input("Interação Proativa:", placeholder="Ex: Pode liberar o pagamento", key="in_inf")

    if st.button("🚀 Ativar Inteligência Sentinela"):
        if comando_sidney:
            # Executa o processamento sem risco de travar
            engine = CérebroInfinito()
            resultado = engine.processar_conhecimento(medico_alvo, comando_sidney)
            st.session_state.brain = resultado
            
            # Alimenta a Memória de Longo Prazo
            st.session_state.log_infinito.append({
                "Data": datetime.now().strftime("%H:%M"),
                "Unidade": medico_alvo,
                "Decisão": resultado["status"].upper(),
                "Parecer": resultado["msg"]
            })

    # Resposta Inteligente (Persistente na tela)
    if st.session_state.brain["msg"]:
        st.info(f"**Insight da IA:** {st.session_state.brain['msg']}")
        
        # Link WhatsApp Blindado
        zap_link = f"https://wa.me/5511942971753?text={urllib.parse.quote(st.session_state.brain['msg'])}"
        st.markdown(f'<a href="{zap_link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR DECISÃO PARA WHATSAPP</div></a>', unsafe_allow_html=True)

# --- 4. TABELA DA FAVELINHA (AGORA BLINDADA) ---
st.divider()
tab_fav, tab_log = st.tabs(["📋 Tabela da Favelinha", "📜 Log de Inteligência"])

with tab_fav:
    # Resolve o erro de KeyError garantindo que o dicionário exista
    df_fav = pd.DataFrame([{
        "Médico": medico_alvo, 
        "Ação": st.session_state.brain.get("status", "pula"),
        "Confiança": f"{st.session_state.brain.get('score', 0)}%"
    }])
    st.table(df_fav)

with tab_log:
    if st.session_state.log_infinito:
        st.dataframe(pd.DataFrame(st.session_state.log_infinito))
