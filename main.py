import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. CONFIGURAÇÃO E BLINDAGEM VISUAL ---
st.set_page_config(page_title="IA-SENTINELA | Padrão Ouro", layout="wide")
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

# --- 2. BASE DE DADOS ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. AUDITORIA GERAL (A BARRIGUINHA QUE VOCÊ GOSTOU) ---
with st.expander("📊 Clique aqui para Auditoria Geral de Valores e Gráficos"):
    st.metric(label="💰 TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")
    st.bar_chart(df.set_index("unidade")["valor"])

# --- 4. RELATÓRIO ANALÍTICO DE ATIVOS ---
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

st.divider()

# --- 5. ÁREA OPERACIONAL E NOVA AUDITORIA INDIVIDUAL ---
col_ia, col_hist = st.columns([1.2, 1])

with col_ia:
    st.subheader("📲 Canal de Comunicação Estratégica")
    
    # Seletor Principal
    unidade_atual = st.selectbox("Selecione o Médico para Interação:", df['unidade'].tolist(), key="main_select")
    
    # --- NOVIDADE: AUDITORIA INDIVIDUALIZADA ---
    dados_medico = df[df['unidade'] == unidade_atual].iloc[0]
    with st.expander(f"🔍 Auditoria Individual: {unidade_atual}"):
        c1, c2 = st.columns(2)
        c1.metric("Exposição Financeira", f"R$ {dados_medico['valor']:,.2f}")
        c2.write(f"Status Atual: **{dados_medico['status']}**")
        # Gráfico focado apenas no doutor selecionado
        st.bar_chart(pd.DataFrame({unidade_atual: [dados_medico['valor']]}), color="#25D366")

    # Entrada de Texto Persistente
    texto_previo = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    questionamento = st.text_area(
        f"Mensagem recebida de {unidade_atual}:", 
        value=texto_previo,
        height=120,
        key=f"input_{unidade_atual}"
    )
    
    if st.button("🚀 Gerar Resposta e Sincronizar"):
        if questionamento:
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Identificação de Motivo
            motivo_id = "Financeiro" if "repasse" in questionamento.lower() else "Documentação"
            
            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo perfeitamente a sua frustração. "
                "Para que eu consiga destravar o valor agora e garantir a sua agenda, "
                "pode me confirmar apenas o reenvio dos arquivos XML?"
            )
            
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_id,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # WhatsApp
    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.success(f"**Parecer Sugerido:**\n\n{h['resposta']}")
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(h['resposta'])}"
        st.markdown(f'<a href="{link_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:10px;border-radius:5px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

with col_hist:
    st.subheader("🧠 Registro de Auditoria")
    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Motivo:** {h.get('motivo')}")
        st.info(f"🕒 **Última Interação:** {h.get('data')}")
        st.text_area("Histórico da Mensagem:", value=h.get('entrada'), height=100, disabled=True)
    else:
        st.write("Aguardando primeira interação com este médico.")

st.divider()
st.caption(f"Sidney Pereira de Almeida | Diretor de Compliance | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
