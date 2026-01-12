import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MOBILE MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    /* Cabeçalho Fixo */
    .header-box { display: flex; justify-content: space-between; align-items: center; padding: 5px 10px; color: #00d4ff; font-weight: bold; font-size: 0.9rem; border-bottom: 1px solid #1c2e4a; }
    .pro-tag { background-color: #00d4ff; color: #0e1117; font-size: 0.6rem; padding: 2px 5px; border-radius: 4px; font-weight: 900; }
    
    /* Ajuste de Container */
    .block-container { padding: 0.5rem 0.5rem !important; }
    header {visibility: hidden;}
    
    /* Estilização das Abas (Tabs) */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        height: 40px; 
        background-color: #1c2e4a; 
        border-radius: 5px; 
        color: white; 
        font-weight: bold;
        padding: 0px 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #00d4ff !important; color: #0e1117 !important; }

    /* Caixas de Status do Relatório */
    .status-box { padding: 12px; border-radius: 5px; margin-top: 8px; font-weight: bold; font-size: 0.9rem; text-align: center; }
    .status-ok { background-color: #15572422; color: #28a745; border: 1px solid #28a745; }
    .status-error { background-color: #721c2422; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
    
    <div class="header-box">
        <span>🏛️ CONTROLE: IA-SENTINELA</span> 
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML", "risco": 32},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Assinatura Digital", "risco": 68},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Erro Cadastral", "risco": 15}
}

# --- 🔍 SELETOR PRINCIPAL ---
medico_sel = st.selectbox("Selecione o Médico:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS ---
p_risco = info["risco"]
p_ok = 100 - p_risco
v_faturamento = info["valor"]
v_pendente = v_faturamento * (p_risco / 100)
v_liberado = v_faturamento * (p_ok / 100)

# --- 🕹️ NAVEGAÇÃO POR ABAS (AQUI OCORRE A MÁGICA) ---
aba_grafico, aba_relatorio = st.tabs(["📊 GRÁFICO", "📄 RELATÓRIO"])

with aba_grafico:
    st.write(f"**Análise Visual: {medico_sel}**")
    chart_data = pd.DataFrame({
        'Status': ['LIBERADO', 'PENDENTE'],
        'Percentual': [p_ok, p_risco]
    })
    
    st.vega_lite_chart(chart_data, {
        'width': 'container', 'height': 250,
        'mark': {'type': 'arc', 'innerRadius': 60, 'outerRadius': 100},
        'encoding': {
            'theta': {'field': 'Percentual', 'type': 'quantitative'},
            'color': {
                'field': 'Status', 
                'type': 'nominal', 
                'scale': {'range': ['#00d4ff', '#ff4b4b']},
                'legend': {'orient': 'bottom', 'labelColor': 'white'}
            }
        }
    })
    st.info(f"O gráfico acima representa {p_ok}% de conformidade.")

with aba_relatorio:
    st.write(f"**Dossiê de Auditoria: {medico_sel}**")
    
    # Caixas de Valor
    st.markdown(f'<div class="status-box status-ok">VALOR LIBERADO: R$ {v_liberado:,.2f} ({p_ok}%)</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="status-box status-error">VALOR PENDENTE: R$ {v_pendente:,.2f} ({p_risco}%)</div>', unsafe_allow_html=True)
    
    # Detalhes Técnicos
    st.write("---")
    st.write(f"**Motivo do Bloqueio:** {info['motivo']}")
    st.write(f"**Volume de Pacientes:** {info['pacientes']}")
    st.write(f"**Faturamento Bruto:** R$ {v_faturamento:,.2f}")
    
