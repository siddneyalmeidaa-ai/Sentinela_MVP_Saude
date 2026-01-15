import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE LIMPA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

# Estilos básicos para evitar erros de renderização no mobile
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .doc-oficial {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 20px !important;
        border-radius: 5px;
        border-top: 12px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS (PADRÃO SIDNEY ALMEIDA) ---
unidades = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "list": [{"PAC": "JOAO SILVA", "PROC": "RAIO-X", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "list": [{"PAC": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "list": [{"PAC": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOT": "LAUDO AUSENTE"}]}
}

# Cabeçalho Sidney Almeida
st.markdown(f"<div style='background:#1c232d; padding:12px; border-radius:8px; border-left:6px solid #00d4ff; color:white;'><b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Escolha a Unidade:", list(unidades.keys()))
dados = unidades[unidade]
v_entra = dados["v"] * ((100 - dados["p"]) / 100)
v_pula = dados["v"] * (dados["p"] / 100)
data_hj = datetime.now().strftime("%d/%m/%Y")

# --- 3. ABAS FUNCIONAIS ---
tab1, tab2, tab3 = st.tabs(["📊 RESUMO", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab1:
    st.subheader(f"Auditoria: {unidade}")
    # Terminologia: ENTRA e PULA
    st.metric("✅ ENTRA", f"R$ {v_entra:,.2f}")
    st.metric("❌ PULA", f"R$ {v_pula:,.2f}")
    st.progress(int(100 - dados["p"]))

with tab2:
    st.markdown(f"### 🏘️ FAVELINHA - {unidade}")
    st.write("Lista de pacientes que devem ser marcados como **PULA**:")
    st.table(pd.DataFrame(dados["list"]))

with tab3:
    # CONSTRUÇÃO SEGURA DO RELATÓRIO (EVITA O ERRO DAS IMAGENS)
    # Criamos a tabela de pacientes separadamente para não quebrar o código
    linhas_tabela = ""
    for item in dados["list"]:
        linhas_tabela += f"<tr><td>{item['PAC']}</td><td>{item['PROC']}</td><td style='color:red;'>{item['MOT']}</td></tr>"

    relatorio_html = f"""
    <div class="doc-oficial">
        <h3 style="text-align:center; color:#1c2e4a; margin:0;">RELATÓRIO TÉCNICO DE AUDITORIA</h3>
        <p style="text-align:center; font-size:10px; color:#666; margin-bottom:20px;">IA-SENTINELA | GESTÃO SIDNEY ALMEIDA</p>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {data_hj}</p>
        <div style="background:#f4f4f4; padding:10px; margin:15px 0; border-left:4px solid #00d4ff;">
            <p style="color:green; margin:2px;"><b>ENTRA:</b> R$ {v_entra:,.2f}</p>
            <p style="color:red; margin:2px;"><b>PULA:</b> R$ {v_pula:,.2f}</p>
        </div>
        <table style="width:100%; border-collapse:collapse; font-size:12px;">
            <tr style="background:#eee;"><th>PACIENTE</th><th>PROCEDIMENTO</th><th>MOTIVO</th></tr>
            {linhas_tabela}
        </table>
        <div style="margin-top:50px; text-align:center; border-top:1px solid #000; width:200px; margin-left:auto; margin-right:auto;">
            <small><b>SIDNEY ALMEIDA</b><br>Diretor Operacional</small>
        </div>
    </div>
    """
    st.markdown(relatorio_html, unsafe_allow_html=True)
    
    # Botão de download simplificado
    st.download_button("⬇️ BAIXAR TEXTO", f"AUDITORIA {unidade}\nENTRA: {v_entra}\nPULA: {v_pula}".encode('utf-8'), f"{unidade}.txt")
    
