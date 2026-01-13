import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import random

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA | Projeto Faraó", layout="wide")
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

# --- 2. BASE DE DADOS (SERVIDOR SENTINELA) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. MOTOR PROJETO FARAÓ (AS 179 CRIANÇAS EM AÇÃO) ---
def motor_projeto_farao(unidade, msg_medico, status, valor):
    """Implementa a pirâmide de decisão das 179 IAs do Projeto Faraó."""
    msg_low = msg_medico.lower().strip()
    
    # Hierarquia de Saudação (Diplomacia)
    saudacoes = ["Olá", "Como vai", "Tudo bem", "Saudações"]
    validacao = [
        "é sempre um prazer falar com sua equipe",
        "sua produção é fundamental para nossa operação",
        "valorizamos muito sua dedicação nos plantões"
    ]
    
    # Núcleo da Resposta (Ação Faraó)
    if status == "RESTRIÇÃO":
        # Estratégia de Destravamento de Valor
        corpo = (
            f"identifiquei que o seu repasse de R$ {valor:,.2f} está temporariamente retido "
            "em uma 'trava de conformidade' por falta de arquivos XML. "
            "Para eu conseguir puxar seu pagamento para o lote prioritário e garantir seu fluxo agora, "
            "preciso apenas que confirme o reenvio desses documentos."
        )
    else:
        # Estratégia de Manutenção de Paz
        corpo = (
            f"verifiquei em tempo real que sua unidade está em CONFORMIDADE OK. "
            f"O valor de R$ {valor:,.2f} está seguindo o fluxo normal de processamento. "
            "Estou monitorando pessoalmente para garantir que o depósito ocorra sem qualquer burocracia."
        )

    # Delineado Final: Se for apenas saudação, a IA toma a frente (Proatividade)
    if len(msg_low) < 30:
        resposta_final = (f"{random.choice(saudacoes)}, {unidade}! {random.choice(validacao)}. "
                          f"Já me antecipei ao seu contato: {corpo} "
                          "Estou aqui para facilitar seu lado financeiro.")
    else:
        resposta_final = (f"{random.choice(saudacoes)}, {unidade}. {random.choice(validacao)}. "
                          f"Sobre seu ponto: {corpo} Conte comigo para destravar o que for necessário.")
        
    # Detecção de Urgência (Vácuo / IA-SENTINELA)
    urgencia = "ALTA (RISCO DE VÁCUO)" if any(x in msg_low for x in ["hoje", "agora", "urgente", "parar", "atraso"]) else "ESTÁVEL"
    return resposta_final, urgencia

# --- 4. AUDITORIA E RELATÓRIO (BARRIGUINHAS) ---
with st.expander("📊 Clique para Auditoria Geral de Valores"):
    st.metric("VALOR TOTAL CONSOLIDADO", f"R$ {df['valor'].sum():,.2f}")
    st.bar_chart(df.set_index("unidade")["valor"])

st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

st.divider()

# --- 5. CANAL DE COMUNICAÇÃO (PROJETO FARAÓ) ---
col_ia, col_hist = st.columns([1.2, 1])

with col_ia:
    st.subheader("📲 Canal de Comunicação Estratégica")
    unidade_atual = st.selectbox("Selecione o Médico/Unidade:", df['unidade'].tolist(), key="main_select")
    
    medico_info = df[df['unidade'] == unidade_atual].iloc[0]
    with st.expander(f"🔍 Auditoria Individual: {unidade_atual}"):
        st.write(f"Exposição Financeira: **R$ {medico_info['valor']:,.2f}**")
        st.write(f"Status no Servidor: **{medico_info['status']}**")

    texto_previo = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    questionamento = st.text_area(f"Mensagem de {unidade_atual}:", value=texto_previo, height=100, key=f"in_{unidade_atual}")
    
    if st.button("🚀 Ativar Projeto Faraó (Gerar Resposta Viva)"):
        if questionamento:
            viva, urg = motor_projeto_farao(unidade_atual, questionamento, medico_info['status'], medico_info['valor'])
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": datetime.now(fuso_br).strftime("%H:%M:%S"),
                "urgencia": urg,
                "entrada": questionamento,
                "resposta": viva
            }
            st.rerun()

    # Exibição do Parecer Estratégico
    if unidade_atual in st.session_state.memoria_unidades:
        atendimento = st.session_state.memoria_unidades[unidade_atual]
        st.success(f"**Parecer Sugerido (Urgência: {atendimento['urgencia']}):**\n\n{atendimento['resposta']}")
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(atendimento['resposta'])}"
        st.markdown(f'<a href="{link_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR VIA WHATSAPP</div></a>', unsafe_allow_html=True)

with col_hist:
    st.subheader("🧠 Registro de Auditoria (Projeto Embrião)")
    if unidade_atual in st.session_state.memoria_unidades:
        atendimento = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Status de Risco:** {atendimento['urgencia']}")
        st.info(f"🕒 **Última Interação:** {atendimento['data']}")
    else:
        st.write("Aguardando ativação das IAs.")

st.divider()
st.caption(f"Sidney Pereira de Almeida | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
