import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# --- PERSONA 17: MALUQUINHA DOS CÓDIGOS (NÚCLEO DE MEMÓRIA) ---
def gerenciar_memoria_eterna():
    arquivo = 'memoria_fenix_bonde.json'
    # Se o arquivo não existir, cria o subconsciente da IA
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump({"aprendizados": [], "configuracoes": {}}, f)
    
    with open(arquivo, 'r') as f:
        return json.load(f)

# Inicialização para evitar o KeyError
if 'brain_state' not in st.session_state:
    st.session_state.brain_state = {"acao": "Pula", "msg": "Iniciando sistemas..."}

# --- MOTOR DE RACIOCÍNIO PROATIVO ---
class InteligenciaFenix:
    def __init__(self, doutor):
        self.doutor = doutor
        self.valor_unidade = 12500.00 # Extraído da sua interface

    def decidir(self, comando):
        # A IA agora identifica intenções proativamente
        cmd = comando.lower()
        if any(x in cmd for x in ["pagar", "liberar", "autorizar"]):
            return "Entra", f"CFO Vision: Autorizando R$ {self.valor_unidade:,.2f} para {self.doutor}."
        
        # Regra do Vácuo (Persona 12)
        return "Pula", f"IA-Sentinela: Aguardando conformidade para {self.doutor}."

# --- INTERFACE GF-17 (VERSÃO 2.0 RAG) ---
st.title("🛡️ GÊMEA FÊNIX BONDE | RAG Ativado")

# Métricas Dinâmicas baseadas no Doutor
st.subheader(f"ESTATUTO ANIMA COSTA: 85% LIBERADO")

dr = st.selectbox("Doutor Responsável:", ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS"])
msg_sidney = st.text_input("Interação com as 17 Inteligências:")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    ia = InteligenciaFenix(dr)
    acao, parecer = ia.decidir(msg_sidney)
    st.session_state.brain_state = {"acao": acao, "msg": parecer}

# Exibição da Tabela da Favelinha (Sempre Visível)
df_fav = pd.DataFrame([{"Doutor": dr, "Ação": st.session_state.brain_state["acao"], "Status": "Sincronizado"}])
st.table(df_fav)

st.info(st.session_state.brain_state["msg"])
