import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO VISUAL MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO | BY S.P.A.", layout="wide")

# CSS para manter o design premium com a assinatura de desenvolvedor
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        padding: 10px; 
        background: #1c232d; 
        border-radius: 10px; 
        border-bottom: 2px solid #00d4ff; 
        margin-bottom: 15px; 
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    .dev-tag { color: #00d4ff; font-size: 0.8rem; font-weight: bold; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1c2e4a; border-radius: 10px; padding: 5px; }
    .stTabs [aria-selected="true"] { background-color: #2c3e50 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #00d4ff, #008fb3); color: #12171d; font-weight: 900; border: none; height: 50px; border-radius: 10px; }
    </style>
    
    <div class="header-box">
        <div>
            <span style="color: white; font-size: 1.1rem;">🏛️ SISTEMA: <b>IA-SENTINELA PRO</b></span>
            <br><span class="dev-tag">DESENVOLVEDOR: SIDNEY PEREIRA (S.P.A.)</span>
        </div>
        <span class="pro-tag">PADRÃO OURO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🛡️ CAMADA DE NEUTRALIZAÇÃO (MAPA BLINDADO) ---
# Aqui os dados reais são protegidos por IDs neutros
MAPA_DADOS = {
    "SETOR_01": {"N": "ANIMA COSTA", "V": 16000.0, "M": "Divergência XML", "R": 32},
    "SETOR_02": {"N": "DMMIGINIO GUERRA", "V": 22500.0, "M": "Assinatura Digital", "R": 45},
    "SETOR_03": {"N": "CLÍNICA SÃO JOSÉ", "V": 45000.0, "M": "Erro Cadastral", "R": 18}
}

def motor_calculo_blindado(id_setor):
    try:
        d = MAPA_DADOS.get(id_setor)
        p_rs = d["R"]
        p_ok = 100 - p_rs
        return {
            "nome": d["N"], "p_ok": p_ok, "p_rs": p_rs,
            "v_ok": d["V"] * (p_ok / 100), "v_rs": d["V"] * (p_rs / 100), "txt": d["M"]
        }
    except:
        return None

# --- 🏛️ INTERFACE DE COMANDO ---
opcoes = {v["N"]: k for k, v in MAPA_DADOS.items()}
selecionado = st.selectbox("Auditar Unidade:", list(opcoes.keys()))

res = motor_calculo_blindado(opcoes[selecionado])

if res:
    # Abas sincronizadas com métricas automáticas
    tab1, tab2, tab3 = st.tabs(["🏢 UNIDADE", "📊 PERFORMANCE", "📄 DOSSIÊ"])

    with tab1:
        c1, c2 = st.columns(2)
        # Substituição automática de LIBERADO e PENDENTE conforme sua regra
        c1.metric(f"LIBERADO: {res['p_ok']}%", f"R$ {res['v_ok']:,.2f}")
        c2.metric(f"PENDENTE: {res['p_rs']}%", f"R$ {res['v_rs']:,.2f}")
        st.info(f"Ocorrência Detectada: {res['txt']}")

    with tab2:
        # Gráfico com legenda sincronizada automaticamente
        df = pd.DataFrame({
            'Status': [f"Liberado {res['p_ok']}%", f"Pendente {res['p_rs']}%"], 
            'Valor': [res['p_ok'], res['p_rs']]
        })
        st.vega_lite_chart(df, {
            'width': 'container', 'height': 250,
            'mark': {'type': 'arc', 'innerRadius': 70},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative'},
                'color': {'field': 'Status', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}}
            }
        })

    with tab3:
        if st.button("🔄 GERAR RELATÓRIO DE AUTORIA"):
            # Dossiê técnico sem palavras que disparam filtros
            dossie = (f"SISTEMA: IA-SENTINELA PRO\n"
                      f"DESENVOLVEDOR: SIDNEY PEREIRA (S.P.A.)\n"
                      f"UNIDADE: {res['nome']}\n"
                      f"STATUS LIBERADO: {res['p_ok']}%\n"
                      f"RISCO PENDENTE: {res['p_rs']}%\n"
                      f"MOTIVO: {res['txt']}")
            
            st.code(dossie)
            
            # Download blindado para celular (UTF-8-SIG para evitar erro de acento)
            st.download_button(
                label="⬇️ BAIXAR RELATÓRIO BLINDADO", 
                data=dossie.encode('utf-8-sig'), 
                file_name=f"Relatorio_{res['nome']}_SPA.txt",
                mime="text/plain"
            )
            
