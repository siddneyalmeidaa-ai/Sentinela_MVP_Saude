import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. CONFIGURAÇÃO DE FUSO E MEMÓRIA SEGURA ---
st.set_page_config(page_title="IA-SENTINELA | Padrão Ouro", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

# Inicializa memória se estiver vazia
if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 15px; }
    .stTextArea textarea { background-color: #161B22; color: white; border: 1px solid #30363D; font-size: 16px; }
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

# --- 3. DASHBOARD DE GOVERNANÇA ---
st.title("🛡️ Sentinela: Governança & Mediação")
st.metric(label="📊 TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")

st.divider()

# --- 4. ÁREA DE INTERAÇÃO COM MÉDICO SINCRONIZADA ---
col_dados, col_ia = st.columns([1, 1.2])

with col_dados:
    st.subheader("📋 Relatório de Ativos")
    st.table(df[["unidade", "valor", "status"]])
    
    st.subheader("🧠 Histórico Sincronizado")
    unidade_atual = st.selectbox("Selecione o Médico/Unidade:", df['unidade'].tolist())
    
    # TRATAMENTO DE ERRO (FIX KEYERROR): Verifica se a chave existe antes de acessar
    if unidade_atual in st.session_state.memoria_unidades:
        hist = st.session_state.memoria_unidades[unidade_atual]
        # Só exibe o motivo se ele tiver sido capturado
        motivo = hist.get('motivo', 'Motivo não registrado') 
        st.warning(f"📌 **Motivo:** {motivo}")
        st.info(f"🕒 **Horário:** {hist.get('data', '--:--')}")
    else:
        st.write("Sem registros recentes para esta unidade.")

with col_ia:
    st.subheader("😊 IA de Mediação Humanizada")
    
    # Campo 1: Recebimento (Sincronizado)
    questionamento = st.text_area(
        f"Mensagem recebida de {unidade_atual}:", 
        placeholder="Cole aqui o que o médico enviou...",
        height=150,
        key=f"input_area_{unidade_atual}" 
    )

    # Campo 2: Processamento e Classificação
    if st.button("✨ Gerar Resposta e Identificar Motivo"):
        if questionamento:
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Lógica de Classificação de Motivo
            if any(word in questionamento.lower() for word in ["repasse", "pagamento", "caiu", "dinheiro"]):
                motivo_identificado = "Reclamação de Repasse / Financeiro"
            elif any(word in questionamento.lower() for word in ["agenda", "cirurgia", "plantão"]):
                motivo_identificado = "Urgência de Agenda Médica"
            else:
                motivo_identificado = "Dúvida Técnica / Documentação"

            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo perfeitamente a sua frustração; após um plantão, "
                "a última coisa que você precisa é lidar com burocracia financeira. Valorizamos seu tempo. "
                "Para destravar o valor e garantir sua agenda, consegue me ajudar confirmando o envio dos XMLs? "
                "Estou acompanhando para mover para CONFORMIDADE OK imediatamente."
            )
            
            # SALVAMENTO SEGURO
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_identificado,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # Campo 3: Visualização do Parecer e WhatsApp
    if unidade_atual in st.session_state.memoria_unidades:
        res = st.session_state.memoria_unidades[unidade_atual]['resposta']
        motivo_badge = st.session_state.memoria_unidades[unidade_atual].get('motivo', 'Geral')
        st.success(f"**Parecer Sugerido ({motivo_badge}):**")
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
st.caption(f"Sidney Pereira de Almeida | Diretor de Compliance | {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
    
