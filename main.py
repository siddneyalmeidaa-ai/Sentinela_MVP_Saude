import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA QUÂNTICA DINÂMICA (INDIVIDUALIZADA POR UNIDADE) ---
st.set_page_config(page_title="IA-SENTINELA | Padrão Ouro", layout="wide")

# Inicializa o banco de memória por médico para evitar conflito de dados
if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 15px; }
    .stTextArea textarea { background-color: #161B22; color: white; border: 1px solid #30363D; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (SERVIDOR SINCRONIZADO) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. DASHBOARD DE GOVERNANÇA ---
st.title("🛡️ Governança de Receita")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")

st.divider()

# --- 4. PERFORMANCE E RISCO (GRÁFICO CORRIGIDO) ---
st.subheader("📈 Performance e Risco por Unidade")
df_chart = df.copy()
df_chart['Em Conformidade'] = df_chart.apply(lambda x: x['valor'] if x['status'] == 'CONFORMIDADE OK' else 0, axis=1)
df_chart['Em Restrição'] = df_chart.apply(lambda x: x['valor'] if x['status'] != 'CONFORMIDADE OK' else 0, axis=1)

chart_data = df_chart.set_index("unidade")[['Em Conformidade', 'Em Restrição']]
st.bar_chart(chart_data, color=["#00c853", "#ff4b4b"])

st.divider()

# --- 5. INTERFACE DE INTERAÇÃO SINCRONIZADA ---
col_rel, col_ia = st.columns([1, 1.2])

with col_rel:
    st.subheader("📋 Relatório de Ativos")
    st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))
    
    st.subheader("🧠 Histórico da Unidade")
    # A Troca do Médico aqui agora sincroniza tudo abaixo
    unidade_atual = st.selectbox("Selecione o Médico para Auditar:", df['unidade'].tolist())
    
    if unidade_atual in st.session_state.memoria_unidades:
        hist = st.session_state.memoria_unidades[unidade_atual]
        st.info(f"Última interação registrada: {hist['data']}")
    else:
        st.write("Sem interações prévias para este médico.")

with col_ia:
    st.subheader("😊 IA de Mediação Humanizada")
    
    # Busca texto salvo para este médico específico para evitar dados estáticos de outros médicos
    texto_inicial = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    
    # CAMPO 1: Recebimento do questionamento
    questionamento = st.text_area(
        f"Mensagem recebida de {unidade_atual}:", 
        value=texto_inicial,
        placeholder="Cole a mensagem do médico aqui...",
        height=150,
        key=f"input_{unidade_atual}" # Chave única evita conflito entre médicos
    )
    
    if st.button("✨ Gerar e Salvar Resposta"):
        if questionamento:
            # CAMPO 2: Geração de Resposta Humanizada de Alta Gestão
            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo perfeitamente a sua frustração; após um plantão, "
                "a última coisa que você precisa é lidar com burocracia financeira. Valorizamos muito o seu tempo. "
                "Para que eu consiga destravar o valor e garantir sua agenda, consegue me ajudar confirmando "
                "apenas o reenvio dos XMLs? Estou acompanhando pessoalmente para mover para CONFORMIDADE OK."
            )
            
            # Salvação Tripla na Memória Quântica
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": datetime.now().strftime("%H:%M:%S"),
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # CAMPO 3: Visualização e Envio para WhatsApp
    if unidade_atual in st.session_state.memoria_unidades:
        res_gerada = st.session_state.memoria_unidades[unidade_atual]['resposta']
        st.success("**Resposta Estratégica Sugerida:**")
        st.write(res_gerada)
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(res_gerada)}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                    🚀 ENVIAR PARA WHATSAPP ({unidade_atual})
                </div>
            </a>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Sidney Pereira de Almeida | Diretor de Compliance")
        
