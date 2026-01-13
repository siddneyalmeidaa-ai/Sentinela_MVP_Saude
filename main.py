import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. SETUP EXECUTIVO ---
st.set_page_config(page_title="Executive Analytics | IA-SENTINELA", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 10px; }
    .stTable { background-color: #161B22; }
</style>""", unsafe_allow_html=True)

# --- 2. BASE DE DADOS DO SERVIDOR ---
db_data = [
    {"unidade": "ANIMA COSTA", "faturamento": 12500.0, "status": "LIBERADO"},
    {"unidade": "DR. SILVA", "faturamento": 1.0, "status": "LIBERADO"},
    {"unidade": "INTERFILE - BI", "faturamento": 5400.0, "status": "PENDENTE"},
    {"unidade": "DR. MARCOS", "faturamento": 8900.0, "status": "LIBERADO"},
    {"unidade": "LAB CLINIC", "faturamento": 0.80, "status": "LIBERADO"}
]

# --- 3. MOTOR DE INTELIGÊNCIA ---
def auditoria_inteligente(valor, status):
    if valor <= 1.0:
        return "PULA", "⚠️ INCONSISTÊNCIA DE DADOS", "#ff4b4b"
    elif status == "PENDENTE":
        return "NÃO ENTRA", "🟡 PENDÊNCIA TÉCNICA EM TRATATIVA", "#f1e05a"
    else:
        return "ENTRA", "🟢 CONFORMIDADE VALIDADA", "#00c853"

# Processamento
processados = []
for item in db_data:
    veredito, parecer, cor = auditoria_inteligente(item['faturamento'], item['status'])
    processados.append({
        "Unidade de Negócio": item['unidade'],
        "Exposição Financeira": item['faturamento'],
        "Veredito": veredito,
        "Parecer Técnico": parecer,
        "Cor": cor
    })

df = pd.DataFrame(processados)

# --- 4. CABEÇALHO CONSOLIDADO ---
st.title("🛡️ SENTINELA | Governança de Receita")
st.caption("Conselho Consultivo | Relatório Estratégico Q2-2026")

total_geral = df["Exposição Financeira"].sum()
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_geral:,.2f}")

st.divider()

# --- 5. INTERATIVIDADE E GRÁFICOS ---
st.subheader("📈 Inteligência de Performance e Pendências")

# Gráfico de Barras Colorido (Inteligente)
# Criamos colunas para separar o que está liberado do que está pendente/pula
df['Liberado'] = df.apply(lambda x: x['Exposição Financeira'] if x['Veredito'] == 'ENTRA' else 0, axis=1)
df['Em Tratativa/Inconsistente'] = df.apply(lambda x: x['Exposição Financeira'] if x['Veredito'] != 'ENTRA' else 0, axis=1)

chart_data = df.set_index("Unidade de Negócio")[['Liberado', 'Em Tratativa/Inconsistente']]
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"])

# --- 6. RESUMO EXECUTIVO ---
c1, c2 = st.columns(2)
with c1:
    st.metric(label="ASSETS EM CONFORMIDADE (68%)", value="R$ 10.880,00")
with c2:
    st.metric(label="PENDÊNCIAS EM TRATATIVA (32%)", value="R$ 5.120,00", delta="Risco Mitigado", delta_color="normal")

# --- 7. RELATÓRIO ANALÍTICO (TABELA DA FAVELINHA) ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["Unidade de Negócio", "Exposição Financeira", "Veredito", "Parecer Técnico"]])

# --- 8. DISPARO DE COMPLIANCE ---
st.subheader("📲 Canal de Comunicação Direta")
col_zap1, col_zap2 = st.columns([1, 2])

with col_zap1:
    numero_zap = st.text_input("Destinatário:", value="5511942971753")
with col_zap2:
    unidade_alerta = st.selectbox("Selecione a Unidade de Negócio", df["Unidade de Negócio"].tolist())

if len(numero_zap) > 10:
    row = df[df["Unidade de Negócio"] == unidade_alerta].iloc[0]
    mensagem = (
        f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
        f"🏥 *UNIDADE:* {row['Unidade de Negócio']}\n"
        f"⚖️ *STATUS:* *{row['Veredito']}*\n"
        f"📝 *PARECER:* {row['Parecer Técnico']}\n"
        f"💰 *EXPOSIÇÃO:* R$ {row['Exposição Financeira']:,.2f}"
    )
    link = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(mensagem)}"
    st.link_button(f"🚀 Emitir Comunicado Oficial: {unidade_alerta}", link)

st.caption("Sidney Pereira de Almeida | Diretor de Auditoria e Compliance")
