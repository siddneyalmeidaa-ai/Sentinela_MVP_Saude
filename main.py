import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE IDENTIDADE VISUAL SPA ---
st.set_page_config(page_title="IA-SENTINELA PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stHeader"] {display: none !important;}
    
    /* ESTILO PAPEL TIMBRADO PROFISSIONAL */
    .papel-timbrado {
        background-color: white;
        color: #1a1a1a;
        padding: 50px;
        border-radius: 2px;
        border-top: 15px solid #00d4ff;
        font-family: 'Times New Roman', Times, serif;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
        max-width: 800px;
        margin: auto;
    }
    .cabecalho-spa { text-align: center; border-bottom: 2px solid #00d4ff; padding-bottom: 10px; margin-bottom: 30px; }
    .titulo-doc { font-size: 22px; font-weight: bold; color: #1c2e4a; margin: 0; }
    .subtitulo-doc { font-size: 12px; color: #555; letter-spacing: 2px; }
    .campo-dado { border-bottom: 1px solid #eee; padding: 10px 0; font-size: 14px; }
    .secao-verde { color: #2e7d32; font-weight: bold; }
    .secao-vermelha { color: #c62828; font-weight: bold; }
    .tabela-pendencias { width: 100%; border-collapse: collapse; margin-top: 20px; }
    .tabela-pendencias th { background: #f8f9fa; text-align: left; padding: 8px; font-size: 12px; border-bottom: 2px solid #ddd; }
    .tabela-pendencias td { padding: 8px; font-size: 13px; border-bottom: 1px solid #eee; }
    .rodape-assinatura { margin-top: 60px; text-align: center; border-top: 1px solid #333; width: 250px; margin-left: auto; margin-right: auto; padding-top: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS DINÂMICO ---
dados_medicos = {
    "ANIMA COSTA": {
        "valor": 16000.0, "p_pen": 15,
        "pacientes": [
            {"PAC": "JOAO SILVA", "PROC": "RAIO-X", "MOTIVO": "FALTA ASSINATURA"},
            {"PAC": "MARIA SOUZA", "PROC": "CONSULTA", "MOTIVO": "GUIA EXPIRADA"}
        ]
    },
    "DMMIGINIO GUERRA": {
        "valor": 22500.0, "p_pen": 22,
        "pacientes": [
            {"PAC": "CARLOS LIMA", "PROC": "RESSONÂNCIA", "MOTIVO": "XML INVÁLIDO"}
        ]
    },
    "CLÍNICA SÃO JOSÉ": {
        "valor": 45000.0, "p_pen": 18,
        "pacientes": [
            {"PAC": "ANA PAULA", "PROC": "TOMOGRAFIA", "MOTIVO": "CÓDIGO TUSS DIVERGENTE"},
            {"PAC": "PEDRO GOMES", "PROC": "ULTRASSOM", "MOTIVO": "LAUDO AUSENTE"}
        ]
    }
}

# Cabeçalho da App
st.markdown("<div style='background: #1c232d; padding: 15px; border-radius: 10px; margin-bottom: 20px; color: white;'>"
            "<b>SIDNEY PEREIRA DE ALMEIDA</b><br><small style='color: #00d4ff;'>DIRETOR OPERACIONAL | IA-SENTINELA</small></div>", unsafe_allow_html=True)

unidade = st.selectbox("Selecione a Unidade para Auditoria:", list(dados_medicos.keys()))
info = dados_medicos[unidade]
v_liberado = info["valor"] * ((100 - info["p_pen"]) / 100)
v_pendente = info["valor"] * (info["p_pen"] / 100)
data_relatorio = datetime.now().strftime("%d/%m/%Y às %H:%M")

# --- 3. ABAS OPERACIONAIS ---
tab_auditoria, tab_relatorio = st.tabs(["📊 AUDITORIA EM TEMPO REAL", "📄 VISUALIZAR PAPEL TIMBRADO"])

with tab_auditoria:
    st.write(f"### 📍 Unidade: {unidade}")
    c1, c2 = st.columns(2)
    c1.metric("PROCEDE (LIBERADO)", f"R$ {v_liberado:,.2f}")
    c2.metric("NÃO PROCEDE (PENDENTE)", f"R$ {v_pendente:,.2f}")
    st.markdown("#### Detalhamento de Pacientes Pendentes")
    st.table(pd.DataFrame(info["pacientes"]))

with tab_relatorio:
    # --- CONSTRUÇÃO DO TIMBRADO HTML ---
    linhas_tabela = "".join([f"<tr><td>{p['PAC']}</td><td>{p['PROC']}</td><td>{p['MOTIVO']}</td></tr>" for p in info["pacientes"]])
    
    html_timbrado = f"""
    <div class="papel-timbrado">
        <div class="cabecalho-spa">
            <p class="titulo-doc">RELATÓRIO TÉCNICO DE AUDITORIA</p>
            <p class="subtitulo-doc">IA-SENTINELA | SIDNEY PEREIRA DE ALMEIDA</p>
        </div>
        
        <div class="campo-dado"><b>UNIDADE:</b> {unidade}</div>
        <div class="campo-dado"><b>DATA DE EMISSÃO:</b> {data_relatorio}</div>
        <div class="campo-dado"><b>STATUS GERAL:</b> AUDITADO</div>
        
        <div style="margin-top: 30px;">
            <p class="secao-verde">✅ PROCEDE: {100-info['p_pen']}% (R$ {v_liberado:,.2f})</p>
            <p class="secao-vermelha">❌ NÃO PROCEDE: {info['p_pen']}% (R$ {v_pendente:,.2f})</p>
        </div>
        
        <p style="margin-top: 30px; font-weight: bold; border-bottom: 1px solid #333;">PACIENTES COM PENDÊNCIA TÉCNICA:</p>
        <table class="tabela-pendencias">
            <thead><tr><th>PACIENTE</th><th>PROCEDIMENTO</th><th>MOTIVO DA GLOSA</th></tr></thead>
            <tbody>{linhas_tabela}</tbody>
        </table>
        
        <div class="rodape-assinatura">
            <b>SIDNEY PEREIRA DE ALMEIDA</b><br>Diretor Operacional SPA
        </div>
    </div>
    """
    st.markdown(html_timbrado, unsafe_allow_html=True)

    # --- GERADOR DE TXT CORRIGIDO (F-STRINGS SEGURAS) ---
    lista_txt = "".join([f"- {p['PAC']} | {p['PROC']} | {p['MOTIVO']}\\n" for p in info["pacientes"]])
    texto_oficial = (
        f"------------------------------------------\\n"
        f"      RELATORIO DE AUDITORIA SPA          \\n"
        f"------------------------------------------\\n"
        f"UNIDADE: {unidade}\\n"
        f"DATA: {data_relatorio}\\n"
        f"------------------------------------------\\n"
        f"PROCEDE: {100-info['p_pen']}% (R$ {v_liberado:,.2f})\\n"
        f"NAO PROCEDE: {info['p_pen']}% (R$ {v_pendente:,.2f})\\n"
        f"------------------------------------------\\n"
        f"PACIENTES PENDENTES:\\n{lista_txt}"
        f"------------------------------------------\\n"
        f"ASSINADO: SIDNEY PEREIRA DE ALMEIDA\\n"
    )

    st.download_button(
        label="⬇️ BAIXAR RELATÓRIO OFICIAL (.TXT)",
        data=texto_oficial.encode('utf-8'),
        file_name=f"Auditoria_{unidade.replace(' ', '_')}.txt",
        mime="text/plain"
    )

st.caption("IA-SENTINELA PRO | Gestão Sidney Almeida")
