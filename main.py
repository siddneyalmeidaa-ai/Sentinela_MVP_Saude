import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. ESTILOS (MANTENDO O SEU PADRÃO)
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .topo-sa {
        display: flex; align-items: center; gap: 15px;
        padding: 15px; background: #1c232d; border-radius: 10px; margin-bottom: 20px;
    }
    .logo-sa {
        background-color: #00d4ff; color: white; width: 45px; height: 45px;
        border-radius: 50%; display: flex; align-items: center; justify-content: center;
        font-weight: bold; font-size: 20px;
    }
    .card-resumo {
        background: white; padding: 15px; border-radius: 10px;
        text-align: center; border: 1px solid #ddd; color: #333;
    }
    .folha-branca {
        background: white !important; color: black !important;
        padding: 30px !important; border-radius: 5px;
        border-top: 15px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO
st.markdown(f"""
    <div class="topo-sa">
        <div class="logo-sa">SA</div>
        <div>
            <p style="color:white; margin:0; font-weight:bold;">IA-SENTINELA PRO</p>
            <p style="color:#00d4ff; margin:0; font-size:12px;">SIDNEY PEREIRA DE ALMEIDA | DIRETOR OPERACIONAL</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. DADOS
db = {
    "ANIMA COSTA": {"total": 16000.0, "lib_p": 85, "pen_p": 15, "fav": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"total": 22500.0, "lib_p": 78, "pen_p": 22, "fav": ["CARLOS LIMA: XML INVÁLIDO", "ANA PAULA: LAUDO AUSENTE"]}
}

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
d = db[unidade]
v_lib = d["total"] * (d["lib_p"] / 100)
v_pen = d["total"] * (d["pen_p"] / 100)

tab1, tab2, tab3 = st.tabs(["💰 VALORES", "📊 GRÁFICOS", "📄 RELATÓRIO"])

# ABA 1: VALORES (CORRIGIDO PARA APARECER O TOTAL)
with tab1:
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="card-resumo"><small>VALOR TOTAL</small><h2>R$ {d["total"]:,.2f}</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="card-resumo"><small style="color:green;">LIBERADO</small><h2 style="color:green;">R$ {v_lib:,.2f}</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="card-resumo"><small style="color:red;">PENDENTE</small><h2 style="color:red;">R$ {v_pen:,.2f}</h2></div>', unsafe_allow_html=True)

# ABA 2: GRÁFICOS
with tab2:
    fig = go.Figure(data=[go.Pie(labels=['LIBERADO', 'PENDENTE'], values=[v_lib, v_pen], hole=.5, marker_colors=['#00d4ff', '#ff4b4b'])])
    st.plotly_chart(fig, use_container_width=True)

# ABA 3: RELATÓRIO (CORRIGIDO O ERRO DE EXIBIÇÃO DE CÓDIGO)
with tab3:
    # Geramos a lista de pacientes aqui
    lista_texto = ""
    for p in d["fav"]:
        lista_texto += f"<p style='margin:5px 0;'>• {p}</p>"

    st.markdown(f"""
    <div class="folha-branca">
        <h2 style="text-align:center;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
        <hr>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <p style="color:green;"><b>VALOR LIBERADO:</b> R$ {v_lib:,.2f}</p>
        <p style="color:red;"><b>VALOR PENDENTE:</b> R$ {v_pen:,.2f}</p>
        <br>
        <div style="background:#f9f9f9; padding:15px; border-radius:5px; border:1px solid #eee;">
            <b>🏘️ TABELA DA FAVELINHA:</b>
            {lista_texto}
        </div>
        <br><br>
        <div style="text-align:center; border-top:1px solid #ccc; width:250px; margin:auto; padding-top:10px;">
            <b>SIDNEY ALMEIDA</b><br><small>Diretor Operacional</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
