import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE TELA ---
st.set_page_config(page_title="SISTEMA SIDNEY ALMEIDA", layout="wide")

# Estilo para o Relatório Papel Timbrado (Limpando o erro de código)
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .pdf-container {
        background-color: white !important;
        color: black !important;
        padding: 30px !important;
        border: 1px solid #ddd;
        border-top: 15px solid #00d4ff;
        font-family: 'Arial', sans-serif;
    }
    .status-box { padding: 10px; border-radius: 5px; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS PADRÃO ---
db = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "gl": [{"PAC": "JOAO SILVA", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "gl": [{"PAC": "CARLOS LIMA", "MOT": "XML INVÁLIDO"}]},
}

# Identificação do Diretor
st.markdown(f"<div style='background:#1c232d; padding:15px; border-radius:8px; border-left:8px solid #00d4ff; color:white;'>"
            f"<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
info = db[unidade]
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y")

# --- 3. MENU DE NAVEGAÇÃO ---
aba1, aba2, aba3 = st.tabs(["📊 AUDITORIA", "🏘️ FAVELINHA", "📜 GERAR PDF"])

with aba1:
    st.write(f"### Unidade: {unidade}")
    # Terminologia: ENTRA e PULA (Conforme solicitado)
    st.metric(label="✅ ENTRA", value=f"R$ {v_entra:,.2f}")
    st.metric(label="❌ PULA", value=f"R$ {v_pula:,.2f}")
    st.progress(int(100 - info["p"]))

with aba2:
    st.subheader("🏘️ Tabela da Favelinha")
    st.write("Pacientes Retidos (PULA):")
    st.table(pd.DataFrame(info["gl"]))

with aba3:
    # RELATÓRIO FORMATADO PARA "SALVAR COMO PDF" NO CELULAR
    st.info("💡 Para salvar: No seu navegador, vá em 'Compartilhar' > 'Imprimir' > 'Salvar como PDF'.")
    
    lista_pacientes = "".join([f"<li>{g['PAC']} - {g['MOT']}</li>" for g in info["gl"]])
    
    relatorio_pdf = f"""
    <div class="pdf-container">
        <h2 style="text-align:center; margin-bottom:0;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
        <p style="text-align:center; font-size:12px; color:gray; border-bottom:1px solid #eee; padding-bottom:10px;">IA-SENTINELA | GESTÃO SIDNEY ALMEIDA</p>
        
        <p><b>UNIDADE:</b> {unidade}<br><b>DATA DE EMISSÃO:</b> {hoje}</p>
        
        <div style="background:#e8f5e9; padding:10px; border-left:5px solid green;">
            <b style="color:green;">VALOR ENTRA (LIBERADO):</b> R$ {v_entra:,.2f}
        </div>
        <div style="background:#ffebee; padding:10px; border-left:5px solid red; margin-top:5px;">
            <b style="color:red;">VALOR PULA (RETIDO):</b> R$ {v_pula:,.2f}
        </div>
        
        <h4 style="margin-top:20px; border-bottom:1px solid #000;">DETALHAMENTO DE GLOSAS:</h4>
        <ul>{lista_pacientes}</ul>
        
        <div style="margin-top:50px; text-align:center;">
            <div style="border-top:1px solid #000; width:250px; margin:auto; padding-top:5px;">
                <b>SIDNEY PEREIRA DE ALMEIDA</b><br>
                <small>Diretor Operacional - SPA</small>
            </div>
        </div>
    </div>
    """
    st.markdown(relatorio_pdf, unsafe_allow_html=True)
    
