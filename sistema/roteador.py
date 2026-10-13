import os
from sistema.conhecimento import buscar_conhecimento, resumir_resultados
from sistema.pesquisa_web import buscar_web, formatar_resultados_web

def consultar(termo: str) -> dict:
    """
    Roteia a consulta:
    1. Busca primeiro na base de conhecimento local em Markdown.
    2. Se não encontrar, faz busca autônoma na Web.
    """
    # 1. Busca Local
    resultados_locais = buscar_conhecimento(termo)
    if resultados_locais:
        return {
            "fonte": "local",
            "encontrou": True,
            "resposta": f"📖 **[Base Local]**\n{resumir_resultados(resultados_locais)}"
        }

    # 2. Busca Web (Fallback)
    resultados_web = buscar_web(termo)
    if resultados_web:
        return {
            "fonte": "web",
            "encontrou": True,
            "resposta": formatar_resultados_web(termo, resultados_web)
        }

    return {
        "fonte": "nenhuma",
        "encontrou": False,
        "resposta": f"Não encontrei registros locais nem na internet sobre '{termo}'."
    }
