from interface.componentes import limpar_conteudo, criar_titulo, criar_card


def mostrar(conteudo, config):
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
