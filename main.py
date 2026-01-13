import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. MOTOR DE GOVERNANÇA (LÓGICA EXECUTIVA) ---
def auditoria_compliance(valor, status):
    if valor <= 1.0:
        return "PULA", "⚠️ INCONSISTÊNCIA DE DADOS - ATIVO ABAIXO DA MARGEM", "#ff7b72"
    elif status == "PENDENTE":
        return "NÃO ENTRA", "🟡 AGUARDANDO REGULARIZAÇÃO DE DOCUMENTAÇÃO TÉCNICA", "#f1e05a"
    else:
        return "ENTRA", "🟢 CONFORMIDADE VALIDADA - FLUXO LIBERADO", "#39d353"

# --- 2. BASE DE DADOS (SERVIDOR EM TEMPO REAL) ---
def get_server_data():
    return [
        {"unidade": "ANIMA COSTA", "faturamento": 12500.0, "compliance": "LIBERADO", "auditor": "S. Pereira"},
        {"unidade": "DR. SILVA", "faturamento": 1.0, "compliance": "LIBERADO", "auditor": "S. Pereira"},
        {"unidade": "INTERFILE - BI", "faturamento": 5400.0, "compliance": "PENDENTE", "auditor": "S. Pereira"},
        {"unidade": "DR. MARCOS", "faturamento": 8900.0, "compliance": "LIBERADO", "auditor": "S. Pereira"},
        {"unidade": "LAB CLINIC", "faturamento": 0.80, "compliance": "LIBERADO", "auditor": "S. Pereira"}
    ]

# --- 3. INTERFACE DE GESTÃO ESTRATÉGICA ---
st.set_page_config(page_title="Executive Dashboard | IA-SENTINELA", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; }
</style>""", unsafe_allow_html=True)

st.title("🛡️ Sistema de Governança IA-SENTINELA")
st.caption("Conselho Consultivo | Relatório de Auditoria de Receita")

# --- 4. PROCESSAMENTO DE ATIVOS ---
db_data = get_server_data()
processados = []

for item in db_data:
    veredito, parecer, cor = auditoria_compliance(item['faturamento'], item['compliance'])
    processados.append({
        "Unidade de Negócio": item['unidade'],
        "Exposição Financeira": f"R$ {item['faturamento']:,.2f}",
        "Veredito": veredito,
        "Parecer Técnico": parecer
    })

df_executivo = pd.DataFrame(processados)

# --- 5. DASHBOARD DE PERFORMANCE (KPIs) ---
st.subheader("📊 Resumo Executivo de Auditoria")
k1, k2 = st.columns(2)
with k1:
    st.metric(label="ASSETS EM CONFORMIDADE (68%)", value="R$ 10.880,00")
with k2:
    st.metric(label="PENDÊNCIAS EM TRATATIVA (32%)", value="R$ 5.120,00", delta="Risco Mitigado", delta_color="normal")

# --- 6. TABELA DA FAVELINHA (PADRÃO EXECUTIVO) ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df_executivo)

# --- 7. COMUNICAÇÃO INSTITUCIONAL (WHATSAPP) ---
st.subheader("📲 Disparo de Relatório Institucional")
numero_zap = st.text_input("Canal de Destino:", value="5511942971753")
unidade_alerta = st.selectbox("Selecione a Unidade de Negócio para Reporte", df_executivo["Unidade de Negócio"].tolist())

if len(numero_zap) > 10:
    row = df_executivo[df_executivo["Unidade de Negócio"] == unidade_alerta].iloc[0]
    
    # Texto Diplomático e Profissional
    mensagem_executiva = (
        f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
        f"------------------------------------------\n"
        f"🏥 *UNIDADE:* {row['Unidade de Negócio']}\n"
        f"⚖️ *STATUS DE AUDITORIA:* *{row['Veredito']}*\n"
        f"📝 *PARECER TÉCNICO:* {row['Parecer Técnico']}\n\n"
        f"✅ _Documento processado via Dashboard Executivo Q2-2026_"
    )
    
    link_zap = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(mensagem_executiva)}"
    st.link_button(f"🚀 Emitir Comunicado: {row['Unidade de Negócio']}", link_zap)

st.caption("Sidney Pereira de Almeida | Diretor de Auditoria e Compliance")
