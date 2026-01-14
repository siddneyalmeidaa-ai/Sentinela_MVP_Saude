import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import random
import io

# Ferramentas de Alta Performance para PDF Profissional
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- 1. CONFIGURAÇÃO DO SERVIDOR ---
st.set_page_config(page_title="Sentinela | Projeto Frajola", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')
agora_br = datetime.now(fuso_br).strftime("%d/%m/%Y %H:%M")

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("<style>[data-testid='stSidebar'] {display: none;} header {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# --- 2. BASE DE DADOS (OS PRODUTOS DA FEIRA) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. MOTOR DE PDF PROFISSIONAL (TIMBRADO) ---
def gerar_pdf_sentinela(dados, titulo_relatorio):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    elementos = []
    
    styles = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle('T', fontSize=22, alignment=1, spaceAfter=10, fontName="Helvetica-Bold")
    estilo_sub = ParagraphStyle('S', fontSize=10, alignment=1, textColor=colors.gray, spaceAfter=20)

    # Cabeçalho de Autoridade
    elementos.append(Paragraph("S E N T I N E L A", estilo_titulo))
    elementos.append(Paragraph(f"{titulo_relatorio} - PROJETO FRAJOLA", estilo_sub))
    
    # Tabela com Design Zebrado
    tabela_dados = [["ITEM/UNIDADE", "VALOR NOMINAL", "STATUS"]]
    for _, r in dados.iterrows():
        # Limpeza para evitar erro de leitura no celular
        nome = str(r['unidade']).replace("Ã", "A").replace("Ó", "O").replace("Ç", "C")
        tabela_dados.append([nome, f"R$ {r['valor']:,.2f}", r['status']])
    
    t = Table(tabela_dados, colWidths=[200, 120, 140])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1B2631")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.HexColor("#EAECEE")]),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ]))
    elementos.append(t)
    
    elementos.append(Spacer(1, 40))
    elementos.append(Paragraph(f"Responsável pela Governança: Sidney Pereira de Almeida | {agora_br}", ParagraphStyle('F', fontSize=8, alignment=1)))
    
    doc.build(elementos)
    buffer.seek(0)
    return buffer

# --- 4. DIVISÃO POR ABAS (A "OUTRA FEIRA") ---
st.title("🛡️ Sentinela: Operação Frajola")
tab_ia, tab_pdf = st.tabs(["🚀 Gestão das 17 IAs", "📑 Central de Relatórios Apartada"])

with tab_ia:
    st.subheader("📊 Painel de Controle Operacional")
    st.metric("CONSOLIDADO TOTAL (FEIRA ATUAL)", "R$ 26.801,80")
    
    col_sel, col_res = st.columns([1, 1.2])
    with col_sel:
        u_atual = st.selectbox("Selecione a Unidade para Auditar:", df['unidade'].tolist())
        med_info = df[df['unidade'] == u_atual].iloc[0]
        st.warning(f"Status Atual: {med_info['status']}")
        msg_in = st.text_area("Entrada do Médico:", placeholder="Ex: Boa tarde!")
        
    with col_res:
        if st.button("🚀 Ativar DNA das 17 IAs"):
            # Lógica Proativa Sidney
            diagnostico = "travado por falta de XML" if med_info['status'] == "RESTRIÇÃO" else "em Conformidade OK"
            resposta = f"Olá, {u_atual}! Já verifiquei aqui. Seu repasse de R$ {med_info['valor']:,.2f} está {diagnostico}. Estou monitorando para o próximo lote."
            st.session_state.memoria_unidades[u_atual] = {"txt": resposta}
            
        if u_atual in st.session_state.memoria_unidades:
            res_final = st.session_state.memoria_unidades[u_atual]["txt"]
            st.success(f"**Parecer Sentinela:**\n\n{res_final}")
            zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(res_final)}"
            st.markdown(f'<a href="{zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:10px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR VIA WHATSAPP</div></a>', unsafe_allow_html=True)

with tab_pdf:
    st.subheader("📥 Exportação de Documentos de Auditoria")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("📌 **Relatório 01: Consolidado Geral**")
        st.write("Contém o valor total de R$ 26.801,80 e todas as clínicas.")
        pdf_geral = gerar_pdf_sentinela(df, "RELATÓRIO CONSOLIDADO GERAL")
        st.download_button("📥 Baixar PDF Consolidado", data=pdf_geral, file_name="Consolidado_Frajola.pdf", use_container_width=True)
        
    with c2:
        st.warning("📌 **Relatório 02: Por Unidade/Médico**")
        st.write("Gera um documento exclusivo e apartado da unidade escolhida.")
        u_alvo = st.selectbox("Escolha a Clínica/Médico:", df['unidade'].tolist(), key="rel_individual")
        df_ind = df[df['unidade'] == u_alvo]
        pdf_ind = gerar_pdf_sentinela(df_ind, f"RELATÓRIO INDIVIDUAL: {u_alvo}")
        st.download_button(f"📥 Baixar PDF {u_alvo}", data=pdf_ind, file_name=f"Relatorio_{u_alvo}.pdf", use_container_width=True)

st.divider()
st.caption(f"Sidney Pereira de Almeida | {agora_br} | 17 IAs Ativas")
    
