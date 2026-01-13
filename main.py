import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. CONFIGURAÇÃO DE TEMPO REAL E OCULTAÇÃO DE INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA | Operacional", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

# CSS AVANÇADO: Oculta Sidebar, Menu, Cabeçalho e Ajusta o Topo
st.markdown("""
    <style>
    /* Oculta a barra lateral (sidebar) */
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarCollapsedControl"] {display: none;}
    
    /* Oculta o menu superior (três pontos) e o deploy */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Remove o espaço em branco do topo */
    .block-container { padding-top: 0rem; padding-bottom: 0rem; }
    
    /* Estilização de Tabelas e Áreas */
    .main { background-color: #0E1117; }
    div[data-testid="stTable"] { background-color: #161B22; border-radius: 10px; }
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

# --- 3. EXIBIÇÃO DO RELATÓRIO (DIRETO AO PONTO) ---
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

st.divider()

# --- 4. CANAL DE COMUNICAÇÃO SINCRONIZADO ---
col_ia, col_hist = st.columns([1.2, 1])

with col_ia:
    st.subheader("📲 Canal de Comunicação Estratégica")
    
    # Seletor de Unidade (O único controle necessário)
    unidade_atual = st.selectbox("Unidade para Atendimento:", df['unidade'].tolist(), key="atendimento_selector")
    
    # Memória por médico para não misturar mensagens
    texto_persistente = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    
    questionamento = st.text_area(
        f"Mensagem de {unidade_atual}:", 
        value=texto_persistente,
        placeholder="Cole a mensagem do médico aqui...",
        height=150,
        key=f"input_area_{unidade_atual}" 
    )
    
    if st.button("🚀 Gerar Resposta e Classificar"):
        if questionamento:
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Inteligência de Motivo
            if any(w in questionamento.lower() for w in ["repasse", "pagamento", "caiu"]):
                motivo_id = "Financeiro"
            elif any(w in questionamento.lower() for w in ["agenda", "cirurgia"]):
                motivo_id = "Agenda"
            else:
                motivo_id = "Documentação"

            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo sua frustração. "
                "Para destravar o valor e garantir sua agenda sem atrasos, "
                "consegue me ajudar confirmando o envio dos XMLs? Estou acompanhando pessoalmente."
            )
            
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_id,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # WhatsApp e Parecer
    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.success(f"**Parecer Sugerido ({h['motivo']}):**")
        st.write(h['resposta'])
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(h['resposta'])}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold;">
                    🚀 ENVIAR RESPOSTA PARA {unidade_atual}
                </div>
            </a>
        """, unsafe_allow_html=True)

with col_hist:
    st.subheader("🧠 Registro de Auditoria")
    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Motivo:** {h.get('motivo')}")
        st.info(f"🕒 **Horário (Brasília):** {h.get('data')}")
        st.text("Entrada original:")
        st.caption(h.get('entrada')[:150] + "...")
    else:
        st.write("Sem interações registradas para esta unidade.")

st.divider()
st.caption(f"Sidney Pereira de Almeida | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
        
