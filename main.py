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

# --- 2. INTERFACE DIRETA (MOBILE FIRST) ---
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
    /* Estilo para os inputs na tela principal */
    .stTextInput>div>div>input { background-color: #161B22; color: white; border: 1px solid #30363D; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO")
st.caption("Dashboard de Auditoria | Controle Direto")

# --- PAINEL DE CONTROLE NA TELA PRINCIPAL ---
st.subheader("⚙️ Configurações da Rodada")
c1, c2 = st.columns(2)

with c1:
    medico = st.selectbox("Unidade", ["ANIMA COSTA", "DR. SILVA", "INTERFILE - BI"])
    valor_rodada = st.number_input("Valor da Rodada", value=2500.0)

with c2:
    status_rodada = st.radio("Status do Faturamento", ["LIBERADO", "PENDENTE"])
    # CAMPO DE WHATSAPP AGORA ESTÁ AQUI NA FRENTE
    numero_zap = st.text_input("WhatsApp (55 + DDD + Número)", value="55", key="main_zap")

st.divider()

# Processamento
acao, motivo, cor = processar_auditoria(valor_rodada, status_rodada)

# KPIs (68% vs 32%)
k1, k2 = st.columns(2)
with k1:
    st.metric(label="ASSETS LIBERADOS (68%)", value="R$ 10.880,00")
with k2:
    st.metric(label="PENDÊNCIA OPERACIONAL (32%)", value="R$ 5.120,00", delta="-32%", delta_color="inverse")

# Bloco de Decisão
st.markdown(f"""
    <div class="decisao-box" style="background-color: {cor}22; border-color: {cor};">
        <h1 style="color: {cor}; margin:0;">DECISÃO: {acao}</h1>
        <p style="color: #8B949E; font-size: 18px;">Insight: {motivo}</p>
    </div>
""", unsafe_allow_html=True)

# --- AÇÃO WHATSAPP ---
msg_texto = f"""🛡️ *IA-SENTINELA - AUDITORIA*
-----------------------------------------
🏥 *Unidade:* {medico}
💰 *Valor:* R$ {valor_rodada:,.2f}
⚖️ *Decisão:* *{acao}*
📝 *Motivo:* {motivo}
✅ _Sincronizado Q2-2026_"""

link_zap = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(msg_texto)}"

st.write("### 📲 Disparar Insight")
if len(numero_zap) > 10:
    st.link_button("🚀 ENVIAR RELATÓRIO PARA WHATSAPP", link_zap)
else:
    st.info("💡 Digite o número do WhatsApp acima para habilitar o envio.")

st.divider()

# Tabela da Favelinha
st.subheader("📊 Critical Audit Log")
df = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Monitoramento"],
    "Insight Ativo": ["Erro XML", "Divergência TUSS", f"Ação: {acao}"]
})
st.table(df)

st.caption("Auditor: Sidney Pereira de Almeida")
