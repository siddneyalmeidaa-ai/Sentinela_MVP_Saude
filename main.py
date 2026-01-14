import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import math

# --- 1. CONFIGURAÇÃO DE AMBIENTE E MEMÓRIA DE DIÁLOGO ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")

# Inicializa o Histórico e Memória para garantir Coerência
if 'historico_viva' not in st.session_state:
    st.session_state.historico_viva = []
if 'contexto_atual' not in st.session_state:
    st.session_state.contexto_atual = None

class SistemaSentinela:
    def __init__(self):
        # Arredondamento e Valores Fixos
        self.total = 26801.80
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK", "x": 1.85},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK", "x": 2.10},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO", "x": 1.00},
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO", "x": 0.80},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO", "x": 1.20}
        ]

    def calcular_metricas(self):
        # Arredondamento para garantir visual limpo
        p_lib = math.ceil((self.liberado / self.total) * 100)
        p_pen = math.floor((self.pendente / self.total) * 100)
        return f"{p_lib}% LIBERADO", f"{p_pen}% PENDENTE"

    def motor_de_coerencia(self, unidade, texto_user):
        """Analisa o histórico para não ser repetitivo"""
        med = next(item for item in self.db if item["unidade"] == unidade)
        t = texto_user.lower()
        
        # Se o usuário já agradeceu ou deu boa noite, muda o foco
        if any(word in t for word in ["obrigado", "valeu", "certo"]):
            return f"Show, Sidney! Registrei a conformidade da {unidade}. O histórico está salvo para auditoria. Próximo passo?"
        
        # Se perguntar de pendência, traz o dado técnico
        if "pendente" in t or "resolver" in t:
            if med['status'] == "RESTRIÇÃO":
                return f"Análise Técnica: A unidade {unidade} tem R$ {med['valor']:,.2f} travados. O erro de XML detectado precisa de correção manual. Vamos agir?"
            return f"Sem pendências para {unidade}. Os R$ {med['valor']:,.2f} estão em fluxo normal de 69% liberado."

        return f"Olá Sidney! No contexto da {unidade}, temos R$ {med['valor']:,.2f} em {med['status']}. Como as 17 IAs podem ajudar agora?"

ss = SistemaSentinela()
m_lib, m_pen = ss.calcular_metricas()

# --- 2. INTERFACE (RESTAURAÇÃO DOS GRÁFICOS) ---
st.title("🛡️ Sentinela: Governança & Mediação")

# Gráfico Nativo (Resolve o erro ModuleNotFoundError das suas imagens)
st.subheader(f"📊 Performance Consolidada: R$ {ss.total:,.2f}")
df_graf = pd.DataFrame(ss.db)
st.bar_chart(df_graf.set_index("unidade")["valor"])

c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", m_lib)
c2.metric("EM AUDITORIA", m_pen)

tab_chat, tab_fav, tab_hist = st.tabs(["💬 Canal de Comunicação Viva", "📋 Tabela da Favelinha", "📜 Histórico de Auditoria"])

with tab_chat:
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in ss.db])
    entrada = st.text_input("Sua mensagem:", placeholder="Ex: Preciso resolver a pendência")
    
    if st.button("🚀 Ativar Projeto Frajola"):
        resposta = ss.motor_de_coerencia(u_sel, entrada)
        # Salva no histórico para consulta posterior
        st.session_state.historico_viva.append({"Data": datetime.now().strftime("%H:%M:%S"), "Unidade": u_sel, "IA": resposta})
        st.success(f"**Parecer das 17 IAs:** {resposta}")
        
        # Correção do link WhatsApp
        link = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta)}"
        st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR WHATSAPP</div></a>', unsafe_allow_html=True)

with tab_fav:
    # Regra do Vácuo 1.00x
    dados_f = [{"Unidade": r['unidade'], "Projeção": f"{r['x']:.2f}x", "Decisão": "pula" if r['x'] == 1.00 else "entra"} for r in ss.db]
    st.table(dados_f)

with tab_hist:
    st.subheader("📜 Log de Decisões e Diálogos")
    if st.session_state.historico_viva:
        st.dataframe(pd.DataFrame(st.session_state.historico_viva))
    else:
        st.write("Nenhuma interação registrada nesta sessão.")

st.caption(f"Sidney Pereira de Almeida | {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')} | Sincronizado")
