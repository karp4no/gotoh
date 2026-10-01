import tkinter as tk
from tkinter import ttk, messagebox

from sistema.memoria import (
    carregar_memoria,
    adicionar_nota,
    remover_nota
)

from interface.componentes import (
    limpar_conteudo,
    criar_titulo,
    criar_card,
    criar_botao_acao
)

from interface.tema import (
    FUNDO,
    FUNDO_CARD,
    BORDA,
    TEXTO,
    FONTE,
    VERMELHO
)


def mostrar(conteudo):
    limpar_conteudo(conteudo)

    memoria = carregar_memoria()

    criar_titulo(
        conteudo,
        "📝 Notas",
        "Anotações e informações importantes."
    )

    area_adicionar = tk.Frame(
        conteudo,
        bg=FUNDO
    )

    area_adicionar.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )

    entrada = ttk.Entry(
        area_adicionar,
        style="Gotoh.TEntry"
    )

    entrada.pack(
        side="left",
        fill="x",
        expand=True
    )

    def adicionar():
        texto = entrada.get().strip()

        if not texto:
            messagebox.showwarning(
                "Nota",
                "Digite uma nota primeiro."
            )
            return

        adicionar_nota(texto)
        mostrar(conteudo)

    criar_botao_acao(
        area_adicionar,
        "+ Salvar nota",
        adicionar
    )

    if not memoria["notas"]:
        criar_card(
            conteudo,
            "Nenhuma nota",
            "Adicione sua primeira nota acima."
        )
        return

    for indice, nota in enumerate(memoria["notas"]):

        card = tk.Frame(
            conteudo,
            bg=FUNDO_CARD,
            highlightbackground=BORDA,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            padx=30,
            pady=5
        )

        tk.Label(
            card,
            text="📝 " + nota,
            font=(FONTE, 9),
            fg=TEXTO,
            bg=FUNDO_CARD,
            anchor="w",
            justify="left"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=14,
            pady=12
        )

        criar_botao_acao(
            card,
            "Remover",
            lambda i=indice: (
                remover_nota(i),
                mostrar(conteudo)
            ),
            VERMELHO
        )
