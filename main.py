import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. SETUP DE SEGURANÇA E MEMÓRIA QUÂNTICA (TRIFASE) ---
st.set_page_config(page_title="IA-SENTINELA | Padrão Ouro", layout="wide")

# Inicialização da Memória de Longo Prazo da Sessão
if 'memoria_sentinela' not in st.session_state:
    st.session_state.memoria_sentinela = []

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 15px; }
    .stTextArea textarea { background-color: #161B22; color: white; border: 1px solid #30363D; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS ESTRATÉGICA (SERVIDOR EXECUTIVO) ---
# Aqui os dados são sincronizados com os status de Conformidade
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)
total_geral = df["valor"].sum()

# --- 3. DASHBOARD DE GOVERNANÇA DE RECEITA ---
st.title("🛡️ Governança de Receita | IA-SENTINELA")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_geral:,.2f}")

st.divider()

# --- 4. GRÁFICO DE PERFORMANCE (CORREÇÃO DEFINITIVA DE ESCALA) ---
# Garantindo que as barras apareçam do zero para todas as unidades
st.subheader("📈 Performance e Risco por Unidade")
df_chart = df.copy()
df_chart['Em Conformidade'] = df_chart.apply(lambda x: x['valor'] if x['status'] == 'CONFORMIDADE OK' else 0, axis=1)
df_chart['Em Restrição/Análise'] = df_chart.apply(lambda x: x['valor'] if x['status'] != 'CONFORMIDADE OK' else 0, axis=1)

chart_data = df_chart.set_index("unidade")[['Em Conformidade', 'Em Restrição/Análise']]
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"]) # Verde para OK, Vermelho para Risco

# --- 5. MÓDULO DE INTERAÇÃO E MEMÓRIA DE HISTÓRICO ---
st.divider()
col_hist, col_ia = st.columns([1, 1.2])

with col_hist:
    st.subheader("🧠 Histórico de Conversas (Salvação Automática)")
    if st.session_state.memoria_sentinela:
        for m in reversed(st.session_state.memoria_sentinela):
            with st.expander(f"📌 {m['data']} - {m['unidade']}"):
                st.write(f"**Médico:** {m['entrada']}")
                st.write(f"**IA:** {m['resposta']}")
    else:
        st.info("Nenhuma interação registrada nesta sessão.")

with col_ia:
    st.subheader("😊 IA de Mediação Humanizada")
    
    unidade_alvo = st.selectbox("Selecione a Unidade/Médico para Interação:", df['unidade'].tolist())
    
    # Reclamação do Médico (Padrão para Teste de Estresse)
    msg_medico = (
        "Sidney, acabei de sair do plantão e vi que o repasse das minhas cirurgias "
        "ainda não caiu. Isso é um descaso com o meu tempo! Já enviei os prontuários "
        "e as guias assinadas. Preciso que libere esse valor de R$ 5.400,00 agora, "
        "senão não terei como manter minha agenda da próxima semana com vocês."
    )
    
    entrada_texto = st.text_area("Mensagem Recebida:", value=msg_medico, height=150)
    
    # Geração da Resposta com Inteligência Humanizada
    resposta_humanizada = (
        f"Olá, {unidade_alvo}. Entendo perfeitamente a sua frustração; após um plantão, "
        "a última coisa que você precisa é lidar com burocracia financeira. Valorizamos muito o seu tempo. "
        "Para que eu consiga destravar o valor e garantir sua agenda da semana que vem sem preocupações, "
        "consegue me ajudar confirmando apenas o reenvio dos arquivos XML? "
        "Estou acompanhando pessoalmente para mover para CONFORMIDADE OK imediatamente."
    )

    if st.button("✨ Gerar e Salvar na Memória"):
        # Salvação Automática na Memória Quântica
        st.session_state.memoria_sentinela.append({
            "data": datetime.now().strftime("%H:%M:%S"),
            "unidade": unidade_alvo,
            "entrada": entrada_texto,
            "resposta": resposta_humanizada
        })
        st.success("**Resposta Estratégica Gerada com Sucesso!**")
        st.write(resposta_humanizada)
        st.rerun()

    # Link Direto para WhatsApp (Fim da duplicidade)
    link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta_humanizada)}"
    st.markdown(f"""
        <a href="{link_zap}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                🚀 ENVIAR PARA O WHATSAPP
            </div>
        </a>
    """, unsafe_allow_html=True)

# --- 6. TABELA DA FAVELINHA (RELATÓRIO ANALÍTICO) ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "Exposição (R$)", "status": "Veredito"}))

st.caption("Sidney Pereira de Almeida | Diretor de Compliance & Inteligência de Gestão")
    
