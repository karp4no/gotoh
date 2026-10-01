from sistema.conhecimento import buscar_conhecimento, resumir_resultados


def consultar(termo):
    termo = termo.strip()

    if not termo:
        return {
            "fonte": None,
            "encontrou": False,
            "resposta": "Não recebi um assunto para pesquisar."
        }

    resultados = buscar_conhecimento(termo)

    if resultados:
        return {
            "fonte": "local",
            "encontrou": True,
            "resposta": resumir_resultados(resultados)
        }

    return {
        "fonte": None,
        "encontrou": False,
        "resposta": None
    }
