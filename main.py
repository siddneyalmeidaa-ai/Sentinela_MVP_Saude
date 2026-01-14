import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io

# Tenta importar o ReportLab para o PDF Profissional
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    PDF_READY = True
except ImportError:
    PDF_READY = False

# --- 1. CONFIGURAÇÃO E BLINDAGEM ---
st.set_page_config(page_title="Sentinela | Projeto Frajola", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')
agora_br = datetime.now(fuso_br).strftime("%d/%m/%Y %H:%M")

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

# CSS para esconder menus e focar na Governança
st.markdown("<style>[data-testid='stSidebar'] {display: none;} footer {visibility: hidden;} header {visibility: hidden;}</style>", unsafe_allow_html=True)

# --- 2. BASE DE DADOS SINCRONIZADA (R$ 26.801,80) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. MOTOR DAS 17 IAs (PROJETO FRAJOLA) ---
def motor_frajola(unidade, msg_medico, status, valor):
    msg_low = msg_medico.lower().strip()
    
    if status == "RESTRIÇÃO":
        corpo = f"identifiquei que o seu repasse de R$ {valor:,.2f} está temporariamente retido por falta de arquivos XML. Vamos destravar isso agora?"
    else:
        corpo = f"verifiquei que sua unidade está em CONFORMIDADE OK. O valor de R$ {valor:,.2f} segue o fluxo normal de depósito."

    if len(msg_low) < 25:
        return f"Olá, {unidade}! Já me antecipei ao seu contato e auditei seu caso: {corpo}", "NORMAL"
    else:
        return f"Prezado(a) {unidade}, entendo perfeitamente. {corpo} Estou acompanhando pessoalmente.", "ALTA"

# --- 4. INTERFACE VISUAL (ABAS APARTADAS) ---
st.title("🛡️ Sentinela: Governança & Mediação")

tab_operacional, tab_relatorios = st.tabs(["🚀 Operacional & 17 IAs", "📑 Central de Relatórios"])

with tab_operacional:
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric("VALOR TOTAL CONSOLIDADO", "R$ 26,801.80")
    with col_m2:
        st.info(f"🕒 Servidor Ativo: {agora_br}")

    with st.expander("📊 Performance por Unidade"):
        st.bar_chart(df.set_index("unidade")["valor"])

    st.subheader("📲 Canal de Comunicação Estratégica")
    u_selecionada = st.selectbox("Selecione o Médico:", df['unidade'].tolist())
    medico_info = df[df['unidade'] == u_selecionada].iloc[0]
    
    entrada = st.text_area(f"Mensagem de {u_selecionada}:", placeholder="Ex: Boa tarde!")
    
    if st.button("🚀 Ativar Projeto Frajola (17 IAs)"):
        if entrada:
            viva, urgencia = motor_frajola(u_selecionada, entrada, medico_info['status'], medico_info['valor'])
            st.session_state.memoria_unidades[u_selecionada] = {
                "data": datetime.now(fuso_br).strftime("%H:%M:%S"),
                "status": urgencia, "resposta": viva
            }
            st.rerun()

    if u_selecionada in st.session_state.memoria_unidades:
        atend = st.session_state.memoria_unidades[u_selecionada]
        st.success(f"**Parecer Sugerido (Urgência: {atend['status']}):**\n\n{atend['resposta']}")
        zap_link = f"https://wa.me/5511942971753?text={urllib.parse.quote(atend['resposta'])}"
        st.markdown(f'<a href="{zap_link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

with tab_relatorios:
    st.subheader("📥 Central de Exportação")
    
    def gerar_pdf(dados, tipo):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        elementos = []
        styles = getSampleStyleSheet()
        
        elementos.append(Paragraph("S E N T I N E L A", ParagraphStyle('T', fontSize=22, alignment=1, fontName="Helvetica-Bold")))
        elementos.append(Paragraph(f"RELATORIO {tipo} - PROJETO FRAJOLA", ParagraphStyle('S', fontSize=10, alignment=1, textColor=colors.gray)))
        elementos.append(Spacer(1, 20))
        
        t_data = [["UNIDADE", "VALOR (R$)", "STATUS"]]
        for _, r in dados.iterrows():
            # Limpeza de caracteres para evitar erro no PDF
            unid = str(r['unidade']).replace("Ã", "A").replace("Ó", "O").replace("Ç", "C")
            t_data.append([unid, f"{r['valor']:,.2f}", r['status']])
        
        t = Table(t_data, colWidths=[180, 100, 150])
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

    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.info("📊 **Relatório Consolidado**")
        if PDF_READY:
            st.download_button("📥 Baixar PDF Consolidado", data=gerar_pdf(df, "CONSOLIDADO"), file_name="Consolidado_Frajola.pdf", use_container_width=True)
        else:
            st.error("Biblioteca 'reportlab' ausente.")

    with col_r2:
        st.warning("🩺 **Relatório por Unidade**")
        u_rel = st.selectbox("Escolha a Unidade:", df['unidade'].tolist(), key="rel_ind")
        if PDF_READY:
            st.download_button(f"📥 Baixar PDF {u_rel}", data=gerar_pdf(df[df['unidade'] == u_rel], f"INDIVIDUAL: {u_rel}"), file_name=f"Relatorio_{u_rel}.pdf", use_container_width=True)

st.divider()
st.caption(f"Sidney Pereira de Almeida | {agora_br}")
