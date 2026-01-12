import streamlit as st
import pandas as pd
import random

# --- 🏛️ CONFIGURAÇÃO MASTER ---
st.set_page_config(page_title="IA-SENTINELA", page_icon="🏛️", layout="wide")
st.title("🏛️ PORTAL DE AUDITORIA ALPHA VIP")

# --- 🧠 DICIONÁRIO DE INTELIGÊNCIA (VALORES ÚNICOS POR MÉDICO) ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML no lote 402."},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Ausência de assinatura digital no prontuário."},
    "DR. ALPHA TESTE": {"valor": 12000.0, "pacientes": 45, "motivo": "CID-10 incompatível com o procedimento realizado."},
    "DRA. ELENA SILVA": {"valor": 18900.0, "pacientes": 92, "motivo": "Duplicidade de cobrança em exames laboratoriais."},
    "DR. MARCOS PONTES": {"valor": 25000.0, "pacientes": 150, "motivo": "Falta de autorização prévia da operadora."},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Inconsistência cadastral de beneficiários inativos."},
    "DRA. BEATRIZ LINS": {"valor": 14200.0, "pacientes": 60, "motivo": "Glosa técnica por falta de relatório cirúrgico."},
    "DR. RICARDO MELO": {"valor": 19800.0, "pacientes": 88, "motivo": "Material especial cobrado fora da tabela brasíndice."},
    "CENTRO MÉDICO VIP": {"valor": 31000.0, "pacientes": 210, "motivo": "Taxa de sala acima do valor contratualizado."},
    "AUDITORIA GERAL": {"valor": 150000.0, "pacientes": 1200, "motivo": "Múltiplas inconsistências em processamento de lote."}
}

with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico = st.selectbox("Selecione o Médico", list(dados_medicos.keys()))
    
    # Carrega os valores reais de cada médico selecionado
    info = dados_medicos[medico]
    
    valor_total = st.number_input("Faturamento (R$)", value=info["valor"])
    qtd_pacientes = st.slider("Total de Pacientes", 1, 1500, info["pacientes"])
    st.divider()
    st.write("👤 **Auditor:** Sidney Almeida")

# --- 📈 CÁLCULOS TÉCNICOS ---
p_pendente = 32
p_liberado = 68
v_pendente = valor_total * 0.32
v_liberado = valor_total * 0.68
ticket_medio = valor_total / qtd_pacientes

# --- 📊 DASHBOARD SUPERIOR ---
st.subheader(f"📊 Análise Personalizada: {medico}")
c1, c2, c3 = st.columns(3)
with c1: st.metric("PACIENTES", f"{qtd_pacientes}")
with c2: st.metric("TICKET MÉDIO", f"R$ {ticket_medio:,.2f}")
with c3: st.metric("RISCO (32%)", f"R$ {v_pendente:,.2f}", delta="-32%", delta_color="inverse")

# --- 🍕 PIZZA COM RÓTULOS ---
df_pizza = pd.DataFrame({
    "Status": [f"PENDENTE ({p_pendente}%)", f"LIBERADO ({p_liberado}%)"],
    "Valor": [p_pendente, p_liberado]
})

st.vega_lite_chart(df_pizza, {
    'mark': {'type': 'arc', 'innerRadius': 55, 'tooltip': True},
    'encoding': {
        'theta': {'field': 'Valor', 'type': 'quantitative'},
        'color': {
            'field': 'Status', 
            'type': 'nominal', 
            'scale': {'range': ['#ff4b4b', '#1c2e4a']}
        }
    }
}, use_container_width=True)

# --- 🚀 RELATÓRIO DETALHADO (PERSONALIZADO) ---
if st.button("🚀 GERAR RELATÓRIO DETALHADO"):
    st.balloons()
    st.divider()
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 📈 Resumo do Faturamento")
        st.write(f"**Bruto Analisado:** R$ {valor_total:,.2f}")
        st.write(f"**Liquidez Imediata (68%):** R$ {v_liberado:,.2f}")
        st.write(f"**Glosa Projetada (32%):** R$ {v_pendente:,.2f}")
    
    with col_b:
        st.write("### 🔍 Diagnóstico IA-SENTINELA")
        st.write(f"**Médico:** {medico}")
        st.error(f"⚠️ **MOTIVO DA PENDÊNCIA:** {info['motivo']}")
        st.info(f"💡 **DICA:** Ajuste o ticket médio de R$ {ticket_medio:,.2f} para aumentar a margem.")

    st.success(f"✅ Documento oficial de {medico} pronto para auditoria.")
    
