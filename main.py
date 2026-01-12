import streamlit as st
import pandas as pd

# --- 🏛️ CONFIGURAÇÃO MASTER ---
st.set_page_config(page_title="IA-SENTINELA", page_icon="🏛️", layout="wide")
st.title("🏛️ PORTAL DE AUDITORIA ALPHA VIP")

# --- 🧠 DICIONÁRIO DINÂMICO (CADA MÉDICO COM SEU VALOR REAL) ---
dados_medicos = {
    "ANIMA COSTA": {"valor": 16000.0, "pacientes": 85, "motivo": "Divergência de XML no lote 402."},
    "DMMIGINIO GUERRA": {"valor": 22500.0, "pacientes": 110, "motivo": "Ausência de assinatura digital no prontuário."},
    "DR. ALPHA TESTE": {"valor": 12000.0, "pacientes": 45, "motivo": "CID-10 incompatível com o procedimento."},
    "DRA. ELENA SILVA": {"valor": 18900.0, "pacientes": 92, "motivo": "Duplicidade de cobrança detectada."},
    "DR. MARCOS PONTES": {"valor": 25000.0, "pacientes": 150, "motivo": "Falta de autorização prévia da operadora."},
    "CLÍNICA SÃO JOSÉ": {"valor": 45000.0, "pacientes": 320, "motivo": "Inconsistência cadastral de beneficiários."},
    "DRA. BEATRIZ LINS": {"valor": 14200.0, "pacientes": 60, "motivo": "Glosa técnica: falta de relatório cirúrgico."},
    "DR. RICARDO MELO": {"valor": 19800.0, "pacientes": 88, "motivo": "Material especial fora da tabela brasíndice."},
    "CENTRO MÉDICO VIP": {"valor": 31000.0, "pacientes": 210, "motivo": "Taxa de sala acima do valor contratual."},
    "AUDITORIA GERAL": {"valor": 150000.0, "pacientes": 1200, "motivo": "Múltiplas inconsistências em processamento."}
}

with st.sidebar:
    st.header("⚙️ Painel de Controle")
    medico_sel = st.selectbox("Selecione o Médico", list(dados_medicos.keys()))
    
    # BUSCA OS DADOS DO MÉDICO SELECIONADO
    info = dados_medicos[medico_sel]
    
    # PERMITE AJUSTE MANUAL SE PRECISAR
    faturamento_real = st.number_input("Faturamento (R$)", value=info["valor"])
    pacientes_real = st.number_input("Total de Pacientes", value=info["pacientes"])
    st.divider()
    st.write("👤 **Auditor:** Sidney Almeida")

# --- 📈 CÁLCULOS EM TEMPO REAL (MUDAM COM O MÉDICO) ---
# Definimos 32% como a margem de risco padrão da sua auditoria
v_pendente = faturamento_real * 0.32
v_liberado = faturamento_real * 0.68
tkt_medio = faturamento_real / pacientes_real if pacientes_real > 0 else 0

# --- 📊 DASHBOARD SUPERIOR ---
st.subheader(f"📊 Relatório Alpha: {medico_sel}")
c1, c2, c3 = st.columns(3)
with c1: st.metric("PACIENTES", f"{pacientes_real}")
with c2: st.metric("TICKET MÉDIO", f"R$ {tkt_medio:,.2f}")
with c3: st.metric("EM RISCO (32%)", f"R$ {v_pendente:,.2f}", "-32%")

# --- 🍕 PIZZA DINÂMICA (RÓTULOS ATUALIZADOS) ---
df_pizza = pd.DataFrame({
    "Status": [f"PENDENTE (R$ {v_pendente:,.2f})", f"LIBERADO (R$ {v_liberado:,.2f})"],
    "Percentual": [32, 68]
})

st.vega_lite_chart(df_pizza, {
    'mark': {'type': 'arc', 'innerRadius': 50, 'tooltip': True},
    'encoding': {
        'theta': {'field': 'Percentual', 'type': 'quantitative'},
        'color': {
            'field': 'Status', 
            'type': 'nominal', 
            'scale': {'range': ['#ff4b4b', '#1c2e4a']}
        }
    }
}, use_container_width=True)

# --- 🚀 RELATÓRIO DETALHADO (CALCULADO NA HORA) ---
if st.button("🚀 GERAR RELATÓRIO DETALHADO"):
    st.balloons()
    st.divider()
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 📈 Detalhamento Financeiro")
        st.write(f"**Médico Selecionado:** {medico_sel}")
        st.write(f"**Faturamento Bruto:** R$ {faturamento_real:,.2f}")
        st.write(f"**Fatia Liberada (68%):** R$ {v_liberado:,.2f}")
        st.warning(f"**Fatia em Risco (32%):** R$ {v_pendente:,.2f}")
    
    with col_b:
        st.write("### 🔍 Diagnóstico Técnico")
        st.error(f"⚠️ **MOTIVO DA PENDÊNCIA:** {info['motivo']}")
        st.info(f"💡 **ANÁLISE:** O ticket médio de R$ {tkt_medio:,.2f} está sendo impactado pelas glosas identificadas.")

    st.success(f"✅ Auditoria de {medico_sel} concluída com valores reais.")
    
