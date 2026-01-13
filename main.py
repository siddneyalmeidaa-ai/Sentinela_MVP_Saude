import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. SETUP DE SEGURANÇA ---
st.set_page_config(page_title="Governança Executiva", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 12px; }
</style>""", unsafe_allow_html=True)

# --- 2. BASE DE DADOS INTEGRADA (TERMINOLOGIA ÚNICA) ---
db_servidor = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "PENDÊNCIA TÉCNICA"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]

df = pd.DataFrame(db_servidor)
total_geral = df["valor"].sum()

# --- 3. DASHBOARD ESTRATÉGICO ---
st.title("🛡️ Governança de Receita")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_geral:,.2f}")

st.divider()

# --- 4. GRÁFICO DE BARRAS (CORREÇÃO DE ESCALA) ---
st.subheader("📈 Performance e Risco por Unidade")

# Criando colunas para visualização lado a lado
df['Em Conformidade'] = df.apply(lambda x: x['valor'] if x['status'] == 'CONFORMIDADE OK' else 0, axis=1)
df['Em Restrição/Análise'] = df.apply(lambda x: x['valor'] if x['status'] != 'CONFORMIDADE OK' else 0, axis=1)

# Prepara os dados para o gráfico nativo (Evita erro de ModuleNotFound)
chart_data = df.set_index("unidade")[['Em Conformidade', 'Em Restrição/Análise']]

# st.bar_chart nativo com cores fixas: Verde para Conformidade e Vermelho para Risco
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"]) 

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
