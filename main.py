import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE DESIGN PROFISSIONAL ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* ESTILO PAPEL TIMBRADO PARA PRINT */
    .folha-timbrada {
        background-color: white !important;
        color: #1a1a1a !important;
        padding: 40px !important;
        border-radius: 8px;
        border-top: 15px solid #00d4ff;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        max-width: 900px;
        margin: auto;
    }
    .topo-timbrado { text-align: center; border-bottom: 2px solid #00d4ff; padding-bottom: 15px; margin-bottom: 20px; }
    .tabela-oficial { width: 100%; border-collapse: collapse; margin-top: 20px; }
    .tabela-oficial th { background: #f2f2f2; padding: 12px; text-align: left; border-bottom: 2px solid #333; color: black; }
    .tabela-oficial td { padding: 12px; border-bottom: 1px solid #eee; color: #333; font-size: 14px; }
    .assinatura-area { margin-top: 60px; text-align: center; border-top: 1px solid #333; width: 280px; margin-left: auto; margin-right: auto; padding-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DADOS DE AUDITORIA (SEM VÁCUO) ---
dados_medicos = {
    "ANIMA COSTA": {
        "valor": 16000.0, "p_pen": 15,
        "pacientes": [
            {"PAC": "JOAO SILVA", "PROC": "RAIO-X", "MOT": "FALTA ASSINATURA"},
            {"PAC": "MARIA SOUZA", "PROC": "CONSULTA", "MOT": "GUIA EXPIRADA"}
        ]
    },
    "DMMIGINIO GUERRA": {
        "valor": 22500.0, "p_pen": 22,
        "pacientes": [
            {"PAC": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOT": "XML INVÁLIDO"}
        ]
    },
    "CLÍNICA SÃO JOSÉ": {
        "valor": 45000.0, "p_pen": 18,
        "pacientes": [
            {"PAC": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOT": "CÓDIGO TUSS DIVERGENTE"},
            {"PAC": "PEDRO GOMES", "PROC": "ULTRASSOM", "MOT": "LAUDO AUSENTE"}
        ]
    }
}

# Cabeçalho da App
st.markdown("<div style='background: #1c232d; padding: 20px; border-radius: 10px; border-left: 5px solid #00d4ff; color: white; margin-bottom: 20px;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color: #00d4ff;'>DIRETOR OPERACIONAL | IA-SENTINELA</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(dados_medicos.keys()))
info = dados_medicos[unidade]
v_liberado = info["valor"] * ((100 - info["p_pen"]) / 100)
v_pendente = info["valor"] * (info["p_pen"] / 100)
data_relatorio = datetime.now().strftime("%d/%m/%Y - %H:%M")

# --- 3. ABAS ORGANIZADAS ---
tab1, tab2 = st.tabs(["📊 AUDITORIA EM TEMPO REAL", "📄 VISUALIZAR RELATÓRIO TIMBRADO"])

with tab1:
    st.markdown(f"### 📍 Unidade: {unidade}")
    c1, c2 = st.columns(2)
    c1.metric("PROCEDE (LIBERADO)", f"R$ {v_liberado:,.2f}")
    c2.metric("NÃO PROCEDE (PENDENTE)", f"R$ {v_pendente:,.2f}")
    st.markdown("#### Tabela de Pendências")
    st.table(pd.DataFrame(info["pacientes"]))

with tab2:
    # Construção da Tabela HTML
    linhas = "".join([f"<tr><td>{p['PAC']}</td><td>{p['PROC']}</td><td style='color:red;'>{p['MOT']}</td></tr>" for p in info["pacientes"]])
    
    # VISUAL DO PAPEL TIMBRADO (CORRIGIDO)
    st.markdown(f"""
    <div class="folha-timbrada">
        <div class="topo-timbrado">
            <h2 style="margin:0; color:#1c2e4a;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
            <p style="margin:0; font-size:12px; color:#555;">IA-SENTINELA | GESTÃO DE GLOSAS</p>
        </div>
        
        <div style="margin-bottom: 20px;">
            <p><b>UNIDADE:</b> {unidade}</p>
            <p><b>EMISSÃO:</b> {data_relatorio}</p>
            <p><b>RESPONSÁVEL:</b> SIDNEY PEREIRA DE ALMEIDA</p>
        </div>
        
        <div style="background:#f9f9f9; padding:15px; border-radius:5px; border:1px solid #ddd;">
            <p style="color:green; margin:5px;"><b>✅ PROCEDE:</b> {100-info['p_pen']}% (R$ {v_liberado:,.2f})</p>
            <p style="color:red; margin:5px;"><b>❌ NÃO PROCEDE:</b> {info['p_pen']}% (R$ {v_pendente:,.2f})</p>
        </div>
        
        <table class="tabela-oficial">
            <thead>
                <tr><th>PACIENTE</th><th>PROCEDIMENTO</th><th>MOTIVO DA GLOSA</th></tr>
            </thead>
            <tbody>
                {linhas}
            </tbody>
        </table>
        
        <div class="assinatura-area">
            <span style="font-size:14px; font-weight:bold;">SIDNEY PEREIRA DE ALMEIDA</span><br>
            <span style="font-size:11px; color:#666;">Diretor Operacional SPA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # BOTÃO DE DOWNLOAD ORGANIZADO
    lista_txt = "".join([f"- {p['PAC']} | {p['PROC']} | {p['MOT']}\\n" for p in info["pacientes"]])
    texto_download = (
        f"------------------------------------------\\n"
        f"       RELATORIO DE AUDITORIA SPA         \\n"
        f"------------------------------------------\\n"
        f"UNIDADE: {unidade}\\n"
        f"DATA: {data_relatorio}\\n"
        f"------------------------------------------\\n"
        f"PROCEDE: {100-info['p_pen']}% (R$ {v_liberado:,.2f})\\n"
        f"NAO PROCEDE: {info['p_pen']}% (R$ {v_pendente:,.2f})\\n"
        f"------------------------------------------\\n"
        f"LISTA DE PENDENCIAS:\\n{lista_txt}"
        f"------------------------------------------\\n"
        f"ASSINADO: SIDNEY PEREIRA DE ALMEIDA\\n"
    )

    st.download_button(
        label="⬇️ BAIXAR CERTIFICADO OFICIAL (.TXT)",
        data=texto_download.encode('utf-8'),
        file_name=f"Relatorio_{unidade}.txt",
        mime="text/plain"
    )

st.caption("IA-SENTINELA PRO | Sistema Sidney Almeida")
