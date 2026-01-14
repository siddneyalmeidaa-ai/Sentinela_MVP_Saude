import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import io

# Importações para o PDF Profissional (ReportLab)
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- CONFIGURAÇÃO DE AMBIENTE ---
fuso_br = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso_br).strftime("%d/%m/%Y %H:%M")

# Dados Sincronizados (R$ 26.801,80)
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- MOTOR DE PDF DE ALTA GOVERNANÇA ---
def gerar_pdf_premium(dados, tipo_relatorio):
    buffer = io.BytesIO()
    # Margens amplas para visual profissional
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=30)
    styles = getSampleStyleSheet()
    elementos = []

    # 1. TIMBRE ESTILIZADO
    timbre_style = ParagraphStyle(
        'Timbre', fontSize=28, textColor=colors.HexColor("#1B2631"),
        alignment=1, spaceAfter=2, fontName="Helvetica-Bold", leading=32
    )
    sub_style = ParagraphStyle(
        'Sub', fontSize=10, alignment=1, textColor=colors.gray, spaceAfter=30
    )

    elementos.append(Paragraph("S E N T I N E L A", timbre_style))
    elementos.append(Paragraph(f"{tipo_relatorio} | PROJETO FRAJOLA", sub_style))
    
    # 2. BOX DE INFOS EXECUTIVAS
    info_data = [
        [f"RESPONSÁVEL: SIDNEY PEREIRA DE ALMEIDA", f"EMISSÃO: {agora}"],
        [f"SISTEMA: 17 INTELIGÊNCIAS ATIVAS", f"TOTAL EM AUDITORIA: R$ {dados['valor'].sum():,.2f}"]
    ]
    t_info = Table(info_data, colWidths=[250, 200])
    t_info.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor("#2C3E50")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    elementos.append(t_info)
    elementos.append(Spacer(1, 20))

    # 3. TABELA ANALÍTICA ZEBRADA (PADRÃO OURO)
    # Limpando caracteres especiais para evitar erros de renderização
    dados_tabela = [["UNIDADE / MÉDICO", "VALOR (R$)", "STATUS FINAL"]]
    for _, row in dados.iterrows():
        nome_limpo = str(row['unidade']).replace("Ã", "A").replace("Ç", "C").replace("Ó", "O")
        dados_tabela.append([nome_limpo, f"{row['valor']:,.2f}", row['status']])

    t = Table(dados_tabela, colWidths=[200, 110, 140])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1B2631")), # Cabeçalho Grafite Profissional
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#EAECEE")]), # Efeito Zebrado
        ('GRID', (0, 0), (-1, -1), 0.3, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    elementos.append(t)

    # 4. RODAPÉ DE AUTENTICIDADE
    elementos.append(Spacer(1, 60))
    rodape = Paragraph(
        "Este documento é parte integrante do sistema de governança das 17 IAs Sentinela.<br/>"
        "A autenticidade deste relatório é garantida pelo log de transações do servidor.",
        ParagraphStyle('F', fontSize=7, alignment=1, textColor=colors.gray)
    )
    elementos.append(rodape)

    doc.build(elementos)
    buffer.seek(0)
    return buffer

# --- INTERFACE STREAMLIT ---
st.title("🛡️ Sentinela: Governança & Mediação")

tab1, tab2 = st.tabs(["🚀 Gestão das 17 IAs", "📑 Central de Exportação"])

with tab1:
    st.metric("VALOR TOTAL CONSOLIDADO", "R$ 26,801.80")
    st.table(df)

with tab2:
    st.subheader("📑 Área de Exportação (Padrão Sidney)")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.info("📊 **Relatório Consolidado**")
        st.write("Visão geral de todas as unidades e ativos.")
        pdf_geral = gerar_pdf_premium(df, "RELATÓRIO CONSOLIDADO")
        st.download_button(
            label="📥 Baixar PDF Geral (Premium)",
            data=pdf_geral,
            file_name=f"Sentinela_Consolidado_{datetime.now().strftime('%d%m%Y')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        
    with col_b:
        st.warning("🩺 **Relatório Individual**")
        st.write("Documento apartado apenas da unidade selecionada.")
        unidade_alvo = st.selectbox("Escolha a Unidade:", df['unidade'].tolist())
        df_ind = df[df['unidade'] == unidade_alvo]
        pdf_ind = gerar_pdf_premium(df_ind, f"RELATÓRIO INDIVIDUAL: {unidade_alvo}")
        st.download_button(
            label=f"📥 Baixar PDF {unidade_alvo}",
            data=pdf_ind,
            file_name=f"Relatorio_{unidade_alvo}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.caption(f"Sidney Pereira de Almeida | {agora}")
