from interface.componentes import limpar_conteudo, criar_titulo, criar_card


def mostrar(conteudo):
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
