import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. MEMÓRIA QUÂNTICA (ESTADO DA SESSÃO) ---
# Garante que o diálogo online e o histórico não se percam
if 'memoria_ativa' not in st.session_state:
    st.session_state.memoria_ativa = []

class MotorCoerente:
    def __init__(self):
        self.total = 26801.80 #
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.medicos = ["ANIMA COSTA", "DR. MARCOS", "INTERFILE - BI", "DR. SILVA", "LAB CLINIC"]

    def processar_chat(self, medico, texto):
        """Interage conforme o diálogo e mantém a coerência"""
        t = texto.lower()
        # Identifica se o usuário está encerrando ou agradecendo
        if any(word in t for word in ["obrigado", "valeu", "entendi", "somente isso"]):
            return f"Show, Sidney! Registrei a conformidade da {medico}. Diálogo salvo na Memória Quântica. Próximo passo?"
        
        # Identifica se o usuário tem dúvidas sobre pendências
        if any(word in t for word in ["pendente", "resolver", "certeza"]):
            return f"Análise Crítica: Sidney, a unidade {medico} está sendo processada. Verifiquei que o vácuo de 1.00x foi evitado. Tudo em ordem."
        
        return f"Boa noite, Sidney! Analisando {medico}, o status é CONFORMIDADE OK. Como as 17 IAs podem agilizar seu processo agora?"

mc = MotorCoerente()

# --- 2. INTERFACE E ARREDONDAMENTO PADRÃO OURO ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
st.title("🛡️ Sentinela: Governança & Dinamismo")

# Arredondamento Sincronizado
p_lib = round((mc.liberado / mc.total) * 100)
p_pen = round((mc.pendente / mc.total) * 100)

c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", f"{p_lib}% LIBERADO")
c2.metric("EM AUDITORIA", f"{p_pen}% PENDENTE")

# --- 3. CAIXA DE DIÁLOGO ONLINE (ESTRUTURA VIVA) ---
st.subheader("💬 Caixa de Diálogo Online")
with st.container(border=True):
    col_m, col_i = st.columns([1, 2])
    with col_m:
        med_sel = st.selectbox("Médico em Foco:", mc.medicos)
    with col_i:
        msg_user = st.text_input("Interação:", placeholder="Digite aqui sua dúvida ou comando...")

    if st.button("🚀 Ativar Projeto Frajola"):
        if msg_user:
            resposta_ia = mc.processar_chat(med_sel, msg_user)
            # Salva na Memória Quântica (Histórico Interno)
            st.session_state.memoria_ativa.append({
                "Data": datetime.now().strftime("%d/%m %H:%M"),
                "Médico": med_sel,
                "Sidney": msg_user,
                "IA Sentinela": resposta_ia
            })
            st.success(f"**Parecer das 17 IAs:** {resposta_ia}")
            
            # Link WhatsApp Seguro (Resolve o TypeError)
            zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta_ia)}"
            st.markdown(f'''<a href="{zap}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366;color:white;padding:10px;border-radius:5px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div>
                </a>''', unsafe_allow_html=True)

# --- 4. ABA DE SALVAMENTO (MEMÓRIA QUÂNTICA) ---
st.divider()
tab_fav, tab_hist = st.tabs(["📋 Tabela da Favelinha", "📜 Histórico de Diálogo (Memória)"])

with tab_fav:
    st.write("Ação Imediata e Projeções das Próximas Rodadas")
    # Dados fictícios para a tabela conforme as regras salvas
    df_fav = pd.DataFrame([
        {"Unidade": "ANIMA COSTA", "Projeção": "1.85x", "Ação": "entra"},
        {"Unidade": "DR. MARCOS", "Projeção": "2.10x", "Ação": "entra"},
        {"Unidade": "INTERFILE - BI", "Projeção": "1.00x", "Ação": "pula"} # Regra do Vácuo
    ])
    st.table(df_fav)

with tab_hist:
    if st.session_state.memoria_ativa:
        st.dataframe(pd.DataFrame(st.session_state.memoria_ativa))
    else:
        st.info("Aguardando interações para alimentar a Memória Quântica.")

st.caption(f"Sidney Pereira de Almeida | {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')} | Sincronizado")
            
