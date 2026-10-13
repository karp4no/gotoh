# ============================================================
# TEMA VISUAL DO GOTOH (MINIMALISTA DARK VIOLET)
# ============================================================

TEMAS = {
    "minimalista_dark": {
        # Fundos escuros profundos e limpos
        "FUNDO": "#0D0A14",             # Preto com fundo roxo sutil
        "FUNDO_SECUNDARIO": "#140F21",  # Superfície elevada 1
        "FUNDO_CARD": "#1C152E",        # Cards e blocos
        "FUNDO_CARD_HOVER": "#271E3E",  # Hover de elementos
        "FUNDO_CONVERSA": "#110D1B",   # Áreas de leitura
        "FUNDO_INPUT": "#151022",      # Campo de digitação
        
        # Textos com alto contraste e legibilidade
        "TEXTO": "#F3F4F6",            # Texto principal
        "TEXTO_SECUNDARIO": "#A7A5B8", # Subtítulos e detalhes
        "TEXTO_FRACO": "#6C6680",      # Placeholders
        "TEXTO_GOTOH": "#F1EAFF",      # Resposta do assistente
        "TEXTO_USUARIO": "#E9D5FF",    # Mensagem do usuário
        
        # Destaques em Roxo Vibrante e Elegante
        "ROXO_SUAVE": "#C084FC",       # Destaques sutis
        "ROXO": "#9333EA",             # Ação principal e botões
        "ROXO_CLARO": "#A855F7",       # Hover de botões
        "ROXO_ESCURO": "#581C87",      # Bordas de foco / sombras
        "AZUL": "#3B82F6",             # Mantido para links / badges
        
        # Estrutura e Indicadores
        "BORDA": "#2B2142",            # Linhas finas de divisão
        "VERMELHO": "#EF4444",
        "VERDE": "#10B981",
        "FONTE": "DejaVu Sans",
    }
}

# Tema ativo padrão (Minimalista Dark Violet)
TEMA_ATUAL = TEMAS["minimalista_dark"]

# Exportação direta de constantes para compatibilidade total
FUNDO = TEMA_ATUAL["FUNDO"]
FUNDO_SECUNDARIO = TEMA_ATUAL["FUNDO_SECUNDARIO"]
FUNDO_CARD = TEMA_ATUAL["FUNDO_CARD"]
FUNDO_CARD_HOVER = TEMA_ATUAL["FUNDO_CARD_HOVER"]
FUNDO_CONVERSA = TEMA_ATUAL["FUNDO_CONVERSA"]
FUNDO_INPUT = TEMA_ATUAL["FUNDO_INPUT"]

TEXTO = TEMA_ATUAL["TEXTO"]
TEXTO_SECUNDARIO = TEMA_ATUAL["TEXTO_SECUNDARIO"]
TEXTO_FRACO = TEMA_ATUAL["TEXTO_FRACO"]
TEXTO_GOTOH = TEMA_ATUAL["TEXTO_GOTOH"]
TEXTO_USUARIO = TEMA_ATUAL["TEXTO_USUARIO"]

ROXO_SUAVE = TEMA_ATUAL["ROXO_SUAVE"]
ROXO = TEMA_ATUAL["ROXO"]
ROXO_CLARO = TEMA_ATUAL["ROXO_CLARO"]
ROXO_ESCURO = TEMA_ATUAL["ROXO_ESCURO"]
AZUL = TEMA_ATUAL["AZUL"]

BORDA = TEMA_ATUAL["BORDA"]
VERMELHO = TEMA_ATUAL["VERMELHO"]
VERDE = TEMA_ATUAL["VERDE"]

FONTE = TEMA_ATUAL["FONTE"]

TAMANHO_JANELA = "1100x700"
MIN_LARGURA = 900
MIN_ALTURA = 600
LARGURA_MENU = 245
