import streamlit as st
import pandas as pd

# CONFIGURAÇÃO PADRÃO OURO - IA-SENTINELA PRO
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

st.title("🛡️ IA-SENTINELA PRO | Sistema de Auditoria 2026")
st.subheader("Foco: Eliminação de Vácuo Operacional (1.00x)")

# 1. ENTRADA DE DADOS DA RODADA
with st.sidebar:
    st.header("⚙️ Configuração da Rodada")
    doctor_name = st.selectbox("Selecione o Doutor", ["Dr. Silva", "Dra. Maria", "Dr. Santos"])
    venda_valor = st.number_input("Valor da Rodada", min_value=0.0, value=1000.0)
    status_inicial = st.selectbox("Status Atual", ["LIBERADO", "PENDENTE"])

# 2. LÓGICA DE AUDITORIA (O "X" DA PROJEÇÃO)
def processar_decisao(valor, status):
    # Regra: Se estiver no vácuo (Death Zone), a IA bloqueia
    if valor <= 1.00:
        return "PULA (Vácuo Detectado)", "🔴"
    elif status == "PENDENTE":
        return "NÃO ENTRA (Aguardando Liberação)", "🟡"
    else:
        return "ENTRA (Operação Liberada)", "🟢"

decisao, icone = processar_decisao(venda_valor, status_inicial)

# 3. INTERFACE VISUAL (PADRÃO EXECUTIVO)
col1, col2 = st.columns(2)

with col1:
    st.metric(label=f"Métrica: {status_inicial}", value=f"{venda_valor} pts", delta="Status Sincronizado")
    st.write(f"### Ação Imediata: {icone} {decisao}")

with col2:
    # Simulação da Tabela da Favelinha para Auditoria
    st.write("### 📊 Tabela da Favelinha")
    data = {
        "Rodada": ["Atual", "Projeção +1", "Projeção +2"],
        "Ação": [decisao, "Analisando...", "Aguardando"],
        "Risco": ["1.00x" if venda_valor <= 1.00 else "Baixo", "-", "-"]
    }
    st.table(data)

# 4. BOTÃO DE DOWNLOAD (CONFIGURADO SEM ERRO DE ACENTO)
csv = pd.DataFrame(data).to_csv(index=False).encode('utf-8')
st.download_button(
    label="Baixar Relatorio de Auditoria",
    data=csv,
    file_name='relatorio_ia_sentinela.csv',
    mime='text/csv',
)

st.success(f"Sistema sincronizado para {doctor_name}. Nenhuma morte operacional detectada.")
