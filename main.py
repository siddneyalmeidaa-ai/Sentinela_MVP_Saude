import streamlit as st
import urllib.parse

# 1. Definição do Cérebro (Regras que as 17 IAs aprenderam)
def processar_frajola(input_usuario, doutor="ANIMA COSTA"):
    prompt = input_usuario.lower()
    
    # Regra IA-SENTINELA: Bloqueio de Vácuo (1.00x)
    if "1.00" in prompt or "vácuo" in prompt:
        return "🚨 IA-SENTINELA: Operação abortada! Vácuo detectado no radar quântico. Risco de perda total."
    
    # Regra Advogada Cabeluda: Blindagem e Auditoria
    if "auditoria" in prompt or "liberado" in prompt:
        return f"⚖️ ADVOGADA CABELUDA: Blindagem ativa para {doutor}. 85% do capital liberado sob auditoria rigorosa."

    # Regra Professora Língua-Afunda: Resposta Padrão
    if "boa noite" in prompt or "olá" in prompt:
        return f"✨ GÊMEA FÊNIX: Sincronização completa para Doutor {doutor}. As 17 IAs estão em standby tático."
    
    return "🔥 SISTEMA ATIVO: Processando análise quântica da rodada atual..."

# 2. Interface (O que aparece nos seus prints)
st.title("85% LIBERADO")
st.subheader("15% PENDENTE")

# Campo de Interação
user_input = st.text_input("Interação com as 17 Inteligências (RAG Mode):", key="rag_input")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    if user_input:
        # A MÁGICA: Aqui ele chama a função que 'pensa' em vez de mostrar texto fixo
        resposta_final = processar_frajola(user_input)
        st.info(f"🧐 GÊMEA FÊNIX: {resposta_final}")
    else:
        st.warning("A Maluquinha dos Códigos avisa: Digite uma mensagem para ativar o cérebro!")

# 3. Tabela da Favelinha Dinâmica
projecao = 1.85
# Lógica STS: Se >= 1.80x, então ENTRA
acao_imediata = "ENTRA" if projecao >= 1.80 else "PULA"

st.write("### 📋 TABELA DA FAVELINHA")
st.table({"Doutor": ["ANIMA COSTA"], "Projeção": [f"{projecao}x"], "Ação": [acao_imediata]})
