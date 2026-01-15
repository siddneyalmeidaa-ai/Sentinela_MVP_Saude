import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. DESIGN ORIGINAL RESTAURADO (DISCRETO E LADO A LADO)
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .topo-sa {
        display: flex; align-items: center; gap: 10px;
        padding: 10px; margin-bottom: 20px; border-bottom: 1px solid #333;
    }
    .logo-circulo {
        background-color: #1c232d; color: #00d4ff;
        width: 40px; height: 40px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center; font-weight: bold;
    }
    .card-resumo {
        padding: 15px; border-radius: 10px; background: #f8f9fa;
        text-align: center; border: 1px solid #ddd;
    }
    /* CORREÇÃO DO RELATÓRIO: TUDO DENTRO DA ÁREA BRANCA */
    .relatorio-folha {
        background-color: white !important; color: black !important;
        padding: 25px !important; border-top: 10px solid #00d4ff;
        border-radius: 8px; font-family: Arial, sans-serif;
        min-height: 500px; /* Garante espaço para a lista */
    }
    .lista-favelinha {
        margin-top: 20px; padding: 15px;
        background-color: #f1f1f1; border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO RESTAURADO
st.markdown("""
    <div class="topo-sa">
        <div class="logo-circulo">SA</div>
        <div>
            <b style='color:white;'>IA-SENTINELA PRO</b><br>
            <small style='color:gray;'>S. P. ALMEIDA - DIRETOR OPERACIONAL</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. BASE DE DADOS
db = {
    "ANIMA COSTA": {"total": 16000.0, "lib_p": 85, "pen_p": 15, "fav": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"total": 22500.0, "lib_p": 78, "pen_p": 22, "fav": ["CARLOS LIMA: XML INVÁLIDO", "ANA PAULA: LAUDO AUSENTE"]}
}

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
d = db[unidade]
v_lib = d["total"] * (d["lib_p"] / 100)
v_pen = d["total"] * (d["pen_p"] / 100)

# 4. ABAS SINCROZINADAS
tab_v, tab_g, tab_r = st.tabs(["💰 VALORES", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab_v:
    # Restaurado os cards pequenos lado a lado (conforme image.png 22:49)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="card-resumo"><small>VALOR TOTAL</small><h4>R$ {d["total"]:,.2f}</h4></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="card-resumo"><small style="color:green;">LIBERADO</small><h4 style="color:green;">R$ {v_lib:,.2f}</h4><small>{d["lib_p"]}%</small></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="card-resumo"><small style="color:red;">PENDENTE</small><h4 style="color:red;">R$ {v_pen:,.2f}</h4><small>{d["pen_p"]}%</small></div>', unsafe_allow_html=True)

with tab_g:
    col_a, col_b = st.columns(2)
    with col_a:
        fig_p = go.Figure(data=[go.Pie(labels=['LIBERADO', 'PENDENTE'], values=[v_lib, v_pen], hole=.5, marker_colors=['#00d4ff', '#ff4b4b'])])
        st.plotly_chart(fig_p, use_container_width=True)
    with col_b:
        fig_b = go.Figure(go.Bar(x=['LIBERADO', 'PENDENTE'], y=[v_lib, v_pen], marker_color=['#00d4ff', '#ff4b4b']))
        st.plotly_chart(fig_b, use_container_width=True)

with tab_r:
    # A lista agora é gerada dentro da div principal para não vazar
    pacientes_html = "".join([f"<p style='margin:5px 0;'>• {p}</p>" for p in d["fav"]])
    
    st.markdown(f"""
    <div class="relatorio-folha">
        <h3 style="text-align:center;">RELATÓRIO TÉCNICO DE AUDITORIA</h3>
        <hr>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <p style="color:green;"><b>VALOR LIBERADO:</b> R$ {v_lib:,.2f}</p>
        <p style="color:red;"><b>VALOR PENDENTE:</b> R$ {v_pen:,.2f}</p>
        
        <div class="lista-favelinha">
            <b>🏘️ TABELA DA FAVELINHA (PENDÊNCIAS):</b><br>
            {pacientes_html}
        </div>
        
        <br><br><br>
        <div style="text-align:center; border-top:1px solid #ccc; width:200px; margin:auto;">
            <b>SIDNEY ALMEIDA</b><br><small>Diretor Operacional</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
