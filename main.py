import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE BLINDADA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .papel-branco {
        background-color: white !important;
        color: black !important;
        padding: 20px !important;
        border-radius: 5px;
        border-top: 10px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .tabela-fav { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .tabela-fav th { background: #eee; color: black; text-align: left; padding: 8px; font-size: 12px; }
    .tabela-fav td { border-bottom: 1px solid #ddd; padding: 8px; font-size: 12px; color: #333; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DADOS DE AUDITORIA ---
db = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "gl": [{"PAC": "JOAO SILVA", "PROC": "RAIO-X", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "gl": [{"PAC": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "gl": [{"PAC": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOT": "LAUDO AUSENTE"}]}
}

# Cabeçalho Sidney Almeida
st.markdown("<div style='background:#1c232d; padding:12px; border-radius:8px; border-left:5px solid #00d4ff; color:white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
info = db[unidade]
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y")

# --- 3. INTERFACE DE ABAS ---
tab1, tab2, tab3 = st.tabs(["📊 RESUMO", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab1:
    st.subheader(f"Auditoria: {unidade}")
    # Terminologia Correta: ENTRA e PULA
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")
    st.progress(int(100 - info["p"]))

with tab2:
    st.markdown(f"### 🏘️ FAVELINHA - {unidade}")
    st.table(pd.DataFrame(info["gl"]))
    st.error("🚨 IMPORTANTE: Os itens listados acima devem ser marcados como PULA.")

with tab3:
    # RELATÓRIO TÉCNICO LIMPO (SEM VAZAMENTO DE CÓDIGO)
    linhas_html = ""
    for g in info["gl"]:
        linhas_html += f"<tr><td>{g['PAC']}</td><td>{g['PROC']}</td><td style='color:red;'>{g['MOT']}</td></tr>"

    relatorio_html = f"""
    <div class="papel-branco">
        <div style="text-align:center; border-bottom:2px solid #00d4ff; padding-bottom:10px; margin-bottom:15px;">
            <h3 style="margin:0; color:#1c2e4a;">RELATÓRIO TÉCNICO DE AUDITORIA</h3>
            <p style="margin:0; font-size:10px; color:#666;">SPA | GESTÃO SIDNEY ALMEIDA</p>
        </div>
        <p style="font-size:12px;"><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {hoje}</p>
        <div style="background:#f9f9f9; padding:10px; border-radius:5px; margin: 10px 0; border-left: 5px solid #00d4ff;">
            <p style="color:green; margin:2px; font-size:14px;"><b>✅ ENTRA:</b> R$ {v_entra:,.2f}</p>
            <p style="color:red; margin:2px; font-size:14px;"><b>❌ PULA:</b> R$ {v_pula:,.2f}</p>
        </div>
        <table class="tabela-fav">
            <thead><tr><th>PACIENTE</th><th>PROCEDIMENTO</th><th>MOTIVO (PULA)</th></tr></thead>
            <tbody>{linhas_html}</tbody>
        </table>
        <div style="margin-top:40px; text-align:center;">
            <div style="border-top:1px solid #000; width:200px; margin:auto; padding-top:5px;">
                <small><b>SIDNEY ALMEIDA</b><br>Diretor Operacional</small>
            </div>
        </div>
    </div>
    """
    st.markdown(relatorio_html, unsafe_allow_html=True)
    st.download_button("⬇️ BAIXAR TEXTO", f"AUDITORIA {unidade}\nENTRA: {v_entra}\nPULA: {v_pula}".encode('utf-8'), f"{unidade}.txt")
    
