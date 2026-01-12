import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO VISUAL PREMIUM ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #12171d; }
    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 10px; background: #1c232d; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 15px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1c232d; border-radius: 10px; padding: 5px; gap: 5px; }
    .stTabs [data-baseweb="tab"] { height: 45px; color: #8899A6; font-weight: bold; border: none !important; }
    .stTabs [aria-selected="true"] { background-color: #2c3645 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }

    /* Botão Gerar Relatório */
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #00d4ff, #008fb3);
        color: #12171d; font-weight: 900; border: none; height: 50px;
        border-radius: 10px; font-size: 1rem;
    }
    
    .report-card { background: #ffffff; color: #000000; padding: 20px; border-radius: 5px; font-family: 'Courier New', monospace; line-height: 1.2; }
    .data-card { background: #1c232d; padding: 15px; border-radius: 12px; border-left: 5px solid #00d4ff; margin-bottom: 10px; }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.1rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 BASE DE DADOS CONSOLIDADA ---
dados_medicos = {
    "ANIMA COSTA": {
        "valor": 16000.0, "pacientes_total": 85, "motivo": "Divergência de XML", "risco": 32,
        "detalhes": [["João Silva", "XML Inválido"], ["Maria Oliveira", "Divergência Tuss"]]
    },
    "DMMIGINIO GUERRA": {
        "valor": 22500.0, "pacientes_total": 110, "motivo": "Assinatura Digital", "risco": 68,
        "detalhes": [["João Souza", "Assinatura"], ["Ana Costa", "Assinatura"]]
    },
    "CLÍNICA SÃO JOSÉ": {
        "valor": 45000.0, "pacientes_total": 320, "motivo": "Erro Cadastral", "risco": 15,
        "detalhes": [["Carlos Luz", "CPF Inválido"], ["Bia Rosa", "Falta Guia"]]
    }
}

medico_sel = st.selectbox("Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[medico_sel]

# --- 📈 CÁLCULOS ---
p_risco = info["risco"]
p_ok = 100 - p_risco
v_liberado = info["valor"] * (p_ok / 100)
v_pendente = info["valor"] * (p_risco / 100)

tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICO", "📄 RELATÓRIO"])

with tab1:
    st.markdown(f"""
    <div class="data-card">
        <div style="color: #8899A6; font-size: 0.8rem;">FATURAMENTO ANALISADO</div>
        <div style="color: white; font-size: 1.5rem; font-weight: bold;">R$ {info['valor']:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)
    st.table(pd.DataFrame(info["detalhes"], columns=["Paciente", "Motivo"]))

with tab2:
    df_p = pd.DataFrame({'Status': ['LIBERADO', 'PENDENTE'], 'Perc': [p_ok, p_risco]})
    st.vega_lite_chart(df_p, {
        'width': 'container', 'height': 300,
        'mark': {'type': 'arc', 'innerRadius': 80, 'outerRadius': 120},
        'encoding': {
            'theta': {'field': 'Perc', 'type': 'quantitative'},
            'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}}
        }
    })

with tab3:
    st.subheader("📥 Dossiê Alpha de Auditoria")
    if st.button("📑 GERAR RELATÓRIO CONSOLIDADO"):
        
        # --- MONTAGEM DO TEXTO DO RELATÓRIO ---
        relatorio_texto = f"""
        ==========================================
        DOSSIÊ DE AUDITORIA - IA-SENTINELA PRO
        ==========================================
        MÉDICO/UNIDADE: {medico_sel}
        DATA DA EMISSÃO: 11/01/2026
        ------------------------------------------
        RESUMO FINANCEIRO:
        - Faturamento Total: R$ {info['valor']:,.2f}
        - Valor Liberado: R$ {v_liberado:,.2f} ({p_ok}%)
        - Valor em Risco: R$ {v_pendente:,.2f} ({p_risco}%)
        ------------------------------------------
        DETALHAMENTO DE PENDÊNCIAS:
        Principal Motivo: {info['motivo']}
        
        Lista de Pacientes:
        """
        for p, m in info["detalhes"]:
            relatorio_texto += f"\n - {p.ljust(20)} | Motivo: {m}"
            
        relatorio_texto += "\n------------------------------------------\nSTATUS: AGUARDANDO CORREÇÃO\n=========================================="

        st.markdown(f"**Relatório Pronto para Impressão:**")
        st.code(relatorio_texto, language="text") # Mostra na tela bonitinho
        
        st.download_button(
            label="⬇️ BAIXAR RELATÓRIO FINAL (PDF/TXT)",
            data=relatorio_texto,
            file_name=f"Relatorio_{medico_sel}_Consolidado.txt",
            mime="text/plain"
        )
        
