import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

# --- 1. SETUP EXECUTIVO ---
st.set_page_config(page_title="Governança Executiva", layout="wide")

# --- 2. BASE DE DADOS (SERVIDOR - PADRÃO OURO) ---
db_servidor = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "PENDÊNCIA TÉCNICA"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]

df = pd.DataFrame(db_servidor)

# --- 3. CABEÇALHO CONSOLIDADO ---
total_geral = df["valor"].sum()
st.title("🛡️ Governança de Receita")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_geral:,.2f}")

st.divider()

# --- 4. GRÁFICO DE BARRAS EXECUTIVO (CORREÇÃO DE ESCALA) ---
st.subheader("📈 Mapa de Exposição Financeira por Unidade")

# Criando a lógica de cores para o gráfico
df['Cor'] = df['status'].apply(lambda x: '#00c853' if x == 'CONFORMIDADE OK' else '#ff4b4b')

# Gerando o gráfico com Plotly para garantir que as barras apareçam do zero
fig = px.bar(
    df, 
    x='unidade', 
    y='valor', 
    color='status',
    color_discrete_map={'CONFORMIDADE OK': '#00c853', 'RESTRIÇÃO': '#ff4b4b', 'PENDÊNCIA TÉCNICA': '#f1e05a'},
    labels={'unidade': 'Unidade de Negócio', 'valor': 'Exposição (R$)'},
    text_auto='.2s'
)

# Ajuste fino da escala para não "sumir" com as barras
fig.update_layout(
    yaxis=dict(range=[0, df['valor'].max() * 1.2]), # Força o eixo a começar em 0
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="white",
    showlegend=True
)

st.plotly_chart(fig, use_container_width=True)

# --- 5. RELATÓRIO ANALÍTICO (TABELA DA FAVELINHA) ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["unidade", "valor", "status"]].rename(columns={
    "unidade": "Unidade de Negócio",
    "valor": "Exposição Financeira",
    "status": "Status de Auditoria"
}))

# --- 6. COMUNICADO INSTITUCIONAL ---
st.divider()
st.subheader("📲 Comunicado Institucional")
unidade_alerta = st.selectbox("Selecione a Unidade para Reporte", df["unidade"].tolist())
row = df[df["unidade"] == unidade_alerta].iloc[0]

mensagem = (
    f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
    f"------------------------------------------\n"
    f"🏥 *UNIDADE:* {row['unidade']}\n"
    f"⚖️ *STATUS:* *{row['status']}*\n"
    f"💰 *EXPOSIÇÃO:* R$ {row['valor']:,.2f}\n\n"
    f"✅ _Documento Auditado Q2-2026_"
)
link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(mensagem)}"

st.markdown(f"""
    <div style="text-align: center;">
        <a href="{link_zap}" target="_blank" style="
            background-color: #25D366; 
            color: white; 
            padding: 18px 40px; 
            border-radius: 15px; 
            text-decoration: none; 
            font-weight: bold; 
            font-size: 20px;
            display: inline-block;">
            🚀 EMITIR COMUNICADO OFICIAL: {unidade_alerta}
        </a>
    </div>
""", unsafe_allow_html=True)

st.caption("Sidney Pereira de Almeida | Diretor de Compliance")
