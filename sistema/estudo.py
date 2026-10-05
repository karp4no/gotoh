from pathlib import Path


def limpar_texto(texto):
    linhas = []
    for linha in texto.splitlines():
        linha = linha.strip()
        if linha:
            linhas.append(linha)
    return '\n'.join(linhas)


def buscar_no_material(texto, termo):
    termo = termo.strip().lower()

    if not termo:
        return []

    linhas = texto.splitlines()
    resultados = []

    for numero, linha in enumerate(linhas, start=1):
        if termo in linha.lower():
            inicio = max(0, numero - 2)
            fim = min(len(linhas), numero + 2)
            resultados.append({
                "linha": numero,
                "trecho": "\n".join(linhas[inicio:fim])
            })

    return resultados


def analisar_material(texto):
    texto_limpo = limpar_texto(texto)
    linhas = texto_limpo.splitlines()
    palavras = texto_limpo.split()

    return {
        "caracteres": len(texto_limpo),
        "linhas": len(linhas),
        "palavras": len(palavras),
        "texto": texto_limpo,
    }


def preparar_estudo(texto, assunto=None):
    analise = analisar_material(texto)

    resultado = {
        "tipo": "material de estudo",
        "assunto": assunto,
        "estatisticas": {
            "caracteres": analise["caracteres"],
            "linhas": analise["linhas"],
            "palavras": analise["palavras"],
        },
        "texto": analise["texto"],
    }

    if assunto:
        resultado["ocorrencias"] = buscar_no_material(texto, assunto)

    return resultado
