import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- CLASSE CORE GF-17 (SISTEMA DE ELITE) ---
class GF17_Elite:
    def __init__(self):
        # 1. MEMÓRIA DE LONGO PRAZO (Onde a IA tira a informação)
        # Em um cenário real, isso viria de um arquivo .json ou banco de dados
        self.banco_dados = {
            "ANIMA COSTA": {"liberado": 85, "pendente": 15, "proj_x": 1.85},
            "INTERFILE - BI": {"liberado": 40, "pendente": 60, "proj_x": 1.00}, # VÁCUO
            "DR. MARCOS": {"liberado": 70, "pendente": 30, "proj_x": 2.10}
        }

    def processar_decisao(self, dr, comando_sidney):
        dados = self.banco_dados.get(dr)
        x = dados["proj_x"]
        
        # Lógica IA-SENTINELA: Defesa de Vácuo (1.00x)
        if x == 1.00:
            msg = "⚠️ ALERTA IA-SENTINELA: VÁCUO DETECTADO (1.00x). Operação abortada para proteção de ROI."
            return "PULA", msg, "error"
        
        # Lógica CFO VISION: Execução baseada no comando
        if any(cmd in comando_sidney.lower() for cmd in ["pode", "liberar", "pagar"]):
            msg = f"✅ CFO VISION: Ordem executada. {dr} com Projeção {x}x enviado para ENTRA."
            return "ENTRA", msg, "success"
        
        return "PULA", f"🧐 GÊMEA FÊNIX: Aguardando gatilho tático para {dr} ({x}x).", "info"

# --- INTERFACE DE EXECUÇÃO ---
st.set_page_config(page_title="GF-17 CORE", layout="wide")
st.title("🛡️ GÊMEA FÊNIX 17 | Versão 2026.1.14")

if 'brain' not in st.session_state:
    st.session_state.brain = {"acao": "PULA", "msg": "Sistemas em Stand-by", "tipo": "info"}

core = GF17_Elite()

# --- INPUT E MÉTRICAS ---
dr_selecionado = st.selectbox("Doutor Responsável:", list(core.banco_dados.keys()))
dados_dr = core.banco_dados[dr_selecionado]

# Substituindo palavras por % reais (Regra CFO VISION)
c1, c2 = st.columns(2)
c1.metric(f"ESTATUTO {dr_selecionado}", f"{dados_dr['liberado']}% LIBERADO")
c2.metric("EM AUDITORIA", f"{dados_dr['pendente']}% PENDENTE")

comando = st.text_input("Interação com as 17 Inteligências (RAG Mode):")

if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
    acao, parecer, tipo = core.processar_decisao(dr_selecionado, comando)
    st.session_state.brain = {"acao": acao, "msg": parecer, "tipo": tipo}

# --- TABELA DA FAVELINHA (PADRÃO OURO) ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA")
df_fav = pd.DataFrame([{
    "Doutor": dr_selecionado,
    "Projeção Rodada": f"{dados_dr['proj_x']}x",
    "Ação Imediata": st.session_state.brain["acao"]
}])
st.table(df_fav)

# Exibição do Parecer da IA
res = st.session_state.brain
if res["tipo"] == "success": st.success(res["msg"])
elif res["tipo"] == "error": st.error(res["msg"])
else: st.info(res["msg"])

# FIX MOBILE: URL Encoding (Maluquinha dos Códigos)
msg_link = urllib.parse.quote(res["msg"])
st.markdown(f'<a href="https://wa.me/5511942971753?text={msg_link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)
