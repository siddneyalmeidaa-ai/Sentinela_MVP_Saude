import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

# Estilos para garantir que o Relatório Timbrado funcione no celular
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* ESTILO PAPEL TIMBRADO BRANCO */
    .papel-branco {
        background-color: white !important;
        color: black !important;
        padding: 20px !important;
        border-radius: 5px;
        border-top: 12px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    .tabela-oficial { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .tabela-oficial th { background: #f2f2f2; color: black; padding: 8px; border-bottom: 2px solid #333; text-align: left; }
    .tabela-oficial td { padding: 8px; border-bottom: 1px solid #ddd; color: #333; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS (CONFIGURADO) ---
dados_medicos = {
    "ANIMA COSTA": {"v": 16000.0, "p": 15, "list": [{"PAC": "JOAO SILVA", "MOT": "FALTA ASSINATURA"}]},
    "DMMIGINIO GUERRA": {"v": 22500.0, "p": 22, "list": [{"PAC": "CARLOS LIMA", "MOT": "XML INVÁLIDO"}]},
    "CLÍNICA SÃO JOSÉ": {"v": 45000.0, "p": 18, "list": [{"PAC": "ANA PAULA", "MOT": "LAUDO AUSENTE"}]}
}

# Cabeçalho Sidney Almeida
st.markdown("<div style='background:#1c232d; padding:15px; border-radius:10px; border-left:5px solid #00d4ff; color:white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color:#00d4ff;'>DIRETOR OPERACIONAL | IA-SENTINELA</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade:", list(dados_medicos.keys()))
info = dados_medicos[unidade]
v_ent = info["v"] * ((100 - info["p"]) / 100)
v_pul = info["v"] * (info["p"] / 100)
data_obs = datetime.now().strftime("%d/%m/%Y %H:%M")

# --- 3. AS ABAS VOLTARAM (PIZZA, FAVELINHA E RELATÓRIO) ---
tab_pizza, tab_favelinha, tab_relatorio = st.tabs(["⭕ PIZZA (%)", "🏘️ FAVELINHA", "📄 PAPEL TIMBRADO"])

with tab_pizza:
    st.markdown(f"### 📊 Auditoria: {unidade}")
    col1, col2 = st.columns(2)
    col1.metric(f"ENTRA ({100-info['p']}%)", f"R$ {v_ent:,.2f}")
    col2.metric(f"PULA ({info['p']}%)", f"R$ {v_pul:,.2f}")
    
    fig = px.pie(values=[v_ent, v_pul], names=["ENTRA", "PULA"], hole=0.5,
                 color_discrete_sequence=["#00d4ff", "#ff4b4b"])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with tab_favelinha:
    st.markdown("### 🏘️ Tabela da Favelinha (Ação Imediata)")
    st.table(pd.DataFrame(info["list"]))
    st.info("💡 Projeção de Vácuo (Death Zone): 0%. IA-SENTINELA monitorando.")

with tab_relatorio:
    # Gerar a tabela do relatório sem quebrar o código HTML
    linhas = "".join([f"<tr><td>{p['PAC']}</td><td style='color:red;'>{p['MOT']}</td></tr>" for p in info["list"]])

    # RELATÓRIO TIMBRADO (BLINDADO CONTRA ERROS)
    # Usei f-strings simples para evitar o erro de 'unterminated triple-quoted'
    st.markdown(f"""
    <div class="papel-branco">
        <div style="text-align:center; border-bottom:2px solid #00d4ff; padding-bottom:10px; margin-bottom:20px;">
            <h3 style="margin:0;">RELATÓRIO TÉCNICO DE AUDITORIA</h3>
            <p style="margin:0; font-size:12px; color:#666;">CERTIFICADO SPA - GESTÃO SIDNEY ALMEIDA</p>
        </div>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {data_obs}</p>
        <div style="background:#f9f9f9; padding:10px; border-radius:5px; margin: 15px 0;">
            <p style="color:green; margin:5px;"><b>✅ PROCEDE (ENTRA):</b> R$ {v_ent:,.2f}</p>
            <p style="color:red; margin:5px;"><b>❌ NÃO PROCEDE (PULA):</b> R$ {v_pul:,.2f}</p>
        </div>
        <table class="tabela-oficial">
            <thead><tr><th>PACIENTE</th><th>MOTIVO DA PENDÊNCIA</th></tr></thead>
            <tbody>{linhas}</tbody>
        </table>
        <div style="margin-top:50px; text-align:center;">
            <div style="border-top:1px solid #000; width:260px; margin:auto; padding-top:5px;">
                <b>SIDNEY PEREIRA DE ALMEIDA</b><br><small>Diretor Operacional SPA</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Download sem erro de acento no celular
    st.download_button("⬇️ BAIXAR RELATÓRIO (.TXT)", f"AUDITORIA {unidade}\\nSTATUS: CONCLUIDO".encode('utf-8'), f"Audit_{unidade}.txt")

st.caption("IA-SENTINELA PRO | Padrão Ouro V80")
    
