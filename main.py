import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io

# --- 1. MOTOR DE INTELIGÊNCIA GF-17 (BIGODE) ---
class Fenix17System:
    def __init__(self, doutor="Sidney"):
        self.doutor = doutor
        # Sincronização conforme dados dos prints
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
        ]

    def auditoria_cfo(self):
        soma = self.liberado + self.pendente
        return f"{(self.liberado / soma) * 100:.0f}% LIBERADO", f"{(self.pendente / soma) * 100:.0f}% PENDENTE"

    def motor_frajola_viva(self, unidade, status, valor):
        """Linguagem Inteligente e Proativa das 17 IAs"""
        if status == "RESTRIÇÃO":
            return f"Olá, {unidade}! Já me antecipei ao seu contato e auditei seu caso: identifiquei que o seu repasse de R$ {valor:,.2f} está temporariamente retido por falta de arquivos XML. Vamos destravar isso agora?"
        return f"Prezado(a) {unidade}, verifiquei aqui que seu status está em CONFORMIDADE OK. O processamento de R$ {valor:,.2f} segue o fluxo normal."

# --- 2. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
fuso = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
gf17 = Fenix17System()

st.title("🛡️ Sentinela: Governança & Mediação")
st.metric("VALOR TOTAL CONSOLIDADO", "R$ 26,801.80")

tab_op, tab_pdf = st.tabs(["🚀 Operação 17 IAs", "📑 Central de Relatórios"])

with tab_op:
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in gf17.db])
    med_info = next(item for item in gf17.db if item["unidade"] == u_sel)
    
    msg_medico = st.text_area(f"Mensagem de {u_sel}:", placeholder="Ex: Boa noite")
    
    if st.button("🚀 Ativar Projeto Frajola (Gerar Resposta Viva)"):
        resposta = gf17.motor_frajola_viva(u_sel, med_info['status'], med_info['valor'])
        st.success(f"**Parecer Sugerido (Urgência: NORMAL):**\n\n{resposta}")
        zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta)}"
        st.markdown(f'<a href="{zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

with tab_pdf:
    st.subheader("📑 Área de Exportação (Padrão Sidney)")
    try:
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        
        def gerar_pdf():
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer)
            elementos = [Paragraph("S E N T I N E L A - RELATORIO", getSampleStyleSheet()['Title'])]
            # Tabela Padrão Ouro
            t_data = [["UNIDADE", "VALOR", "STATUS"]] + [[d['unidade'], f"{d['valor']:,.2f}", d['status']] for d in gf17.db]
            t = Table(t_data)
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.grey), ('GRID',(0,0),(-1,-1),0.5,colors.black)]))
            elementos.append(t)
            doc.build(elementos)
            buffer.seek(0)
            return buffer

        st.download_button("📥 Baixar PDF Geral", data=gerar_pdf(), file_name="Relatorio_Sentinela.pdf")
    except ImportError:
        st.error("⚠️ Biblioteca de PDF não instalada. Por favor, adicione 'reportlab' ao seu arquivo requirements.txt.")

st.caption(f"Sidney Pereira de Almeida | {agora}")
        
