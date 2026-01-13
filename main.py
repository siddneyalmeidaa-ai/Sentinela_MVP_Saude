import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. SETUP E MEMÓRIA QUÂNTICA (SESSION STATE) ---
st.set_page_config(page_title="IA-SENTINELA | Memória de Gestão", layout="wide")

# Inicializa o histórico se não existir (A Memória do Sistema)
if 'historico_interacoes' not in st.session_state:
    st.session_state.historico_interacoes = []

# --- 2. BASE DE DATA (SERVIDOR PADRÃO OURO) ---
db = [
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. INTERFACE E DASHBOARD ---
st.title("🛡️ Sentinela: Governança com Memória de Histórico")
st.metric(label="📊 TOTAL EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")

st.divider()

# --- 4. MÓDULO DE MEDIAÇÃO COM REGISTRO DE MEMÓRIA ---
col_a, col_b = st.columns([1, 1.2])

with col_a:
    st.subheader("📋 Status Atual das Unidades")
    st.table(df)
    
    # Exibição da Memória de Conversas
    st.subheader("🧠 Memória de Conversas (Histórico)")
    if st.session_state.historico_interacoes:
        for idx, item in enumerate(reversed(st.session_state.historico_interacoes)):
            with st.expander(f"📌 {item['data']} - {item['unidade']}"):
                st.write(f"**Médico enviou:** {item['entrada']}")
                st.write(f"**IA Respondeu:** {item['resposta']}")
    else:
        st.info("Nenhuma interação registrada nesta sessão.")

with col_b:
    st.subheader("🤖 IA de Mediação Humanizada")
    
    # Seleção de quem está falando para a Memória Quântica
    unidade_selecionada = st.selectbox("Selecione a Unidade/Médico:", df['unidade'].tolist())
    
    # Reclamação Simulada do Médico
    reclamacao_medico = (
        "Sidney, acabei de sair do plantão e vi que o repasse das minhas cirurgias "
        "ainda não caiu. Isso é um descaso com o meu tempo! Já enviei os prontuários "
        "e as guias assinadas. Preciso que libere esse valor de R$ 5.400,00 agora, "
        "senão não terei como manter minha agenda da próxima semana com vocês."
    )
    
    entrada = st.text_area("Mensagem Recebida:", value=reclamacao_medico, height=150)
    
    if st.button("✨ Gerar e Salvar na Memória"):
        # Resposta Humanizada de Alta Gestão
        resposta_final = (
            f"Olá, {unidade_selecionada}. Entendo perfeitamente a sua frustração; após um plantão, "
            "a última coisa que você precisa é lidar com burocracia financeira. Valorizamos muito o seu tempo. "
            "Para destravar o valor e garantir sua agenda, consegue me ajudar apenas com o reenvio dos XMLs? "
            "Estou acompanhando pessoalmente para mover para CONFORMIDADE OK imediatamente."
        )
        
        # Salvando na "Memória Quântica" da Sessão
        st.session_state.historico_interacoes.append({
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "unidade": unidade_selecionada,
            "entrada": entrada,
            "resposta": resposta_final
        })
        
        st.success("**Resposta Humanizada Gerada:**")
        st.write(resposta_final)
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta_final)}"
        st.link_button("🚀 Enviar e Registrar", link_zap)

st.caption("Sidney Pereira de Almeida | Gestão de Histórico e Compliance")
