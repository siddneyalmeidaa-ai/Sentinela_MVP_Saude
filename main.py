import streamlit as st
import pandas as pd
import urllib.parse

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

# --- 2. INTERFACE EXECUTIVA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")
st.markdown("""<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border: 1px solid #30363D; border-radius: 12px; padding: 15px; }
    .decisao-box { padding: 20px; border-radius: 12px; text-align: center; margin: 15px 0; border: 2px solid; }
</style>""", unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO")
st.caption("Automação Ativa | Sincronização com Servidor")

# --- 3. PROCESSAMENTO EM LOTE ---
dados = buscar_dados_servidor()
resultados = []

for item in dados:
    acao, motivo, cor = processar_auditoria(item['valor'], item['status'])
    resultados.append({
        "Médico": item['medico'],
        "Paciente": item['paciente'],
        "Valor (R$)": f"{item['valor']:,.2f}",
        "Decisão": acao,
        "Insight Ativo": motivo
    })

df = pd.DataFrame(resultados)

# --- 4. DASHBOARD DE KPIs ---
c1, c2 = st.columns(2)
with c1:
    st.metric(label="ASSETS LIBERADOS (68%)", value="R$ 10.880,00") # Valores fixos conforme imagem
with c2:
    st.metric(label="PENDÊNCIA OPERACIONAL (32%)", value="R$ 5.120,00", delta="-32%", delta_color="inverse")

# --- 5. TABELA DA FAVELINHA AUTOMATIZADA ---
st.divider()
st.subheader("📊 Tabela da Favelinha (Auditada via Servidor)")
st.table(df)

# --- 6. ENVIO RÁPIDO WHATSAPP (VALIDADO) ---
st.subheader("📲 Disparar Relatório")
numero_zap = st.text_input("WhatsApp para Envio (55...)", value="5511942971753") # Seu número da imagem
medico_alerta = st.selectbox("Escolha o médico para reportar", df["Médico"].tolist())

if len(numero_zap) > 10:
    row = df[df["Médico"] == medico_alerta].iloc[0]
    msg = f"🛡️ *IA-SENTINELA*\n🏥 *Unidade:* {row['Médico']}\n⚖️ *Decisão:* {row['Decisão']}\n📝 *Motivo:* {row['Insight Ativo']}"
    link = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(msg)}"
    st.link_button(f"🚀 Enviar Report de {medico_alerta}", link)

st.caption("Auditor: Sidney Pereira de Almeida | Q2-2026")
