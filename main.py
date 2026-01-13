import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. SETUP EXECUTIVO ---
st.set_page_config(page_title="Executive Analytics | IA-SENTINELA", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 10px; }
</style>""", unsafe_allow_html=True)

# --- 2. BASE DE DADOS DO SERVIDOR ---
db_data = [
    {"unidade": "ANIMA COSTA", "faturamento": 12500.0, "status": "LIBERADO"},
    {"unidade": "DR. SILVA", "faturamento": 1.0, "status": "LIBERADO"},
    {"unidade": "INTERFILE - BI", "faturamento": 5400.0, "status": "PENDENTE"},
    {"unidade": "DR. MARCOS", "faturamento": 8900.0, "status": "LIBERADO"},
    {"unidade": "LAB CLINIC", "faturamento": 0.80, "status": "LIBERADO"}
]

# --- 3. MOTOR DE INTELIGÊNCIA (TERMINOLOGIA TÉCNICA) ---
def auditoria_inteligente(valor, status):
    if valor <= 1.0:
        return "PULA", "⚠️ INCONSISTÊNCIA DE DADOS", "#ff4b4b"
    elif status == "PENDENTE":
        return "NÃO ENTRA", "🟡 PENDÊNCIA TÉCNICA EM TRATATIVA", "#f1e05a"
    else:
        # Nova terminologia diplomática solicitada
        return "CONFORMIDADE OK", "🟢 VALIDAÇÃO TÉCNICA CONCLUÍDA", "#00c853"

# Processamento
processados = []
for item in db_data:
    veredito, parecer, cor = auditoria_inteligente(item['faturamento'], item['status'])
    processados.append({
        "Unidade de Negócio": item['unidade'],
        "Exposição Financeira": item['faturamento'],
        "Veredito": veredito,
        "Parecer Técnico": parecer
    })

df = pd.DataFrame(processados)

# --- 4. CABEÇALHO CONSOLIDADO ---
st.title("🛡️ SENTINELA | Governança de Receita")
total_geral = df["Exposição Financeira"].sum()
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_geral:,.2f}") #

st.divider()

# --- 5. GRÁFICO DE PERFORMANCE E PENDÊNCIAS ---
st.subheader("📈 Análise de Conformidade por Unidade")

# Criando as colunas separadas para o gráfico de barras lateral
df['Conformidade'] = df.apply(lambda x: x['Exposição Financeira'] if x['Veredito'] == 'CONFORMIDADE OK' else 0, axis=1)
df['Pendentes/Inconsistentes'] = df.apply(lambda x: x['Exposição Financeira'] if x['Veredito'] != 'CONFORMIDADE OK' else 0, axis=1)

chart_data = df.set_index("Unidade de Negócio")[['Conformidade', 'Pendentes/Inconsistentes']]
# Exibe a barra de Conformidade (Verde) e a de Pendentes (Vermelho) lado a lado
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"]) 

# --- 6. RELATÓRIO ANALÍTICO ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["Unidade de Negócio", "Exposição Financeira", "Veredito", "Parecer Técnico"]])

# --- 7. DISPARO DE COMPLIANCE (WHATSAPP) ---
st.subheader("📲 Canal de Comunicação Direta")
unidade_alerta = st.selectbox("Selecione a Unidade para Reporte", df["Unidade de Negócio"].tolist())
numero_zap = "5511942971753" # Fixado conforme sua tela

row = df[df["Unidade de Negócio"] == unidade_alerta].iloc[0]
mensagem = (
    f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
    f"------------------------------------------\n"
    f"🏥 *UNIDADE:* {row['Unidade de Negócio']}\n"
    f"⚖️ *STATUS:* *{row['Veredito']}*\n"
    f"📝 *PARECER:* {row['Parecer Técnico']}\n"
    f"💰 *EXPOSIÇÃO:* R$ {row['Exposição Financeira']:,.2f}\n\n"
    f"✅ _Documento Auditado Q2-2026_"
)
link = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(mensagem)}"
st.link_button(f"🚀 Emitir Comunicado Oficial: {unidade_alerta}", link)

st.caption("Sidney Pereira de Almeida | Diretor de Auditoria e Compliance")
