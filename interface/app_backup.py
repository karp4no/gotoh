import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent


def carregar_configuracao():
    caminho = BASE / "sistema" / "config.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def iniciar():
    config = carregar_configuracao()

    janela = tk.Tk()
    janela.title("Gotoh — Mentor de Estudos")
    janela.geometry("1000x650")
    janela.minsize(800, 500)

    estilo = ttk.Style()
    estilo.theme_use("clam")

    # Cabeçalho
    cabecalho = ttk.Frame(janela, padding=20)
    cabecalho.pack(fill="x")

    titulo = ttk.Label(
        cabecalho,
        text="🤖 GOTOH",
        font=("Sans", 24, "bold")
    )
    titulo.pack(anchor="w")

    subtitulo = ttk.Label(
        cabecalho,
        text="Seu mentor pessoal de estudos",
        font=("Sans", 12)
    )
    subtitulo.pack(anchor="w", pady=(5, 0))

    # Área principal
    principal = ttk.Frame(janela, padding=20)
    principal.pack(fill="both", expand=True)

    # Menu lateral
    menu = ttk.LabelFrame(
        principal,
        text="Estudos",
        padding=15
    )
    menu.pack(side="left", fill="y", padx=(0, 20))

    areas = [
        "🧠 Programação",
        "🌐 Desenvolvimento Web",
        "🐍 Python",
        "🗄️ Banco de Dados",
        "🔧 Git e GitHub",
        "🤖 Inteligência Artificial"
    ]

    for area in areas:
        botao = ttk.Button(
            menu,
            text=area,
            width=25
        )
        botao.pack(fill="x", pady=5)

    # Conteúdo
    conteudo = ttk.Frame(principal, padding=10)
    conteudo.pack(side="left", fill="both", expand=True)

    saudacao = ttk.Label(
        conteudo,
        text="Olá! 👋",
        font=("Sans", 22, "bold")
    )
    saudacao.pack(anchor="w")

    descricao = ttk.Label(
        conteudo,
        text=(
            "Estou pronto para te ajudar a estudar Ciência da Computação.\n\n"
            "Escolha uma área ao lado para começar."
        ),
        font=("Sans", 12),
        justify="left"
    )
    descricao.pack(anchor="w", pady=(10, 30))

    # Cards
    cards = ttk.Frame(conteudo)
    cards.pack(fill="x")

    opcoes = [
        ("📖", "Continuar estudo"),
        ("💻", "Projetos"),
        ("🧪", "Exercícios"),
        ("📊", "Meu progresso")
    ]

    for icone, texto in opcoes:
        card = ttk.LabelFrame(
            cards,
            text=f"{icone} {texto}",
            padding=20
        )
        card.pack(side="left", fill="both", expand=True, padx=5)

        ttk.Label(
            card,
            text="Em construção",
            font=("Sans", 10)
        ).pack()

    # Rodapé
    rodape = ttk.Label(
        janela,
        text="Gotoh • Mentor de estudos • Ciência da Computação",
        padding=10
    )
    rodape.pack(fill="x")

    janela.mainloop()


if __name__ == "__main__":
    iniciar()
