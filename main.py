import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E OCULTAÇÃO TOTAL DO TOPO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    /* Blindagem: Oculta Share, Star, Edit e GitHub */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header {visibility: hidden !important;} 
    footer {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0); height: 0px;}

    /* Design VIP Sentinela - Ajuste de Margens */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 15px; background: linear-gradient(90deg, #0e1117, #1c232d); 
        border-radius: 12px; border-left: 6px solid #00d4ff; margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 4px 10px; border-radius: 6px; font-weight: 900; font-size: 0.75rem; }
    [data-testid="stMetricValue"] { color: #00d4ff !important; font-size: 1.8rem !important; font-weight: 800; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.2rem; letter-spacing: 1px;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V26 - FINAL</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (VALORES FIXOS PARA SEGURANÇA) ---
dados_medicos = {
    "ANIMA COSTA": {
        "liberado": 13600.0,
        "pendente": 2400.0,
        "p_ok": 85,
        "p_pend": 15,
        "pacientes": [
            {"nome": "João Silva", "glosa": "XML Inválido", "valor": 1200.0},
            {"nome": "Maria Oliveira", "glosa": "Divergência Tuss", "valor": 1200.0}
        ]
    },
    "DMMIGINIO GUERRA": {
        "liberado": 17550.0,
        "pendente": 4950.0,
        "p_ok": 78,
        "p_pend": 22,
        "pacientes": [
            {"nome": "João Souza", "glosa": "Assinatura Digital", "valor": 1650.0},
            {"nome": "Ana Costa", "glosa": "Falta Assinatura", "valor": 1650.0},
            {"nome": "Carlos Luz", "glosa": "Bula Memória", "valor": 1650.0}
        ]
    }
}

# --- 3. INTERFACE OPERACIONAL ---
tab1, tab2, tab3 = st.tabs(["🏥 PAINEL", "📊 ANÁLISE", "📄 DOSSIÊ"])

with tab1:
    # Seletor de Doutor Sincronizado
    st.markdown("#### 🕵️ Seleção de Unidade")
    medico_sel = st.selectbox("Doutor Responsável:", list(dados_medicos.keys()))
    info = dados_medicos[medico_sel]

    st.markdown("---")
    
    # Exibição de Métricas Reais (Sem manipulação de slider)
    col_m1, col_m2 = st.columns(2)
    col_m1.metric(f"{info['p_ok']}% LIBERADO", f"R$ {info['liberado']:,.2f}")
    col_m2.metric(f"{info['p_pend']}% PENDENTE", f"R$ {info['pendente']:,.2f}", delta=f"-{info['p_pend']}%", delta_color="inverse")
    
    st.markdown("#### 📌 Lista de Pacientes")
    df_pacientes = pd.DataFrame([
        {"Paciente": p["nome"], "Motivo": p["glosa"], "Valor (R$)": f"R$ {p['valor']:,.2f}"} 
        for p in info["pacientes"]
    ])
    st.table(df_pacientes)

with tab2:
    st.markdown("#### 📊 Distribuição de Faturamento")
    # Gráfico Redimensionado para não cortar no celular
    source = pd.DataFrame({
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [info['p_ok'], info['p_pend']]
    })
    
    st.vega_lite_chart(source, {
        "width": "container", "height": 250,
        "mark": {"type": "arc", "innerRadius": 60, "outerRadius": 90, "stroke": "#0e1117", "strokeWidth": 2},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {"field": "Status", "type": "nominal", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
        },
        "view": {"stroke": None}
    })

with tab3:
    if st.button("🚀 GERAR RELATÓRIO"):
        txt_lista = "".join([f"- {p['nome']} ({p['glosa']}): R$ {p['valor']:,.2f}\n" for p in info["pacientes"]])
        relatorio = f"""
==========================================
   DOSSIÊ DE AUDITORIA - IA-SENTINELA 
==========================================
DOUTOR   : {medico_sel}
DATA     : 14/01/2026
------------------------------------------
LIBERADO : {info['p_ok']}% (R$ {info['liberado']:,.2f})
PENDENTE : {info['p_pend']}% (R$ {info['pendente']:,.2f})

DETALHAMENTO:
{txt_lista}
=========================================="""
        st.code(relatorio)
        st.download_button("⬇️ BAIXAR (.TXT)", relatorio.encode('utf-8-sig'), f"Sentinela_{medico_sel}.txt")
        
