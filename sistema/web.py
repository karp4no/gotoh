import json
import urllib.parse
import urllib.request


def pesquisar(consulta, quantidade=5):
    consulta = consulta.strip()

    if not consulta:
        return []

    parametros = urllib.parse.urlencode({
        "q": consulta,
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1
    })

    url = "https://api.duckduckgo.com/?" + parametros

    try:
        requisicao = urllib.request.Request(
            url,
            headers={"User-Agent": "Gotoh/1.0"}
        )

        with urllib.request.urlopen(requisicao, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))

    except Exception:
        return []

    resultados = []

    if dados.get("AbstractText"):
        resultados.append({
            "titulo": dados.get("Heading", consulta),
            "resumo": dados["AbstractText"],
            "url": dados.get("AbstractURL", "")
        })

    def adicionar_itens(itens):
        for item in itens:
            if len(resultados) >= quantidade:
                return

            texto = item.get("Text", "")
            url_item = item.get("FirstURL", "")

            if texto and url_item:
                resultados.append({
                    "titulo": texto,
                    "resumo": texto,
                    "url": url_item
                })

    adicionar_itens(dados.get("RelatedTopics", []))

    return resultados
