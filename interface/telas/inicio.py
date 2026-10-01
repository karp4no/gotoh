import tkinter as tk

from sistema.memoria import carregar_memoria
from interface.componentes import limpar_conteudo, criar_titulo, criar_card


def mostrar(conteudo):
    limpar_conteudo(conteudo)

    memoria = carregar_memoria()
    nome = memoria["usuario"]["nome"]

    criar_titulo(
        conteudo,
        f"Olá, {nome}! 👋",
        "O que vamos fazer hoje?"
    )

    criar_card(
        conteudo,
        "📚 Estudos",
        "Continue seus estudos e organize seu aprendizado."
    )

    criar_card(
        conteudo,
        "📋 Tarefas",
        f"Você possui {len(memoria['tarefas'])} tarefa(s) registrada(s)."
    )

    criar_card(
        conteudo,
        "🚀 Projetos",
        "Acompanhe seus projetos e trabalhos em andamento."
    )

    criar_card(
        conteudo,
        "📝 Notas",
        f"Você possui {len(memoria['notas'])} nota(s) registrada(s)."
    )
