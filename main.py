import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. CONFIGURAÇÃO DE TEMPO REAL E OCULTAÇÃO DE SIDEBAR ---
st.set_page_config(page_title="IA-SENTINELA | Operacional", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

# CSS para ocultar a Sidebar (Rádio/Área lateral) e Menus do topo
st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarCollapsedControl"] {display: none;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 0rem; }
    .main { background-color: #0E1117; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (DADOS DE DIRETORIA) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. AUDITORIA OCULTA (VALORES E GRÁFICOS EM EXPANDERS) ---
# Aqui os dados ficam guardados para não "encher" o cabeçalho
with st.expander("📊 Clique aqui para Auditoria de Valores e Gráficos"):
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💰 TOTAL CONSOLIDADO", value=f"R$ {df['valor'].sum():,.2f}")
    with col2:
        st.write("Gráfico de Risco por Unidade")
        st.bar_chart(df.set_index("unidade")["valor"])

# --- 4. RELATÓRIO ANALÍTICO (O QUE VOCÊ VÊ PRIMEIRO) ---
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

st.divider()

# --- 5. CANAL DE COMUNICAÇÃO E HISTÓRICO SINCRONIZADO ---
col_ia, col_hist = st.columns([1.2, 1])

with col_ia:
    st.subheader("📲 Canal de Comunicação Estratégica")
    
    # Seletor que sincroniza TUDO abaixo
    unidade_atual = st.selectbox("Selecione o Médico para Interação:", df['unidade'].tolist(), key="main_select")
    
    # Persistência de texto por unidade
    texto_persistente = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    
    questionamento = st.text_area(
        f"Mensagem de {unidade_atual}:", 
        value=texto_persistente,
        height=150,
        key=f"input_{unidade_atual}" # Chave dinâmica evita erro de duplicidade
    )
    
    if st.button("🚀 Gerar Resposta e Salvar na Memória"):
        if questionamento:
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Inteligência de Motivo Automática
            if any(w in questionamento.lower() for w in ["repasse", "pagamento", "caiu"]):
                motivo_id = "Financeiro"
            elif any(w in questionamento.lower() for w in ["agenda", "cirurgia"]):
                motivo_id = "Agenda / Operacional"
            else:
                motivo_id = "Documentação"

            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo sua frustração. "
                "Para que eu consiga destravar o valor e garantir sua agenda sem atrasos, "
                "consegue me ajudar confirmando o envio dos XMLs? Estou acompanhando pessoalmente."
            )
            
            # Salva na Memória Sincronizada
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_id,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.success("**Parecer Sugerido:**")
        st.write(h['resposta'])
        
        # WhatsApp com correção de acentos (urllib) [cite: 2026-01-12]
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(h['resposta'])}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold;">
                    🚀 ENVIAR VIA WHATSAPP
                </div>
            </a>
        """, unsafe_allow_html=True)

with col_hist:
    st.subheader("🧠 Registro de Auditoria")
    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Motivo Identificado:** {h.get('motivo')}")
        st.info(f"🕒 **Horário (Brasília):** {h.get('data')}")
        st.text("Última entrada recebida:")
        st.caption(h.get('entrada')[:200] + "...")
    else:
        st.write("Sem interações registradas para esta unidade hoje.")

st.divider()
# Rodapé com horário travado em Brasília para auditoria
st.caption(f"Sidney Pereira de Almeida | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
        
