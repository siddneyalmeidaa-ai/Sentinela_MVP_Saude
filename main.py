import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE SEGURANÇA MOBILE ---
st.set_page_config(page_title="SISTEMA SIDNEY", layout="wide")

# Estilos ultra-reduzidos para evitar travamento no celular
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .area-relatorio {
        background: white !important;
        color: black !important;
        padding: 15px;
        border-top: 10px solid #00d4ff;
        font-family: sans-serif;
    }
    .box-verde { color: green; font-weight: bold; border-left: 4px solid green; padding-left: 10px; }
    .box-vermelha { color: red; font-weight: bold; border-left: 4px solid red; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DADOS DA OPERAÇÃO ---
db = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "gl": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "gl": ["CARLOS LIMA: XML INVÁLIDO"]}
}

st.write(f"### DIRETOR: SIDNEY PEREIRA DE ALMEIDA")

unidade = st.selectbox("Escolha a Unidade:", list(db.keys()))
info = db[unidade]
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y")

# --- 3. SISTEMA DE ABAS ---
aba1, aba2, aba3 = st.tabs(["📊 AUDITORIA", "🏘️ FAVELINHA", "📄 ABRIR EM PDF"])

with aba1:
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")

with aba2:
    st.subheader("🏘️ Favelinha (Pendências)")
    for item in info["gl"]:
        st.error(item)

with aba3:
    # ESTA ABA GERA O DOCUMENTO PARA O SENHOR SALVAR EM PDF
    st.warning("📥 PARA SALVAR EM PDF: No topo do seu navegador (Chrome), clique nos '3 pontinhos' > Compartilhar > Imprimir > Salvar como PDF.")
    
    # Construção de texto simples para evitar erro de 'SyntaxError'
    conteudo = f"""
    <div class="area-relatorio">
        <h2 style="text-align:center;">RELATÓRIO DE AUDITORIA</h2>
        <p style="text-align:center; font-size:10px;">SPA | GESTÃO SIDNEY ALMEIDA</p>
        <hr>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {hoje}</p>
        <p class="box-verde">✅ ENTRA: R$ {v_entra:,.2f}</p>
        <p class="box-vermelha">❌ PULA: R$ {v_pula:,.2f}</p>
        <hr>
        <p><b>LISTA DA FAVELINHA:</b></p>
        <p>{'<br>'.join(info['gl'])}</p>
        <br><br>
        <div style="text-align:center; border-top:1px solid black; width:200px; margin:auto;">
            <b>SIDNEY ALMEIDA</b><br><small>Diretor Operacional</small>
        </div>
    </div>
    """
    st.markdown(conteudo, unsafe_allow_html=True)
    
