import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. SETUP DE SEGURANÇA ---
st.set_page_config(page_title="Governança | IA-SENTINELA", layout="wide")

# Inicialização da Trava de Disparo (Session State)
if 'disparo_concluido' not in st.session_state:
    st.session_state.disparo_concluido = False

# --- 2. BASE DE DADOS (TERMINOLOGIA EXECUTIVA ÚNICA) ---
db_executiva = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO TÉCNICA"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "EM ANÁLISE"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO TÉCNICA"}
]

# --- 3. DASHBOARD CONSOLIDADO ---
st.title("🛡️ SENTINELA | Governança de Receita")
total = sum(item['valor'] for item in db_executiva)
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total:,.2f}")

st.divider()

# --- 4. RELATÓRIO ANALÍTICO (TABELA DA FAVELINHA) ---
df = pd.DataFrame(db_executiva)
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df)

# --- 5. LÓGICA DE DISPARO ÚNICO (SOLUÇÃO DA DUPLICIDADE) ---
st.subheader("📲 Canal de Comunicação Institucional")
unidade_alerta = st.selectbox("Selecione a Unidade para Reporte", df["unidade"].tolist())
row = df[df["unidade"] == unidade_alerta].iloc[0]

# Formatação Diplomática
mensagem = (
    f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
    f"------------------------------------------\n"
    f"🏥 *UNIDADE:* {row['unidade']}\n"
    f"⚖️ *STATUS:* *{row['status']}*\n"
    f"💰 *EXPOSIÇÃO:* R$ {row['valor']:,.2f}\n\n"
    f"✅ _Documento Auditado Q2-2026_"
)

link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(mensagem)}"

# BOTÃO COM TRAVA: Só permite um clique por vez
if st.button(f"🚀 GERAR COMUNICADO ÚNICO: {unidade_alerta}"):
    st.session_state.disparo_concluido = True
    # O link é exibido apenas após o clique deliberado
    st.markdown(f"""
        <meta http-equiv="refresh" content="0; url={link_zap}">
        <p style="color: #00c853;">✅ Redirecionando para envio único...</p>
        <a href="{link_zap}" target="_blank">Clique aqui se não for redirecionado.</a>
    """, unsafe_allow_html=True)

st.caption("Sidney Pereira de Almeida | Diretor de Compliance")
    
