import tkinter as tk
from tkinter import ttk, messagebox

from sistema.memoria import (
    carregar_memoria,
    adicionar_tarefa,
    concluir_tarefa,
    remover_tarefa
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
    TEXTO_SECUNDARIO,
    FONTE,
    AZUL,
    VERMELHO
)


def mostrar(conteudo):
    limpar_conteudo(conteudo)

    memoria = carregar_memoria()

    criar_titulo(
        conteudo,
        "📋 Tarefas",
        "Organize o que precisa ser feito."
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
                "Tarefa",
                "Digite uma tarefa primeiro."
            )
            return

        adicionar_tarefa(texto)
        mostrar(conteudo)

    criar_botao_acao(
        area_adicionar,
        "+ Adicionar",
        adicionar
    )

    if not memoria["tarefas"]:
        criar_card(
            conteudo,
            "Nenhuma tarefa",
            "Adicione sua primeira tarefa acima."
        )
        return

    for indice, tarefa in enumerate(memoria["tarefas"]):

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

        texto = tarefa["texto"]

        if tarefa["concluida"]:
            texto = "✓ " + texto
        else:
            texto = "☐ " + texto

        tk.Label(
            card,
            text=texto,
            font=(FONTE, 9),
            fg=TEXTO_SECUNDARIO if tarefa["concluida"] else TEXTO,
            bg=FUNDO_CARD,
            anchor="w"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=14,
            pady=12
        )

        if not tarefa["concluida"]:
            criar_botao_acao(
                card,
                "Concluir",
                lambda i=indice: (
                    concluir_tarefa(i),
                    mostrar(conteudo)
                ),
                AZUL
            )

        criar_botao_acao(
            card,
            "Remover",
            lambda i=indice: (
                remover_tarefa(i),
                mostrar(conteudo)
            ),
            VERMELHO
        )
