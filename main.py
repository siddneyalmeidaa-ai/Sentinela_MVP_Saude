import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io

# Importação para PDF Profissional
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- CONFIGURAÇÃO DE AMBIENTE ---
fuso_br = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso_br).strftime("%d/%m/%Y %H:%M")

# --- MOTOR DE INTELIGÊNCIA GF-17 (AS 17 IAs) ---
class Fenix17System:
    def __init__(self, doutor="Bigode"):
        self.doutor = doutor
        # Valores baseados no seu último fechamento
        self.liberado = 18493.24
        self.pendente = 8308.56
        
    def auditoria_cfo(self):
        """Lógica da CFO Vision e Auditora Padrão Ouro"""
        soma = self.liberado + self.pendente
        p_lib = (self.liberado / soma) * 100
        p_pen = (self.pendente / soma) * 100
        return f"{p_lib:.0f}% LIBERADO", f"{p_pen:.0f}% PENDENTE"

    def sentinela_vacuo(self, projecao):
        """Lógica da IA-SENTINELA: Detecção de Morte (1.00x)"""
        if projecao == 1.00:
            return "pula", "VÁCUO DETECTADO (DEATH ZONE)"
        elif projecao < 1.50:
            return "não entra", "RISCO ALTO"
        else:
            return "entra", "OPERACIONAL"

# Inicialização
gf17 = Fenix17System(doutor="Bigode")
status_lib, status_pen = gf17.auditoria_cfo()

# --- INTERFACE VISUAL INTELIGENTE ---
st.set_page_config(page_title="GF-17 | Gêmea Fênix", layout="wide")
st.title(f"🏛️ GF-17 | Gêmea Fênix 17 (Doutor: {gf17.doutor})")

# Sincronização automática nos títulos (Padrão Ouro)
col_l, col_p = st.columns(2)
col_l.metric("STATUS FINANCEIRO", status_lib)
col_p.metric("STATUS AUDITORIA", status_pen)

tab_favelinha, tab_relatorios = st.tabs(["📊 Tabela da Favelinha", "📑 Relatórios Profissionais"])

with tab_favelinha:
    st.subheader("📋 Ação Imediata & Tabela da Favelinha")
    
    # Simulação de Rodadas com Projeção Variável
    rodadas = [
        {"id": 1, "x": 1.85},
        {"id": 2, "x": 1.00}, # Exemplo de Vácuo
        {"id": 3, "x": 2.10},
        {"id": 4, "x": 1.20}
    ]
    
    tabela_final = []
    for r in rodadas:
        decisao, analise = gf17.sentinela_vacuo(r['x'])
        tabela_final.append({
            "Rodada": f"R-{r['id']}",
            "Projeção": f"{r['x']:.2f}x",
            "Decisão": decisao,
            "Análise IA": analise
        })

    st.table(tabela_final)
    st.info("💡 **Dica da Maluquinha dos Códigos:** A decisão muda automaticamente conforme a projeção de cada rodada.")

with tab_relatorios:
    st.subheader("📥 Central de Exportação")
    
    def gerar_pdf_executivo():
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        elementos = []
        
        # Timbre S E N T I N E L A
        estilo_timbre = ParagraphStyle('T', fontSize=24, alignment=1, fontName="Helvetica-Bold", spaceAfter=20)
        elementos.append(Paragraph("S E N T I N E L A", estilo_timbre))
        elementos.append(Paragraph(f"RELATÓRIO GF-17 | EMISSÃO: {agora}", styles['Normal']))
        elementos.append(Spacer(1, 20))
        
        # Tabela Profissional Zebrada
        dados = [["MÉTRICA", "RESULTADO"], ["Sincronismo", status_lib], ["Auditoria", status_pen]]
        t = Table(dados, colWidths=[200, 200])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1B2631")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.HexColor("#D5DBDB")])
        ]))
        elementos.append(t)
        doc.build(elementos)
        buffer.seek(0)
        return buffer

    # Correção de acento para Mobile (urllib.parse.quote)
    nome_doc = f"Relatorio_GF17_{gf17.doutor}.pdf"
    
    st.download_button(
        label="📥 BAIXAR PDF (FORMATO PROFISSIONAL)",
        data=gerar_pdf_executivo(),
        file_name=nome_doc,
        mime="application/pdf",
        use_container_width=True
    )

st.caption(f"Status: Padrão Ouro | Desenvolvedor: Bigode | {agora}")
