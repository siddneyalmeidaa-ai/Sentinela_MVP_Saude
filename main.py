from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def gerar_pdf_premium(dataframe):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    styles = getSampleStyleSheet()
    elements = []

    # --- 1. TIMBRE E CABEÇALHO ---
    titulo_style = ParagraphStyle(
        'TituloStyle',
        parent=styles['Headline1'],
        fontSize=22,
        textColor=colors.HexColor("#0E1117"),
        alignment=1, # Centralizado
        spaceAfter=10
    )
    
    subtitulo_style = ParagraphStyle(
        'SubStyle',
        fontSize=10,
        alignment=1,
        textColor=colors.grey,
        spaceAfter=20
    )

    elements.append(Paragraph("S E N T I N E L A", titulo_style))
    elements.append(Paragraph(f"RELATÓRIO DE GOVERNANÇA - PROJETO FRAJOLA (17 IAs)", subtitulo_style))
    elements.append(Spacer(1, 12))

    # --- 2. INFOS DE DIRETORIA ---
    agora_br = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M")
    info_data = [
        [f"RESPONSÁVEL: SIDNEY PEREIRA DE ALMEIDA", f"DATA: {agora_br}"],
        [f"STATUS DO SERVIDOR: OPERACIONAL", f"TOTAL EM AUDITORIA: R$ {dataframe['valor'].sum():,.2f}"]
    ]
    t_info = Table(info_data, colWidths=[3.5*inch, 3.5*inch])
    t_info.setStyle(TableStyle([
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(t_info)
    elements.append(Spacer(1, 20))

    # --- 3. TABELA ANALÍTICA (FORMATO EXECUTIVO) ---
    # Preparar dados para a tabela
    dados_tabela = [["UNIDADE", "VALOR (R$)", "STATUS DE CONFORMIDADE"]]
    for _, row in dataframe.iterrows():
        dados_tabela.append([
            row['unidade'], 
            f"R$ {row['valor']:,.2f}", 
            row['status']
        ])

    t = Table(dados_tabela, colWidths=[2.5*inch, 2.25*inch, 2.25*inch])
    
    # Estilização da Tabela (Zebrada e com Bordas Profissionais)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#161B22")), # Cabeçalho escuro
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#E8E8E8")]), # Efeito zebrado
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    t.setStyle(style)
    elements.append(t)

    # --- 4. RODAPÉ DE AUTENTICIDADE ---
    elements.append(Spacer(1, 40))
    rodape_style = ParagraphStyle('Rodape', fontSize=8, alignment=1, textColor=colors.grey)
    elements.append(Paragraph("Este documento é gerado automaticamente pelo Sistema Sentinela - 17 IAs Ativas.", rodape_style))
    elements.append(Paragraph("A autenticidade deste relatório pode ser verificada no log do servidor.", rodape_style))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# --- BOTÃO DE DOWNLOAD NO STREAMLIT ---
st.divider()
pdf_buffer = gerar_pdf_premium(df)
st.download_button(
    label="📑 Baixar Relatório Executivo Frajola",
    data=pdf_buffer,
    file_name=f"Governança_Frajola_{datetime.now().strftime('%d_%m_%Y')}.pdf",
    mime="application/pdf",
    use_container_width=True
)
