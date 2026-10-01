import tkinter as tk

from sistema.agente import processar_comando

from interface.tema import (
    FUNDO,
    FUNDO_SECUNDARIO,
    FUNDO_CARD,
    ROXO,
    ROXO_CLARO,
    TEXTO,
    TEXTO_SECUNDARIO,
    BORDA,
    FONTE
)

from interface.componentes import limpar_conteudo


def mostrar(conteudo):
    limpar_conteudo(conteudo)

    # CABEÇALHO

    cabecalho = tk.Frame(
        conteudo,
        bg=FUNDO
    )

    cabecalho.pack(
        fill="x",
        padx=30,
        pady=(25, 10)
    )

    tk.Label(
        cabecalho,
        text="Conversa",
        bg=FUNDO,
        fg=TEXTO,
        font=(FONTE, 22, "bold")
    ).pack(
        anchor="w"
    )

    tk.Label(
        cabecalho,
        text="Fale com o Gotoh e deixe ele cuidar das informações.",
        bg=FUNDO,
        fg=TEXTO_SECUNDARIO,
        font=(FONTE, 10)
    ).pack(
        anchor="w",
        pady=(4, 0)
    )

    # ÁREA PRINCIPAL DA CONVERSA

    area = tk.Frame(
        conteudo,
        bg=FUNDO_CARD,
        highlightbackground=BORDA,
        highlightthickness=1
    )

    area.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    conversa = tk.Text(
        area,
        bg=FUNDO_CARD,
        fg=TEXTO,
        insertbackground=TEXTO,
        font=(FONTE, 11),
        wrap="word",
        relief="flat",
        bd=0,
        padx=20,
        pady=20,
        state="disabled"
    )

    conversa.pack(
        fill="both",
        expand=True
    )

    # ESTILO DAS MENSAGENS

    conversa.tag_configure(
        "gotoh",
        foreground=ROXO_CLARO,
        spacing1=8,
        spacing3=8
    )

    conversa.tag_configure(
        "usuario",
        foreground=TEXTO,
        spacing1=8,
        spacing3=8
    )

    # ADICIONAR MENSAGEM

    def adicionar_mensagem(remetente, mensagem, tag):
        conversa.config(state="normal")

        conversa.insert(
            "end",
            f"{remetente}\n",
            tag
        )

        conversa.insert(
            "end",
            f"{mensagem}\n\n",
            tag
        )

        conversa.config(state="disabled")

        conversa.see("end")

    # MENSAGEM INICIAL

    adicionar_mensagem(
        "Gotoh",
        "Olá! Estou pronto. Você pode me pedir para guardar informações, criar tarefas ou consultar suas memórias.",
        "gotoh"
    )

    # CAMPO DE TEXTO

    entrada_frame = tk.Frame(
        conteudo,
        bg=FUNDO
    )

    entrada_frame.pack(
        fill="x",
        padx=30,
        pady=(5, 25)
    )

    entrada = tk.Entry(
        entrada_frame,
        bg=FUNDO_SECUNDARIO,
        fg=TEXTO,
        insertbackground=TEXTO,
        font=(FONTE, 11),
        relief="flat",
        bd=0
    )

    entrada.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=12,
        padx=(0, 10)
    )

    def enviar():
        texto = entrada.get().strip()

        if not texto:
            return

        adicionar_mensagem(
            "Você",
            texto,
            "usuario"
        )

        entrada.delete(
            0,
            "end"
        )

        resposta = processar_comando(texto)

        adicionar_mensagem(
            "Gotoh",
            resposta,
            "gotoh"
        )

    botao = tk.Button(
        entrada_frame,
        text="Enviar",
        command=enviar,
        bg=ROXO,
        fg="white",
        activebackground=ROXO_CLARO,
        activeforeground="white",
        font=(FONTE, 10, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=22,
        pady=10
    )

    botao.pack(
        side="right"
    )

    entrada.bind(
        "<Return>",
        lambda evento: enviar()
    )

    entrada.focus_set()
