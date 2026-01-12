import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO VISUAL MASTER ---
st.set_page_config(page_title="IA-SENTINELA PRO | BY S.P.A.", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .header-box { display: flex; justify-content: space-between; align-items: center; padding: 10px; background: #1c232d; border-radius: 10px; border-bottom: 2px solid #00d4ff; margin-bottom: 15px; }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    .dev-tag { color: #00d4ff; font-size: 0.8rem; font-weight: bold; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1c2e4a; border-radius: 10px; padding: 5px; }
    .stTabs [aria-selected="true"] { background-color: #2c3e50 !important; color: #00d4ff !important; border-bottom: 3px solid #00d4ff !important; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #00d4ff, #008fb3); color: #12171d; font-weight: 900; border: none; height: 50px; border-radius: 10px; }
    </style>
    <div class="header-box">
        <div>
            <span style="color: white; font-size: 1.1rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span>
            <br><span class="dev-tag">DESENVOLVEDOR: SIDNEY PEREIRA (S.P.A.)</span>
        </div>
        <span class="pro-tag">PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- 🛡️ CAMADA DE NEUTRALIZAÇÃO ---
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
    except: return None

# --- 🏛️ INTERFACE ---
opcoes = {v["N"]: k for k, v in MAPA_DADOS.items()}
selecionado = st.selectbox("Auditar Unidade:", list(opcoes.keys()))
res = motor_calculo_blindado(opcoes[selecionado])

if res:
    tab1, tab2, tab3 = st.tabs(["🏢 CLÍNICA", "📊 GRÁFICO", "📄 RELATÓRIO"])

    with tab1:
        c1, c2 = st.columns(2)
        c1.metric(f"{res['p_ok']}%", f"R$ {res['v_ok']:,.2f}")
        c2.metric(f"{res['p_rs']}%", f"R$ {res['v_rs']:,.2f}")
        st.info(f"Ocorrência: {res['txt']}")

    with tab2:
        df = pd.DataFrame({'S': [f"{res['p_ok']}%", f"{res['p_rs']}%"], 'P': [res['p_ok'], res['p_rs']]})
        st.vega_lite_chart(df, {
            'width': 'container', 'height': 250,
            'mark': {'type': 'arc', 'innerRadius': 70},
            'encoding': {
                'theta': {'field': 'P', 'type': 'quantitative'},
                'color': {'field': 'S', 'type': 'nominal', 'scale': {'range': ['#00d4ff', '#ff4b4b']}}
            }
        })

    with tab3:
        if st.button("🔄 GERAR DOSSIÊ BLINDADO"):
            # FORMATO ANTERIOR RESTAURADO COM NOME DO DESENVOLVEDOR
            dossie = f"ID: {opcoes[selecionado]}\nUNIDADE: {res['nome']}\nCONF: {res['p_ok']}%\nRISCO: {res['p_rs']}%\nMOTIVO: {res['txt']}\nDEV: SIDNEY PEREIRA (S.P.A.)"
            st.code(dossie)
            
            st.download_button(
                "⬇️ BAIXAR RELATÓRIO", 
                dossie.encode('utf-8-sig'), 
                file_name=f"Relatorio_{res['p_ok']}perc.txt"
            )
            
