import json
import tkinter as tk
from pathlib import Path

from interface.tema import (
    FUNDO,
    FUNDO_SECUNDARIO,
    ROXO,
    ROXO_CLARO,
    TEXTO,
    TEXTO_FRACO,
    FONTE,
    TAMANHO_JANELA,
    MIN_LARGURA,
    MIN_ALTURA,
    LARGURA_MENU
)

from interface.componentes import (
    criar_botao,
    configurar_estilo
)

from interface.telas import (
    inicio,
    estudos,
    conhecimento,
    tarefas,
    projetos,
    notas,
    progresso,
    configuracoes,
    conversa
)


BASE = Path(__file__).resolve().parent.parent


def carregar_configuracao():
    caminho = BASE / "sistema" / "config.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def iniciar():
    config = carregar_configuracao()

    janela = tk.Tk()

    configurar_estilo()

    janela.title("Gotoh — Agente Pessoal")
    janela.geometry(TAMANHO_JANELA)
    janela.minsize(MIN_LARGURA, MIN_ALTURA)
    janela.configure(bg=FUNDO)

    menu = tk.Frame(
        janela,
        width=LARGURA_MENU,
        bg=FUNDO_SECUNDARIO
    )

    menu.pack(
        side="left",
        fill="y"
    )

    menu.pack_propagate(False)

    tk.Label(
        menu,
        text="🤖",
        font=(FONTE, 25),
        fg=TEXTO,
        bg=FUNDO_SECUNDARIO
    ).pack(
        pady=(25, 0)
    )

    tk.Label(
        menu,
        text="GOTOH",
        font=(FONTE, 18, "bold"),
        fg=TEXTO,
        bg=FUNDO_SECUNDARIO
    ).pack(
        pady=(3, 0)
    )

    tk.Label(
        menu,
        text="Agente pessoal",
        font=(FONTE, 9),
        fg=ROXO_CLARO,
        bg=FUNDO_SECUNDARIO
    ).pack(
        pady=(0, 25)
    )

    tk.Frame(
        menu,
        height=2,
        bg=ROXO
    ).pack(
        fill="x",
        padx=20,
        pady=(0, 18)
    )

    conteudo = tk.Frame(
        janela,
        bg=FUNDO
    )

    conteudo.pack(
        side="right",
        fill="both",
        expand=True
    )

    criar_botao(
        menu,
        "💬  Conversa",
        lambda: conversa.mostrar(conteudo)
    )

    criar_botao(
        menu,
        "🏠  Início",
        lambda: inicio.mostrar(conteudo)
    )

    criar_botao(
        menu,
        "📚  Estudos",
        lambda: estudos.mostrar(conteudo)
    )

    criar_botao(
        menu,
        "🧠  Conhecimento",
        lambda: conhecimento.mostrar(conteudo)
    )

    criar_botao(
        menu,
        "📋  Tarefas",
        lambda: tarefas.mostrar(conteudo)
    )

    criar_botao(
        menu,
        "🚀  Projetos",
        lambda: projetos.mostrar(conteudo)
    )

    criar_botao(
        menu,
        "📝  Notas",
        lambda: notas.mostrar(conteudo)
    )

    criar_botao(
        menu,
        "📊  Progresso",
        lambda: progresso.mostrar(conteudo)
    )

    tk.Frame(
        menu,
        bg=FUNDO_SECUNDARIO
    ).pack(
        fill="both",
        expand=True
    )

    criar_botao(
        menu,
        "⚙️  Configurações",
        lambda: configuracoes.mostrar(conteudo, config)
    )

    tk.Label(
        menu,
        text="GOTOH • versão inicial",
        font=(FONTE, 8),
        fg=TEXTO_FRACO,
        bg=FUNDO_SECUNDARIO
    ).pack(
        pady=15
    )

    inicio.mostrar(conteudo)

    janela.mainloop()
