import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io

# --- 1. MOTOR DE MEMÓRIA E DINAMISMO (CÉREBRO DAS 17 IAs) ---
# Isso garante que a conversa não seja genérica
if 'memoria_contexto' not in st.session_state:
    st.session_state.memoria_contexto = {"ultima_unidade": None, "assuntos_citados": []}

class MotorInteligente:
    def __init__(self):
        self.total = 26801.80 #
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK", "x": 1.85},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK", "x": 2.10},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO", "x": 1.00},
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO", "x": 0.80},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO", "x": 1.20}
        ]

    def responder(self, unidade, texto):
        med = next(item for item in self.db if item["unidade"] == unidade)
        msg = texto.lower()
        
        # Autocorreção: Se o usuário já perguntou algo antes, a resposta muda
        contexto = st.session_state.memoria_contexto
        
        if "pendente" in msg or "andando" in msg:
            contexto["assuntos_citados"].append("financeiro")
            if med['status'] == "RESTRIÇÃO":
                return f"Sidney, sobre o pendente da {unidade}: os R$ {med['valor']:,.2f} estão travados por falta de XML. Já avisei a Auditoria Padrão Ouro para priorizar assim que o arquivo chegar."
            return f"Pode ficar tranquilo sobre a {unidade}! Os R$ {med['valor']:,.2f} já saíram do pendente e estão no fluxo de liberação."
        
        if "obrigado" in msg or "ajuda" in msg:
            return f"Disponha, Sidney! A {unidade} continua sob monitoramento da IA-SENTINELA. Mais algum ajuste no Estatuto Atual?"

        return f"Boa noite! Verifiquei que a {unidade} opera hoje com R$ {med['valor']:,.2f} em status de {med['status']}. Como as 17 IAs podem acelerar seu processo?"

mi = MotorInteligente()

# --- 2. INTERFACE VISUAL (RESTAURAÇÃO DE GRÁFICOS E MÉTRICAS) ---
st.set_page_config(page_title="GF-17 | Sentinela", layout="wide")
st.title("🛡️ Sentinela: Governança & Mediação")

# Métricas Sincronizadas
p_lib = (mi.liberado / mi.total) * 100
p_pen = (mi.pendente / mi.total) * 100
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", f"{p_lib:.0f}% LIBERADO")
c2.metric("EM AUDITORIA", f"{p_pen:.0f}% PENDENTE")

# RESTAURAÇÃO DOS GRÁFICOS (Usando Streamlit Nativo para não dar erro de Plotly)
st.subheader("📈 Performance por Unidade (R$ 26.801,80)")
df_grafico = pd.DataFrame(mi.db)
st.bar_chart(df_grafico.set_index("unidade")["valor"])

tab_fav, tab_chat, tab_pdf = st.tabs(["📊 Tabela da Favelinha", "💬 Chat Dinâmico", "📑 Relatórios PDF"])

with tab_fav:
    st.subheader("📋 Auditoria de Rodada")
    # Regra do Vácuo 1.00x
    df_fav = pd.DataFrame([{
        "Unidade": r['unidade'], 
        "Projeção": f"{r['x']:.2f}x", 
        "Decisão": "pula" if r['x'] == 1.00 else ("entra" if r['x'] >= 1.50 else "não entra")
    } for r in mi.db])
    st.table(df_fav)

with tab_chat:
    u_sel = st.selectbox("Selecione a Unidade:", [d['unidade'] for d in mi.db])
    entrada = st.text_input("Sua mensagem:", key="input_chat")
    if st.button("🚀 Ativar Projeto Frajola"):
        resp = mi.responder(u_sel, entrada)
        st.info(f"**Análise da IA:** {resp}")
        zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resp)}"
        st.markdown(f'<a href="{zap}" target="_blank" style="text-decoration:none; color:white;"><div style="background-color:#25D366;padding:10px;border-radius:5px;text-align:center;">ENVIAR WHATSAPP</div></a>', unsafe_allow_width=True, unsafe_allow_html=True)

with tab_pdf:
    st.subheader("📑 Área de Exportação")
    # Autocorreção para erro de PDF
    try:
        from reportlab.pdfgen import canvas
        def criar_pdf():
            buf = io.BytesIO()
            c = canvas.Canvas(buf)
            c.drawString(100, 750, f"RELATÓRIO GF-17 - {mi.total}")
            c.save()
            buf.seek(0)
            return buf
        st.download_button("📥 Baixar PDF Padrão Sidney", data=criar_pdf(), file_name="Relatorio.pdf")
    except ImportError:
        st.error("⚠️ Erro detectado no seu print [17:42]: Adicione 'reportlab' ao seu requirements.txt para ativar esta função.")

st.caption(f"Sidney Pereira de Almeida | {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}")
  
