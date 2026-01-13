import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. SETUP DE GOVERNANÇA ---
st.set_page_config(page_title="Governança Executiva | IA-SENTINELA", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 12px; }
</style>""", unsafe_allow_html=True)

# --- 2. BASE DE DADOS DO SERVIDOR (TERMINOLOGIA ATUALIZADA) ---
def buscar_ativos_servidor():
    # A base agora já nasce com a terminologia de conformidade
    return [
        {"unidade": "ANIMA COSTA", "valor": 12500.0, "status_origem": "CONFORMIDADE OK"},
        {"unidade": "DR. SILVA", "valor": 1.0, "status_origem": "RESTRIÇÃO TÉCNICA"},
        {"unidade": "INTERFILE - BI", "valor": 5400.0, "status_origem": "EM ANÁLISE"},
        {"unidade": "DR. MARCOS", "valor": 8900.0, "status_origem": "CONFORMIDADE OK"},
        {"unidade": "LAB CLINIC", "valor": 0.80, "status_origem": "RESTRIÇÃO TÉCNICA"}
    ]

# --- 3. MOTOR DE AUDITORIA DIPLOMÁTICA ---
def analisar_compliance(valor, status):
    if valor <= 1.0 or status == "RESTRIÇÃO TÉCNICA":
        return "RESTRIÇÃO", "⚠️ INCONSISTÊNCIA DE ATIVOS - VALOR ABAIXO DA MARGEM", "#ff4b4b"
    elif status == "EM ANÁLISE":
        return "AGUARDAR", "🟡 AGUARDANDO REGULARIZAÇÃO DE DOCUMENTAÇÃO", "#f1e05a"
    else:
        return "CONFORMIDADE OK", "🟢 VALIDAÇÃO TÉCNICA CONCLUÍDA", "#00c853"

# --- 4. PROCESSAMENTO E CONSOLIDAÇÃO ---
dados_base = buscar_ativos_servidor()
relatorio_final = []
total_consolidado = 0

for item in dados_base:
    status_final, parecer, cor = analisar_compliance(item['valor'], item['status_origem'])
    total_consolidado += item['valor']
    relatorio_final.append({
        "Unidade de Negócio": item['unidade'],
        "Exposição Financeira": item['valor'],
        "Status de Auditoria": status_final,
        "Parecer Técnico": parecer
    })

df = pd.DataFrame(relatorio_final)

# --- 5. DASHBOARD EXECUTIVO ---
st.title("🛡️ SENTINELA | Governança de Receita")
st.caption("Relatório Estratégico de Auditoria | Q2-2026")

# Valor Consolidado
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_consolidado:,.2f}")

st.divider()

# --- 6. GRÁFICO DE CONFORMIDADE (DUAS BARRAS) ---
st.subheader("📈 Mapa de Exposição e Conformidade")

# Criando colunas para o gráfico de barras lateral solicitado
df['Em Conformidade'] = df.apply(lambda x: x['Exposição Financeira'] if x['Status de Auditoria'] == 'CONFORMIDADE OK' else 0, axis=1)
df['Em Restrição/Análise'] = df.apply(lambda x: x['Exposição Financeira'] if x['Status de Auditoria'] != 'CONFORMIDADE OK' else 0, axis=1)

chart_data = df.set_index("Unidade de Negócio")[['Em Conformidade', 'Em Restrição/Análise']]
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"])

# --- 7. RELATÓRIO ANALÍTICO DE ATIVOS ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["Unidade de Negócio", "Exposição Financeira", "Status de Auditoria", "Parecer Técnico"]])

# --- 8. DISPARO ÚNICO DE COMPLIANCE (CORRIGIDO) ---
st.subheader("📲 Canal de Comunicação Institucional")
unidade_alerta = st.selectbox("Selecione a Unidade para Reporte", df["Unidade de Negócio"].tolist())
numero_zap = "5511942971753" #

row = df[df["Unidade de Negócio"] == unidade_alerta].iloc[0]

# Construção do Relatório Diplomático
mensagem = (
    f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
    f"------------------------------------------\n"
    f"🏥 *UNIDADE:* {row['Unidade de Negócio']}\n"
    f"⚖️ *STATUS:* *{row['Status de Auditoria']}*\n"
    f"📝 *PARECER:* {row['Parecer Técnico']}\n"
    f"💰 *EXPOSIÇÃO:* R$ {row['Exposição Financeira']:,.2f}\n\n"
    f"✅ _Documento Auditado Q2-2026_"
)

link_final = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(mensagem)}"

# Botão de disparo único
if st.link_button(f"🚀 Emitir Comunicado Oficial: {unidade_alerta}", link_final):
    st.toast("Relatório preparado para envio único.")

st.caption("Sidney Pereira de Almeida | Diretor de Auditoria e Compliance")
    
