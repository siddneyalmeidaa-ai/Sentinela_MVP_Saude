import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. CONFIGURAÇÃO DE TELA E CSS (LIMPO E SEM ERROS)
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .reportview-container { background: #0e1117; }
    
    /* CABEÇALHO SIDNEY ALMEIDA */
    .topo-sa {
        display: flex; align-items: center; gap: 15px;
        padding: 15px; background: #1c232d; border-radius: 10px; margin-bottom: 20px;
    }
    .logo-sa {
        background-color: #00d4ff; color: white; width: 45px; height: 45px;
        border-radius: 50%; display: flex; align-items: center; justify-content: center;
        font-weight: bold; font-size: 20px;
    }
    .titulo-sistema { color: white; font-size: 18px; font-weight: bold; margin: 0; }
    .sub-diretor { color: #00d4ff; font-size: 12px; font-weight: bold; text-transform: uppercase; }

    /* CARDS FINANCEIROS LADO A LADO */
    .card-resumo {
        background: white; padding: 15px; border-radius: 10px;
        text-align: center; border: 1px solid #ddd; color: #333;
    }
    .card-resumo small { font-weight: bold; color: #666; text-transform: uppercase; }
    .card-resumo h2 { margin: 5px 0; font-size: 22px; }

    /* FOLHA DE RELATÓRIO TÉCNICO */
    .folha-branca {
        background: white !important; color: black !important;
        padding: 30px !important; border-radius: 5px;
        border-top: 15px solid #00d4ff; font-family: sans-serif;
    }
    .favelinha-box {
        background: #f9f9f9; padding: 15px; border-radius: 5px;
        border: 1px solid #eee; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. TOPO DO SISTEMA (ESTILO IDENTIFICADO NOS PRINTS)
st.markdown("""
    <div class="topo-sa">
        <div class="logo-sa">SA</div>
        <div>
            <p class="titulo-sistema">IA-SENTINELA PRO</p>
            <p class="sub-diretor">SIDNEY PEREIRA DE ALMEIDA | DIRETOR OPERACIONAL</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. DADOS SINCRONIZADOS
db = {
    "ANIMA COSTA": {"total": 16000.0, "lib_p": 85, "pen_p": 15, "fav": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"total": 22500.0, "lib_p": 78, "pen_p": 22, "fav": ["CARLOS LIMA: XML INVÁLIDO", "ANA PAULA: LAUDO AUSENTE"]}
}

unidade = st.selectbox("Selecione a Unidade:", list(db.keys()))
d = db[unidade]
v_lib = d["total"] * (d["lib_p"] / 100)
v_pen = d["total"] * (d["pen_p"] / 100)

# 4. ABAS DE NAVEGAÇÃO
tab1, tab2, tab3 = st.tabs(["💰 VALORES", "📊 GRÁFICOS", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"### Auditoria: {unidade}")
    # Restaurando os cards lado a lado com o VALOR TOTAL aparecendo
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="card-resumo"><small>VALOR TOTAL</small><h2>R$ {d["total"]:,.2f}</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="card-resumo"><small style="color:green;">VALOR LIBERADO</small><h2 style="color:green;">R$ {v_lib:,.2f}</h2><p>{d["lib_p"]}%</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="card-resumo"><small style="color:red;">VALOR PENDENTE</small><h2 style="color:red;">R$ {v_pen:,.2f}</h2><p>{d["pen_p"]}%</p></div>', unsafe_allow_html=True)

with tab2:
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_p = go.Figure(data=[go.Pie(labels=['LIBERADO', 'PENDENTE'], values=[v_lib, v_pen], hole=.5, marker_colors=['#00d4ff', '#ff4b4b'])])
        st.plotly_chart(fig_p, use_container_width=True)
    with col_g2:
        fig_b = go.Figure(go.Bar(x=['LIBERADO', 'PENDENTE'], y=[v_lib, v_pen], marker_color=['#00d4ff', '#ff4b4b']))
        st.plotly_chart(fig_b, use_container_width=True)

with tab3:
    # Correção definitiva: a lista é formatada antes de entrar no Markdown
    itens_favelinha = "".join([f"<p style='margin:5px 0;'>• {paciente}</p>" for paciente in d["fav"]])
    
    st.markdown(f"""
    <div class="folha-branca">
        <h2 style="text-align:center;">RELATÓRIO TÉCNICO DE AUDITORIA</h2>
        <p style="text-align:center; font-size:12px; color:gray;">SISTEMA SIDNEY ALMEIDA | IA-SENTINELA</p>
        <hr>
        <p><b>UNIDADE:</b> {unidade} | <b>DATA:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
        <p style="color:green; font-size:18px;"><b>VALOR LIBERADO:</b> R$ {v_lib:,.2f}</p>
        <p style="color:red; font-size:18px;"><b>VALOR PENDENTE:</b> R$ {v_pen:,.2f}</p>
        
        <div class="favelinha-box">
            <b style="font-size:16px;">🏘️ TABELA DA FAVELINHA (DETALHAMENTO):</b>
            <div style="margin-top:10px;">
                {itens_favelinha}
            </div>
        </div>
        
        <br><br><br>
        <div style="text-align:center; border-top: 1px solid #ccc; width:250px; margin: auto; padding-top:10px;">
            <b>SIDNEY ALMEIDA</b><br>
            <small>Diretor Operacional</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
