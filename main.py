import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    .header-box { 
        background: #1c232d; padding: 20px; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #1c2e4a; border-radius: 10px; padding: 5px; }
    .stTabs [data-baseweb="tab"] { color: #8899A6; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #2c3e50 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }
    .report-preview { 
        background: #1c232d; color: white; padding: 25px; 
        border-radius: 10px; border: 2px solid #00d4ff;
        font-family: 'Segoe UI', sans-serif; line-height: 1.6;
    }
    </style>
    <div class="header-box">
        <div style="color: white; font-size: 1.1rem;">
            <b>SIDNEY PEREIRA DE ALMEIDA</b><br>
            <span style="color: #00d4ff; font-size: 0.9rem;">DIRETOR OPERACIONAL | IA-SENTINELA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. MOTOR DE DADOS COM PACIENTES PENDENTES ---
dados_medicos = {
    "ANIMA COSTA": {
        "valor": 16000.0, "p_pen": 15,
        "pacientes": [
            {"PACIENTE": "JOAO SILVA", "PROCEDIMENTO": "RAIO-X", "MOTIVO": "FALTA ASSINATURA"},
            {"PACIENTE": "MARIA SOUZA", "PROCEDIMENTO": "CONSULTA TÉCNICA", "MOTIVO": "GUIA EXPIRADA"}
        ]
    },
    "DMMIGINIO GUERRA": {
        "valor": 22500.0, "p_pen": 22,
        "pacientes": [
            {"PACIENTE": "CARLOS LIMA", "PROCEDIMENTO": "RESSONANCIA", "MOTIVO": "XML INVALIDO"}
        ]
    },
    "CLÍNICA SÃO JOSÉ": {
        "valor": 45000.0, "p_pen": 18,
        "pacientes": [
            {"PACIENTE": "ANA PAULA", "PROCEDIMENTO": "TOMOGRAFIA", "MOTIVO": "CODIGO TUSS DIVERGENTE"},
            {"PACIENTE": "PEDRO GOMES", "PROCEDIMENTO": "ULTRASSOM", "MOTIVO": "LAUDO AUSENTE"}
        ]
    }
}

unidade = st.selectbox("Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[unidade]

p_risco = info["p_pen"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

# --- 3. INDICADORES ---
st.markdown(f"### 📍 Auditoria: {unidade}")
c1, c2 = st.columns(2)
c1.metric("CONFORMIDADE OPERACIONAL", f"R$ {v_liberado:,.2f}")
c2.metric("PROJEÇÃO DE GLOSA", f"R$ {v_pendente:,.2f}")

# --- 4. ABAS OPERACIONAIS ---
tab_fluxo, tab_parecer, tab_cert = st.tabs([
    "📊 ANÁLISE DE GLOSA (H)", "📋 PARECER OPERACIONAL", "📄 CERTIFICADO SPA"
])

with tab_fluxo:
    df_bar = pd.DataFrame({
        'Status': ['LIBERADO', 'PENDENTE'],
        'Valor': [v_liberado, v_pendente],
        'Cor': ['#00d4ff', '#ff4b4b']
    })
    st.vega_lite_chart(df_bar, {
        'width': 'container', 'height': 250,
        'mark': {'type': 'bar', 'cornerRadiusEnd': 10, 'size': 50},
        'encoding': {
            'y': {'field': 'Status', 'type': 'nominal', 'axis': {'labelColor': 'white'}},
            'x': {'field': 'Valor', 'type': 'quantitative', 'axis': {'title': 'Montante R$'}},
            'color': {'field': 'Cor', 'type': 'nominal', 'scale': None}
        }
    })

with tab_parecer:
    st.markdown("### 📋 Listagem de Pacientes Pendentes")
    st.table(pd.DataFrame(info["pacientes"]))

with tab_cert:
    # Construção Segura do Texto (sem erros de aspas)
    lista_txt = ""
    lista_html = ""
    for p in info["pacientes"]:
        lista_txt += f"- {p['PACIENTE']} | {p['PROCEDIMENTO']} | {p['MOTIVO']}\\n"
        lista_html += f"<li><b>{p['PACIENTE']}</b>: {p['MOTIVO']}</li>"

    cert_html = f"""
    <div class="report-preview">
        <h2 style="color: #00d4ff; margin-top:0; text-align:center;">CERTIFICADO SPA</h2>
        <hr style="border: 0.5px solid #444;">
        <b>UNIDADE:</b> {unidade}<br><br>
        ✅ <b>LIBERADO:</b> {p_ok}% (R$ {v_liberado:,.2f}) -> <b>PROCEDE</b><br>
        ❌ <b>PENDENTE:</b> {p_risco}% (R$ {v_pendente:,.2f}) -> <b>NÃO PROCEDE</b><br><br>
        <b>PACIENTES COM PENDÊNCIA TÉCNICA:</b>
        <ul style="color: #ff4b4b;">{lista_html}</ul>
    </div>
    """
    st.markdown(cert_html, unsafe_allow_html=True)
    
    # Gerador de relatório otimizado para celular
    relatorio_final = (
        f"CERTIFICADO SPA\\n"
        f"UNIDADE: {unidade}\\n"
        f"STATUS: AUDITADO\\n"
        f"------------------------------\\n"
        f"LIBERADO: {p_ok}% -> PROCEDE\\n"
        f"PENDENTE: {p_risco}% -> NAO PROCEDE\\n"
        f"------------------------------\\n"
        f"DETALHE DAS PENDENCIAS:\\n{lista_txt}"
    )
    
    st.download_button(
        label="⬇️ BAIXAR RELATÓRIO (.TXT)",
        data=relatorio_final.encode('utf-8'),
        file_name=f"Relatorio_{unidade}.txt",
        mime="text/plain"
    )

st.caption("IA-SENTINELA PRO | Sistema de Gestão SPA")
    
