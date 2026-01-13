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

# --- 2. INTERFACE ---
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

# BARRA LATERAL - ORGANIZADA PARA NÃO TRAVAR
with st.sidebar:
    st.header("⚙️ Configuração")
    
    # Campo de número agora é o primeiro e SEMPRE editável
    numero_zap = st.text_input(
        "WhatsApp (55 + DDD + Número)", 
        value="55", 
        key="zap_input" # Chave única para evitar que o campo fique estático
    )
    
    st.divider()
    medico = st.selectbox("Unidade", ["ANIMA COSTA", "DR. SILVA", "INTERFILE - BI"])
    valor_rodada = st.number_input("Valor da Rodada", value=2500.0)
    status_rodada = st.radio("Status", ["LIBERADO", "PENDENTE"])

# Processamento
st.title("🛡️ IA-SENTINELA PRO")
acao, motivo, cor = processar_auditoria(valor_rodada, status_rodada)

# KPIs (68% vs 32%)
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

# --- 3. WHATSAPP ---
msg_texto = f"""🛡️ *IA-SENTINELA - AUDITORIA*
-----------------------------------------
🏥 *Unidade:* {medico}
💰 *Valor:* R$ {valor_rodada:,.2f}
⚖️ *Decisão:* *{acao}*
📝 *Motivo:* {motivo}
✅ _Sincronizado Q2-2026_"""

link_zap = f"https://wa.me/{numero_zap}?text={urllib.parse.quote(msg_texto)}"

st.write("### 📲 Ação Imediata")
# Só libera se o usuário digitou algo além do "55"
if len(numero_zap) > 10:
    st.link_button("🚀 ENVIAR RELATÓRIO PARA WHATSAPP", link_zap)
else:
    st.warning("👈 Por favor, complete o número do WhatsApp na barra lateral.")

st.divider()
# Tabela da Favelinha
st.subheader("📊 Critical Audit Log")
df = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Analise Atual"],
    "Insight Ativo": ["Erro XML", "Divergência TUSS", f"Ação: {acao}"]
})
st.table(df)
st.caption("Auditor: Sidney Pereira de Almeida")
