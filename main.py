import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO MOBILE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .doc-limpo {
        background-color: white !important;
        color: black !important;
        padding: 20px !important;
        border-radius: 5px;
        border-top: 12px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DADOS (PADRÃO OPERACIONAL) ---
db = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "gl": [{"PAC": "JOAO SILVA", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "gl": [{"PAC": "CARLOS LIMA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "gl": [{"PAC": "ANA PAULA", "MOT": "LAUDO AUSENTE"}]}
}

# Cabeçalho Sidney Almeida
st.markdown("<div style='background:#1c232d; padding:10px; border-radius:5px; color:white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Unidade para Auditoria:", list(db.keys()))
info = db[unidade]
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y")

# --- 3. ABAS DE NAVEGAÇÃO ---
tab1, tab2, tab3 = st.tabs(["📊 RESUMO", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab1:
    st.write(f"### Unidade: {unidade}")
    # Terminologia: ENTRA e PULA
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")
    st.progress(int(100 - info["p"]))

with tab2:
    st.markdown(f"### 🏘️ FAVELINHA - {unidade}")
    st.write("Pacientes identificados para restrição (PULA):")
    st.table(pd.DataFrame(info["gl"]))

with tab3:
    # RELATÓRIO TÉCNICO SEM VAZAMENTO DE CÓDIGO
    # Processamento seguro da lista de glosas
    glosas_texto = ""
    for g in info["gl"]:
        glosas_texto += f"• {g['PAC']}: {g['MOT']}<br>"

    html_v91 = f"""
    <div class="doc-limpo">
        <h3 style="text-align:center; color:#1c2e4a; margin:0;">RELATÓRIO DE AUDITORIA</h3>
        <p style="text-align:center; font-size:10px; color:#666; border-bottom:1px solid #ddd; padding-bottom:10px;">IA-SENTINELA | GESTÃO SIDNEY ALMEIDA</p>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {hoje}</p>
        <div style="background:#f9f9f9; padding:10px; margin:10px 0; border-left:5px solid #00d4ff;">
            <p style="color:green; margin:0;"><b>✅ ENTRA:</b> R$ {v_entra:,.2f}</p>
            <p style="color:red; margin:0;"><b>❌ PULA:</b> R$ {v_pula:,.2f}</p>
        </div>
        <p style="font-size:12px;"><b>DETALHAMENTO PULA:</b><br>{glosas_texto}</p>
        <div style="margin-top:40px; text-align:center; border-top:1px solid #000; width:200px; margin:auto;">
            <small><b>SIDNEY ALMEIDA</b><br>Diretor Operacional</small>
        </div>
    </div>
    """
    st.markdown(html_v91, unsafe_allow_html=True)
    st.download_button("⬇️ BAIXAR TEXTO", f"AUDITORIA {unidade}\nENTRA: {v_entra}\nPULA: {v_pula}".encode('utf-8'), f"{unidade}.txt")
    
