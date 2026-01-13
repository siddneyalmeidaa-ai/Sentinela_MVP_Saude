import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import io
import urllib.parse

# Importações para o PDF de Alto Nível
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- CONFIGURAÇÃO DE AMBIENTE ---
fuso_br = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso_br).strftime("%d/%m/%Y %H:%M")

# Dados do Relatório (Baseado no seu print)
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- FUNÇÃO: GERADOR DE PDF EXECUTIVO (TIMBRADO) ---
def exportar_pdf_premium(data_frame):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    # Estilo do Timbre
    estilo_timbre = ParagraphStyle(
        'Timbre', fontSize=26, textColor=colors.HexColor("#1B2631"),
        alignment=1, spaceAfter=2, fontName="Helvetica-Bold"
    )
    estilo_subtitulo = ParagraphStyle(
        'Sub', fontSize=10, alignment=1, textColor=colors.gray, spaceAfter=30
    )

    # Adicionando o Timbre
    elementos.append(Paragraph("S E N T I N E L A", estilo_timbre))
    elementos.append(Paragraph("PROJETO FRAJOLA | UNIDADE DE GOVERNANÇA E MEDIAÇÃO", estilo_subtitulo))
    
    # Dados de Cabeçalho do Sidney
    meta_dados = [
        [f"RESPONSÁVEL: SIDNEY PEREIRA DE ALMEIDA", f"EMISSÃO: {agora}"],
        [f"SISTEMA: 17 INTELIGÊNCIAS ATIVAS", f"TOTAL AUDITADO: R$ {data_frame['valor'].sum():,.2f}"]
    ]
    t_meta = Table(meta_dados, colWidths=[3.0*72, 3.0*72])
    t_meta.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor("#2C3E50")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    elementos.append(t_meta)
    elementos.append(Spacer(1, 20))

    # Construção da Tabela Zebrada (Profissional)
    dados_tabela = [["UNIDADE ACADÊMICA / MÉDICO", "VALOR (R$)", "STATUS FINAL"]]
    for _, row in data_frame.iterrows():
        dados_tabela.append([row['unidade'], f"{row['valor']:,.2f}", row['status']])

    t = Table(dados_tabela, colWidths=[2.5*72, 1.5*72, 2.0*72])
    estilo_tab = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1B2631")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#D5DBDB")]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    t.setStyle(estilo_tab)
    elementos.append(t)

    # Rodapé de Autenticidade
    elementos.append(Spacer(1, 50))
    elementos.append(Paragraph("Documento oficial para fins de auditoria interna. Gerado via DNA 17-IA.", 
                               ParagraphStyle('F', fontSize=8, alignment=1, textColor=colors.gray)))

    doc.build(elementos)
    buffer.seek(0)
    return buffer

# --- INTERFACE STREAMLIT ---
st.title("🛡️ Sentinela: Governança & Mediação")
st.metric("VALOR TOTAL EM AUDITORIA", f"R$ {df['valor'].sum():,.2f}")

with st.expander("📄 Visualizar Relatório Analítico"):
    st.table(df)

st.divider()
st.subheader("📑 Área de Exportação (Padrão Sidney)")

# Gerar e disponibilizar o PDF
pdf_pronto = exportar_pdf_premium(df)

st.download_button(
    label="📥 BAIXAR RELATÓRIO EXECUTIVO (PDF)",
    data=pdf_pronto,
    file_name=f"Relatorio_Frajola_{datetime.now().strftime('%d%m%Y')}.pdf",
    mime="application/pdf",
    help="Clique para baixar o documento com timbre e formatação de diretoria."
)

st.caption(f"Sidney Pereira de Almeida | {agora}")
    
