import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO E LIMPEZA TOTAL DO TOPO ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

# Link do seu logo (Troque o link abaixo pelo link da sua imagem)
URL_LOGO = "https://cdn-icons-png.flaticon.com/512/3914/3914404.png" 

st.markdown(f"""
    <style>
    /* Oculta completamente a barra de sistema */
    [data-testid="stHeader"] {{display: none !important;}}
    #MainMenu {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
    
    /* Ajuste do container para preencher o espaço preto superior */
    .main .block-container {{padding-top: 0rem;}}

    /* BANNER DE MARCA PERSONALIZADO (Logo + Nome) */
    .brand-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px 10px;
        background: linear-gradient(180deg, #0e1117 0%, #1c232d 100%);
        border-bottom: 2px solid #00d4ff;
        margin-bottom: 20px;
    }}
    .logo-img {{
        width: 60px;
        margin-bottom: 10px;
        filter: drop-shadow(0px 0px 8px #00d4ff);
    }}
    .user-name {{
        color: white;
        font-family: 'Segoe UI', sans-serif;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .system-sub {{
        color: #00d4ff;
        font-size: 0.7rem;
        font-weight: 900;
        letter-spacing: 4px;
    }}
    </style>
    
    <div class="brand-container">
        <img src="{URL_LOGO}" class="logo-img">
        <div class="user-name">SIDNEY OLIVEIRA</div>
        <div class="system-sub">SISTEMA IA-SENTINELA PRO</div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (Sincronizada e Protegida) ---
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

# --- 3. INTERFACE OPERACIONAL ---
medico_sel = st.selectbox("🏥 Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

tab1, tab2, tab3 = st.tabs(["📊 PAINEL", "📈 GRÁFICO", "📄 RELATÓRIO"])

with tab1:
    # Métricas Reais
    c1, c2 = st.columns(2)
    c1.metric(f"{info['p_ok']}% LIBERADO", f"R$ {info['liberado']:,.2f}")
    c2.metric(f"{info['p_pend']}% PENDENTE", f"R$ {info['pendente']:,.2f}", delta=f"-{info['p_pend']}%", delta_color="inverse")
    
    st.markdown("---")
    st.markdown("#### 📌 Detalhamento da Auditoria")
    df_p = pd.DataFrame([
        {"Paciente": p["nome"], "Motivo": p["glosa"], "Valor": f"R$ {p['valor']:,.2f}"} 
        for p in info["pacientes"]
    ])
    st.table(df_p)

with tab2:
    # Gráfico Donut Redimensionado (Sem cortes no celular)
    st.markdown("#### 📊 Composição de Faturamento")
    source = pd.DataFrame({
        "Status": ["LIBERADO", "PENDENTE"],
        "Valor": [info['p_ok'], info['p_pend']]
    })
    
    st.vega_lite_chart(source, {
        "width": "container", "height": 240,
        "mark": {"type": "arc", "innerRadius": 60, "outerRadius": 95, "stroke": "#0e1117", "strokeWidth": 2},
        "encoding": {
            "theta": {"field": "Valor", "type": "quantitative"},
            "color": {"field": "Status", "type": "nominal", "scale": {"range": ["#00d4ff", "#ff4b4b"]}, "legend": {"orient": "bottom", "labelColor": "white"}}
        },
        "view": {"stroke": None}
    })

with tab3:
    # Relatório Gerado
    st.markdown("#### 📄 Dossiê de Auditoria")
    lista_txt = "".join([f"- {p['nome']} ({p['glosa']}): R$ {p['valor']:,.2f}\n" for p in info["pacientes"]])
    relatorio_final = f"SENTINELA PRO V28\nRESPONSÁVEL: {medico_sel}\nLIBERADO: {info['p_ok']}%\nPENDENTE: {info['p_pend']}%\n\nDETALHES:\n{lista_txt}"
    
    st.code(relatorio_final)
    st.download_button("⬇️ BAIXAR RELATORIO", relatorio_final.encode('utf-8-sig'), f"Auditoria_Sentinela.txt")
    
