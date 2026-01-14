import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# --- 1. PERSONA 17: MALUQUINHA DOS CÓDIGOS (NÚCLEO DE MEMÓRIA) ---
def carregar_memoria_longo_prazo():
    if os.path.exists('memoria_fenix.json'):
        with open('memoria_fenix.json', 'r') as f:
            return json.load(f)
    return {"aprendizados": [], "preferencias_sidney": {}, "historico_geral": []}

def salvar_na_mente(dado):
    mente = carregar_memoria_longo_prazo()
    mente["historico_geral"].append(dado)
    with open('memoria_fenix.json', 'w') as f:
        json.dump(mente, f)

# Inicialização da Memória de Trabalho para evitar KeyError
if 'memoria_trabalho' not in st.session_state:
    st.session_state.memoria_trabalho = carregar_memoria_longo_prazo()

# --- 2. MOTOR DE RACIOCÍNIO (CORE DAS 17 PERSONAS) ---
class IAInfinita:
    def __init__(self, doutor):
        self.doutor = doutor
        # Aqui a IA "tira a informação" da memória persistente
        self.contexto = st.session_state.memoria_trabalho

    def gerar_insight(self, comando):
        # Lógica de decisão proativa baseada no histórico
        if "pagar" in comando.lower() or "liberar" in comando.lower():
            acao = "Entra"
            msg = f"CFO Vision: Identificado padrão de confiança. Liberando R$ 12.500,00 para {self.doutor}."
        else:
            acao = "Pula"
            msg = f"IA-Sentinela: Analisando contexto. Aguardando gatilho de segurança para {self.doutor}."
        
        # Salva o aprendizado na memória eterna
        salvar_na_mente({"data": str(datetime.now()), "dr": self.doutor, "cmd": comando, "acao": acao})
        return msg, acao

# --- 3. INTERFACE GÊMEA FÊNIX BONDE 2.0 ---
st.title("🛡️ GÊMEA FÊNIX BONDE: IA PROPRIETÁRIA")

dr_alvo = st.selectbox("Doutor Responsável:", ["ANIMA COSTA", "INTERFILE - BI", "DR. MARCOS"])
cmd = st.text_input("Comando para as 17 Inteligências:")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    brain = IAInfinita(dr_alvo)
    parecer, acao_final = brain.gerar_insight(cmd)
    
    st.info(f"**Parecer das 17 IAs:** {parecer}")
    
    # Tabela da Favelinha (Visível e Proativa)
    df_favelinha = pd.DataFrame([{"Doutor": dr_alvo, "Ação": acao_final, "Status": "Sincronizado"}])
    st.table(df_favelinha)

# Exibição da Memória (Opcional para Auditoria)
with st.expander("📜 Acessar Memória de Longo Prazo"):
    st.write(carregar_memoria_longo_prazo()["historico_geral"])
    
