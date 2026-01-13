import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import random

# --- 1. CONFIGURAÇÃO E BLINDAGEM VISUAL ---
st.set_page_config(page_title="IA-SENTINELA | Projeto Embrião", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarCollapsedControl"] {display: none;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 0rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS SINCRONIZADA ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. MOTOR DE DECISÃO "PROJETO EMBRIÃO" (ORGANISMO VIVO) ---
def motor_projeto_embriao(unidade, mensagem_medico, status_financeiro):
    """Lógica viva que alterna o tom e a estratégia com base no contexto."""
    msg_low = mensagem_medico.lower()
    
    # 1. Identificação de Urgência (Vácuo / Zona de Morte)
    urgencia = "ALTA" if any(w in msg_low for w in ["hoje", "agora", "parar", "agenda"]) else "NORMAL"
    
    # 2. Variáveis de Contexto (O 'DNA' da resposta)
    saudacoes = ["Olá", "Prezado", "Bom dia", "Tudo bem"]
    empatia = [
        "entendo sua preocupação com o repasse",
        "valorizamos muito sua parceria conosco",
        "estou ciente da importância desse fluxo para sua agenda"
    ]
    
    # 3. Decisão Viva (Não padronizada)
    if status_financeiro == "RESTRIÇÃO":
        acao = "precisamos apenas validar o XML final para liberar o pagamento no lote extra."
    else:
        acao = "o sistema já está processando sua conformidade para o próximo ciclo."

    fechamento = [
        "Estou acompanhando pessoalmente.",
        "Vou priorizar seu caso na mesa de auditoria.",
        "Qualquer dúvida, conte comigo diretamente."
    ]

    # Montagem Dinâmica (Organismo Vivo)
    corpo = f"{random.choice(saudacoes)}, {unidade}. {random.choice(empatia)}. No momento, {acao} {random.choice(fechamento)}"
    return corpo, urgencia

# --- 4. INTERFACE OPERACIONAL ---
with st.expander("📊 Auditoria Geral (Barriguinha)"):
    st.metric(label="💰 TOTAL EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")
    st.bar_chart(df.set_index("unidade")["valor"])

st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

st.divider()

col_ia, col_hist = st.columns([1.2, 1])

with col_ia:
    st.subheader("📲 Canal de Comunicação Estratégica")
    unidade_atual = st.selectbox("Selecione o Médico:", df['unidade'].tolist(), key="main_select")
    
    # Auditoria Individual Individualizada
    dados_medico = df[df['unidade'] == unidade_atual].iloc[0]
    with st.expander(f"🔍 Auditoria Individual: {unidade_atual}"):
        st.write(f"Valor em Risco: **R$ {dados_medico['valor']:,.2f}**")
        st.write(f"Veredito: **{dados_medico['status']}**")

    # Entrada do questionamento
    texto_previo = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    questionamento = st.text_area(f"Mensagem de {unidade_atual}:", value=texto_previo, height=120, key=f"in_{unidade_atual}")
    
    if st.button("🚀 Ativar Projeto Embrião (Gerar Resposta Viva)"):
        if questionamento:
            # A IA decide aqui o que falar
            resposta_viva, nivel_urgencia = motor_projeto_embriao(unidade_atual, questionamento, dados_medico['status'])
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "urgencia": nivel_urgencia,
                "entrada": questionamento,
                "resposta": resposta_viva
            }
            st.rerun()

    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.success(f"**Parecer Sugerido (Urgência: {h['urgencia']}):**\n\n{h['resposta']}")
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(h['resposta'])}"
        st.markdown(f'<a href="{link_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR VIA WHATSAPP</div></a>', unsafe_allow_html=True)

with col_hist:
    st.subheader("🧠 Registro de Auditoria")
    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Status de Urgência:** {h.get('urgencia')}")
        st.info(f"🕒 **Última Interação:** {h.get('data')}")
        st.text_area("Entrada original:", value=h.get('entrada'), height=80, disabled=True)
    else:
        st.write("Sem registros.")

st.divider()
st.caption(f"Sidney Pereira de Almeida | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
    
