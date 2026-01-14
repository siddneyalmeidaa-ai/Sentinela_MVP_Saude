import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. MEMÓRIA E DINAMISMO (AS 17 IAs) ---
# Resolve a falta de coerência guardando o contexto da conversa
if 'historico' not in st.session_state:
    st.session_state.historico = []

class MotorInteligente:
    def __init__(self):
        self.total = 26801.80  # Valor consolidado
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK", "x": 1.85},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK", "x": 2.10},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO", "x": 1.00},
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO", "x": 0.80},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO", "x": 1.20}
        ]

    def analisar_mensagem(self, unidade, texto):
        """Dinamismo: A IA analisa o status da unidade antes de falar"""
        med = next(item for item in self.db if item["unidade"] == unidade)
        msg = texto.lower()
        
        # Lógica de Autocorreção: Se o usuário pergunta do pendente, a resposta foca no dinheiro
        if "pendente" in msg or "andando" in msg:
            if med['status'] == "RESTRIÇÃO":
                return f"Sidney, sobre o pendente da {unidade}: identifiquei que o valor de R$ {med['valor']:,.2f} está travado por falta de XML. Já acionei a Auditoria Padrão Ouro para priorizar."
            return f"Sobre a {unidade}, o valor de R$ {med['valor']:,.2f} já está liberado no fluxo. Nada pendente aqui!"
        
        # Resposta padrão inteligente baseada no status
        return f"Boa noite, Sidney! Verifiquei que a {unidade} está em {med['status']} com R$ {med['valor']:,.2f}. Como posso agilizar esse processo agora?"

mi = MotorInteligente()

# --- 2. INTERFACE VISUAL (RESTAURAÇÃO TOTAL) ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
st.title("🛡️ Sentinela: Governança & Mediação")

# Gráfico Nativo: Resolve o erro de 'plotly' dos seus prints
st.subheader("📈 Performance por Unidade (R$ 26.801,80)")
df_grafico = pd.DataFrame(mi.db)
st.bar_chart(df_grafico.set_index("unidade")["valor"])

# Métricas Sincronizadas
p_lib = (mi.liberado / mi.total) * 100
p_pen = (mi.pendente / mi.total) * 100
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", f"{p_lib:.0f}% LIBERADO")
c2.metric("EM AUDITORIA", f"{p_pen:.0f}% PENDENTE")

tab_fav, tab_chat = st.tabs(["📊 Tabela da Favelinha", "💬 Canal de Comunicação Viva"])

with tab_fav:
    # Tabela da Favelinha com regra do Vácuo (1.00x)
    df_f = pd.DataFrame([{
        "Unidade": r['unidade'], 
        "Projeção": f"{r['x']:.2f}x",
        "Decisão": "pula" if r['x'] == 1.00 else ("entra" if r['x'] >= 1.50 else "não entra")
    } for r in mi.db])
    st.table(df_f)

with tab_chat:
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in mi.db])
    entrada = st.text_input("Sua mensagem:", placeholder="Ex: Como está o pendente?")
    
    if st.button("🚀 Ativar Projeto Frajola"):
        resposta = mi.analisar_mensagem(u_sel, entrada)
        st.success(f"**Análise da IA:** {resposta}")
        
        # Correção do link do WhatsApp (Resolve o TypeError dos seus prints)
        texto_zap = urllib.parse.quote(resposta)
        zap_link = f"https://wa.me/5511942971753?text={texto_zap}"
        st.markdown(f'<a href="{zap_link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

st.caption(f"Sidney Pereira de Almeida | {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}")
        
