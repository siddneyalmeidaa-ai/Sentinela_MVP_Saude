import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz  # Biblioteca para gerenciar fuso horário

# --- 1. CONFIGURAÇÃO DE TEMPO REAL (BRASÍLIA) E MEMÓRIA ---
st.set_page_config(page_title="IA-SENTINELA | Sincronia Total", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo') # Trava o horário no Brasil

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 15px; }
    .stTextArea textarea { background-color: #161B22; color: white; border: 1px solid #30363D; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (DADOS SINCRONIZADOS) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. DASHBOARD EXECUTIVO ---
st.title("🛡️ Sentinela: Governança & Mediação")
st.metric(label="📊 TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")

st.divider()

# --- 4. ÁREA DE INTERAÇÃO COM HORÁRIO SINCRONIZADO ---
col_dados, col_ia = st.columns([1, 1.2])

with col_dados:
    st.subheader("📋 Relatório de Ativos")
    st.table(df[["unidade", "valor", "status"]])
    
    st.subheader("🧠 Histórico Sincronizado")
    unidade_atual = st.selectbox("Selecione o Médico/Unidade:", df['unidade'].tolist())
    
    # Exibição segura do histórico para evitar KeyError
    if unidade_atual in st.session_state.memoria_unidades:
        hist = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Motivo:** {hist.get('motivo', 'Motivo não registrado')}")
        st.info(f"🕒 **Horário (Brasília):** {hist.get('data', '--:--')}")
    else:
        st.write("Sem registros recentes para esta unidade.")

with col_ia:
    st.subheader("😊 IA de Mediação Humanizada")
    
    questionamento = st.text_area(
        f"Mensagem recebida de {unidade_atual}:", 
        placeholder="Cole aqui o que o médico enviou...",
        height=150,
        key=f"input_area_{unidade_atual}" 
    )
    
    if st.button("✨ Gerar Resposta e Identificar Motivo"):
        if questionamento:
            # Captura o horário exato de Brasília no momento do clique
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Lógica de Classificação de Motivo
            if any(word in questionamento.lower() for word in ["repasse", "pagamento", "caiu"]):
                motivo_identificado = "Reclamação de Repasse / Financeiro"
            elif any(word in questionamento.lower() for word in ["agenda", "cirurgia"]):
                motivo_identificado = "Urgência de Agenda Médica"
            else:
                motivo_identificado = "Dúvida Técnica / Documentação"

            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo perfeitamente a sua frustração; após um plantão, "
                "a última coisa que você precisa é lidar com burocracia financeira. Valorizamos seu tempo. "
                "Para destravar o valor e garantir sua agenda, consegue me ajudar confirmando o envio dos XMLs? "
                "Estou acompanhando para mover para CONFORMIDADE OK imediatamente."
            )
            
            # Salvamento seguro na memória
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_identificado,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # Campo de Visualização e Envio
    if unidade_atual in st.session_state.memoria_unidades:
        res = st.session_state.memoria_unidades[unidade_atual]['resposta']
        st.success(f"**Parecer Sugerido ({st.session_state.memoria_unidades[unidade_atual].get('motivo')}):**")
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
# Rodapé com a data e hora atualizada de Brasília
st.caption(f"Sidney Pereira de Almeida | Diretor de Compliance | Brasília: {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
        
