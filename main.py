import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import random

# --- 1. CONFIGURAÇÃO E BLINDAGEM ---
st.set_page_config(page_title="IA-SENTINELA | Projeto Embrião", layout="wide")
fuso_br = pytz.timezone('America/Sao_Paulo')

if 'memoria_unidades' not in st.session_state:
    st.session_state.memoria_unidades = {}

st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 0.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BASE DE DATA (AUDITORIA VIVA) ---
db = [
    {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
    {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
    {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
    {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
    {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
]
df = pd.DataFrame(db)

# --- 3. MOTOR PROJETO EMBRIÃO (O DELINEADO DAS 179 IAs) ---
def motor_embriao_sentinela(unidade, msg_medico, status):
    msg_low = msg_medico.lower().strip()
    
    # Matriz de Personalidade Sentinela (Não-robótica)
    saudacoes_vivas = ["Olá", "Como vai", "Tudo bem", "Saudações"]
    validacao_parceria = [
        "é sempre um prazer falar com sua equipe",
        "sabemos do seu compromisso com os atendimentos",
        "sua produção é fundamental para o sistema"
    ]
    
    # 🧬 O CÉREBRO: Decisão baseada no Veredito (Status)
    if status == "RESTRIÇÃO":
        argumento_core = (
            "identifiquei aqui que o seu repasse está em uma 'trava de conformidade' por falta de XML. "
            "Para eu conseguir puxar seu pagamento para o lote prioritário agora
            
