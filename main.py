import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

# Link do seu logo (Substitua quando tiver o link oficial)
URL_LOGO = "https://cdn-icons-png.flaticon.com/512/3914/3914404.png" 

st.markdown(f"""
    <style>
    /* Ocultação total de sistema */
    [data-testid="stHeader"] {{display: none !important;}}
    #MainMenu {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
    
    /* Preenchimento do topo */
    .main .block-container {{padding-top: 0rem;}}

    /* BANNER DE IDENTIDADE: SIDNEY PEREIRA DE ALMEIDA */
    .brand-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 25px 10px;
        background: linear-gradient(180deg, #0e1117 0%, #1c232d 100%);
        border-bottom: 3px solid #00d4ff;
        margin-bottom: 20px;
    }}
    .logo-img {{
        width: 65px;
        margin-bottom: 12px;
        filter: drop-shadow(0px 0px 10px #00d4ff);
    }}
    .user-name {{
        color: white;
        font-family: 'Segoe UI', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    .system-sub {{
        color: #00d4ff;
        font-size: 0.75rem;
        font-weight: 900;
        letter-spacing: 3px;
        margin-top: 5px;
    }}
    </style>
    
    <div class="brand-container">
        <img src="{URL_LOGO}" class="logo-img">
        <div class="user-name">SIDNEY PEREIRA DE ALMEIDA</div>
        <div class="system-sub">DIRETOR OPERACIONAL | IA-SENTINELA</div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. MOTOR DE DADOS SINCRONIZADOS ---
dados_medicos = {
    "ANIMA COSTA": {
        "liberado": 13600.0, "pendente": 2400.0, "p_ok": 85, "p_pend": 15,
        "pacientes": [
            {"nome": "João Silva", "glosa": "XML Inválido", "valor": 1200.0},
            {"nome": "Maria Oliveira", "glosa": "Divergência Tuss", "valor": 1200.0}
        ]
    },
    "DMMIGINIO GUERRA": {
        "liberado": 17550.0, "pendente": 4950.0, "p_ok": 78, "p_pend": 22,
        "pacientes": [
            {"nome": "João Souza", "glosa": "Assinatura Digital", "valor": 1650.0},
            {"nome": "Ana Costa", "glosa": "Falta Assinatura", "valor": 1650.0},
            {"nome": "Carlos Luz", "glosa": "Bula Memória", "valor": 1650.0}
        ]
    }
}

# --- 3. CONTROLE DE NAVEGAÇÃO ---
medico_sel = st.selectbox("🎯 Selecione o Doutor para Análise:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

tab1, tab2, tab3 = st.tabs(["📋 AUDITORIA", "📊 PERFORMANCE", "📩 EXPORTAR"])

with tab1:
    # Métricas Fixas e Seguras
    c1, c2 = st.columns(2)
    c1.metric(f"{info['p_ok']}% LIBERADO", f"R$ {info['liberado']:,.2f}")
    c2.metric(f"{info['p_pend']}% PENDENTE", f"R$ {info['pendente']:,.2f}", delta=f"-{info['p_pend']}%", delta_color="inverse")
    
    st.markdown("---")
    st.markdown("#### 📌 Quadro de Glosas")
    df_p = pd.DataFrame([
        {"Paciente": p["nome"], "Motivo": p["glosa"], "Valor": f"R$ {p['valor']:,.2f}"} 
        for p in info["pacientes"]
    ])
    st.table(df_p)

with tab2:
    # Gráfico Donut Premium (Anti-Corte)
    st.markdown("#### 📊 Visão Geral do Faturamento")
    source = pd.DataFrame({
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [info['p_ok'], info['p_pend']]
    })
    
    st.vega_lite_chart(source, {
        "width": "container", "height": 260,
        "mark": {"type": "arc", "innerRadius": 65, "outerRadius": 100, "stroke": "#0e1117", "strokeWidth": 2},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {"field": "Status", "type": "nominal", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
        },
        "view": {"stroke": None}
    })

with tab3:
    # Relatório de Auditoria Padrão Ouro
    st.markdown("#### 📄 Gerar Dossiê Oficial")
    lista_txt = "".join([f"- {p['nome']} ({p['glosa']}): R$ {p['valor']:,.2f}\n" for p in info["pacientes"]])
    relatorio_final = f"""SISTEMA IA-SENTINELA PRO
RESPONSÁVEL: SIDNEY PEREIRA DE ALMEIDA
UNIDADE: {medico_sel}
------------------------------------------
LIBERADO: {info['p_ok']}% (R$ {info['liberado']:,.2f})
PENDENTE: {info['p_pend']}% (R$ {info['pendente']:,.2f})

DETALHES:
{lista_txt}"""
    
    st.code(relatorio_final)
    st.download_button("⬇️ BAIXAR RELATÓRIO", relatorio_final.encode('utf-8-sig'), f"Relatorio_Sentinela_{medico_sel}.txt")
    
