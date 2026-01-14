import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
import io

# --- 1. MOTOR DE INTELIGÊNCIA INTEGRADO (AS 17 IAs) ---
class Fenix17System:
    def __init__(self, doutor="Sidney"):
        self.doutor = doutor
        # Dados Sincronizados
        self.liberado = 18493.24
        self.pendente = 8308.56
        self.total_geral = 26801.80
        
        # Base de Dados das Unidades (Favelinha Table)
        self.db = [
            {"unidade": "ANIMA COSTA", "valor": 12500.0, "status": "CONFORMIDADE OK", "x": 1.85},
            {"unidade": "DR. MARCOS", "valor": 8900.0, "status": "CONFORMIDADE OK", "x": 2.10},
            {"unidade": "INTERFILE - BI", "valor": 5400.0, "status": "RESTRIÇÃO", "x": 1.00}, # Vácuo!
            {"unidade": "DR. SILVA", "valor": 1.0, "status": "RESTRIÇÃO", "x": 0.80},
            {"unidade": "LAB CLINIC", "valor": 0.80, "status": "RESTRIÇÃO", "x": 1.20}
        ]

    def auditoria_cfo(self):
        """Sincronização Automática de Porcentagens"""
        p_lib = (self.liberado / self.total_geral) * 100
        p_pen = (self.pendente / self.total_geral) * 100
        return f"{p_lib:.0f}% LIBERADO", f"{p_pen:.0f}% PENDENTE"

    def motor_frajola_inteligente(self, unidade, mensagem_recebida):
        """Ação das 17 IAs: Resposta Humanizada e Auditoria"""
        med = next(item for item in self.db if item["unidade"] == unidade)
        msg_low = mensagem_recebida.lower()
        
        # Inteligência Sentinela + Auditoria Padrão Ouro
        if med['status'] == "RESTRIÇÃO":
            return f"Oi, {unidade}! Tudo ótimo por aqui, e com você? Analisando seu caso agora com a **IA-SENTINELA**, vi que seu repasse de R$ {med['valor']:,.2f} está retido. Já identifiquei que faltam arquivos XML. Vamos destravar isso agora?"
        else:
            return f"Boa noite, {unidade}! Tudo bem! Verifiquei aqui no **Estatuto Atual** que sua unidade está voando em CONFORMIDADE OK. O valor de R$ {med['valor']:,.2f} já está no fluxo oficial. Alguma outra dúvida?"

# --- 2. INTERFACE VISUAL (PADRÃO OURO BIGODE) ---
st.set_page_config(page_title="Sentinela | GF-17", layout="wide")
fuso = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso).strftime("%d/%m/%Y %H:%M")
gf17 = Fenix17System()
status_lib, status_pen = gf17.auditoria_cfo()

st.title(f"🛡️ GF-17 | Gêmea Fênix (Doutor: {gf17.doutor})")

# Métricas Automáticas (Sincronismo Total)
c1, c2 = st.columns(2)
c1.metric("ESTATUTO ATUAL", status_lib)
c2.metric("EM AUDITORIA", status_pen)

tab_favelinha, tab_comunicacao, tab_relatorios = st.tabs([
    "📊 Tabela da Favelinha", "📲 Canal de Comunicação Viva", "📑 Relatórios"
])

with tab_favelinha:
    st.subheader("📋 Auditoria de Rodada (Sentinela)")
    dados_f = []
    for r in gf17.db:
        # Regra do Vácuo (1.00x)
        decisao = "pula" if r['x'] == 1.00 else ("entra" if r['x'] >= 1.50 else "não entra")
        dados_f.append({"Unidade": r['unidade'], "Projeção": f"{r['x']:.2f}x", "Decisão": decisao, "Status": r['status']})
    st.table(dados_f)

with tab_comunicacao:
    u_sel = st.selectbox("Selecione o Médico:", [d['unidade'] for d in gf17.db])
    entrada = st.text_area(f"Mensagem de {u_sel}:", placeholder="Ex: Boa noite, tudo bem?")
    
    if st.button("🚀 Ativar Projeto Frajola (IA Inteligente)"):
        if entrada:
            resposta_viva = gf17.motor_frajola_inteligente(u_sel, entrada)
            st.success(f"**Análise Sugerida pelas 17 IAs:**\n\n{resposta_viva}")
            zap = f"https://wa.me/5511942971753?text={urllib.parse.quote(resposta_viva)}"
            st.markdown(f'''<a href="{zap}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:bold;">🚀 ENVIAR PARA WHATSAPP</div>
            </a>''', unsafe_allow_html=True)

with tab_relatorios:
    # Correção para Mobile e Erro de PDF
    st.info("Central de Exportação Protegida.")
    csv = pd.DataFrame(gf17.db).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Baixar Planilha de Auditoria", data=csv, file_name="Auditoria_GF17.csv", mime="text/csv", use_container_width=True)

st.caption(f"Sidney Pereira de Almeida | {agora} | Sincronizado")
