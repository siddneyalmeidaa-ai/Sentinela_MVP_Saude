import streamlit as st
import pandas as pd
from flask import Flask, request, jsonify
import threading

# --- PARTE 1: O CÉREBRO DA IA (LÓGICA DE AUDITORIA) ---
def processar_auditoria(valor, status):
    if valor <= 1.0:
        return "PULA", "🔴 Vácuo Operacional (1.00x)"
    elif status == "PENDENTE":
        return "AGUARDAR", "🟡 Pendência de XML/TUSS"
    else:
        return "ENTRA", "🟢 Fluxo Liberado"

# --- PARTE 2: SINCRONIZAÇÃO WHATSAPP (SERVIDOR API) ---
app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def webhook():
    # O robô do WhatsApp envia os dados para cá
    dados = request.json
    msg_recebida = dados.get('message', '')
    
    # Simulação de resposta automática baseada no valor enviado por msg
    try:
        valor = float(msg_recebida.replace('R$', '').strip())
        acao, detalhe = processar_auditoria(valor, "LIBERADO")
        resposta = f"🛡️ *IA-SENTINELA INFORMA:*\n\nDecisão: *{acao}*\nMotivo: {detalhe}"
    except:
        resposta = "Olá Sidney! Envie o valor da rodada para auditoria."

    return jsonify({"status": "sucesso", "reply": resposta})

# Rodar o servidor em segundo plano para não travar o Dashboard
def run_api():
    app.run(port=5000)

# Inicia a "escuta" do WhatsApp
threading.Thread(target=run_api, daemon=True).start()

# --- PARTE 3: INTERFACE STREAMLIT (VISUAL EXECUTIVO) ---
st.set_page_config(page_title="IA-SENTINELA PRO | SYNC", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border: 1px solid #30363D; border-radius: 12px; padding: 15px; }
    .decisao-card { background-color: #1a2a1d; border: 1px solid #2ea043; padding: 20px; border-radius: 12px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ IA-SENTINELA PRO | WHATSAPP SYNC")
st.caption("Status da API: 🟢 Conectado e Ouvindo")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuração")
    medico = st.selectbox("Unidade", ["ANIMA COSTA", "DR. SILVA", "INTERFILE"])
    valor_input = st.number_input("Valor da Rodada", value=2500.0)
    status_input = st.radio("Status", ["LIBERADO", "PENDENTE"])

# Cálculos Sincronizados
acao_final, motivo_final = processar_auditoria(valor_input, status_input)

# Dashboard
c1, c2 = st.columns(2)
with c1:
    st.metric(label="68% LIBERADO", value="R$ 10.880,00")
with c2:
    st.metric(label="32% PENDENTE", value="R$ 5.120,00", delta="-32%", delta_color="inverse")

st.markdown(f"""
    <div class="decisao-card">
        <h2 style="color: #39d353; margin:0;">DECISÃO: {acao_final}</h2>
        <p style="color: #8B949E;">{motivo_final}</p>
    </div>
""", unsafe_allow_html=True)

# Tabela da Favelinha (Insights Ativos Q2)
st.subheader("📊 Tabela da Favelinha")
df = pd.DataFrame({
    "Paciente": ["João Silva", "Maria Oliveira", "Analise Atual"],
    "Status": ["PENDENTE", "PENDENTE", status_input],
    "Insight Ativo (Q2)": ["Erro XML", "Divergência TUSS", f"Ação: {acao_final}"]
})
st.table(df)

st.success(f"Sistema sincronizado com o WhatsApp. Médico: {medico}")
