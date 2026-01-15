import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE BLINDADA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

# Estilos para o Papel Timbrado e Tabelas
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* DOCUMENTO OFICIAL BRANCO */
    .papel-branco {
        background-color: white !important;
        color: black !important;
        padding: 25px !important;
        border-radius: 5px;
        border-top: 15px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .tabela-favelinha { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .tabela-favelinha th { background: #f2f2f2; color: black; padding: 10px; border-bottom: 2px solid #333; text-align: left; }
    .tabela-favelinha td { padding: 10px; border-bottom: 1px solid #ddd; color: #333; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS ATUALIZADO ---
dados_medicos = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "list": [{"PAC": "JOAO SILVA", "PROC": "RAIO-X", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "list": [{"PAC": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "list": [{"PAC": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOT": "LAUDO AUSENTE"}]}
}

# Identificação Superior Sidney Almeida
st.markdown("<div style='background:#1c232d; padding:15px; border-radius:10px; border-left:5px solid #00d4ff; color:white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL | IA-SENTINELA</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(dados_medicos.keys()))
info = dados_medicos[unidade]
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
data_hoje = datetime.now().strftime("%d/%m/%Y %H:%M")

# --- 3. ABAS COM TERMINOLOGIA CORRETA ---
tab_pizza, tab_favelinha, tab_relatorio = st.tabs(["⭕ PIZZA (%)", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab_pizza:
    st.markdown(f"### 📊 Auditoria: {unidade}")
    col1, col2 = st.columns(2)
    # Terminologia: ENTRA e PULA
    col1.metric("ENTRA", f"R$ {v_entra:,.2f}")
    col2.metric("PULA", f"R$ {v_pula:,.2f}")
    
    fig = px.pie(values=[v_entra, v_pula], names=["ENTRA", "PULA"], hole=0.5,
                 color_discrete_sequence=["#00d4ff", "#ff4b4b"])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with tab_favelinha:
    st.markdown(f"### 🏘️ Tabela da Favelinha - {unidade}")
    # Tabela limpa, sem menção a vácuo
    st.table(pd.DataFrame(info["list"]))
    st.error("🚨 ATENÇÃO: Os itens listados acima devem ser marcados como PULA.")

with tab_relatorio:
    # Gerar linhas da tabela sem quebrar o HTML
    linhas_doc = ""
    for item in info["list"]:
        linhas_doc += f"<tr><td>{item['PAC']}</td><td>{item['PROC']}</td><td style='color:red;'>{item['MOT']}</td></tr>"

    # RELATÓRIO TIMBRADO (BLINDADO CONTRA ERRO DE CÓDIGO)
    st.markdown(f"""
    <div class="papel-branco">
        <div style="text-align:center; border-bottom:2px solid #00d4ff; padding-bottom:10px; margin-bottom:20px;">
            <h2 style="margin:0; color:#1c2e4a;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
            <p style="margin:0; font-size:12px; color:#666;">CERTIFICADO SPA | GESTÃO SIDNEY ALMEIDA</p>
        </div>
        <p><b>UNIDADE AUDITADA:</b> {unidade}</p>
        <p><b>DATA:</b> {data_hoje}</p>
        <div style="margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 5px solid #00d4ff;">
            <p style="color: green; margin: 5px; font-size: 18px;"><b>✅ ENTRA:</b> R$ {v_entra:,.2f}</p>
            <p style="color: red; margin: 5px; font-size: 18px;"><b>❌ PULA:</b> R$ {v_pula:,.2f}</p>
        </div>
        <table class="tabela-favelinha">
            <thead><tr><th>PACIENTE</th><th>PROCEDIMENTO</th><th>MOTIVO (PULA)</th></tr></thead>
            <tbody>{linhas_doc}</tbody>
        </table>
        <div style="margin-top:60px; text-align:center;">
            <div style="border-top:1px solid #000; width:300px; margin:auto; padding-top:5px;">
                <b>SIDNEY PEREIRA DE ALMEIDA</b><br><small>Diretor Operacional SPA</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.download_button("⬇️ BAIXAR RELATÓRIO (.TXT)", f"AUDITORIA {unidade}\\nENTRA: R$ {v_entra}\\nPULA: R$ {v_pula}".encode('utf-8'), f"Audit_{unidade}.txt")

st.caption("IA-SENTINELA PRO | Sistema de Auditoria Sidney Almeida")
    
