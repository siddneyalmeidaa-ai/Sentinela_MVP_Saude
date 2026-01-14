import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io

# --- 1. CONFIGURAÇÃO DE AMBIENTE (AUTO-APRENDIZADO) ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
fuso = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso).strftime("%d/%m/%Y %H:%M")

# Memória de Curto Prazo para Dinamismo (Não esquece o que foi dito)
if 'historico_dialogo' not in st.session_state:
    st.session_state.historico_dialogo = []

# --- 2. MOTOR DE INTELIGÊNCIA (AS 17 IAs) ---
class Fenix17System:
    def __init__(self):
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.total = 26801.80
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK", "x": 1.85},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK", "x": 2.10},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO", "x": 1.00},
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO", "x": 0.80},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO", "x": 1.20}
        ]

    def calcular_metricas(self):
        p_lib = (self.liberado / self.total) * 100
        p_pen = (self.pendente / self.total) * 100
        return f"{p_lib:.0f}% LIBERADO", f"{p_pen:.0f}% PENDENTE"

    def gerar_resposta_dinamica(self, unidade, input_user):
        """Aprende com o diálogo e evita respostas genéricas"""
        med = next(item for item in self.db if item["unidade"] == unidade)
        
        # Analisa se o usuário está perguntando especificamente sobre o pendente
        if "pendente" in input_user.lower():
            if med['status'] == "RESTRIÇÃO":
                return f"Entendi sua dúvida sobre o pendente, {unidade}. Pela minha auditoria, os R$ {med['valor']:,.2f} estão travados por falta de XML. O projeto Frajola precisa desse envio para liberar."
            return f"Sobre o pendente, {unidade}, você está limpo! Os R$ {med['valor']:,.2f} já saíram da auditoria e estão no fluxo de liberação."
        
        # Resposta padrão inteligente
        return f"Boa noite, {unidade}! Verifiquei aqui no Estatuto Atual que sua unidade está com {med['status']} para o valor de R$ {med['valor']:,.2f}. Como posso agilizar seu processo hoje?"

gf17 = Fenix17System()
metric_lib, metric_pen = gf17.calcular_metricas()

# --- 3. INTERFACE VISUAL (RESTAURAÇÃO DOS GRÁFICOS) ---
st.title("🛡️ Sentinela: Governança & Mediação")

# Gráfico de Performance (Restauração)
st.subheader("📈 Performance Consolidada (R$ 26.801,80)")
df_grafico = pd.DataFrame(gf17.db)
st.bar_chart(df_grafico.set_index("unidade")["valor"])

c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", metric_lib)
c2.metric("EM AUDITORIA", metric_pen)

tab1, tab2, tab3 = st.tabs(["📊 Tabela da Favelinha", "🚀 Operação 17 IAs", "📑 Relatórios PDF"])

with tab1:
    st.subheader("📋 Tabela da Favelinha (Ação Imediata)")
    dados_f = []
    for r in gf17.db:
        decisao = "pula" if r['x'] == 1.00 else ("entra" if r['x'] >= 1.50 else "não entra")
        dados_f.append({"Unidade": r['unidade'], "Projeção": f"{r['x']:.2f}x", "Decisão": decisao, "Status": r['status']})
    st.table(dados_f)

with tab2:
    st.subheader("📲 Canal de Comunicação Viva (Dinamismo)")
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in gf17.db])
    entrada = st.text_area("Mensagem:", placeholder="Ex: Como está andando o pendente?")
    
    if st.button("🚀 Ativar Projeto Frajola"):
        resposta = gf17.gerar_resposta_dinamica(u_sel, entrada)
        st.session_state.historico_dialogo.append({"u": u_sel, "m": entrada, "r": resposta})
        st.success(resposta)
        zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta)}"
        st.markdown(f'<a href="{zap}" target="_blank" style="background:green;color:white;padding:10px;border-radius:5px;">🚀 ENVIAR WHATSAPP</a>', unsafe_allow_html=True)

with tab3:
    st.subheader("📑 Exportação (Proteção contra Erros)")
    try:
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        
        def gerar_pdf():
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer)
            elementos = [Paragraph("RELATORIO SENTINELA GF-17", getSampleStyleSheet()['Title'])]
            t_data = [["UNIDADE", "VALOR", "STATUS"]] + [[d['unidade'], d['valor'], d['status']] for d in gf17.db]
            t = Table(t_data)
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.grey), ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
            elementos.append(t)
            doc.build(elementos)
            buffer.seek(0)
            return buffer

        st.download_button("📥 Baixar Relatório PDF", data=gerar_pdf(), file_name="Relatorio_Sentinela.pdf")
    except ImportError:
        st.error("⚠️ Erro de Biblioteca detectado (image 17:42). Por favor, adicione 'reportlab' ao requirements.txt para habilitar o PDF.")

st.caption(f"Sidney Pereira de Almeida | {agora} | Sincronizado")
            
