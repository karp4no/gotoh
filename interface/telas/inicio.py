import tkinter as tk
from interface.tema import (
    FUNDO, FUNDO_CARD, FUNDO_CARD_HOVER, TEXTO, TEXTO_SECUNDARIO, 
    ROXO_SUAVE, BORDA, FONTE
)

def renderizar_inicio(container, usuario="Rodrigo"):
    frame_principal = tk.Frame(container, bg=FUNDO, padx=40, pady=35)
    frame_principal.pack(fill="both", expand=True)

    # Cabecalho Limpo
    lbl_boas_vindas = tk.Label(
        frame_principal, 
        text=f"Olá, {usuario}", 
        font=(FONTE, 20, "bold"), 
        bg=FUNDO, 
        fg=TEXTO,
        anchor="w"
    )
    lbl_boas_vindas.pack(fill="x", pady=(0, 4))

    lbl_sub = tk.Label(
        frame_principal, 
        text="Painel de controle e visão geral do sistema", 
        font=(FONTE, 10), 
        bg=FUNDO, 
        fg=TEXTO_SECUNDARIO,
        anchor="w"
    )
    lbl_sub.pack(fill="x", pady=(0, 30))

    # Lista de Cards
    secoes = [
        ("Estudos", "Continue seus estudos e organize seu aprendizado."),
        ("Tarefas", "Gerencie suas pendências e compromissos registrados."),
        ("Projetos", "Acompanhe o andamento dos seus desenvolvimentos."),
        ("Notas", "Acesse e organize suas anotações rápidas.")
    ]

    for titulo, desc in secoes:
        card = tk.Frame(
            frame_principal, 
            bg=FUNDO_CARD, 
            highlightbackground=BORDA, 
            highlightthickness=1, 
            padx=20, 
            pady=16
        )
        card.pack(fill="x", pady=6)

        t = tk.Label(
            card, 
            text=titulo, 
            font=(FONTE, 11, "bold"), 
            bg=FUNDO_CARD, 
            fg=ROXO_SUAVE, 
            anchor="w"
        )
        t.pack(fill="x")

        d = tk.Label(
            card, 
            text=desc, 
            font=(FONTE, 9), 
            bg=FUNDO_CARD, 
            fg=TEXTO_SECUNDARIO, 
            anchor="w"
        )
        d.pack(fill="x", pady=(4, 0))
