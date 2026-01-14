import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# --- 1. MEMÓRIA QUÂNTICA (NÚCLEO RAG) ---
# Inicialização da estrutura de memória para evitar perdas de contexto
if 'historico_sentinela' not in st.session_state:
    st.session_state.historico_sentinela = []
if 'estado_decisao' not in st.session_state:
    st.session_state.estado_decisao = {"msg": "Aguardando comando...", "acao": "Pula", "cor": "info"}

class NucleoFenix:
    def __init__(self):
        # Base de Dados Dinâmica (Simulando o RAG)
        self.total_consolidado = 26801.80
        self.medicos = {
            "ANIMA COSTA": {"valor": 12500.00, "liberado": 85, "pendente": 15, "proj": "1.85x"},
            "INTERFILE - BI": {"valor": 5400.00, "liberado": 40, "pendente": 60, "proj": "1.00x"}, # VÁCUO
            "DR. MARCOS": {"valor": 8901.80, "liberado": 70, "pendente": 30, "proj": "2.10x"}
        }

    def processar_inteligencia(self, medico, comando):
        """Orquestração das 17 personas para decisão proativa"""
        dados = self.medicos[medico]
        c = comando.lower()
        proj = dados["proj"]
        
        # 1. PERSONA 12 (IA-SENTINELA): Verificação de Vácuo
        if proj == "1.00x":
            return {
                "msg": f"🚨 IA-SENTINELA: VÁCUO detectado em {medico} (1.00x). Ordem de PULA acionada para proteção de capital.",
                "acao": "Pula", "cor": "error", "lib": dados["liberado"], "pen": dados["pendente"]
            }

        # 2. PERSONA 5 (CFO VISION) + PERSONA 15 (AUDITORA): Execução de Pagamento
        if any(x in c for x in ["pagar", "liberar", "autorizado", "pode"]):
            return {
                "msg": f"🚀 CFO VISION: {medico} autorizado. Valor de R$ {dados['valor']:,.2f} processado. Status: ENTRA.",
                "acao": "Entra", "cor": "success", "lib": dados["liberado"], "pen": dados["pendente"]
            }

        # 3. PERSONA 1 (GÊMEA FÊNIX): Saudação e Proatividade
        return {
            "msg": f"Boa noite, Sidney! Unidade {medico} analisada pela Visão 360°. Projeção {proj}. Aguardo gatilho.",
            "acao": "Não Entra", "cor": "info", "lib": dados["liberado"], "pen": dados["pendente"]
        }

# --- 2. INTERFACE PREMIUM (BRANDING MESTRA DA IMAGEM) ---
st.set_page_config(page_title="GÊMEA FÊNIX BONDE 2.0", layout="wide")
st.title("🛡️ GÊMEA FÊNIX BONDE | RAG Ativado")

# Inicializa Motor
nf = NucleoFenix()

# --- 3. CAIXA DE DIÁLOGO ONLINE (PERSONA 4 E 17) ---
with st.container(border=True):
    col_a, col_b = st.columns([1, 2])
    with col_a:
        dr_sel = st.selectbox("Doutor Responsável:", list(nf.medicos.keys()), key="dr_responsavel")
    with col_b:
        cmd_sidney = st.text_input("Comando para as 17 Inteligências:", placeholder="Ex: Pode fazer o pagamento hoje", key="cmd_rag")

    if st.button("🚀 ATIVAR PROJETO FRAJOLA"):
        if cmd_sidney:
            resultado = nf.processar_inteligencia(dr_sel, cmd_sidney)
            st.session_state.estado_decisao = resultado
            # Alimenta Memória de Auditoria (Persona 15)
            st.session_state.historico_sentinela.append({
                "Hora": datetime.now().strftime("%H:%M"),
                "Doutor": dr_sel,
                "Decisão": resultado["acao"],
                "Parecer": resultado["msg"]
            })

# --- 4. MÉTRICAS DINÂMICAS (Sincronização CFO Vision) ---
res = st.session_state.estado_decisao
c1, c2 = st.columns(2)
if "lib" in res:
    c1.metric(f"ESTATUTO {dr_sel}", f"{res['lib']}% LIBERADO")
    c2.metric(f"EM AUDITORIA", f"{res['pen']}% PENDENTE")

# RESPOSTA PROATIVA (AUTONOMIA)
if res["msg"]:
    if res["cor"] == "success": st.success(res["msg"])
    elif res["cor"] == "error": st.error(res["msg"])
    else: st.info(res["msg"])
    
    # MOBILE FIX (Persona 17): URL Encoding seguro
    msg_zap = urllib.parse.quote(res["msg"])
    st.markdown(f'<a href="https://wa.me/5511942971753?text={msg_zap}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 DISPARAR DECISÃO (WHATSAPP)</div></a>', unsafe_allow_html=True)

# --- 5. TABELA DA FAVELINHA (VISUAL SEM CÓDIGO) ---
st.subheader("📋 TABELA DA FAVELINHA (Ação Imediata)")
df_fav = pd.DataFrame([{
    "Doutor": dr_sel,
    "Projeção (x)": nf.medicos[dr_sel]["proj"],
    "Ação": res["acao"],
    "Persona Responsável": "IA-SENTINELA" if res["acao"] == "Pula" else "CFO VISION"
}])
st.table(df_fav)

# --- 6. LOG DE AUDITORIA (MEMÓRIA QUÂNTICA) ---
with st.expander("📜 Log de Inteligência (Histórico RAG)"):
    if st.session_state.historico_sentinela:
        st.dataframe(pd.DataFrame(st.session_state.historico_sentinela))
                                   
