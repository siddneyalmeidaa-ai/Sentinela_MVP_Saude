import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io
import plotly.express as px # Para gráficos mais inteligentes

# --- 1. CONFIGURAÇÃO DE AMBIENTE E MEMÓRIA VIVA ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
fuso = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso).strftime("%d/%m/%Y %H:%M")

# Memória das 17 IAs: O sistema aprende com o diálogo
if 'historico' not in st.session_state:
    st.session_state.historico = []

# --- 2. MOTOR DE INTELIGÊNCIA (PADRÃO OURO) ---
class SistemaFenix17:
    def __init__(self):
        self.total_consolidado = 26801.80 #
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK", "x": 1.85},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK", "x": 2.10},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO", "x": 1.00}, # Vácuo!
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO", "x": 0.80},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO", "x": 1.20}
        ]

    def calcular_porcentagens(self):
        p_lib = (self.liberado / self.total_consolidado) * 100
        p_pen = (self.pendente / self.total_consolidado) * 100
        return f"{p_lib:.0f}% LIBERADO", f"{p_pen:.0f}% PENDENTE"

    def motor_dialogo_inteligente(self, unidade, texto):
        """Autocorreção e Dinamismo: A IA entende a intenção"""
        med = next(item for item in self.db if item["unidade"] == unidade)
        t = texto.lower()
        
        # Inteligência de Contexto: Cruzando Saudação com Auditoria
        if "bom" in t or "boa" in t or "oi" in t:
            prefixo = f"Olá, {unidade}! Analisando aqui seu estatuto agora: "
            if med['status'] == "RESTRIÇÃO":
                return prefixo + f"identifiquei que seus R$ {med['valor']:,.2f} estão presos. O Projeto Frajola detectou falta de XML. Vamos destravar?"
            return prefixo + f"sua unidade está voando com R$ {med['valor']:,.2f} em conformidade. O que mais posso agilizar?"
        
        if "pendente" in t:
            return f"Sobre o pendente de R$ {med['valor']:,.2f}: a Auditora Padrão Ouro está processando os dados para liberação imediata."
            
        return f"Entendi sua solicitação, {unidade}. Pela regra da GF-17, estamos operando em {med['status']}. Como as 17 IAs podem ajudar agora?"

sf = SistemaFenix17()
status_lib, status_pen = sf.calcular_porcentagens()

# --- 3. INTERFACE VISUAL (RESTALRAÇÃO DOS GRÁFICOS) ---
st.title(f"🛡️ Sentinela: Governança & Mediação")
st.subheader(f"VALOR TOTAL CONSOLIDADO: R$ {sf.total_consolidado:,.2f}")

# Gráfico de Performance Restaurado
df_graf = pd.DataFrame(sf.db)
fig = px.bar(df_graf, x="unidade", y="valor", color="status", title="Performance por Unidade")
st.plotly_chart(fig, use_container_width=True)

c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", status_lib)
c2.metric("EM AUDITORIA", status_pen)

tab_fav, tab_ia, tab_pdf = st.tabs(["📊 Tabela da Favelinha", "🚀 Operação 17 IAs", "📑 Relatórios PDF"])

with tab_fav:
    st.subheader("📋 Tabela da Favelinha (Ação Imediata)")
    tabela = []
    for r in sf.db:
        decisao = "pula" if r['x'] == 1.00 else ("entra" if r['x'] >= 1.50 else "não entra")
        status_v = "VÁCUO" if r['x'] == 1.00 else "NORMAL"
        tabela.append({"Unidade": r['unidade'], "Projeção": f"{r['x']:.2f}x", "Decisão": decisao, "Sentinela": status_v})
    st.table(tabela)

with tab_ia:
    st.subheader("📲 Canal de Comunicação Viva (Dinamismo)")
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in sf.db])
    entrada = st.text_input("Sua mensagem:", placeholder="Ex: Boa noite, como está o pendente?")
    
    if st.button("🚀 Ativar Projeto Frajola"):
        resp = sf.motor_dialogo_inteligente(u_sel, entrada)
        st.session_state.historico.append({"user": entrada, "ia": resp})
        st.success(f"**Parecer das 17 IAs:**\n\n{resp}")
        
        zap_url = f"https://wa.me/5511942971753?text={urllib.parse.quote(resp)}"
        st.markdown(f'<a href="{zap_url}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

with tab_pdf:
    st.subheader("📑 Área de Exportação (Padrão Sidney)")
    try:
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        
        def gerar_pdf():
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer)
            elementos = [Paragraph(f"Relatório GF-17 - {sf.doutor}", getSampleStyleSheet()['Title'])]
            elementos.append(Paragraph(f"Status: {status_lib} / {status_pen}", getSampleStyleSheet()['Normal']))
            doc.build(elementos)
            buffer.seek(0)
            return buffer
            
        st.download_button("📥 Baixar Relatório PDF Profissional", data=gerar_pdf(), file_name="Relatorio_GF17.pdf", mime="application/pdf")
    except Exception:
        st.warning("⚠️ Biblioteca de PDF aguardando ativação no requirements.txt.")

st.divider()
st.caption(f"Sidney Pereira de Almeida | {agora} | Sincronizado")
                 
