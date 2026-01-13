import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. CONFIGURAÇÃO E MEMÓRIA DINÂMICA ---
st.set_page_config(page_title="IA-SENTINELA | Sincronizado", layout="wide")

# Inicializa o banco de memória se não existir
if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] { background-color: #161B22; border-radius: 12px; border: 1px solid #30363D; padding: 15px; }
    .stTextArea textarea { background-color: #161B22; color: white; border: 1px solid #30363D; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DADOS (SERVIDOR ATUALIZADO) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. CABEÇALHO ---
st.title("🛡️ Governança Sincronizada")
st.metric(label="📊 TOTAL CONSOLIDADO", value=f"R$ {df['valor'].sum():,.2f}")

st.divider()

# --- 4. ÁREA DE INTERAÇÃO SINCRONIZADA ---
col_dados, col_ia = st.columns([1, 1.2])

with col_dados:
    st.subheader("📋 Relatório de Ativos")
    st.table(df[["unidade", "valor", "status"]])
    
    st.subheader("🧠 Histórico da Unidade")
    unidade_atual = st.selectbox("Selecione o Médico/Unidade para Auditar:", df['unidade'].tolist())
    
    # Busca memória específica da unidade para evitar dados estáticos
    if unidade_atual in st.session_state.memoria_unidades:
        hist = st.session_state.memoria_unidades[unidade_atual]
        st.info(f"Última interação: {hist['data']}")
    else:
        st.write("Sem interações prévias para esta unidade.")

with col_ia:
    st.subheader("😊 IA de Mediação Humanizada")
    
    # Campo 1: Recebimento do Questionamento (Limpa ao trocar unidade se não houver salvo)
    default_msg = "" if unidade_atual not in st.session_state.memoria_unidades else st.session_state.memoria_unidades[unidade_atual]['entrada']
    
    questionamento = st.text_area(
        f"Mensagem recebida de {unidade_atual}:", 
        value=default_msg,
        placeholder="Cole aqui o que o médico enviou...",
        height=150,
        key=f"input_{unidade_atual}" # Chave única por unidade garante a sincronia
    )
    
    # Campo 2: Resposta Inteligente
    if st.button("✨ Gerar Resposta Estratégica"):
        if questionamento:
            # Lógica de resposta humanizada personalizada por unidade
            status_unidade = df[df['unidade'] == unidade_atual]['status'].values[0]
            
            resposta_ia = (
                f"Olá, {unidade_atual}. Compreendo o seu posicionamento. "
                f"No momento, o sistema aponta status de {status_unidade}. "
                "Para que possamos avançar para a CONFORMIDADE OK e liberar o fluxo, "
                "precisamos apenas validar o XML pendente. Estou acompanhando pessoalmente."
            )
            
            # Salva na Memória Quântica da Unidade
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": datetime.now().strftime("%H:%M"),
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # Campo 3: Envio e Visualização
    if unidade_atual in st.session_state.memoria_unidades:
        res = st.session_state.memoria_unidades[unidade_atual]['resposta']
        st.success("**Sugestão de Resposta:**")
        st.write(res)
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(res)}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                    🚀 ENVIAR RESPOSTA PARA {unidade_atual}
                </div>
            </a>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Sidney Pereira de Almeida | Diretor de Compliance")
        
