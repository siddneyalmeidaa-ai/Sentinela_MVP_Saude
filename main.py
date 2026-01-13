import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. CONFIGURAÇÃO DE FUSO E MEMÓRIA ---
st.set_page_config(page_title="IA-SENTINELA | Governança 2.0", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 15px; }
    .stTextArea textarea { background-color: #161B22; color: white; border: 1px solid #30363D; font-size: 16px; }
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

# --- 3. DASHBOARD DE GOVERNANÇA ---
st.title("🛡️ Sentinela: Governança & Mediação")
st.metric(label="📊 TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")

st.divider()

# --- 4. ÁREA DE INTERAÇÃO COM MÉDICO ---
col_dados, col_ia = st.columns([1, 1.2])

with col_dados:
    st.subheader("📋 Relatório de Ativos")
    st.table(df[["unidade", "valor", "status"]])
    
    st.subheader("🧠 Histórico Sincronizado")
    unidade_atual = st.selectbox("Selecione o Médico/Unidade:", df['unidade'].tolist())
    
    # Exibição do Histórico com o NOVO campo "MOTIVO"
    if unidade_atual in st.session_state.memoria_unidades:
        hist = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Motivo:** {hist['motivo']}")
        st.info(f"🕒 **Horário:** {hist['data']}")
    else:
        st.write("Sem registros para esta unidade hoje.")

with col_ia:
    st.subheader("😊 IA de Mediação Humanizada")
    
    # Campo 1: Recebimento do Questionamento
    questionamento = st.text_area(
        f"Mensagem recebida de {unidade_atual}:", 
        placeholder="Cole aqui o que o médico enviou...",
        height=150,
        key=f"input_area_{unidade_atual}" 
    )
    
    # Campo 2: Processamento com Identificação de Motivo
    if st.button("✨ Gerar Resposta e Identificar Motivo"):
        if questionamento:
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Lógica para identificar o Motivo automaticamente
            if "repasse" in questionamento.lower() or "pagamento" in questionamento.lower():
                motivo_identificado = "Reclamação de Repasse / Financeiro"
            elif "agenda" in questionamento.lower() or "cirurgia" in questionamento.lower():
                motivo_identificado = "Urgência de Agenda Médica"
            else:
                motivo_identificado = "Dúvida Técnica / Documentação"

            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo perfeitamente a sua frustração; após um plantão, "
                "a última coisa que você precisa é lidar com burocracia financeira. Valorizamos seu tempo. "
                "Para destravar o valor e garantir sua agenda, consegue me ajudar confirmando o envio dos XMLs? "
                "Estou acompanhando para mover para CONFORMIDADE OK imediatamente."
            )
            
            # Salva na memória com o Motivo
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_identificado,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # Campo 3: Envio e Visualização
    if unidade_atual in st.session_state.memoria_unidades:
        res = st.session_state.memoria_unidades[unidade_atual]['resposta']
        st.success(f"**Parecer Sugerido ({st.session_state.memoria_unidades[unidade_atual]['motivo']}):**")
        st.write(res)
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(res)}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                    🚀 ENVIAR PARA WHATSAPP ({unidade_atual})
                </div>
            </a>
        """, unsafe_allow_html=True)

st.divider()
st.caption(f"Sidney Pereira de Almeida | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
        
