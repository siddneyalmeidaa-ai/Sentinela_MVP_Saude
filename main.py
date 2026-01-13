import streamlit as st
import pandas as pd
import urllib.parse

# --- 1. CONFIGURAÇÃO DE ALTO NÍVEL ---
st.set_page_config(page_title="IA-SENTINELA | Gestão Humanizada", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 15px; }
    .stTextArea textarea { background-color: #161B22; color: white; border: 1px solid #30363D; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (SERVIDOR ESTRATÉGICO) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)
total_consolidado = df["valor"].sum()

# --- 3. DASHBOARD DE GOVERNANÇA ---
st.title("🛡️ SENTINELA | Inteligência Humanizada")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {total_consolidado:,.2f}")

st.divider()

# --- 4. GRÁFICO DE PERFORMANCE (ESCALA CORRIGIDA) ---
st.subheader("📈 Performance e Conformidade por Unidade")
df_chart = df.copy()
df_chart['Conformidade'] = df_chart.apply(lambda x: x['valor'] if x['status'] == 'CONFORMIDADE OK' else 0, axis=1)
df_chart['Restrição/Análise'] = df_chart.apply(lambda x: x['valor'] if x['status'] != 'CONFORMIDADE OK' else 0, axis=1)

chart_data = df_chart.set_index("unidade")[['Conformidade', 'Restrição/Análise']]
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"])

# --- 5. MÓDULO DE INTERAÇÃO INTELIGENTE (MÉDICO) ---
st.divider()
col_a, col_b = st.columns([1, 1.2])

with col_a:
    st.subheader("📋 Relatório Analítico")
    st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))

with col_b:
    st.subheader("🤖 IA de Mediação Humanizada")
    
    # RECLAMAÇÃO DO MÉDICO PARA TESTE
    reclamacao_medico = (
        "Sidney, acabei de sair do plantão e vi que o repasse das minhas cirurgias "
        "ainda não caiu. Isso é um descaso com o meu tempo! Já enviei os prontuários "
        "e as guias assinadas. Preciso que libere esse valor de R$ 5.400,00 agora, "
        "senão não terei como manter minha agenda da próxima semana com vocês."
    )
    
    entrada = st.text_area("Mensagem do Médico:", value=reclamacao_medico, height=180)
    
    if st.button("✨ Gerar Resposta Humanizada"):
        # LÓGICA DE EMPATIA + SOLUÇÃO
        resposta_final = (
            "Olá, Doutor. Entendo perfeitamente a sua frustração; após um plantão, a última coisa que você precisa é lidar com burocracia financeira. "
            "Valorizamos muito o seu tempo e a sua parceria. Verifiquei aqui que o valor de R$ 5.400,00 está retido apenas por um detalhe técnico de validação no sistema. "
            "Para que eu consiga destravar isso agora e garantir a sua agenda da semana que vem sem preocupações, consegue me ajudar confirmando apenas o reenvio dos arquivos XML? "
            "Estou pessoalmente acompanhando para que, assim que você enviar, o sistema mude para CONFORMIDADE OK e o pagamento siga o fluxo prioritário."
        )
        
        st.success("**Resposta Estratégica Sugerida:**")
        st.write(resposta_final)
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta_final)}"
        st.link_button("🚀 Enviar para o WhatsApp", link_zap)

# --- 6. RODAPÉ ---
st.divider()
st.caption("Sidney Pereira de Almeida | Diretor de Compliance")
