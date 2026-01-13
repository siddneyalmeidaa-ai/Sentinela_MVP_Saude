import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. CONFIGURAÇÃO DE TEMPO REAL (BRASÍLIA) ---
st.set_page_config(page_title="IA-SENTINELA | Padrão Ouro", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

# Estilização para remover espaços e focar no conteúdo
st.markdown("""
    <style>
    .block-container { padding-top: 1.5rem; }
    .main { background-color: #0E1117; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (SERVIDOR EXECUTIVO) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. RELATÓRIO ANALÍTICO DE ATIVOS ---
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

st.divider()

# --- 4. CANAL DE COMUNICAÇÃO (CONTATO RÁPIDO) ---
col_ia, col_hist = st.columns([1.2, 1])

with col_ia:
    st.subheader("📲 Canal Oficial de Comunicação")
    
    unidade_atual = st.selectbox("Unidade Destino:", df['unidade'].tolist(), key="destino_select")
    
    texto_persistente = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    
    questionamento = st.text_area(
        f"Mensagem de {unidade_atual}:", 
        value=texto_persistente,
        placeholder="Cole o questionamento do médico aqui...",
        height=150,
        key=f"input_{unidade_atual}" 
    )
    
    if st.button("🚀 Gerar Resposta Estratégica"):
        if questionamento:
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Identificação de Motivo
            if any(w in questionamento.lower() for w in ["repasse", "pagamento", "caiu"]):
                motivo_id = "Financeiro"
            elif any(w in questionamento.lower() for w in ["agenda", "cirurgia"]):
                motivo_id = "Agenda"
            else:
                motivo_id = "Documentação"

            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo sua frustração após o plantão. "
                "Para que eu consiga destravar o valor e garantir sua agenda sem preocupações, "
                "consegue me ajudar confirmando o envio dos XMLs? Estou acompanhando pessoalmente."
            )
            
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_id,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # Botão de Envio para WhatsApp
    if unidade_atual in st.session_state.memoria_unidades:
        res = st.session_state.memoria_unidades[unidade_atual]['resposta']
        st.success("**Resposta Sugerida:**")
        st.write(res)
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(res)}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold;">
                    🚀 ENVIAR RESPOSTA VIA WHATSAPP
                </div>
            </a>
        """, unsafe_allow_html=True)

with col_hist:
    st.subheader("🧠 Registro de Auditoria")
    if unidade_atual in st.session_state.memoria_unidades:
        h = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Motivo:** {h.get('motivo')}")
        st.info(f"🕒 **Última Interação:** {h.get('data')}")
    else:
        st.write("Sem registros de contato hoje para esta unidade.")

st.divider()
st.caption(f"Sidney Pereira de Almeida | Diretor de Compliance | Brasília: {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
        
