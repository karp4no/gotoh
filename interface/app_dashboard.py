import json
import tkinter as tk
from pathlib import Path
from tkinter import ttk


BASE = Path(__file__).resolve().parent.parent


def carregar_configuracao():
    caminho = BASE / "sistema" / "config.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_memoria():
    caminho = BASE / "dados" / "memoria.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def limpar_conteudo(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def criar_titulo(frame, titulo, subtitulo=None):
    tk.Label(
        frame,
        text=titulo,
        font=("Arial", 22, "bold"),
        anchor="w"
    ).pack(fill="x", padx=25, pady=(25, 5))

    if subtitulo:
        tk.Label(
            frame,
            text=subtitulo,
            font=("Arial", 11),
            anchor="w"
        ).pack(fill="x", padx=25, pady=(0, 20))


def criar_card(frame, titulo, descricao, comando=None):
    card = tk.Frame(
        frame,
        bd=1,
        relief="solid",
        padx=15,
        pady=15
    )

    card.pack(
        fill="x",
        padx=25,
        pady=7
    )

    tk.Label(
        card,
        text=titulo,
        font=("Arial", 13, "bold"),
        anchor="w"
    ).pack(fill="x")

    tk.Label(
        card,
        text=descricao,
        font=("Arial", 10),
        anchor="w",
        justify="left"
    ).pack(fill="x", pady=(5, 0))

    if comando:
        ttk.Button(
            card,
            text="Abrir",
            command=comando
        ).pack(anchor="e", pady=(10, 0))


def mostrar_inicio(conteudo, memoria):
    limpar_conteudo(conteudo)

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


def mostrar_estudos(conteudo):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "📚 Estudos",
        "Área para organizar sua jornada de aprendizado."
    )

    criar_card(
        conteudo,
        "💻 Programação",
        "Fundamentos, lógica, algoritmos e desenvolvimento."
    )

    criar_card(
        conteudo,
        "🌐 Desenvolvimento Web",
        "HTML, CSS, JavaScript, acessibilidade e interfaces."
    )

    criar_card(
        conteudo,
        "🐍 Python",
        "Python, automação, backend e projetos."
    )

    criar_card(
        conteudo,
        "🗄️ Banco de Dados",
        "Modelagem, SQL, SQLite e integração com aplicações."
    )

    criar_card(
        conteudo,
        "🤖 Inteligência Artificial",
        "IA, Machine Learning, ética e engenharia de prompts."
    )


def mostrar_conhecimento(conteudo):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "🧠 Conhecimento",
        "Base de conhecimento utilizada pelo Gotoh."
    )

    criar_card(
        conteudo,
        "📖 Base de Estudos",
        "Conteúdos organizados para consulta e aprendizado."
    )

    criar_card(
        conteudo,
        "🧩 Conceitos",
        "Explicações simples para conceitos importantes."
    )


def mostrar_tarefas(conteudo, memoria):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "📋 Tarefas",
        "Organize o que precisa ser feito."
    )

    if not memoria["tarefas"]:
        criar_card(
            conteudo,
            "Nenhuma tarefa ainda",
            "As tarefas poderão ser adicionadas aqui."
        )
    else:
        for tarefa in memoria["tarefas"]:
            criar_card(
                conteudo,
                "📌 Tarefa",
                tarefa
            )


def mostrar_projetos(conteudo):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "🚀 Projetos",
        "Projetos acompanhados pelo Gotoh."
    )

    criar_card(
        conteudo,
        "Job Hunter",
        "Projeto Flask + SQLite para estudos e desenvolvimento."
    )

    criar_card(
        conteudo,
        "Projeto ONG",
        "Projeto web desenvolvido para a faculdade."
    )

    criar_card(
        conteudo,
        "NEXO",
        "Projeto voltado para soluções e automações para empresas."
    )


def mostrar_notas(conteudo, memoria):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "📝 Notas",
        "Anotações e informações importantes."
    )

    if not memoria["notas"]:
        criar_card(
            conteudo,
            "Nenhuma nota ainda",
            "As notas poderão ser adicionadas aqui."
        )
    else:
        for nota in memoria["notas"]:
            criar_card(
                conteudo,
                "📝 Nota",
                nota
            )


def mostrar_progresso(conteudo):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "📊 Progresso",
        "Acompanhe sua evolução."
    )

    criar_card(
        conteudo,
        "🎓 Faculdade",
        "Acompanhar disciplinas, atividades e aprendizados."
    )

    criar_card(
        conteudo,
        "💻 Programação",
        "Acompanhar conceitos estudados e projetos realizados."
    )

    criar_card(
        conteudo,
        "🚀 Projetos",
        "Acompanhar evolução dos projetos pessoais e acadêmicos."
    )


def mostrar_configuracoes(conteudo, config):
    limpar_conteudo(conteudo)

    criar_titulo(
        conteudo,
        "⚙️ Configurações",
        "Informações e configurações atuais do Gotoh."
    )

    criar_card(
        conteudo,
        "🤖 Identidade",
        f"Nome: {config['nome']}\nTipo: {config['tipo']}"
    )

    criar_card(
        conteudo,
        "🌎 Idioma",
        config["idioma"]
    )

    criar_card(
        conteudo,
        "🎯 Nível",
        config["nivel_usuario"]
    )


def iniciar():
    config = carregar_configuracao()
    memoria = carregar_memoria()

    janela = tk.Tk()
    janela.title("Gotoh — Agente Pessoal")
    janela.geometry("1050x650")
    janela.minsize(900, 550)

    # ==========================
    # MENU LATERAL
    # ==========================

    menu = tk.Frame(
        janela,
        width=230,
        bd=1,
        relief="solid"
    )

    menu.pack(
        side="left",
        fill="y"
    )

    tk.Label(
        menu,
        text="🤖 GOTOH",
        font=("Arial", 20, "bold")
    ).pack(
        pady=(25, 5)
    )

    tk.Label(
        menu,
        text="Agente pessoal",
        font=("Arial", 10)
    ).pack(
        pady=(0, 25)
    )

    # ==========================
    # ÁREA PRINCIPAL
    # ==========================

    conteudo = tk.Frame(janela)

    conteudo.pack(
        side="right",
        fill="both",
        expand=True
    )

    def botao(texto, comando):
        ttk.Button(
            menu,
            text=texto,
            command=comando
        ).pack(
            fill="x",
            padx=15,
            pady=4
        )

    botao(
        "🏠  Início",
        lambda: mostrar_inicio(conteudo, memoria)
    )

    botao(
        "📚  Estudos",
        lambda: mostrar_estudos(conteudo)
    )

    botao(
        "🧠  Conhecimento",
        lambda: mostrar_conhecimento(conteudo)
    )

    botao(
        "📋  Tarefas",
        lambda: mostrar_tarefas(conteudo, memoria)
    )

    botao(
        "🚀  Projetos",
        lambda: mostrar_projetos(conteudo)
    )

    botao(
        "📝  Notas",
        lambda: mostrar_notas(conteudo, memoria)
    )

    botao(
        "📊  Progresso",
        lambda: mostrar_progresso(conteudo)
    )

    botao(
        "⚙️  Configurações",
        lambda: mostrar_configuracoes(conteudo, config)
    )

    mostrar_inicio(conteudo, memoria)

    janela.mainloop()


if __name__ == "__main__":
    iniciar()
