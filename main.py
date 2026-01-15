import streamlit as st
import pandas as pd
from datetime import datetime
from fpdf import FPDF
import io

# --- 1. CONFIGURAÇÃO MOBILE ---
st.set_page_config(page_title="SISTEMA SIDNEY PDF", layout="wide")

st.markdown("<style>[data-testid='stHeader'] {display: none !important;}</style>", unsafe_allow_html=True)

# --- 2. DADOS PADRÃO ---
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

# --- 3. FUNÇÃO DO BOTÃO PDF (GERAÇÃO INTERNA) ---
def gerar_pdf_sidney(unidade, v_entra, v_pula, glosas):
    pdf = FPDF()
    pdf.add_page()
    
    # Cabeçalho
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "RELATORIO TECNICO DE AUDITORIA", 0, 1, 'C')
    pdf.set_font("Arial", size=10)
    pdf.cell(190, 5, "SPA | GESTAO SIDNEY ALMEIDA", 0, 1, 'C')
    pdf.ln(10)
    
    # Dados
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 10, f"UNIDADE: {unidade} | DATA: {hoje}", 0, 1)
    
    pdf.set_text_color(0, 128, 0) # Verde
    pdf.cell(190, 10, f"ENTRA: R$ {v_entra:,.2f}", 0, 1)
    
    pdf.set_text_color(255, 0, 0) # Vermelho
    pdf.cell(190, 10, f"PULA: R$ {v_pula:,.2f}", 0, 1)
    
    pdf.set_text_color(0, 0, 0) # Preto
    pdf.ln(5)
    pdf.cell(190, 10, "LISTA DA FAVELINHA:", 0, 1)
    pdf.set_font("Arial", size=11)
    for g in glosas:
        pdf.cell(190, 8, f"- {g}", 0, 1)
        
    # Assinatura
    pdf.ln(30)
    pdf.cell(190, 0, "", 'T', 1, 'C')
    pdf.cell(190, 10, "SIDNEY ALMEIDA", 0, 1, 'C')
    pdf.cell(190, 5, "Diretor Operacional", 0, 1, 'C')
    
    return pdf.output(dest='S').encode('latin-1', 'replace')

# --- 4. INTERFACE ---
aba1, aba2 = st.tabs(["📊 AUDITORIA", "🏘️ FAVELINHA"])

with aba1:
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")
    
    # O BOTÃO QUE O SENHOR PEDIU:
    pdf_bytes = gerar_pdf_sidney(unidade, v_entra, v_pula, info["gl"])
    st.download_button(
        label="📥 CLIQUE PARA GERAR PDF",
        data=pdf_bytes,
        file_name=f"Auditoria_{unidade}.pdf",
        mime="application/pdf"
    )

with aba2:
    st.subheader("🏘️ Favelinha")
    for item in info["gl"]:
        st.error(item)
    
