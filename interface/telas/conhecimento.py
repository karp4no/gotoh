import tkinter as tk

from interface.componentes import (
    limpar_conteudo,
    criar_titulo,
    criar_card
)

from interface.tema import (
    FUNDO,
    FUNDO_CARD,
    FUNDO_CARD_HOVER,
    FUNDO_SECUNDARIO,
    BORDA,
    TEXTO,
    TEXTO_FRACO,
    FONTE,
    ROXO
)

from sistema.conhecimento import (
    listar_areas,
    listar_arquivos,
    ler_conhecimento
)


def nome_bonito(nome):
    return nome.replace("_", " ").replace("-", " ").title()


def mostrar_documento(conteudo, caminho):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "📖 " + caminho.stem.replace("_", " ").title(),
        f"Área: {caminho.parent.name.title()}"
    )

    texto = tk.Text(
        conteudo,
        wrap="word",
        font=(FONTE, 10),
        fg=TEXTO,
        bg="#1A0E29",
        insertbackground=TEXTO,
        selectbackground=ROXO,
        selectforeground="white",
        relief="flat",
        bd=0,
        padx=20,
        pady=20
    )

    texto.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 20)
    )

    texto.insert(
        "1.0",
        ler_conhecimento(caminho)
    )

    texto.config(state="disabled")

    botao = tk.Button(
        conteudo,
        text="← Voltar para Conhecimento",
        command=lambda: mostrar(conteudo),
        font=(FONTE, 9, "bold"),
        fg=TEXTO,
        bg=FUNDO_CARD,
        activeforeground=TEXTO,
        activebackground=FUNDO_CARD_HOVER,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=14,
        pady=8
    )

    botao.pack(
        padx=30,
        pady=(0, 20),
        anchor="w"
    )


def mostrar(conteudo):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "🧠 Conhecimento",
        "O Gotoh encontra automaticamente os conteúdos disponíveis."
    )

    areas = listar_areas()

    if not areas:
        criar_card(
            conteudo,
            "Nenhum conteúdo encontrado",
            "Adicione arquivos .md dentro da pasta conhecimento."
        )
        return

    for area in areas:

        arquivos = listar_arquivos(area)

        card = tk.Frame(
            conteudo,
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
            pady=15
        )

        tk.Label(
            interior,
            text="📂 " + nome_bonito(area),
            font=(FONTE, 12, "bold"),
            fg=TEXTO,
            bg=FUNDO_CARD,
            anchor="w"
        ).pack(fill="x")

        if not arquivos:
            tk.Label(
                interior,
                text="Nenhum conteúdo nesta área.",
                font=(FONTE, 9),
                fg=TEXTO_FRACO,
                bg=FUNDO_CARD,
                anchor="w"
            ).pack(
                fill="x",
                pady=(8, 0)
            )

        for arquivo in arquivos:

            botao = tk.Button(
                interior,
                text="📖 " + arquivo.stem.replace("_", " ").title(),
                command=lambda caminho=arquivo: mostrar_documento(
                    conteudo,
                    caminho
                ),
                font=(FONTE, 9),
                fg=TEXTO,
                bg=FUNDO_SECUNDARIO,
                activeforeground=TEXTO,
                activebackground=FUNDO_CARD_HOVER,
                relief="flat",
                bd=0,
                cursor="hand2",
                anchor="w",
                padx=12,
                pady=8
            )

            botao.pack(
                fill="x",
                pady=(8, 0)
            )
