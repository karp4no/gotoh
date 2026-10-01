import tkinter as tk
from tkinter import ttk

from interface.tema import (
    FUNDO,
    FUNDO_SECUNDARIO,
    FUNDO_CARD,
    FUNDO_CARD_HOVER,
    ROXO,
    ROXO_CLARO,
    TEXTO,
    TEXTO_SECUNDARIO,
    TEXTO_FRACO,
    BORDA,
    FONTE
)


def limpar_conteudo(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def criar_titulo(frame, titulo, subtitulo=None):
    tk.Label(
        frame,
        text=titulo,
        font=(FONTE, 22, "bold"),
        fg=TEXTO,
        bg=FUNDO,
        anchor="w"
    ).pack(
        fill="x",
        padx=30,
        pady=(30, 5)
    )

    if subtitulo:
        tk.Label(
            frame,
            text=subtitulo,
            font=(FONTE, 10),
            fg=TEXTO_SECUNDARIO,
            bg=FUNDO,
            anchor="w"
        ).pack(
            fill="x",
            padx=30,
            pady=(0, 22)
        )


def criar_card(frame, titulo, descricao):
    card = tk.Frame(
        frame,
        bg=FUNDO_CARD,
        highlightbackground=BORDA,
        highlightthickness=1
    )

    card.pack(
        fill="x",
        padx=30,
        pady=6
    )

    interior = tk.Frame(
        card,
        bg=FUNDO_CARD
    )

    interior.pack(
        fill="both",
        expand=True,
        padx=18,
        pady=16
    )

    tk.Label(
        interior,
        text=titulo,
        font=(FONTE, 12, "bold"),
        fg=TEXTO,
        bg=FUNDO_CARD,
        anchor="w"
    ).pack(fill="x")

    tk.Label(
        interior,
        text=descricao,
        font=(FONTE, 9),
        fg=TEXTO_SECUNDARIO,
        bg=FUNDO_CARD,
        anchor="w",
        justify="left"
    ).pack(
        fill="x",
        pady=(6, 0)
    )


def criar_botao(parent, texto, comando):
    botao = tk.Button(
        parent,
        text=texto,
        command=comando,
        font=(FONTE, 10),
        fg=TEXTO,
        bg=FUNDO_SECUNDARIO,
        activeforeground=TEXTO,
        activebackground=FUNDO_CARD_HOVER,
        relief="flat",
        bd=0,
        cursor="hand2",
        anchor="w",
        padx=16,
        pady=10
    )

    botao.pack(
        fill="x",
        padx=14,
        pady=2
    )

    botao.bind(
        "<Enter>",
        lambda event: botao.config(bg=FUNDO_CARD_HOVER)
    )

    botao.bind(
        "<Leave>",
        lambda event: botao.config(bg=FUNDO_SECUNDARIO)
    )

    return botao


def criar_botao_acao(parent, texto, comando, cor=ROXO):
    botao = tk.Button(
        parent,
        text=texto,
        command=comando,
        font=(FONTE, 9, "bold"),
        fg="white",
        bg=cor,
        activeforeground="white",
        activebackground=ROXO_CLARO,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=15,
        pady=8
    )

    botao.pack(
        side="left",
        padx=(10, 0)
    )

    return botao


def configurar_estilo():
    estilo = ttk.Style()

    try:
        estilo.theme_use("clam")
    except tk.TclError:
        pass

    estilo.configure(
        "Gotoh.TEntry",
        fieldbackground="#1C102B",
        foreground=TEXTO,
        bordercolor=BORDA,
        lightcolor=BORDA,
        darkcolor=BORDA,
        padding=8
    )
