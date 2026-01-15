import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO LEVE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    .doc-limpo {
        background-color: white !important;
        color: black !important;
        padding: 20px !important;
        border-radius: 5px;
        border-top: 10px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DADOS (SINCRONIZAÇÃO AUTOMÁTICA) ---
unidades = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "gl": [{"PAC": "JOAO SILVA", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "gl": [{"PAC": "CARLOS LIMA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "gl": [{"PAC": "ANA PAULA", "MOT": "LAUDO AUSENTE"}]}
}

st.markdown(f"<div style='color:white; background:#1c232d; padding:10px; border-radius:5px;'><b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL</small></div>", unsafe_allow_html=True)

escolha = st.selectbox("Selecione a Unidade:", list(unidades.keys()))
info = unidades[escolha]

# Cálculos Automáticos
v_entra = info["v"] * ((100 - info["p"]) / 100)
v_pula = info["v"] * (info["p"] / 100)
data_hj = datetime.now().strftime("%d/%m/%Y")

# --- 3. ABAS COM TERMINOLOGIA CORRETA ---
aba1, aba2, aba3 = st.tabs(["⭕ PIZZA (%)", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with aba1:
    st.write(f"### Unidade: {escolha}")
    c1, c2 = st.columns(2)
    # Terminologia: ENTRA e PULA
    c1.metric("ENTRA", f"R$ {v_entra:,.2f}")
    c2.metric("PULA", f"R$ {v_pula:,.2f}")
    
    fig = px.pie(values=[v_entra, v_pula], names=["ENTRA", "PULA"], hole=0.5, color_discrete_sequence=["#00d4ff", "#ff4b4b"])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

with aba2:
    st.write(f"### 🏘️ FAVELINHA - {escolha}")
    st.table(pd.DataFrame(info["gl"]))
    st.error("🚨 Ação Imediata: Itens acima devem ser marcados como PULA.")

with aba3:
    # RELATÓRIO TÉCNICO LIMPO (SEM CÓDIGO VAZANDO)
    rel_txt = f"""
    <div class="doc-limpo">
        <h2 style="text-align:center; color:#1c2e4a; margin-bottom:5px;">RELATÓRIO DE AUDITORIA</h2>
        <p style="text-align:center; font-size:12px; border-bottom:1px solid #ddd; padding-bottom:10px;">IA-SENTINELA | GESTÃO SIDNEY ALMEIDA</p>
        <p><b>UNIDADE:</b> {escolha} | <b>DATA:</b> {data_hj}</p>
        <div style="background:#f9f9f9; padding:10px; margin:10px 0;">
            <p style="color:green;"><b>✅ ENTRA:</b> R$ {v_entra:,.2f} ({100-info['p']}%)</p>
            <p style="color:red;"><b>❌ PULA:</b> R$ {v_pula:,.2f} ({info['p']}%)</p>
        </div>
        <p><b>DETALHAMENTO PULA:</b></p>
        <small>Verifique os pacientes na aba Favelinha para ação corretiva imediata.</small>
        <div style="margin-top:40px; text-align:center; border-top:1px solid #000; width:200px; margin-left:auto; margin-right:auto;">
            <b>SIDNEY ALMEIDA</b>
        </div>
    </div>
    """
    st.markdown(rel_txt, unsafe_allow_html=True)
    
    # Download sem erro de acento
    st.download_button("⬇️ BAIXAR TEXTO", f"AUDITORIA {escolha}\\
    
