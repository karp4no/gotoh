from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
PASTA_CONHECIMENTO = BASE / "conhecimento"


def listar_areas():
    areas = []

    if not PASTA_CONHECIMENTO.exists():
        return areas

    for pasta in sorted(PASTA_CONHECIMENTO.iterdir()):
        if pasta.is_dir():
            areas.append(pasta.name)

    return areas


def listar_arquivos(area):
    pasta = PASTA_CONHECIMENTO / area

    if not pasta.exists() or not pasta.is_dir():
        return []

    return sorted(
        arquivo
        for arquivo in pasta.iterdir()
        if arquivo.is_file() and arquivo.suffix == ".md"
    )


def ler_conhecimento(caminho):
    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:
        return arquivo.read()


def buscar_arquivos(termo):
    termo = termo.strip().lower()

    if not termo:
        return []

    resultados = []

    for arquivo in PASTA_CONHECIMENTO.rglob("*.md"):
        if termo in arquivo.name.lower():
            resultados.append(arquivo)

    return resultados


def buscar_conhecimento(termo):
    """
    Procura o termo dentro do conteúdo dos arquivos Markdown.
    Retorna os trechos relevantes encontrados.
    """

    termo = termo.strip().lower()

    if not termo:
        return []

    resultados = []

    for arquivo in PASTA_CONHECIMENTO.rglob("*.md"):

        try:
            conteudo = ler_conhecimento(arquivo)
        except OSError:
            continue

        linhas = conteudo.splitlines()

        encontrados = []

        for numero, linha in enumerate(linhas, start=1):
            if termo in linha.lower():
                inicio = max(0, numero - 2)
                fim = min(len(linhas), numero + 2)

                trecho = "\n".join(
                    linhas[inicio:fim]
                )

                encontrados.append({
                    "linha": numero,
                    "trecho": trecho
                })

        if encontrados:
            resultados.append({
                "arquivo": arquivo,
                "nome": arquivo.name,
                "area": arquivo.parent.name,
                "resultados": encontrados
            })

    return resultados


def resumir_resultados(resultados):
    if not resultados:
        return "Não encontrei informações sobre esse assunto no meu conhecimento."

    resposta = "Encontrei estas informações:\n\n"

    for resultado in resultados:

        resposta += (
            f"📚 {resultado['area']} / "
            f"{resultado['nome']}\n"
        )

        for item in resultado["resultados"][:3]:
            resposta += f"{item['trecho']}\n\n"

    return resposta.strip()
