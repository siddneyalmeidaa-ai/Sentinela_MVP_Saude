import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO VISUAL MASTER & BLINDAGEM ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide")

# ESTE BLOCO OCULTA O MENU, O BOTÃO GITHUB E O FOOTER "MADE WITH STREAMLIT"
st.markdown("""
    <style>
    /* Oculta o cabeçalho padrão do Streamlit (Botões da direita) */
    header {visibility: hidden;}
    
    /* Oculta o rodapé padrão */
    footer {visibility: hidden;}
    
    /* Ajusta o espaçamento para compensar o cabeçalho oculto */
    .main .block-container { padding-top: 1rem; }

    .header-box { 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 15px; background: #1c232d; border-radius: 10px;
        border-bottom: 2px solid #00d4ff; margin-bottom: 20px;
    }
    .pro-tag { background: #00d4ff; color: #12171d; padding: 2px 8px; border-radius: 5px; font-weight: 900; font-size: 0.7rem; }
    
    .report-preview { 
        background: #f8f9fa; color: #1a1a1a; padding: 20px; 
        border-radius: 8px; font-family: 'Courier New', monospace; 
        font-size: 0.85rem; border: 1px solid #dee2e6; white-space: pre-wrap;
    }
    </style>
    
    <div class="header-box">
        <span style="color: white; font-size: 1.2rem;">🏛️ CONTROLE: <b>IA-SENTINELA</b></span> 
        <span class="pro-tag">PRO V17 - PROTEGIDO</span>
    </div>
    """, unsafe_allow_html=True)

# --- CONTINUAÇÃO DO CÓDIGO (DADOS E LÓGICA) ---
# Use a base de dados corrigida que enviamos anteriormente para evitar o SyntaxError
dados_medicos = {
    "ANIMA COSTA": {
        "valor": 16000.0, "motivo": "Divergência de XML", "risco": 15,
        "detalhes": [["João Silva", "XML Inválido"], ["Maria Oliveira", "Divergência Tuss"]]
    },
    "DMMIGINIO GUERRA": {
        "valor": 22500.0, "motivo": "Assinatura Digital", "risco": 45,
        "detalhes": [["João Souza", "Falta Assinatura"], ["Ana Costa", "Falta Assinatura"]]
    },
    "CLÍNICA SÃO JOSÉ": {
        "valor": 45000.0, "motivo": "Erro Cadastral", "risco": 18,
        "detalhes": [["Carlos Luz", "CPF Inválido"], ["Bia Rosa", "Guia Ausente"]]
    }
}

# (O restante do código de abas, gráficos e relatório permanece o mesmo)
