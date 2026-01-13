import streamlit as st
import pandas as pd
import urllib.parse
import plotly.express as px

# --- 1. SIMULAÇÃO DE SERVIDOR (BASE DE MÉDICOS) ---
def buscar_dados_servidor():
    return [
        {"medico": "ANIMA COSTA", "valor": 12500.0, "status": "LIBERADO", "paciente": "Carlos Eduardo"},
        {"medico": "DR. SILVA", "valor": 1.0, "status": "LIBERADO", "paciente": "Marta Souza"},
        {"medico": "INTERFILE - BI", "valor": 5400.0, "status": "PENDENTE", "paciente": "Roberto Alencar"},
        {"medico": "DR. MARCOS", "valor": 8900.0, "status": "LIBERADO", "paciente": "Ana Paula"},
        {"medico": "LAB CLINIC", "valor": 0.80, "status": "LIBERADO", "paciente": "Vácuo Teste"}
    ]

def processar_auditoria(valor, status):
    if valor <= 1.0:
        return "PULA", "🔴 VÁCUO OPERACIONAL (1.00x)", "#ff7b72"
    elif status == "PENDENTE":
        return "AGUARDAR", "🟡 PENDÊNCIA TÉCNICA (XML/TUSS)", "#f1e05a"
    else:
        return "ENTRA", "🟢 FLUXO SEGURO - LIBERADO", "#39d353"

# --- 2. CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border: 1px solid #30363D; border-radius: 12px; padding: 15px; }
    .stTable { background-color: #161B22; border-radius: 10px; }
</style>""", unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO")
st.caption("Automação Ativa | Sincronização com Servidor")

# --- 3. PROCESSAMENTO EM LOTE ---
dados = buscar_dados_servidor()
resultados = []
contagem = {"ENTRA": 0, "PULA": 0, "AGUARDAR": 0}

for item in dados:
    acao, motivo, cor = processar_auditoria(item['valor'], item['status'])
    contagem[acao] += 1
    resultados.append({
        "Médico": item['medico'],
        "Valor (R$)": item['valor'],
        "Decisão": acao,
        "Insight Ativo": motivo
    })

df = pd.DataFrame(resultados)

# --- 4. DASHBOARD DE PROJEÇÃO (O "X" DA RODADA) ---
c1, c2 = st.columns([1, 1])

with c1:
    st.subheader("📈 Projeção de Próximas Rodadas")
    fig = px.pie(
        values=[contagem["ENTRA"], contagem["PULA"] + contagem["AGUARDAR"]], 
        names=["LIBERADO", "PENDENTE/VÁCUO"],
        color_discrete_sequence=["#39d353", "#ff7b72"],
        hole=0.5
    )
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), showlegend=True, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.metric(label="TAXA DE SUCESSO (LIBERADO)", value=f"{(contagem['ENTRA']/len(dados))*100:.1f}%")
    st.metric(label="RISCO DE VÁCUO (PULA)", value=f"{(contagem['PULA']/len(dados))*100:.1f}%", delta="Atenção", delta_color="inverse")

# --- 5. TABELA DA FAVELINHA AUTOMATIZADA ---
st.divider()
st.subheader("📊 Tabela da Favelinha (Auditada via Servidor)")
st.table(df)

# --- 6. ENVIO RÁPIDO ---
st.subheader("📲 Enviar Insight da Base")
numero_zap = st.text_input("Seu WhatsApp (55...)", value="55")
medico_alerta = st.selectbox("Escolha o Médico para reportar", df["Médico"].tolist())

if len(numero_zap) > 10:
    row = df[df["Médico"] == medico_alerta].iloc[0]
    msg = f"🛡️ *IA-SENTINELA*\n🏥 *Unidade:* {row['Médico']}\n⚖️ *Decisão:* {row['Decisão']}\n📝 *Motivo:* {row['Insight Ativo']}"
    link = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(msg)}"
    st.link_button(f"🚀 Enviar Report de {medico_alerta}", link)

st.caption("Sistema Sincronizado | Auditor: Sidney Pereira de Almeida")
