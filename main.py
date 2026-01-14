import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA QUÂNTICA E REDE NEURAL DE ESTADO ---
if 'memoria_infinita' not in st.session_state:
    st.session_state.memoria_infinita = []
if 'brain_state' not in st.session_state:
    st.session_state.brain_state = {"fluxo": "estável", "risco": "baixo"}

class IASentinelaInfinita:
    def __init__(self):
        self.valor_unidade = 12500.00
        # Simulação de base de conhecimento "Infinita"
        self.kpi_historico = {"ANIMA COSTA": 0.98, "DR. MARCOS": 0.95, "INTERFILE - BI": 0.40}

    def raciocinio_preditivo(self, medico, comando):
        """A IA antecipa o vácuo e sugere ações antes da pergunta"""
        c = comando.lower()
        confianca = self.kpi_historico.get(medico, 0.50)
        
        # 1. Sugestão Proativa Baseada em Risco
        if confianca < 0.50 and "pagar" not in c:
            return {
                "ia": f"⚠️ ALERTA DE VÁCUO: Sidney, a {medico} está com score de conformidade baixo ({confianca*100}%). "
                      "Minha inteligência sugere 'PULA' até que o XML seja auditado. Deseja manter o bloqueio?",
                "status": "pula"
            }
        
        # 2. Execução de Ordem com Confirmação de Fluxo
        if any(x in c for x in ["pode liberar", "pagamento hoje", "autorizado"]):
            return {
                "ia": f"✅ INTELIGÊNCIA APLICADA: Ordem recebida. Unidade {medico} movida para 'ENTRA'. "
                      f"O valor de R$ {self.valor_unidade:,.2f} foi blindado contra o vácuo de 1.00x. "
                      "Protocolo de pagamento gerado. Próximo médico?",
                "status": "entra"
            }

        return {
            "ia": f"Boa noite, Sidney. Sistema Sentinela Online. Analisando {medico}, detecto estabilidade no fluxo. "
                  "Aguardando gatilho de decisão para processamento.",
            "status": "pula"
        }

# --- 2. INTERFACE ESTATÍSTICA (PADRÃO OURO) ---
st.set_page_config(page_title="Sentinela Infinita | GF-17", layout="wide")
st.title("🛡️ Sentinela: Inteligência Infinita")

# Sincronização Automática
col1, col2, col3 = st.columns(3)
col1.metric("ESTATUTO LIBERADO", "69%", "2% vs ontem")
col2.metric("EM AUDITORIA", "31%", "-1% vs ontem")
col3.metric("SCORE DE CONFIANÇA", "ALTO", delta_color="normal")

# --- 3. CAIXA DE DIÁLOGO ON-LINE (NÚCLEO VIVO) ---
st.subheader("💬 Diálogo On-line & Processamento Neural")
with st.container(border=True):
    med_sel = st.selectbox("Unidade em Análise:", ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS"], key="med_inf")
    msg_sidney = st.text_input("Comando Neural:", placeholder="Ex: Pode liberar o pagamento", key="in_inf")

    if st.button("🚀 Ativar Inteligência Sentinela"):
        if msg_sidney:
            brain = IASentinelaInfinita()
            decisao = brain.raciocinio_preditivo(med_sel, msg_sidney)
            
            # Persistência na Memória Quântica
            st.session_state.memoria_infinita.append({
                "T": datetime.now().strftime("%H:%M"),
                "U": med_sel,
                "Msg": msg_sidney,
                "IA": decisao["ia"]
            })
            st.session_state.brain_state = decisao

    # Resposta Inteligente (Persistente)
    if st.session_state.brain_state.get("ia"):
        st.info(f"**Insight da IA Sentinela:** {st.session_state.brain_state['ia']}")
        
        # Link WhatsApp Blindado
        zap_msg = urllib.parse.quote(st.session_state.brain_state["ia"])
        st.markdown(f'''
            <a href="https://wa.me/5511942971753?text={zap_msg}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">
                    🚀 ENVIAR DECISÃO PARA AUDITORIA
                </div>
            </a>
        ''', unsafe_allow_html=True)

# --- 4. TABELA DA FAVELINHA & PROJEÇÃO ---
st.divider()
t1, t2 = st.tabs(["📋 Tabela da Favelinha (Ação)", "📜 Log de Inteligência"])

with t1:
    # A IA agora sugere a decisão baseada no risco histórico
    st.table(pd.DataFrame([{
        "Unidade": med_sel, 
        "Ação Sugerida": st.session_state.brain_state["status"],
        "Risco de Vácuo": "BAIXO" if st.session_state.brain_state["status"] == "entra" else "ALTO"
    }]))

with t2:
    if st.session_state.memoria_infinita:
        st.dataframe(pd.DataFrame(st.session_state.memoria_infinita))
            
