import streamlit as st
import plotly.graph_objects as go

# 1. CONFIGURAÇÃO DE ESTÉTICA E DESIGN (INTERFACE LIMPA)
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
        font-family: sans-serif;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO PERSONALIZADO
st.markdown("""
    <div class="main-header">
        <h2 style='margin:0;'>SIDNEY PEREIRA DE ALMEIDA</h2>
        <p style='margin:0; color:#00d4ff; font-weight:bold;'>DIRETOR OPERACIONAL | IA-SENTINELA PRO</p>
    </div>
    """, unsafe_allow_html=True)

# 3. BASE DE DADOS (Drs. e Unidades)
unidades = {
    "ANIMA COSTA": {"liberado": 85, "pendente": 15},
    "DMMIGINIO GUERRA": {"liberado": 78, "pendente": 22},
    "DR. EXEMPLO 03": {"liberado": 92, "pendente": 8}
}

# 4. CRIAÇÃO DAS ABAS (UMA PARA CADA GRÁFICO)
abas = st.tabs([f"📊 {nome}" for nome in unidades.keys()])

# 5. GERADOR DE GRÁFICOS POR ABA
for i, nome_unidade in enumerate(unidades.keys()):
    with abas[i]:
        dados = unidades[nome_unidade]
        p_lib = dados["liberado"]
        p_pen = dados["pendente"]
        
        # Criando o Gráfico de Rosca com Terminologia Correta
        fig = go.Figure(data=[go.Pie(
            labels=[f'LIBERADO ({p_lib}%)', f'PENDENTE ({p_pen}%)'],
            values=[p_lib, p_pen],
            hole=.6,
            marker_colors=['#00d4ff', '#ff4b4b'], # Azul e Vermelho
            textinfo='label'
        )])

        fig.update_layout(
            title=dict(text=f"AUDITORIA: {nome_unidade}", font=dict(size=20)),
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            margin=dict(t=50, b=50, l=0, r=0),
            annotations=[dict(text='SPA', x=0.5, y=0.5, font_size=24, showarrow=False, font_color="#1c232d")]
        )

        st.plotly_chart(fig, use_container_width=True)

# 6. RODAPÉ TÉCNICO
st.markdown("<hr><p style='text-align:center; color:gray;'>Sistema Sincronizado para Dispositivos Móveis</p>", unsafe_allow_html=True)
