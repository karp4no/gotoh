from pathlib import Path

import pymupdf as fitz


EXTENSOES_SUPORTADAS = {
    ".pdf",
}


def arquivo_suportado(caminho):
    return Path(caminho).suffix.lower() in EXTENSOES_SUPORTADAS


def ler_pdf(caminho):
    caminho = Path(caminho)

    if not caminho.exists():
        return {
            "sucesso": False,
            "erro": "Arquivo não encontrado.",
            "texto": "",
            "paginas": 0,
        }

    if caminho.suffix.lower() != ".pdf":
        return {
            "sucesso": False,
            "erro": "O arquivo informado não é um PDF.",
            "texto": "",
            "paginas": 0,
        }

    try:
        documento = fitz.open(caminho)

        paginas = []

        for numero, pagina in enumerate(documento, start=1):
            texto = pagina.get_text("text").strip()

            if texto:
                paginas.append(
                    f"--- Página {numero} ---\n{texto}"
                )

        resultado = {
            "sucesso": True,
            "erro": None,
            "texto": "\n\n".join(paginas),
            "paginas": len(documento),
            "paginas_com_texto": len(paginas),
            "arquivo": caminho.name,
        }

        documento.close()

        return resultado

    except Exception as erro:
        return {
            "sucesso": False,
            "erro": str(erro),
            "texto": "",
            "paginas": 0,
        }


def obter_informacoes_pdf(caminho):
    resultado = ler_pdf(caminho)

    if not resultado["sucesso"]:
        return resultado

    texto = resultado["texto"]

    return {
        "sucesso": True,
        "arquivo": resultado["arquivo"],
        "paginas": resultado["paginas"],
        "paginas_com_texto": resultado["paginas_com_texto"],
        "caracteres": len(texto),
        "texto": texto,
    }
