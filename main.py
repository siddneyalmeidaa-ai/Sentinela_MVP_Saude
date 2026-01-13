import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. CONFIGURAÇÃO DE ALTO NÍVEL ---
st.set_page_config(page_title="Governança Executiva | IA-SENTINELA", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 12px; }
</style>""", unsafe_allow_html=True)

# --- 2. BASE DE DADOS PURA (TERMINOLOGIA EXECUTIVA) ---
def get_assets():
    return [
        {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
        {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO TÉCNICA"},
        {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "EM ANÁLISE"},
        {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
        {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO TÉCNICA"}
    ]

# --- 3. MOTOR DE AUDITORIA ---
processados = []
total_consolidado = 0
for item in get_assets():
    total_consolidado += item['valor']
    if item['valor'] <= 1.0 or item['status'] == "RESTRIÇÃO TÉCNICA":
        veredito, parecer = "RESTRIÇÃO", "⚠️ INCONSISTÊNCIA DE ATIVOS"
    elif item['status'] == "EM ANÁLISE":
        veredito, parecer = "EM ANÁLISE", "🟡 AGUARDANDO REGULARIZAÇÃO"
    else:
        veredito, parecer = "CONFORMIDADE OK", "🟢 VALIDAÇÃO TÉCNICA CONCLUÍDA"
    
    processados.append({
        "Unidade de Negócio": item['unidade'],
        "Exposição Financeira": item['valor'],
        "Status de Auditoria": veredito,
        "Parecer Técnico": parecer
    })

df = pd.DataFrame(processados)

# --- 4. DASHBOARD EXECUTIVO ---
st.title("🛡️ SENTINELA | Governança de Receita")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_consolidado:,.2f}")

st.divider()

# --- 5. GRÁFICO DE BARRAS LATERAL (INTELIGENTE) ---
st.subheader("📈 Mapa de Exposição e Conformidade")
df_chart = df.copy()
df_chart['Conformidade'] = df_chart.apply(lambda x: x['Exposição Financeira'] if x['Status de Auditoria'] == 'CONFORMIDADE OK' else 0, axis=1)
df_chart['Restrição/Análise'] = df_chart.apply(lambda x: x['Exposição Financeira'] if x['Status de Auditoria'] != 'CONFORMIDADE OK' else 0, axis=1)

st.bar_chart(df_chart.set_index("Unidade de Negócio")[['Conformidade', 'Restrição/Análise']], color=["#00c853", "#ff4b4b"])

# --- 6. TABELA DA FAVELINHA (DIPLOMÁTICA) ---
st.divider()
st.subheader("📋 Relatório Analítico de Ativos")
st.table(df[["Unidade de Negócio", "Exposição Financeira", "Status de Auditoria", "Parecer Técnico"]])

# --- 7. DISPARO ÚNICO (SOLUÇÃO DE DUPLICIDADE) ---
st.subheader("📲 Comunicado Institucional")
unidade_alerta = st.selectbox("Selecione a Unidade para Reporte", df["Unidade de Negócio"].tolist())
numero_zap = "5511942971753"

row = df[df["Unidade de Negócio"] == unidade_alerta].iloc[0]

# Formatação Executiva da Mensagem
mensagem = (
    f"🛡️ *RELATÓRIO DE GOVERNANÇA - IA-SENTINELA*\n"
    f"------------------------------------------\n"
    f"🏥 *UNIDADE:* {row['Unidade de Negócio']}\n"
    f"⚖️ *STATUS:* *{row['Status de Auditoria']}*\n"
    f"📝 *PARECER:* {row['Parecer Técnico']}\n"
    f"💰 *EXPOSIÇÃO:* R$ {row['Exposição Financeira']:,.2f}\n\n"
    f"✅ _Documento Auditado Q2-2026_"
)

# LINK ÚNICO - Evita o disparo duplo por recarregamento
link_zap = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(mensagem)}"

# Usando markdown para um link limpo que não dispara duas vezes
st.markdown(f"""
    <a href="{link_zap}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 18px;">
            🚀 EMITIR COMUNICADO OFICIAL: {unidade_alerta}
        </div>
    </a>
""", unsafe_allow_html=True)

st.caption("Sidney Pereira de Almeida | Diretor de Compliance")
