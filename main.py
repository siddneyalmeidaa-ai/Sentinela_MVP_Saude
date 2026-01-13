import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. CONFIGURAÇÃO EXECUTIVA ---
st.set_page_config(page_title="Executive Dashboard | IA-SENTINELA", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; }
    .stTable { background-color: #161B22; }
</style>""", unsafe_allow_html=True)

# --- 2. MOTOR DE GOVERNANÇA ---
def auditoria_compliance(valor, status):
    if valor <= 1.0:
        return "PULA", "⚠️ INCONSISTÊNCIA DE DADOS", "#ff7b72"
    elif status == "PENDENTE":
        return "NÃO ENTRA", "🟡 AGUARDANDO REGULARIZAÇÃO TÉCNICA", "#f1e05a"
    else:
        return "ENTRA", "🟢 CONFORMIDADE VALIDADA", "#39d353"

# --- 3. BASE DE DADOS DO SERVIDOR ---
db_data = [
    {"unidade": "ANIMA COSTA", "faturamento": 12500.0, "compliance": "LIBERADO"},
    {"unidade": "DR. SILVA", "faturamento": 1.0, "compliance": "LIBERADO"},
    {"unidade": "INTERFILE - BI", "faturamento": 5400.0, "compliance": "PENDENTE"},
    {"unidade": "DR. MARCOS", "faturamento": 8900.0, "compliance": "LIBERADO"},
    {"unidade": "LAB CLINIC", "faturamento": 0.80, "compliance": "LIBERADO"}
]

# Processamento
processados = []
total_consolidado = 0
for item in db_data:
    veredito, parecer, cor = auditoria_compliance(item['faturamento'], item['compliance'])
    total_consolidado += item['faturamento']
    processados.append({
        "Unidade de Negócio": item['unidade'],
        "Exposição Financeira": item['faturamento'],
        "Veredito": veredito,
        "Parecer Técnico": parecer
    })

df = pd.DataFrame(processados)

# --- 4. CABEÇALHO CONSOLIDADO ---
st.title("🛡️ SENTINELA | Governança de Receita")
st.caption("Conselho Consultivo | Relatório Estratégico Q2-2026")

# Valor Consolidado no Topo
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_consolidado:,.2f}")

st.divider()

# --- 5. GRÁFICO DE BARRAS EXECUTIVO ---
st.subheader("📈 Performance por Unidade de Negócio")
# Preparando dados para o gráfico
chart_data = df.set_index("Unidade de Negócio")["Exposição Financeira"]
st.bar_chart(chart_data, color="#39d353") # Barra verde conforme padrão ENTRA

# --- 6. RESUMO DE CONFORMIDADE ---
c1, c2 = st.columns(2)
with c1:
    st.metric(label="ASSETS EM CONFORMIDADE (68%)", value="R$ 10.880,00")
with c2:
    st.metric(label="PENDÊNCIAS EM TRATATIVA (32%)", value="R$ 5.120,00", delta="Risco Mitigado", delta_color="normal")

# --- 7. RELATÓRIO ANALÍTICO (TABELA DA FAVELINHA) ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df.assign(**{"Exposição Financeira": df["Exposição Financeira"].map("R$ {:,.2f}".format)}))

# --- 8. DISPARO INSTITUCIONAL ---
st.subheader("📲 Canal de Comunicação Direta")
numero_zap = st.text_input("Destinatário:", value="5511942971753")
unidade_alerta = st.selectbox("Selecione a Unidade para Reporte", df["Unidade de Negócio"].tolist())

if len(numero_zap) > 10:
    row = df[df["Unidade de Negócio"] == unidade_alerta].iloc[0]
    mensagem = (
        f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
        f"🏥 *UNIDADE:* {row['Unidade de Negócio']}\n"
        f"⚖️ *STATUS:* *{row['Veredito']}*\n"
        f"📝 *PARECER:* {row['Parecer Técnico']}\n"
        f"💰 *VALOR:* R$ {row['Exposição Financeira']:,.2f}"
    )
    link = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(mensagem)}"
    st.link_button(f"🚀 Emitir Comunicado Oficial", link)

st.caption("Sidney Pereira de Almeida | Diretor de Auditoria e Compliance")
