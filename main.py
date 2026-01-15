import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO DE TELA (LIMPA E RÁPIDA)
st.set_page_config(page_title="SISTEMA SIDNEY ALMEIDA", layout="wide")

# Estilo para o papel timbrado não vazar código
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .folha-timbrada {
        background-color: white !important;
        color: black !important;
        padding: 30px !important;
        border-radius: 5px;
        border-top: 15px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .btn-pdf {
        background-color: #00d4ff;
        color: white;
        padding: 15px;
        text-align: center;
        border-radius: 8px;
        text-decoration: none;
        display: block;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# DADOS DA AUDITORIA
unidade = st.selectbox("Unidade:", ["ANIMA COSTA", "DMMIGINIO GUERRA"])
v_total = 16000.0 if unidade == "ANIMA COSTA" else 22500.0
v_entra = v_total * 0.85
v_pula = v_total * 0.15
hoje = datetime.now().strftime("%d/%m/%Y")

# INTERFACE DE ABAS
tab1, tab2 = st.tabs(["📊 RESUMO", "📄 GERAR PDF AGORA"])

with tab1:
    st.write(f"### Diretor Sidney: {unidade}")
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")

with tab2:
    # BOTÃO VISUAL QUE ORIENTA O PDF
    st.markdown('<div class="btn-pdf">COMO GERAR O PDF: Clique nos 3 pontinhos do Chrome > Compartilhar > Imprimir</div>', unsafe_allow_html=True)
    
    # RELATÓRIO QUE SERÁ "IMPRESSO" COMO PDF
    html_final = f"""
    <div class="folha-timbrada">
        <h2 style="text-align:center;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
        <p style="text-align:center; font-size:10px; color:gray;">SISTEMA SIDNEY ALMEIDA | IA-SENTINELA</p>
        <hr>
        <p><b>UNIDADE:</b> {unidade}<br><b>DATA:</b> {hoje}</p>
        <p style="color:green;"><b>VALOR ENTRA:</b> R$ {v_entra:,.2f}</p>
        <p style="color:red;"><b>VALOR PULA:</b> R$ {v_pula:,.2f}</p>
        <br>
        <p><b>LISTA DA FAVELINHA:</b><br>
        - JOAO SILVA: FALTA ASSINATURA<br>
        - MARIA SOUZA: GUIA EXPIRADA</p>
        <br><br><br>
        <div style="text-align:center; border-top:1px solid black; width:250px; margin:auto;">
            <b>SIDNEY ALMEIDA</b><br><small>Diretor Operacional</small>
        </div>
    </div>
    """
    st.markdown(html_final, unsafe_allow_html=True)
    
