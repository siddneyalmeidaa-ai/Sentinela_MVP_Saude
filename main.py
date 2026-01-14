import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E OCULTAÇÃO TOTAL DO CABEÇALHO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    /* Blindagem: Oculta Share, Star, Edit e GitHub no topo */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    header {visibility: hidden !important;} 
    footer {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0); height: 0px;}

    /* Design VIP Sentinela */
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 20px; background: linear-gradient(90deg, #0e1117, #1c232d); 
        border-radius: 15px; border-left: 6px solid #00d4ff; margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 4px 12px; border-radius: 6px; font-weight: 900; font-size: 0.8rem; }
    [data-testid="stMetricValue"] { color: #00d4ff !important; font-size: 2rem !important; font-weight: 800; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.4rem; letter-spacing: 1px;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V25 - PREMIUM</span>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (DADOS REAIS SINCRONIZADOS) ---
dados_medicos = {
    "ANIMA COSTA": {
        "faturamento": 16000.0,
        "pacientes": [
            {"nome": "João Silva", "glosa": "XML Inválido"},
            {"nome": "Maria Oliveira", "glosa": "Divergência Tuss"}
        ]
    },
    "DMMIGINIO GUERRA": {
        "faturamento": 22500.0,
        "pacientes": [
            {"nome": "João Souza", "glosa": "Assinatura Digital"},
            {"nome": "Ana Costa", "glosa": "Falta Assinatura"},
            {"nome": "Carlos Luz", "glosa": "Bula Memória"}
        ]
    }
}

# --- 3. INTERFACE OPERACIONAL (ABAS) ---
tab1, tab2, tab3 = st.tabs(["🏥 PAINEL DE CONTROLE", "📈 ANÁLISE GRÁFICA", "📄 DOSSIÊ FINAL"])

with tab1:
    st.subheader("🕵️ Seleção de Unidade")
    c_sel1, c_sel2 = st.columns([1, 1])
    
    with c_sel1:
        # Sincronização corrigida: O sistema agora lê a 'info' baseada nesta seleção
        medico_sel = st.selectbox("Doutor Responsável:", list(dados_medicos.keys()), key="sel_med")
        info = dados_medicos[medico_sel]
    
    with c_sel2:
        p_ok = st.slider("Porcentagem Liberada:", 0, 100, 85, key="slider_p")
        p_risco = 100 - p_ok

    st.markdown("---")
    
    # Cálculos Automáticos em Tempo Real
    v_total = info["faturamento"]
    v_liberado = v_total * (p_ok / 100)
    v_pendente = v_total * (p_risco / 100)
    valor_individual = v_pendente / len(info["pacientes"]) if info["pacientes"] else 0

    col_m1, col_m2 = st.columns(2)
    col_m1.metric(f"{p_ok}% LIBERADO", f"R$ {v_liberado:,.2f}")
    col_m2.metric(f"{p_risco}% PENDENTE", f"R$ {v_pendente:,.2f}", delta=f"-{p_risco}%", delta_color="inverse")
    
    st.markdown("#### 📌 Lista de Pacientes Auditados")
    # Gerando tabela dinâmica baseada no doutor selecionado
    df_pacientes = pd.DataFrame([
        {"Paciente": p["nome"], "Motivo": p["glosa"], "Glosa (R$)": f"R$ {valor_por_paciente:,.2f}" if 'valor_por_paciente' in locals() else f"R$ {valor_individual:,.2f}"} 
        for p in info["pacientes"]
    ])
    st.table(df_pacientes)

with tab2:
    st.subheader("📊 Performance de Auditoria")
    # Gráfico Donut Premium (Design Superior)
    source = pd.DataFrame({
        "Status": [f"LIBERADO ({p_ok}%)", f"PENDENTE ({p_risco}%)"],
        "Valor": [p_ok, p_risco],
        "Cor": ["#228B22", "#B22222"]
    })
    
    st.vega_lite_chart(source, {
        "width": 400, "height": 300,
        "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 110, "stroke": "#0e1117", "strokeWidth": 2},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {"field": "Status", "type": "nominal", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
        },
        "view": {"stroke": None}
    })

with tab3:
    if st.button("🚀 GERAR DOSSIÊ PADRÃO OURO"):
        txt_lista = "".join([f"- {p['nome']} ({p['glosa']}): R$ {valor_individual:,.2f}\n" for p in info["pacientes"]])
        relatorio = f"""
==========================================
   DOSSIÊ DE AUDITORIA - IA-SENTINELA 
==========================================
DOUTOR   : {medico_sel}
DATA     : 14/01/2026
------------------------------------------
LIBERADO : {p_ok}% (R$ {v_liberado:,.2f})
PENDENTE : {p_risco}% (R$ {v_pendente:,.2f})

DETALHAMENTO DE GLOSAS:
{txt_lista}
=========================================="""
        st.code(relatorio)
        st.download_button("⬇️ BAIXAR RELATÓRIO (.TXT)", relatorio.encode('utf-8-sig'), f"Sentinela_{medico_sel}.txt")
    
