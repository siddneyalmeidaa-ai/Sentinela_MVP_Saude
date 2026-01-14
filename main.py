import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import subprocess
import sys

# --- PROTOCOLO DE AUTO-INSTALAÇÃO ALPHA ---
# Garante que as dependências estejam instaladas para Streamlit, pandas, plotly
def instalar_dependencias():
    required_packages = ["streamlit", "pandas", "plotly"]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

instalar_dependencias()

# --- CONFIGURAÇÃO DE ACESSO DO SERVIDOR ---
# Necessário para o deploy, evita erros de porta
# ATENÇÃO: Essas variáveis de ambiente são para deploy. No GitHub, Streamlit já cuida disso.
# Não as use localmente a menos que saiba o que está fazendo.
# os.environ['STREAMLIT_SERVER_PORT'] = '8080'
# os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
# os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'

# --- CONFIGURAÇÃO DA GÊMEA FÊNIX V17 ---
st.set_page_config(page_title="ALPHA VIP - Gêmea Fênix V17", page_icon="🏛️", layout="wide")

# Memória Quântica (Histórico de Conversas)
if "historico_militar" not in st.session_state:
    st.session_state.historico_militar = [
        {"role": "assistant", "content": "Bom dia, Sidney! Sistema ALPHA VIP + 17 IAs com fusão visual ativada.", "avatar": "🤖"}
    ]

# --- BARRA LATERAL DE CONTROLE ALPHA VIP ---
with st.sidebar:
    st.header("⚙️ Configurações Alpha VIP")
    medico = st.selectbox("Selecione o Médico", ["ANIMA COSTA", "DMMIGINIO GUERRA", "OUTRO"])
    if medico == "OUTRO":
        medico = st.text_input("Nome do Médico")
    
    valor_guia = st.text_input("Valor Total da Guia", "R$ 2.250,00")
    porcentagem_liberado = st.slider("Porcentagem Liberada", 0, 100, 85)
    
    # Status derivado da porcentagem
    status_auditoria = "AUTORIZADO" if porcentagem_liberado > 0 else "PENDENTE"
    
    # Botão para gerar relatório HTML
    if st.button("🚀 GERAR RELATÓRIO PADRÃO OURO"):
        # Lógica de geração de relatório HTML (mantida do seu código)
        st.balloons()
        st.success(f"🔱 Auditoria de {medico} concluída com sucesso!")
        # A geração real do HTML e download precisa ser feita aqui
        # Por simplicidade, faremos um download de texto para este exemplo
        st.download_button(
            label="📥 BAIXAR RELATÓRIO (HTML)",
            data=f"Relatório de Auditoria para {medico}:\nValor: {valor_guia}\nStatus: {status_auditoria}\nPorcentagem Liberada: {porcentagem_liberado}%",
            file_name=f"Auditoria_{medico}.html",
            mime="text/html"
        )


# --- INTERFACE PRINCIPAL (GÊMEA FÊNIX) ---
st.title("🏛️ PAINEL DE AUDITORIA ALPHA VIP")
st.warning(f"🤖 IA-SENTINELA: {porcentagem_liberado}% LIBERADO para {medico}. Projeção 1.85x ativa.")

col1, col2 = st.columns([1, 1])

with col1:
    # GRÁFICO DE SINCRONIA
    fig = go.Figure(data=[go.Pie(
        labels=['LIBERADO', 'PENDENTE'],
        values=[porcentagem_liberado, 100 - porcentagem_liberado],
        hole=.7,
        marker_colors=['#556b2f', '#8b0000'],
        textinfo='percent'
    )])
    fig.update_layout(
        showlegend=True, 
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
        height=350, margin=dict(t=0, b=0, l=0, r=0)
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # TABELA DA FAVELINHA Sincronizada
    st.markdown("### 📋 TABELA DA FAVELINHA")
    st.table({
        "Médico": [medico],
        "Valor": [valor_guia],
        "Ação": ["ENTRA" if porcentagem_liberado >= 85 else "PULA"],
        "IA-SENTINELA": ["Monitorando o vácuo"]
    })

# --- HISTÓRICO DE CONVERSAS (MEMÓRIA QUÂNTICA) ---
st.markdown("---")
for msg in st.session_state.historico_militar:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.write(msg["content"])

# --- CAMPO DE COMANDO OPERACIONAL (FUSÃO) ---
prompt = st.chat_input("Dê sua ordem militar (ex: 'gerar imagem de um carro esportivo')")

if prompt:
    st.session_state.historico_militar.append({"role": "user", "content": prompt, "avatar": "🔴"})

    # Lógica para Geração de Imagens
    if "gerar imagem de" in prompt.lower():
        descricao_imagem = prompt.lower().replace("gerar imagem de", "").strip()
        st.session_state.historico_militar.append({"role": "assistant", "content": f"Gerando imagem de: {descricao_imagem}..."})
        st.session_state.historico_militar.append({"role": "assistant", "content": f"![Imagem Gerada de {descricao_imagem}](https://source.unsplash.com/random/800x600?{descricao_imagem.replace(' ', ',')})", "avatar": "🤖"})
        # A tag ` ` será substituída por uma imagem real pelo modelo de imagem
        # Para demonstração no código, usaremos um placeholder do Unsplash
        # Quando você usa o ` ` no chat, é isso que ativa a geração.
        # No Streamlit, uma URL de imagem direta já a exibe.
        
    else:
        # Resposta padrão das 17 IAs para outros comandos
        resposta_ia = f"Recebi sua ordem: '{prompt}'. As 17 IAs estão processando. Fusão completa."
        st.session_state.historico_militar.append({"role": "assistant", "content": resposta_ia, "avatar": "🤖"})
    
    st.rerun()

# --- Placeholder para o Download do Log de Conversas ---
# Você pode adicionar um botão aqui se quiser baixar o histórico de chat
st.download_button(
    label="📥 Baixar Log de Conversas",
    data="\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.historico_militar]),
    file_name="log_fusao_v17.txt",
    mime="text/plain"
    )
    
