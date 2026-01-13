import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. MOTOR DE INTELIGÊNCIA Q2-2026 ---
def processar_auditoria(valor, status):
    if valor <= 1.0:
        return "PULA", "🔴 VÁCUO OPERACIONAL (1.00x)", "#ff7b72"
    elif status == "PENDENTE":
        return "AGUARDAR", "🟡 PENDÊNCIA TÉCNICA (XML/TUSS)", "#f1e05a"
    else:
        return "ENTRA", "🟢 FLUXO SEGURO - LIBERADO", "#39d353"

# --- 2. CONFIGURAÇÃO DA INTERFACE ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] {
        background-color: #161B22; border: 1px solid #30363D;
        border-radius: 12px; padding: 15px;
    }
    .decisao-box {
        padding: 20px; border-radius: 12px;
        text-align: center; margin: 15px 0; border: 2px solid;
    }
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3.5em;
        background-color: #25D366; color: white; font-weight: bold;
        border: none; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO")
st.caption("Dashboard Executivo | Sincronização WhatsApp Ativa")

# Barra Lateral (Corrigida para evitar o erro de Syntax)
with st.sidebar:
    st.header("⚙️ Configuração")
    medico = st.selectbox("Unidade", ["ANIMA COSTA", "DR. SILVA", "INTERFILE - BI"])
    valor_rodada = st.number_input("Valor da Rodada", value=2500.0)
    status_rodada = st.radio("Status", ["LIBERADO", "PENDENTE"])
    st.divider()
    # Coloque seu número com 55 + DDD + Numero (ex: 5511999999999)
    numero_padrao = st.text_input("Enviar para (WhatsApp)", value="5511999999999")

# Cálculos
acao, motivo, cor = processar_auditoria(valor_rodada, status_rodada)

# Dashboard (68% vs 32%)
c1, c2 = st.columns(2)
with c1:
    st.metric(label="ASSETS LIBERADOS (68%)", value="R$ 10.880,00")
with c2:
    st.metric(label="PENDÊNCIA OPERACIONAL (32%)", value="R$ 5.120,00", delta="-32%", delta_color="inverse")

# Bloco de Decisão Central
st.markdown(f"""
    <div class="decisao-box" style="background-color: {cor}22; border-color: {cor};">
        <h1 style="color: {cor}; margin:0;">DECISÃO: {acao}</h1>
        <p style="color: #8B949E; font-size: 18px;">Insight: {motivo}</p>
    </div>
""", unsafe_allow_html=True)

# --- 3. BOTÃO WHATSAPP ---
msg_formatada = f"""🛡️ *IA-SENTINELA - AUDITORIA*
-----------------------------------------
🏥 *Unidade:* {medico}
💰 *Valor:* R$ {valor_rodada:,.2f}
⚖️ *Decisão:* *{acao}*
📝 *Motivo:* {motivo}

✅ _Gerado via Dashboard IA-SENTINELA_"""

link_final = f"https://wa.me/{numero_padrao}?text={urllib.parse.quote(msg_formatada)}"

st.write("### 📲 Ação Imediata")
if st.button("🚀 ENVIAR RELATÓRIO PARA WHATSAPP"):
    st.markdown(f'<meta http-equiv="refresh" content="0;URL={link_final}">', unsafe_allow_html=True)
    st.success("Encaminhando para o WhatsApp...")

st.divider()

# Tabela da Favelinha
st.subheader("📊 Critical Audit Log")
df = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Analise"],
    "Insight Ativo (Q2)": ["Erro XML", "Divergência TUSS", f"Ação: {acao}"]
})
st.table(df)

st.caption(f"Operação: {medico} | Auditor: Sidney Pereira de Almeida")
