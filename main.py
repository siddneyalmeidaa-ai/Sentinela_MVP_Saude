import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. DESIGN PROFISSIONAL E DISCRETO
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .topo-area {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 0;
        border-bottom: 1px solid #eee;
        margin-bottom: 20px;
    }
    .logo-sa {
        background-color: #1c232d;
        color: #00d4ff;
        width: 38px;
        height: 38px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }
    .sistema-nome { color: #1c232d; font-size: 18px; font-weight: bold; }
    .diretor-info { color: #888; font-size: 12px; margin-left: auto; }
    
    /* FOLHA DO RELATÓRIO - CONTENÇÃO TOTAL */
    .relatorio-folha {
        background-color: white !important;
        color: black !important;
        padding: 30px !important;
        border-top: 12px solid #00d4ff;
        border-radius: 4px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-family: 'Arial', sans-serif;
    }
    .favelinha-container {
        background-color: #f9f9f9;
        border-left: 5px solid #ff4b4b;
        padding: 15px;
        margin-top: 15px;
        border-radius: 4px;
    }
    .card-resumo {
        padding: 15px;
        border-radius: 8px;
        background: #f8f9fa;
        text-align: center;
        border: 1px solid #efefef;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. TOPO DISCRETO
st.markdown("""
    <div class="topo-area">
        <div class="logo-sa">SA</div>
        <span class="sistema-nome">IA-SENTINELA PRO</span>
        <span class="diretor-info">S. P. ALMEIDA - DIRETOR OPERACIONAL</span>
    </div>
    """, unsafe_allow_html=True)

# 3. BASE DE DADOS
db = {
    "ANIMA COSTA": {"total": 16000.0, "lib_p": 85, "pen_p": 15, "fav": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"total": 22500.0, "lib_p": 78, "pen_p": 22, "fav": ["CARLOS LIMA: XML INVÁLIDO", "ANA PAULA: LAUDO AUSENTE"]}
}

unidade = st.selectbox("Unidade:", list(db.keys()))
d = db[unidade]
v_lib = d["total"] * (d["lib_p"] / 100)
v_pen = d["total"] * (d["pen_p"] / 100)

# 4. INTERFACE EM ABAS
tab1, tab2, tab3 = st.tabs(["💰 VALORES", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"#### Resumo Financeiro: {unidade}")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="card-resumo"><small>VALOR TOTAL</small><br><b style="font-size:20px;">R$ {d["total"]:,.2f}</b></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="card-resumo"><small style="color:green;">VALOR LIBERADO</small><br><b style="font-size:20px; color:green;">R$ {v_lib:,.2f}</b></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="card-resumo"><small style="color:red;">VALOR PENDENTE</small><br><b style="font-size:20px; color:red;">R$ {v_pen:,.2f}</b></div>', unsafe_allow_html=True)

with tab2:
    fig = go.Figure(data=[go.Pie(labels=['LIBERADO', 'PENDENTE'], values=[v_lib, v_pen], hole=.5, marker_colors=['#00d4ff', '#ff4b4b'])])
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    # Construção da lista de pacientes garantindo que fique DENTRO da div
    lista_html = "".join([f"<li style='margin-bottom:8px;'>{paciente}</li>" for paciente in d["fav"]])
    
    st.markdown(f"""
    <div class="relatorio-folha">
        <h2 style="text-align:center; margin-bottom:5px;">RELATÓRIO DE AUDITORIA</h2>
        <p style="text-align:center; font-size:12px; color:gray; margin-top:0;">SISTEMA IA-SENTINELA | GESTÃO SIDNEY ALMEIDA</p>
        <hr>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        
        <div style="display: flex; justify-content: space-between; margin: 20px 0;">
            <div style="color:green;"><b>TOTAL LIBERADO:</b><br>R$ {v_lib:,.2f} ({d['lib_p']}%)</div>
            <div style="color:red; text-align:right;"><b>TOTAL PENDENTE:</b><br>R$ {v_pen:,.2f} ({d['pen_p']}%)</div>
        </div>

        <div class="favelinha-container">
            <h4 style="margin-top:0;">🏘️ TABELA DA FAVELINHA (DETALHAMENTO)</h4>
            <ul style="padding-left:20px; margin-bottom:0;">
                {lista_html}
            </ul>
        </div>
        
        <br><br>
        <div style="text-align:center; border-top:1px solid #eee; width:220px; margin: 30px auto 0 auto; padding-top:10px;">
            <b style="font-size:14px;">SIDNEY ALMEIDA</b><br>
            <small style="color:gray;">Diretor Operacional</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
