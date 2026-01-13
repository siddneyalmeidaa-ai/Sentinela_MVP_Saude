import streamlit as st
import pandas as pd
from flask import Flask, request, jsonify
import threading

# --- 1. MOTOR DE INTELIGÊNCIA (LÓGICA E INSIGHTS) ---
def realizar_auditoria(valor, status):
    if valor <= 1.0:
        return "PULA", "🔴 VÁCUO OPERACIONAL (1.00x)", "#ff7b72"
    elif status == "PENDENTE":
        return "AGUARDAR", "🟡 PENDÊNCIA TÉCNICA (XML/TUSS)", "#f1e05a"
    else:
        return "ENTRA", "🟢 FLUXO SEGURO - LIBERADO", "#39d353"

# --- 2. SINCRONIZAÇÃO WHATSAPP (SERVIDOR API) ---
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_sync():
    dados = request.json
    return jsonify({"status": "IA-SENTINELA ATIVA", "msg": "Sincronizado"})

def iniciar_servidor():
    try:
        app.run(port=5000)
    except:
        pass

# Inicia a escuta em segundo plano para não travar o visual
threading.Thread(target=iniciar_servidor, daemon=True).start()

# --- 3. INTERFACE EXECUTIVA (STREAMLIT) ---
st.set_page_config(page_title="IA-SENTINELA PRO | Q2-2026", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 15px;
    }
    .decisao-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
        border: 2px solid;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO")
st.caption("Monitoramento e Observabilidade | Sincronizado Q2-2026")

# Barra Lateral
with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Unidade/Doutor", ["ANIMA COSTA", "DR. SILVA", "INTERFILE - BI"])
    valor_rodada = st.number_input("Input de Valor", value=2500.0)
    status_rodada = st.radio("Status do Faturamento", ["LIBERADO", "PENDENTE"])

# Processamento da Decisão
acao, motivo, cor = realizar_auditoria(valor_rodada, status_rodada)

# Dashboard de KPIs (Padrão 68% vs 32%)
c1, c2 = st.columns(2)
with c1:
    st.metric(label="ASSETS LIBERADOS (68%)", value="R$ 10.880,00")
    st.markdown("🟢 <span style='color:#8B949E;'>Faturamento Ativo</span>", unsafe_allow_html=True)
with c2:
    st.metric(label="PENDÊNCIA OPERACIONAL (32%)", value="R$ 5.120,00", delta="-32%", delta_color="inverse")
    st.markdown("🔴 <span style='color:#8B949E;'>Risco de Glosa</span>", unsafe_allow_html=True)

# Bloco de Ação Imediata Centralizado
st.markdown(f"""
    <div class="decisao-box" style="background-color: {cor}22; border-color: {cor};">
        <h1 style="color: {cor}; margin:0;">DECISÃO: {acao}</h1>
        <p style="color: #8B949E; font-size: 18px;">Auditoria de Q2 Sincronizada</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Tabela da Favelinha (Insights Ativos Q2)
st.subheader("📊 Critical Audit Log (Tabela da Favelinha)")
df_favelinha = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Analise Atual"],
    "Insight Ativo (Q2)": ["Erro XML - Corrigir Tag", "Divergência TUSS", f"Ação: {acao}"]
})
st.table(df_favelinha)

st.write("---")
st.caption(f"Operação: {medico} | Desenvolvido por Sidney Pereira de Almeida")
