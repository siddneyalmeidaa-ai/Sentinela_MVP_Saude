import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO VISUAL PREMIUM ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #12171d; }
    /* Cabeçalho Neon */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 10px; background: #1c232d; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    
    /* Abas Customizadas Estilo App */
    .stTabs [data-baseweb="tab-list"] { background-color: #1c232d; border-radius: 10px; padding: 5px; gap: 5px; }
    .stTabs [data-baseweb="tab"] { 
        height: 45px; color: #8899A6; font-weight: bold; border: none !important;
    }
    .stTabs [aria-selected="true"] { background-color: #2c3645 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }

    /* Botão PDF Magnético */
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #00d4ff, #008fb3);
        color: #12171d; font-weight: 900; border: none; height: 55px;
        border-radius: 12px; font-size: 1rem; text-transform: uppercase;
        box-shadow: 0px 4px 15px rgba(0, 212, 255, 0.3);
    }
    
    /* Cartão de Dados */
    .data-card { background: #1c232d; padding: 15px; border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 10px; }
    .val-liberado { color: #28a745; font-size: 1.2rem; font-weight: bold; }
    .val-pendente { color: #ff4b4b; font-size: 1.2rem; font-weight: bold; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.1rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML", "risco": 32},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Assinatura Digital", "risco": 68},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Erro Cadastral", "risco": 15}
}

medico_sel = st.selectbox("Selecione a Unidade:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS ---
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

# --- 🕹️ NAVEGAÇÃO APP ---
tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICO", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"""
    <div class="data-card">
        <div style="color: #8899A6; font-size: 0.8rem;">FATURAMENTO BRUTO</div>
        <div style="color: white; font-size: 1.5rem; font-weight: bold;">R$ {info['valor']:,.2f}</div>
        <br>
        <div style="color: #8899A6; font-size: 0.8rem;">PACIENTES ATENDIDOS</div>
        <div style="color: white; font-size: 1.2rem;">{info['pacientes']} Unidades</div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("<h4 style='text-align: center; color: white;'>Análise de Risco Operacional</h4>", unsafe_allow_html=True)
    df_p = pd.DataFrame({'Status': ['LIBERADO', 'PENDENTE'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_p, {
        'width': 'container', 'height': 280,
        'mark': {'type': 'arc', 'innerRadius': 80, 'outerRadius': 120, 'cornerRadius': 10},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}, 'legend': {'orient': 'bottom', 'labelColor': 'white'}}
        }
    })

with tab3:
    st.markdown("### 📥 Central de Documentos")
    if st.button("⬇️ GERAR RELATÓRIO PDF"):
        st.success(f"O Relatório de {medico_sel} está sendo processado...")
        st.markdown(f"""
        <div class="data-card" style="border-left-color: #28a745;">
            <div style="color: #8899A6;">DOSSIÊ INTERNO: AUDITORIA FINAL</div>
            <div class="val-liberado">VALOR LIBERADO: R$ {v_liberado:,.2f} ({p_ok}%)</div>
            <div class="val-pendente">VALOR BLOQUEADO: R$ {v_pendente:,.2f} ({p_risco}%)</div>
            <hr style="border: 0.5px solid #2c3645;">
            <div style="color: white;"><b>MOTIVO:</b> {info['motivo']}</div>
        </div>
        """, unsafe_allow_html=True)
        # Aqui o usuário simula o download
        st.download_button("Clique aqui para baixar o PDF", "Dados do Relatório", file_name=f"Relatorio_{medico_sel}.txt")
    
