import os
# Comando para instalar a ferramenta de PDF faltante automaticamente
try:
    from fpdf import FPDF
except ImportError:
    os.system('pip install fpdf')
    from fpdf import FPDF

import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- CONFIGURAÇÃO MOBILE ---
st.set_page_config(page_title="SISTEMA SIDNEY PDF", layout="wide")
st.markdown("<style>[data-testid='stHeader'] {display: none !important;}</style>", unsafe_allow_html=True)

# --- DADOS ---
db = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "gl": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "gl": ["CARLOS LIMA: XML INVÁLIDO"]}
}

st.markdown(f"<div style='background:#1c232d; padding:15px; border-left:8px solid #00d4ff; color:white;'>"
            f"<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
info = db[unidade]
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y")

# --- FUNÇÃO DO PDF (REPARADA) ---
def gerar_pdf_final(unidade, v_entra, v_pula, glosas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "RELATORIO DE AUDITORIA", 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 10, f"UNIDADE: {unidade} | DATA: {hoje}", 0, 1)
    pdf.set_text_color(0, 128, 0)
    pdf.cell(190, 10, f"ENTRA: R$ {v_entra:,.2f}", 0, 1)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(190, 10, f"PULA: R$ {v_pula:,.2f}", 0, 1)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    pdf.cell(190, 10, "LISTA DA FAVELINHA:", 0, 1)
    for g in glosas:
        pdf.cell(190, 8, f"- {g}", 0, 1)
    return pdf.output(dest='S').encode('latin-1', 'replace')

# --- INTERFACE ---
aba1, aba2 = st.tabs(["📊 AUDITORIA", "🏘️ FAVELINHA"])

with aba1:
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")
    
    # O BOTÃO QUE VAI ABRIR O PDF
    try:
        pdf_data = gerar_pdf_final(unidade, v_entra, v_pula, info["gl"])
        st.download_button(
            label="📥 ABRIR EM PDF",
            data=pdf_data,
            file_name=f"Auditoria_{unidade}.pdf",
            mime="application/pdf"
        )
    except:
        st.warning("Aguarde 5 segundos e atualize a página para o PDF ativar.")

with aba2:
    for item in info["gl"]:
        st.error(item)
        
