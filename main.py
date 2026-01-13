import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA QUÂNTICA (TRIFASE) ---
if 'memoria_sentinela' not in st.session_state:
    st.session_state.memoria_sentinela = []

# --- 2. MOTOR DE DADOS ---
db = [
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. INTERFACE EXECUTIVA ---
st.title("🛡️ Sentinela: Governança com Memória Tripla")
st.metric(label="📊 TOTAL EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")

st.divider()

col_a, col_b = st.columns([1, 1.2])

with col_a:
    st.subheader("🧠 Histórico de Conversas (Salvação Automática)")
    if st.session_state.memoria_sentinela:
        for m in reversed(st.session_state.memoria_sentinela):
            with st.expander(f"📌 {m['data']} - {m['unidade']}"):
                st.write(f"**Médico:** {m['entrada']}")
                st.write(f"**IA:** {m['resposta']}")
    else:
        st.info("Nenhuma interação registrada nesta sessão.")

with col_b:
    st.subheader("🤖 IA de Mediação Humanizada")
    unidade = st.selectbox("Unidade/Médico:", df['unidade'].tolist())
    
    # Simulação da reclamação do médico
    reclamacao_medico = (
        "Sidney, acabei de sair do plantão e vi que o repasse das minhas cirurgias "
        "ainda não caiu. Isso é um descaso com o meu tempo! Já enviei os prontuários "
        "e as guias assinadas. Preciso que libere esse valor de R$ 5.400,00 agora, "
        "senão não terei como manter minha agenda da próxima semana com vocês."
    )
    
    entrada = st.text_area("Mensagem Recebida:", value=reclamacao_medico, height=150)
    
    # Geração da Resposta Inteligente
    resposta_ia = (
        f"Olá, {unidade}. Entendo perfeitamente a sua frustração; após um plantão, "
        "a última coisa que você precisa é lidar com burocracia financeira. "
        "Para destravar o valor e garantir sua agenda, consegue me ajudar apenas com o reenvio dos XMLs? "
        "Estou acompanhando pessoalmente para mover para CONFORMIDADE OK imediatamente."
    )

    if st.button("✨ Gerar e Salvar na Memória"):
        st.success("**Resposta Humanizada Gerada:**")
        st.write(resposta_ia)
        
        # Salvação Automática na Memória do Sistema
        st.session_state.memoria_sentinela.append({
            "data": datetime.now().strftime("%H:%M:%S"),
            "unidade": unidade,
            "entrada": entrada,
            "resposta": resposta_ia
        })
        st.rerun() # Atualiza para mostrar no histórico na hora

    link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta_ia)}"
    st.link_button("🚀 Enviar para o WhatsApp", link_zap)
    
