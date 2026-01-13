import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz

# --- 1. CONFIGURAÇÃO DE TEMPO REAL (BRASÍLIA) E MEMÓRIA ---
st.set_page_config(page_title="IA-SENTINELA | Padrão Ouro", layout="wide")

# Força o fuso horário de Brasília (America/Sao_Paulo)
fuso_br = pytz.timezone('America/Sao_Paulo')

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

# --- 2. BASE DE DADOS SINCRONIZADA ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. DASHBOARD DE GOVERNANÇA (VISUALIZAÇÃO COMPLETA) ---
st.title("🛡️ Sentinela: Governança & Mediação")
st.metric(label="📊 VALOR TOTAL CONSOLIDADO EM AUDITORIA", value=f"R$ {df['valor'].sum():,.2f}")

# Gráfico de Performance Restaurado
st.subheader("📈 Performance e Risco por Unidade")
df_chart = df.copy()
df_chart['OK'] = df_chart.apply(lambda x: x['valor'] if x['status'] == 'CONFORMIDADE OK' else 0, axis=1)
df_chart['RESTRIÇÃO'] = df_chart.apply(lambda x: x['valor'] if x['status'] != 'CONFORMIDADE OK' else 0, axis=1)
st.bar_chart(df_chart.set_index("unidade")[['OK', 'RESTRIÇÃO']], color=["#00c853", "#ff4b4b"])

st.divider()

# --- 4. ÁREA DE INTERAÇÃO E MEMÓRIA DE DIRETORIA ---
col_dados, col_ia = st.columns([1, 1.2])

with col_dados:
    st.subheader("📋 Relatório de Ativos")
    st.table(df[["unidade", "valor", "status"]].rename(columns={"unidade": "Unidade", "valor": "R$", "status": "Veredito"}))
    
    st.subheader("🧠 Histórico Sincronizado")
    # Seleção de médico que sincroniza todo o histórico abaixo
    unidade_atual = st.selectbox("Selecione o Médico/Unidade para Auditar:", df['unidade'].tolist(), key="main_selector")
    
    if unidade_atual in st.session_state.memoria_unidades:
        hist = st.session_state.memoria_unidades[unidade_atual]
        st.warning(f"📌 **Motivo:** {hist.get('motivo', 'Não classificado')}")
        st.info(f"🕒 **Horário (Brasília):** {hist.get('data', '--:--')}")
    else:
        st.write("Sem registros prévios para esta unidade hoje.")

with col_ia:
    st.subheader("😊 IA de Mediação Humanizada")
    
    # Busca o texto que já estava no campo para este médico (se houver)
    texto_persistente = st.session_state.memoria_unidades.get(unidade_atual, {}).get('entrada', "")
    
    # Campo de Entrada: Sincronizado individualmente por médico
    questionamento = st.text_area(
        f"Mensagem recebida de {unidade_atual}:", 
        value=texto_persistente,
        placeholder="Cole aqui o que o médico enviou...",
        height=150,
        key=f"input_area_{unidade_atual}" 
    )
    
    if st.button("✨ Gerar Resposta e Classificar"):
        if questionamento:
            # Captura a hora REAL no fuso de Brasília
            agora_br = datetime.now(fuso_br).strftime("%H:%M:%S")
            
            # Inteligência de Motivo Automática
            if any(word in questionamento.lower() for word in ["repasse", "pagamento", "caiu", "dinheiro"]):
                motivo_id = "Reclamação Financeira"
            elif any(word in questionamento.lower() for word in ["agenda", "cirurgia", "plantão"]):
                motivo_id = "Urgência de Agenda"
            else:
                motivo_id = "Dúvida Técnica / Documental"

            # Resposta Humanizada de Alta Gestão
            resposta_ia = (
                f"Olá, {unidade_atual}. Entendo perfeitamente a sua frustração; após um plantão, "
                "a última coisa que você precisa é lidar com burocracia financeira. Valorizamos seu tempo. "
                "Para que eu consiga destravar o valor e garantir sua agenda da semana que vem sem preocupações, "
                "consegue me ajudar confirmando o envio dos arquivos XML? Estou acompanhando pessoalmente."
            )
            
            # Salvação na Memória Individualizada
            st.session_state.memoria_unidades[unidade_atual] = {
                "data": agora_br,
                "motivo": motivo_id,
                "entrada": questionamento,
                "resposta": resposta_ia
            }
            st.rerun()

    # Visualização da Sugestão e Envio
    if unidade_atual in st.session_state.memoria_unidades:
        res = st.session_state.memoria_unidades[unidade_atual]['resposta']
        motivo_badge = st.session_state.memoria_unidades[unidade_atual].get('motivo')
        st.success(f"**Parecer Sugerido ({motivo_badge}):**")
        st.write(res)
        
        link_zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(res)}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                    🚀 ENVIAR PARA WHATSAPP ({unidade_atual})
                </div>
            </a>
        """, unsafe_allow_html=True)

st.divider()
# Rodapé com Horário de Brasília sincronizado com o sistema
st.caption(f"Sidney Pereira de Almeida | Diretor de Compliance | Brasília: {datetime.now(fuso_br).strftime('%d/%m/%Y %H:%M')}")
