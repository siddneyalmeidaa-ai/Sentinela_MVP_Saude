import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. CONFIGURAÇÃO DE DESIGN (DISCRETO E PROFISSIONAL)
st.set_page_config(page_title="SISTEMA SA", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .topo-discreto {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 10px;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }
    .logo-sa {
        background-color: #00d4ff;
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 18px;
    }
    .nome-discreto {
        color: #555;
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
    }
    .card-valor {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        background-color: #f8f9fa;
        border: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. TOPO DISCRETO (LOGO E NOME)
st.markdown("""
    <div class="topo-discreto">
        <div class="logo-sa">SA</div>
        <div class="nome-discreto">Sidney Pereira de Almeida - Diretor Operacional</div>
    </div>
    """, unsafe_allow_html=True)

# 3. BASE DE DADOS E FILTRO
db = {
    "ANIMA COSTA": {"total": 16000.0, "lib_p": 85, "pen_p": 15, "fav": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"total": 22500.0, "lib_p": 78, "pen_p": 22, "fav": ["CARLOS LIMA: XML INVÁLIDO"]}
}

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
dados = db[unidade]
v_lib = dados["total"] * (dados["lib_p"] / 100)
v_pen = dados["total"] * (dados["pen_p"] / 100)

# 4. INTERFACE POR ABAS
tab1, tab2, tab3 = st.tabs(["💰 VALORES", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"### Auditoria Financeira: {unidade}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="card-valor"><b>VALOR TOTAL</b><br><h2 style="color:#1c232d;">R$ {dados["total"]:,.2f}</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="card-valor"><b>LIBERADO</b><br><h2 style="color:green;">R$ {v_lib:,.2f}</h2><small>{dados["lib_p"]}%</small></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card-valor"><b>PENDENTE</b><br><h2 style="color:red;">R$ {v_pen:,.2f}</h2><small>{dados["pen_p"]}%</small></div>', unsafe_allow_html=True)

with tab2:
    col_a, col_b = st.columns(2)
    with col_a:
        fig_p = go.Figure(data=[go.Pie(labels=['LIBERADO', 'PENDENTE'], values=[v_lib, v_pen], hole=.5, marker_colors=['#00d4ff', '#ff4b4b'])])
        fig_p.update_layout(title="Proporção %", showlegend=False)
        st.plotly_chart(fig_p, use_container_width=True)
    with col_b:
        fig_b = go.Figure(go.Bar(x=['LIBERADO', 'PENDENTE'], y=[v_lib, v_pen], marker_color=['#00d4ff', '#ff4b4b']))
        fig_b.update_layout(title="Volumes R$")
        st.plotly_chart(fig_b, use_container_width=True)

with tab3:
    st.markdown(f"""
    <div style="background:white; padding:20px; border:1px solid #ddd;">
        <h3 style="text-align:center;">RELATÓRIO TÉCNICO DE AUDITORIA</h3>
        <hr>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <p><b>VALOR LIBERADO:</b> R$ {v_lib:,.2f}</p>
        <p><b>VALOR PENDENTE:</b> R$ {v_pen:,.2f}</p>
        <br>
        <b>🏘️ TABELA DA FAVELINHA (PENDÊNCIAS):</b>
    """, unsafe_allow_html=True)
    for f in dados["fav"]:
        st.write(f"- {f}")
    st.markdown("</div>", unsafe_allow_html=True)
    
