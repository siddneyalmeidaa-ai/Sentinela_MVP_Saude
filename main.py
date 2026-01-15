import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. CONFIGURAÇÃO DE DESIGN (DISCRETO E PROFISSIONAL)
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    [data-testid="stHeader"] {display: none !important;}
    .topo-area {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 0;
        margin-bottom: 20px;
    }
    .logo-sa {
        background-color: #00d4ff;
        color: white;
        width: 35px;
        height: 35px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 16px;
    }
    .sistema-nome {
        color: #333;
        font-size: 18px;
        font-weight: bold;
        margin-right: 15px;
    }
    .diretor-info {
        color: #777;
        font-size: 12px;
        font-weight: normal;
    }
    .card-valor {
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        margin-bottom: 10px;
    }
    .card-valor h2 {
        margin: 5px 0;
        font-size: 24px;
    }
    .card-valor small {
        color: #666;
    }
    .relatorio-folha {
        background-color: white !important;
        color: black !important;
        padding: 25px !important;
        border-top: 10px solid #00d4ff;
        border-radius: 8px;
        font-family: Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. TOPO DO SISTEMA (LOGO, NOME DO SISTEMA E SEU NOME DISCRETO)
st.markdown("""
    <div class="topo-area">
        <div class="logo-sa">SA</div>
        <span class="sistema-nome">IA-SENTINELA PRO</span>
        <span class="diretor-info">Sidney Pereira de Almeida - Diretor Operacional</span>
    </div>
    """, unsafe_allow_html=True)

# 3. BASE DE DADOS E FILTRO DE UNIDADE
db = {
    "ANIMA COSTA": {"total": 16000.0, "lib_p": 85, "pen_p": 15, "fav": ["JOAO SILVA: FALTA ASSINATURA", "MARIA SOUZA: GUIA EXPIRADA"]},
    "DMMIGINIO GUERRA": {"total": 22500.0, "lib_p": 78, "pen_p": 22, "fav": ["CARLOS LIMA: XML INVÁLIDO", "ANA PAULA: LAUDO AUSENTE"]}
}

unidade_selecionada = st.selectbox("Selecione a Unidade para Auditoria:", list(db.keys()))
dados = db[unidade_selecionada]
valor_liberado = dados["total"] * (dados["lib_p"] / 100)
valor_pendente = dados["total"] * (dados["pen_p"] / 100)
data_atual = datetime.now().strftime("%d/%m/%Y")

# 4. INTERFACE EM ABAS: VALORES, GRÁFICOS, RELATÓRIO
tab_valores, tab_graficos, tab_relatorio = st.tabs(["💰 VALORES", "📊 GRÁFICOS", "📄 RELATÓRIO"])

# --- ABA 1: VALORES FINANCEIROS ---
with tab_valores:
    st.markdown(f"### Auditoria Financeira: {unidade_selecionada}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="card-valor"><b>VALOR TOTAL</b><br><h2 style="color:#1c232d;">R$ {dados["total"]:,.2f}</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="card-valor"><b>LIBERADO</b><br><h2 style="color:green;">R$ {valor_liberado:,.2f}</h2><small>{dados["lib_p"]}%</small></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card-valor"><b>PENDENTE</b><br><h2 style="color:red;">R$ {valor_pendente:,.2f}</h2><small>{dados["pen_p"]}%</small></div>', unsafe_allow_html=True)

# --- ABA 2: GRÁFICOS (PIZZA E BARRAS) ---
with tab_graficos:
    st.markdown(f"### Proporção de Auditoria: {unidade_selecionada}")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_pizza = go.Figure(data=[go.Pie(
            labels=[f'LIBERADO ({dados["lib_p"]}%)', f'PENDENTE ({dados["pen_p"]}%)'],
            values=[valor_liberado, valor_pendente],
            hole=.5,
            marker_colors=['#00d4ff', '#ff4b4b']
        )])
        fig_pizza.update_layout(title="Proporção Percentual", showlegend=False)
        st.plotly_chart(fig_pizza, use_container_width=True)
    with col_g2:
        fig_barras = go.Figure(go.Bar(
            x=['LIBERADO', 'PENDENTE'],
            y=[valor_liberado, valor_pendente],
            marker_color=['#00d4ff', '#ff4b4b']
        ))
        fig_barras.update_layout(title="Volumes Financeiros")
        st.plotly_chart(fig_barras, use_container_width=True)

# --- ABA 3: RELATÓRIO TÉCNICO (COM FAVELINHA) ---
with tab_relatorio:
    st.markdown(f"""
    <div class="relatorio-folha">
        <h3 style="text-align:center;">RELATÓRIO TÉCNICO DE AUDITORIA</h3>
        <hr>
        <p><b>UNIDADE:</b> {unidade_selecionada} | <b>DATA:</b> {data_atual}</p>
        <p style="color:green;"><b>VALOR LIBERADO:</b> R$ {valor_liberado:,.2f} ({dados['lib_p']}%)</p>
        <p style="color:red;"><b>VALOR PENDENTE:</b> R$ {valor_pendente:,.2f} ({dados['pen_p']}%)</p>
        <br>
        <h4 style="border-bottom: 1px solid #e9ecef; padding-bottom: 5px;">🏘️ TABELA DA FAVELINHA (PENDÊNCIAS)</h4>
    """, unsafe_allow_html=True)
    
    for item in dados["fav"]:
        st.write(f"• {item}")
        
    st.markdown(f"""
        <br><br>
        <div style="text-align:center; border-top:1px solid #ccc; width:200px; margin:auto; padding-top:10px;">
            <b>SIDNEY ALMEIDA</b><br><small>Diretor Operacional</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📱 Para gerar PDF: No seu celular, use 'Compartilhar' > 'Imprimir' > 'Salvar como PDF'.")

st.markdown("<hr><p style='text-align:center; color:#999; font-size:12px;'>Sistema Otimizado para Dispositivos Móveis</p>", unsafe_allow_html=True)
        
