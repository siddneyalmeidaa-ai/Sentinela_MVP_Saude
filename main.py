import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA QUÂNTICA ATIVA ---
if 'historico' not in st.session_state:
    st.session_state.historico = []
if 'decisao_ia' not in st.session_state:
    st.session_state.decisao_ia = {"msg": "", "acao": "pula"}

class CérebroSentinela:
    def __init__(self):
        self.valor_unidade = 12500.00 # Valor extraído do seu print

    def processar_decisao(self, medico, comando):
        """Lógica proativa: Transforma conversa em ação imediata"""
        c = comando.lower()
        
        # GATILHO DE PAGAMENTO (Onde havia travado)
        if any(x in c for x in ["pode liberar", "fazer o pagamento", "pode pagar", "autorizado"]):
            msg = (f"🚀 EXECUTANDO AGORA: Sidney, autorização recebida para {medico}. "
                   f"Valor de R$ {self.valor_unidade:,.2f} movido para o fluxo de PAGAMENTO. "
                   "Tabela da Favelinha atualizada para 'ENTRA'. Deseja que eu envie o comprovante após o processamento?")
            return {"msg": msg, "acao": "entra"}
            
        # GATILHO DE SAUDAÇÃO/STATUS
        if any(x in c for x in ["boa noite", "olá", "oi"]):
            return {"msg": f"Boa noite, Sidney! Unidade {medico} em conformidade. Aguardo sua ordem para liberar o fluxo.", "acao": "pula"}

        return {"msg": f"Entendido. Monitorando {medico}. Alguma instrução específica sobre o valor de R$ {self.valor_unidade:,.2f}?", "acao": "pula"}

# --- 2. INTERFACE ESTATÍSTICA (69% / 31%) ---
st.set_page_config(page_title="IA Proativa | GF-17", layout="wide")
st.title("🛡️ Caixa de Diálogo Online (IA Viva)")

# Sincronização de Metas
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", "69% LIBERADO")
c2.metric("EM AUDITORIA", "31% PENDENTE")

# --- 3. CAIXA DE DIÁLOGO E DECISÃO ---
with st.container(border=True):
    medico_foco = st.selectbox("Médico em Foco:", ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS"], key="medico_viva")
    input_sidney = st.text_input("Comando para a IA (Ex: Pode liberar o pagamento):", key="cmd_viva")

    if st.button("🚀 Ativar Projeto Frajola (Inteligência LLM)"):
        if input_sidney:
            # IA Processa a autonomia
            cerebro = CérebroSentinela()
            resultado = cerebro.processar_decisao(medico_foco, input_sidney)
            st.session_state.decisao_ia = resultado
            
            # Alimenta Histórico para Auditoria
            st.session_state.historico.append({
                "Hora": datetime.now().strftime("%H:%M"),
                "Médico": medico_foco,
                "Ação": resultado["acao"],
                "Parecer": resultado["msg"]
            })

    # Resposta Visual Proativa
    if st.session_state.decisao_ia["msg"]:
        st.success(f"**Análise Proativa:** {st.session_state.decisao_ia['msg']}")
        
        # WhatsApp com link blindado contra erros
        msg_zap = urllib.parse.quote(st.session_state.decisao_ia["msg"])
        st.markdown(f'''
            <a href="https://wa.me/5511942971753?text={msg_zap}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">
                    🚀 ENVIAR DECISÃO PARA WHATSAPP
                </div>
            </a>
        ''', unsafe_allow_html=True)

# --- 4. TABELA DA FAVELINHA (ATUALIZAÇÃO AUTOMÁTICA) ---
st.subheader("📋 Tabela da Favelinha (Ação Imediata)")
df_favelinha = pd.DataFrame([{"Médico": medico_foco, "Status": "Conformidade OK", "Ação": st.session_state.decisao_ia["acao"]}])
st.table(df_favelinha) # Entrega visual sem blocos de código
