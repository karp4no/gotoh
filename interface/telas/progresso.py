from interface.componentes import limpar_conteudo, criar_titulo, criar_card


def mostrar(conteudo):
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
