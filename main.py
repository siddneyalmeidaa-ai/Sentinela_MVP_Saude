import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. DESIGN E CABEÇALHO (ESTÉTICA PREMIUM)
st.set_page_config(page_title="SISTEMA SIDNEY ALMEIDA", layout="wide")
st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .main-header {
        background-color: #1c232d;
        padding: 20px;
        border-radius: 10px;
        border-left: 10px solid #00d4ff;
        color: white;
        margin-bottom: 25px;
    }
    .relatorio-folha {
        background-color: white !important;
        color: black !important;
        padding: 30px !important;
        border-top: 15px solid #00d4ff;
        font-family: Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h2 style='margin:0;'>SIDNEY PEREIRA DE ALMEIDA</h2>
        <p style='margin:0; color:#00d4ff; font-weight:bold;'>DIRETOR OPERACIONAL | IA-SENTINELA PRO</p>
    </div>
    """, unsafe_allow_html=True)

# 2. BASE DE DADOS SINCRONIZADA
db = {
    "ANIMA COSTA": {"total": 16000.0, "lib_p": 85, "pen_p": 15, "fav": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"total": 22500.0, "lib_p": 78, "pen_p": 22, "fav": ["CARLOS LIMA: XML INVÁLIDO"]}
}

unidade = st.selectbox("Selecione a Unidade para Auditoria:", list(db.keys()))
dados = db[unidade]
v_liberado = dados["total"] * (dados["lib_p"] / 100)
v_pendente = dados["total"] * (dados["pen_p"] / 100)
hoje = datetime.now().strftime("%d/%m/%Y")

# 3. INTERFACE EM ABAS (ESTRUTURA COMPLETA)
tab_resumo, tab_barras, tab_relatorio = st.tabs(["📊 RESUMO PIZZA", "📈 BARRAS HORIZONTAL", "📄 RELATÓRIO TÉCNICO"])

# --- ABA 1: GRÁFICO PIZZA ---
with tab_resumo:
    st.subheader(f"Status: {unidade}")
    fig1 = go.Figure(data=[go.Pie(
        labels=[f'LIBERADO ({dados["lib_p"]}%)', f'PENDENTE ({dados["pen_p"]}%)'],
        values=[v_liberado, v_pendente],
        hole=.5,
        marker_colors=['#00d4ff', '#ff4b4b']
    )])
    fig1.update_layout(legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(fig1, use_container_width=True)

# --- ABA 2: GRÁFICO DE BARRAS HORIZONTAL ---
with tab_barras:
    st.subheader("Análise de Volume Financeiro")
    fig2 = go.Figure(go.Bar(
        x=[v_liberado, v_pendente],
        y=['LIBERADO', 'PENDENTE'],
        orientation='h',
        marker_color=['#00d4ff', '#ff4b4b'],
        text=[f"R$ {v_liberado:,.2f}", f"R$ {v_pendente:,.2f}"],
        textposition='auto'
    ))
    st.plotly_chart(fig2, use_container_width=True)

# --- ABA 3: RELATÓRIO E TABELA DA FAVELINHA ---
with tab_relatorio:
    st.markdown(f"""
    <div class="relatorio-folha">
        <h2 style="text-align:center;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
        <p style="text-align:center; font-size:12px;">SISTEMA SIDNEY ALMEIDA | IA-SENTINELA</p>
        <hr>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {hoje}</p>
        <p style="color:green;"><b>VALOR LIBERADO:</b> R$ {v_liberado:,.2f} ({dados['lib_p']}%)</p>
        <p style="color:red;"><b>VALOR PENDENTE:</b> R$ {v_pendente:,.2f} ({dados['pen_p']}%)</p>
        <br>
        <h4 style="border-bottom: 2px solid #f0f2f6;">🏘️ TABELA DA FAVELINHA (PENDÊNCIAS)</h4>
    """, unsafe_allow_html=True)
    
    for item in dados["fav"]:
        st.write(f"⚠️ {item}")
        
    st.markdown(f"""
        <br><br><br>
        <div style="text-align:center; border-top:1px solid black; width:250px; margin:auto;">
            <b>SIDNEY ALMEIDA</b><br><small>Diretor Operacional</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📱 PARA PDF: Clique nos 3 pontinhos do Chrome > Compartilhar > Imprimir.")
    
