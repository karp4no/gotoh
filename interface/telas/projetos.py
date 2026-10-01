from interface.componentes import limpar_conteudo, criar_titulo, criar_card


def mostrar(conteudo):
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
