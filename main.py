import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io

# --- 1. MOTOR DE INTELIGÊNCIA GF-17 (AS 17 IAs) ---
class Fenix17System:
    def __init__(self, doutor="Bigode"):
        self.doutor = doutor
        # Dados Sincronizados
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.total_geral = 26801.80
        
        # Base de Dados das Unidades
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK"},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK"},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO"},
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO"},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO"}
        ]

    def calcular_metricas(self):
        """Sincronização CFO Vision"""
        p_lib = (self.liberado / self.total_geral) * 100
        p_pen = (self.pendente / self.total_geral) * 100
        return f"{p_lib:.0f}% LIBERADO", f"{p_pen:.0f}% PENDENTE"

    def sentinela_vacuo(self, x):
        """Regra IA-SENTINELA: 1.00x é Vácuo"""
        if x == 1.00: return "pula", "VÁCUO (DEATH ZONE)"
        return "entra" if x >= 1.50 else "não entra", "OPERACIONAL"

# Inicialização do Sistema
gf17 = Fenix17System()
status_lib, status_pen = gf17.calcular_metricas()

# --- 2. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
fuso = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso).strftime("%d/%m/%Y %H:%M")

st.title(f"🛡️ GF-17 | Gêmea Fênix 17 (Doutor: {gf17.doutor})")

# Métricas com Sincronismo Automático
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", status_lib)
c2.metric("EM AUDITORIA", status_pen)

tab_favelinha, tab_operacao, tab_pdf = st.tabs([
    "📊 Tabela da Favelinha", "🚀 Operação 17 IAs", "📑 Relatórios"
])

with tab_favelinha:
    st.subheader("📋 Ação Imediata (Regra Bigode)")
    # Projeção dinâmica por rodada
    rodadas = [
        {"id": 1, "x": 1.85}, {"id": 2, "x": 1.00}, {"id": 3, "x": 2.10}
    ]
    dados_f = []
    for r in rodadas:
        decisao, obs = gf17.sentinela_vacuo(r['x'])
        dados_f.append({"Rodada": r['id'], "Projeção": f"{r['x']:.2f}x", "Decisão": decisao, "Status": obs})
    
    st.table(dados_f)
    st.warning("⚠️ IA-SENTINELA monitorando o Vácuo.")

with tab_operacao:
    st.subheader("📲 Canal de Comunicação Viva")
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in gf17.db])
    med = next(item for item in gf17.db if item["unidade"] == u_sel)
    
    msg = st.text_area(f"Mensagem de {u_sel}:", placeholder="Ex: Boa noite")
    
    if st.button("🚀 Ativar Projeto Frajola"):
        if med['status'] == "RESTRIÇÃO":
            res = f"Olá, {u_sel}! Já me antecipei e auditei seu caso: identifiquei que seu repasse de R$ {med['valor']:,.2f} está retido por falta de XML. Vamos destravar isso agora?"
        else:
            res = f"Prezado(a) {u_sel}, verifiquei que seu status está em CONFORMIDADE OK para o valor de R$ {med['valor']:,.2f}."
        
        st.success(res)
        zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(res)}"
        st.markdown(f'''<a href="{zap}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div>
        </a>''', unsafe_allow_html=True)

with tab_pdf:
    st.subheader("📥 Exportação de Dados")
    # Exportação em CSV para evitar o erro de biblioteca no celular
    csv = pd.DataFrame(gf17.db).to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Relatório (Formato Excel/CSV)",
        data=csv,
        file_name=urllib.parse.quote(f"Relatorio_GF17_{gf17.doutor}.csv"),
        mime="text/csv",
        use_container_width=True
    )

st.divider()
st.caption(f"Sidney Pereira de Almeida | {agora} | Sincronizado")
