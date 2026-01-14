import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. CÉREBRO DA IA (ESTADO DE MEMÓRIA) ---
if 'memoria_proativa' not in st.session_state:
    st.session_state.memoria_proativa = []
if 'insight_ia' not in st.session_state:
    st.session_state.insight_ia = ""

class IAResolutiva:
    def __init__(self):
        self.estatuto_liberado = 69 #
        self.estatuto_pendente = 31 #
        self.valor_foco = 12500.00 # Valor fixado conforme seus prints

    def analisar_e_responder(self, medico, texto_usuario):
        """Simula a proatividade humana com base no contexto"""
        t = texto_usuario.lower()
        
        # Lógica Proativa de Saudação e Status
        if any(x in t for x in ["boa noite", "olá", "oi"]):
            return (f"Boa noite, Sidney! Já adiantei a análise da unidade {medico}. "
                    f"O valor de R$ {self.valor_foco:,.2f} está em CONFORMIDADE OK. "
                    "Minha sugestão proativa: Já podemos liberar para pagamento hoje. Prosseguimos?")

        # Lógica de Resolução de Pendências
        if "pendente" in t or "resolver" in t:
            return (f"Sidney, identifiquei que o gargalo na unidade {medico} é documental. "
                    f"Mesmo com {self.estatuto_pendente}% pendente no total, esta unidade está limpa. "
                    "Vou preparar o texto para o WhatsApp agora para não perdermos tempo.")

        # Lógica de Finalização Inteligente
        if any(x in t for x in ["obrigado", "valeu", "entendi", "somente isso"]):
            return (f"Perfeito, Sidney! Unidade {medico} processada com sucesso. "
                    "Já atualizei a Tabela da Favelinha para 'ENTRA'. Próximo médico da lista?")

        return f"Entendido, Sidney. Analisando o cenário de {medico}, a melhor ação agora é a aceleração do fluxo oficial."

ia_viva = IAResolutiva()

# --- 2. INTERFACE ESTATÍSTICA (PADRÃO OURO) ---
st.set_page_config(page_title="IA Sentinela Proativa", layout="wide")
st.title("🛡️ Caixa de Diálogo Online (IA Viva)")

# Métricas Sincronizadas
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", f"{ia_viva.estatuto_liberado}% LIBERADO")
c2.metric("EM AUDITORIA", f"{ia_viva.estatuto_pendente}% PENDENTE")

# --- 3. CANAL DE COMUNICAÇÃO PROATIVO ---
with st.container(border=True):
    medico_alvo = st.selectbox("Médico em Foco:", ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS"], key="sel_ia")
    input_user = st.text_input("Sua mensagem para a IA:", placeholder="Fale com a IA aqui...", key="chat_ia")

    if st.button("🚀 Ativar Projeto Frajola (Inteligência LLM)"):
        if input_user:
            # A IA gera um insight proativo
            resultado = ia_viva.analisar_e_responder(medico_alvo, input_user)
            st.session_state.insight_ia = resultado
            
            # Grava na Memória Quântica
            st.session_state.memoria_proativa.append({
                "Hora": datetime.now().strftime("%H:%M"),
                "Unidade": medico_alvo,
                "Você": input_user,
                "IA Proativa": resultado
            })

    # Balão de Resposta "Humana"
    if st.session_state.insight_ia:
        st.success(f"**Análise da IA:** {st.session_state.insight_ia}")
        
        # Link WhatsApp Seguro (Sem erros de acento)
        msg_formatada = urllib.parse.quote(st.session_state.insight_ia)
        st.markdown(f'''
            <a href="https://wa.me/5511942971753?text={msg_formatada}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">
                    🚀 ENVIAR PARA WHATSAPP
                </div>
            </a>
        ''', unsafe_allow_html=True)

# --- 4. MEMÓRIA E AUDITORIA ---
st.divider()
t1, t2 = st.tabs(["📋 Tabela da Favelinha", "📜 Histórico de Diálogo (Memória)"])

with t1:
    # Ação determinada pela proatividade da IA
    acao = "entra" if "conformidade" in st.session_state.insight_ia.lower() else "pula"
    st.table(pd.DataFrame([{"Médico": medico_alvo, "Ação": acao, "Valor": f"R$ {ia_viva.valor_foco:,.2f}"}]))

with t2:
    if st.session_state.memoria_proativa:
        st.dataframe(pd.DataFrame(st.session_state.memoria_proativa))
        
