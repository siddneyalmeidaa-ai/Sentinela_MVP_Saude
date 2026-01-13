import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. MOTOR DE INTELIGÊNCIA ---
def processar_auditoria(valor, status):
    if valor <= 1.0:
        return "PULA", "🔴 VÁCUO OPERACIONAL (1.00x)", "#ff7b72"
    elif status == "PENDENTE":
        return "AGUARDAR", "🟡 PENDÊNCIA TÉCNICA (XML/TUSS)", "#f1e05a"
    else:
        return "ENTRA", "🟢 FLUXO SEGURO - LIBERADO", "#39d353"

# --- 2. INTERFACE EXECUTIVA ---
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
    .stLinkButton>a {
        width: 100% !important; background-color: #25D366 !important;
        color: white !important; font-weight: bold !important;
        border-radius: 12px !important; height: 3.5em !important;
        display: flex !important; align-items: center !important;
        justify-content: center !important; text-decoration: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO")
st.caption("Status API: 🟢 Sincronizado | Padrão Q2-2026")

with st.sidebar:
    st.header("⚙️ Configuração")
    medico = st.selectbox("Unidade", ["ANIMA COSTA", "DR. SILVA", "INTERFILE - BI"])
    valor_rodada = st.number_input("Valor da Rodada", value=2500.0)
    status_rodada = st.radio("Status", ["LIBERADO", "PENDENTE"])
    st.divider()
    # CAMPO CRÍTICO: Digite 55 + DDD + Numero (Total 13 dígitos)
    numero_zap = st.text_input("WhatsApp Destino", value="55", help="Ex: 5511988887777")

# Processamento
acao, motivo, cor = processar_auditoria(valor_rodada, status_rodada)

# KPIs (Mantendo a visão de 68% vs 32%)
c1, c2 = st.columns(2)
with c1:
    st.metric(label="ASSETS LIBERADOS (68%)", value="R$ 10.880,00")
with c2:
    st.metric(label="PENDÊNCIA OPERACIONAL (32%)", value="R$ 5.120,00", delta="-32%", delta_color="inverse")

# Bloco de Decisão
st.markdown(f"""
    <div class="decisao-box" style="background-color: {cor}22; border-color: {cor};">
        <h1 style="color: {cor}; margin:0;">DECISÃO: {acao}</h1>
        <p style="color: #8B949E; font-size: 18px;">Insight Ativo: {motivo}</p>
    </div>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE ENVIO SEGURA ---
msg_texto = f"""🛡️ *IA-SENTINELA - AUDITORIA*
-----------------------------------------
🏥 *Unidade:* {medico}
💰 *Valor:* R$ {valor_rodada:,.2f}
⚖️ *Decisão:* *{acao}*
📝 *Motivo:* {motivo}

✅ _Auditoria Sincronizada via Dashboard_"""

link_zap = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(msg_texto)}"

st.write("### 📲 Ação Imediata")
# Só mostra o botão se o número tiver o tamanho correto para evitar erro 55
if len(numero_zap) >= 12:
    st.link_button("🚀 ENVIAR RELATÓRIO PARA WHATSAPP", link_zap)
else:
    st.warning("⚠️ Digite o número completo com DDD (ex: 5511912345678) para liberar o envio.")

st.divider()

# Tabela da Favelinha
st.subheader("📊 Critical Audit Log")
df = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Monitoramento Atual"],
    "Insight Ativo (Q2)": ["Erro XML", "Divergência TUSS", f"Ação: {acao}"]
})
st.table(df)

st.caption(f"Operador: Sidney Pereira de Almeida | Q2-2026")
