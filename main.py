import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. SETUP DE SEGURANÇA MÁXIMA ---
st.set_page_config(page_title="Governança Executiva | IA-SENTINELA", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 12px; }
</style>""", unsafe_allow_html=True)

# --- 2. BASE DE DADOS INTEGRADA (TERMINOLOGIA ÚNICA) ---
# Aqui mudamos a terminologia na "raiz" da informação
db_servidor = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status_base": "CONFORMIDADE OK"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status_base": "RESTRIÇÃO"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status_base": "PENDÊNCIA TÉCNICA"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status_base": "CONFORMIDADE OK"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status_base": "RESTRIÇÃO"}
]

# --- 3. PROCESSAMENTO ANALÍTICO ---
total_geral = sum(item['valor'] for item in db_servidor)
df = pd.DataFrame(db_servidor)

# --- 4. DASHBOARD ESTRATÉGICO ---
st.title("🛡️ SENTINELA | Governança de Receita")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_geral:,.2f}")

st.divider()

# --- 5. GRÁFICO DE CONFORMIDADE LADO A LADO ---
st.subheader("📈 Performance e Risco por Unidade")
df['Em Conformidade'] = df.apply(lambda x: x['valor'] if x['status_base'] == 'CONFORMIDADE OK' else 0, axis=1)
df['Em Restrição/Análise'] = df.apply(lambda x: x['valor'] if x['status_base'] != 'CONFORMIDADE OK' else 0, axis=1)

chart_data = df.set_index("unidade")[['Em Conformidade', 'Em Restrição/Análise']]
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"]) 

# --- 6. RELATÓRIO ANALÍTICO (TABELA DA FAVELINHA ATUALIZADA) ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
# Exibindo com a nova terminologia executiva
st.table(df[["unidade", "valor", "status_base"]].rename(columns={
    "unidade": "Unidade de Negócio",
    "valor": "Exposição Financeira",
    "status_base": "Status de Auditoria"
}))

# --- 7. DISPARO ÚNICO E MANUAL (SOLUÇÃO DA DUPLICIDADE) ---
st.divider()
st.subheader("📲 Comunicado Institucional")
unidade_alerta = st.selectbox("Selecione a Unidade para Reporte", df["unidade"].tolist())
row = df[df["unidade"] == unidade_alerta].iloc[0]

# Construção da Mensagem Diplomática
mensagem = (
    f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
    f"------------------------------------------\n"
    f"🏥 *UNIDADE:* {row['unidade']}\n"
    f"⚖️ *STATUS:* *{row['status_base']}*\n"
    f"💰 *EXPOSIÇÃO:* R$ {row['valor']:,.2f}\n\n"
    f"✅ _Documento Auditado Q2-2026_"
)
link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(mensagem)}"

# O segredo aqui é o link manual: ele NÃO dispara sozinho
st.markdown(f"""
    <div style="text-align: center; padding: 20px;">
        <p style="color: #888;">Clique abaixo para abrir o WhatsApp manualmente e evitar duplicidade:</p>
        <a href="{link_zap}" target="_blank" style="
            background-color: #25D366; 
            color: white; 
            padding: 15px 30px; 
            border-radius: 10px; 
            text-decoration: none; 
            font-weight: bold; 
            font-size: 18px;
            display: inline-block;">
            🚀 ENVIAR RELATÓRIO: {unidade_alerta}
        </a>
    </div>
""", unsafe_allow_html=True)

st.caption("Sidney Pereira de Almeida | Diretor de Compliance")
