import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import random

# --- 1. CONFIGURAÇÃO E BLINDAGEM VISUAL ---
st.set_page_config(page_title="IA-SENTINELA | Organismo Vivo", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 0.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (SERVIDOR) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. MOTOR VIVO (PROJETO EMBRIÃO) ---
def gerar_resposta_viva(unidade, msg_medico, status):
    saudacoes = ["Olá", "Tudo bem", "Prezado(a)"]
    empatia = [
        "compreendo a urgência sobre o repasse",
        "estou ciente da importância desse fluxo",
        "valorizamos sua atuação na ponta"
    ]
    acao = "precisamos validar o XML final" if status == "RESTRIÇÃO" else "o lote extra está em processamento"
    viva = f"{random.choice(saudacoes)}, {unidade}. {random.choice(empatia)}. No momento, {acao}. Estou acompanhando."
    urgencia = "ALTA" if any(x in msg_medico.lower() for x in ["hoje", "agora", "parar"]) else "NORMAL"
    return viva, urgencia

# --- 4. INTERFACE DE AUDITORIA (BARRIGUINHAS) ---
with st.expander("📊 Auditoria Geral de Valores"):
    st.metric("TOTAL EM AUDITORIA", f"R$ {df['valor'].sum():,.2f}")
    st.bar_chart(df.set_index("unidade")["valor"])

st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

st.divider()

# --- 5. CANAL ESTRATÉGICO SINCRONIZADO ---
col_ia, col_hist = st.columns([1.2, 1])

with col_ia:
    st.subheader("📲 Canal de Comunicação Estratégica")
    unidade_atual = st.selectbox("Selecione o Médico:", df['unidade'].tolist(), key="main_select")
    
    # Auditoria Individual (Barriguinha)
    medico_info = df[df['unidade'] == unidade_atual].iloc[0]
    with st.expander(f"🔍 Auditoria Individual: {unidade_atual}"):
        st.write(f"Exposição: **R$ {medico_info['valor']:,.2f}**")
        st.write(f"Veredito: **{medico_info['status']}**")

    # Input de Texto
    texto_previo = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    questionamento = st.text_area(f"Mensagem de {unidade_atual}:", value=texto_previo, height=120, key=f"in_{unidade_atual}")
    
    if st.button("🚀 Ativar Projeto Embrião (Gerar Resposta Viva)"):
        if questionamento:
            viva, urg = gerar_resposta_viva(unidade_atual, questionamento, medico_info['status'])
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": datetime.now(fuso_br).strftime("%H:%M:%S"),
                "urgencia": urg,
                "entrada": questionamento,
                "resposta": viva
            }
            st.rerun()

    # Exibição Protegida (Evita o KeyError)
    if unidade_atual in st.session_state.memoria_unidades:
        atendimento = st.session_state.memoria_unidades[unidade_atual]
        st.success(f"**Parecer Sugerido (Urgência: {atendimento['urgencia']}):**\n\n{atendimento['resposta']}")
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(atendimento['resposta'])}"
        st.markdown(f'<a href="{link_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

with col_hist:
    st.subheader("🧠 Registro de Auditoria")
    if unidade_atual in st.session_state.memoria_unidades:
        atendimento = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Status:** {atendimento['urgencia']}")
        st.info(f"🕒 **Horário:** {atendimento['data']}")
        st.caption(f"Entrada registrada: {atendimento['entrada'][:100]}...")
    else:
        st.write("Aguardando interação.")

st.divider()
st.caption(f"Sidney Pereira de Almeida | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
    
