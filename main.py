import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE AMBIENTE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* ESTILO DO RELATÓRIO TIMBRADO - BRANCO E LIMPO */
    .doc-oficial {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 25px !important;
        border-radius: 10px;
        border-top: 15px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .tabela-fav { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .tabela-fav th { background: #eeeeee; color: black; padding: 10px; border-bottom: 2px solid #333; text-align: left; }
    .tabela-fav td { padding: 10px; border-bottom: 1px solid #ddd; color: #333; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DADOS DE AUDITORIA ---
dados = {
    "ANIMA COSTA": {"tot": 16000.0, "p": 15, "glosas": [{"PACIENTE": "JOAO SILVA", "PROC": "RAIO-X", "MOTIVO": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"tot": 22500.0, "p": 22, "glosas": [{"PACIENTE": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOTIVO": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"tot": 45000.0, "p": 18, "glosas": [{"PACIENTE": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOTIVO": "LAUDO AUSENTE"}]}
}

# Cabeçalho de Identificação
st.markdown("<div style='background:#1c232d; padding:15px; border-radius:10px; border-left:5px solid #00d4ff; color:white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL | IA-SENTINELA</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(dados.keys()))
info = dados[unidade]
v_entra = info["tot"] * ((100 - info["p"]) / 100)
v_pula = info["tot"] * (info["p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y %H:%M")

# --- 3. INTERFACE DE ABAS (FOCO TOTAL NA TERMINOLOGIA) ---
tab_pizza, tab_favelinha, tab_relatorio = st.tabs(["⭕ PIZZA (%)", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab_pizza:
    st.markdown(f"### 📊 Auditoria: {unidade}")
    c1, c2 = st.columns(2)
    # Terminologia correta: ENTRA e PULA
    c1.metric("ENTRA", f"R$ {v_entra:,.2f}")
    c2.metric("PULA", f"R$ {v_pula:,.2f}")
    
    fig = px.pie(values=[v_entra, v_pula], names=["ENTRA", "PULA"], hole=0.5,
                 color_discrete_sequence=["#00d4ff", "#ff4b4b"])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with tab_favelinha:
    st.markdown(f"### 🏘️ FAVELINHA - {unidade}")
    # Tabela limpa conforme solicitado
    st.table(pd.DataFrame(info["glosas"]))
    st.error("🚨 IMPORTANTE: Os pacientes acima devem ser marcados como PULA.")

with tab_relatorio:
    # Construção segura da tabela para evitar SyntaxError no celular
    linhas = ""
    for g in info["glosas"]:
        linhas += f"<tr><td>{g['PACIENTE']}</td><td>{g['PROC']}</td><td style='color:red;'>{g['MOTIVO']}</td></tr>"

    # HTML BLINDADO DO RELATÓRIO
    relatorio_html = f"""
    <div class="doc-oficial">
        <div style="text-align:center; border-bottom:2px solid #00d4ff; padding-bottom:10px; margin-bottom:20px;">
            <h2 style="margin:0; color:#1c2e4a;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
            <p style="margin:0; font-size:12px; color:#666;">CERTIFICADO SPA | GESTÃO SIDNEY ALMEIDA</p>
        </div>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {hoje}</p>
        <div style="background:#f9f9f9; padding:15px; border-radius:5px; margin: 15px 0; border-left: 5px solid #00d4ff;">
            <p style="color:green; margin:5px; font-size:16px;"><b>✅ ENTRA:</b> R$ {v_entra:,.2f}</p>
            <p style="color:red; margin:5px; font-size:16px;"><b>❌ PULA:</b> R$ {v_pula:,.2f}</p>
        </div>
        <table class="tabela-fav">
            <thead><tr><th>PACIENTE</th><th>PROCEDIMENTO</th><th>MOTIVO (PULA)</th></tr></thead>
            <tbody>{linhas}</tbody>
        </table>
        <div style="margin-top:60px; text-align:center;">
            <div style="border-top:1px solid #000; width:300px; margin:auto; padding-top:5px;">
                <b>SIDNEY PEREIRA DE ALMEIDA</b><br><small>Diretor Operacional SPA</small>
            </div>
        </div>
    </div>
    """
    st.markdown(relatorio_html, unsafe_allow_html=True)
    
    st.download_button("⬇️ BAIXAR CERTIFICADO (.TXT)", f"AUDITORIA {unidade}\\nENTRA: R$ {v_entra}\\nPULA: R$ {v_pula}".encode('utf-8'), f"Relatorio_{unidade}.txt")

st.caption("IA-SENTINELA PRO | Sistema Sidney Almeida")
