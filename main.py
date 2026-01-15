import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE AMBIENTE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .relatorio-branco {
        background-color: white !important;
        color: black !important;
        padding: 20px !important;
        border-radius: 8px;
        border-top: 10px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DADOS (PADRÃO SIDNEY ALMEIDA) ---
db = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "g": [{"PAC": "JOAO SILVA", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "g": [{"PAC": "CARLOS LIMA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "g": [{"PAC": "ANA PAULA", "MOT": "LAUDO AUSENTE"}]}
}

st.markdown(f"<div style='background:#1c232d; padding:10px; border-radius:5px; border-left:5px solid #00d4ff; color:white;'><b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
info = db[unidade]
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y")

# --- 3. INTERFACE DE ABAS ---
tab1, tab2, tab3 = st.tabs(["📊 RESUMO", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab1:
    st.write(f"### Auditoria: {unidade}")
    # Terminologia Correta: ENTRA e PULA
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")
    st.progress(int(100 - info["p"]))

with tab2:
    st.write(f"### 🏘️ FAVELINHA - {unidade}")
    st.write("Pacientes com restrição (PULA):")
    st.table(pd.DataFrame(info["g"]))

with tab3:
    # RELATÓRIO LIMPO E SEM CÓDIGOS APARENTES
    # Criando a lista de glosas de forma segura para não quebrar o celular
    lista_glosas = ""
    for item in info["g"]:
        lista_glosas += f"• {item['PAC']}: {item['MOT']}<br>"

    html_v88 = f"""
    <div class="relatorio-branco">
        <h3 style="text-align:center; color:#1c2e4a; margin:0;">RELATÓRIO TÉCNICO DE AUDITORIA</h3>
        <p style="text-align:center; font-size:10px; color:#666; border-bottom:1px solid #ddd; padding-bottom:10px;">SPA | GESTÃO SIDNEY ALMEIDA</p>
        <p><b>UNIDADE:</b> {unidade}<br><b>DATA:</b> {hoje}</p>
        <div style="background:#f4f4f4; padding:10px; margin:10px 0; border-left:5px solid #00d4ff;">
            <p style="color:green; margin:0;"><b>✅ ENTRA:</b> R$ {v_entra:,.2f}</p>
            <p style="color:red; margin:0;"><b>❌ PULA:</b> R$ {v_pula:,.2f}</p>
        </div>
        <p><b>DETALHAMENTO (PULA):</b><br><small>{lista_glosas}</small></p>
        <div style="margin-top:40px; text-align:center; border-top:1px solid #000; width:200px; margin-left:auto; margin-right:auto;">
            <small><b>SIDNEY ALMEIDA</b><br>Diretor Operacional</small>
        </div>
    </div>
    """
    st.markdown(html_v88, unsafe_allow_html=True)
    st.download_button("⬇️ BAIXAR CERTIFICADO", f"AUDITORIA {unidade}\nENTRA: {v_entra}\nPULA: {v_pula}".encode('utf-8'), f"Audit_{unidade}.txt")
    
