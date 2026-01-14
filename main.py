# --- NÚCLEO ACIMA DA MÉDIA: PROJETO FRAJOLA ---

class ProjetoFrajola:
    def __init__(self):
        self.inteligencias = ["IA-SENTINELA", "Advogada Cabeluda", "Maluquinha dos Códigos", "CFO Vision", "Professora Língua-Afunda"] # +12
        self.regras = "Padrão Ouro"

    def processar_rag(self, mensagem, contexto_doutor):
        # Aqui entra o aprendizado que elas tiveram
        if "vácuo" in mensagem.lower() or "1.00" in mensagem:
            return "🚨 IA-SENTINELA: Bloqueio ativado. Risco de vácuo detectado no sistema."
        
        if "auditoria" in mensagem.lower():
            return "⚖️ ADVOGADA CABELUDA: Iniciando blindagem de ativos para " + contexto_doutor
            
        return "🔥 GÊMEA FÊNIX: Processando inteligência para o Projeto Frajola..."

    def atualizar_favelinha(self, projecao):
        # Lógica que você viu na sua tabela (1.85x)
        if projecao < 2.00:
            return "PULA (Aguardando Gatilho Tático)"
        return "ENTRA (Padrão Ouro Liberado)"

# --- INTEGRAÇÃO COM A UI ---
# Use este dicionário para alimentar o seu 'st.table' ou 'st.dataframe'
