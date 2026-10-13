from pathlib import Path
from datetime import datetime

RAIZ = Path(__file__).resolve().parent

ARQUIVO_CONTEXTO = RAIZ / "CONTEXTO.md"
ARQUIVO_CODIGO = RAIZ / "codigo-atual.txt"

EXTENSOES_CODIGO = {
    ".py",
    ".js",
    ".html",
    ".css",
    ".json",
    ".md",
}

DIRETORIOS_IGNORADOS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
}

ARQUIVOS_IGNORADOS = {
    "memoria.json",
    "codigo-atual.txt",
    "CONTEXTO.md",
    "gerar-contexto.py",
}


def arquivo_de_codigo(caminho):
    if caminho.name in ARQUIVOS_IGNORADOS:
        return False

    if any(parte in DIRETORIOS_IGNORADOS for parte in caminho.parts):
        return False

    return caminho.suffix.lower() in EXTENSOES_CODIGO


def listar_arquivos():
    arquivos = []

    for caminho in RAIZ.rglob("*"):
        if caminho.is_file() and arquivo_de_codigo(caminho):
            arquivos.append(caminho)

    return sorted(arquivos)


def gerar_codigo():
    arquivos = listar_arquivos()

    with ARQUIVO_CODIGO.open("w", encoding="utf-8") as arquivo:
        arquivo.write(
            "GOTOH — CÓDIGO ATUAL\n"
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
        )

        arquivo.write(
            "Este arquivo é um snapshot do código atual do projeto.\n"
            "Arquivos sensíveis, ambiente virtual e dados de memória foram excluídos.\n\n"
        )

        for caminho in arquivos:
            relativo = caminho.relative_to(RAIZ)

            arquivo.write("\n")
            arquivo.write("=" * 72 + "\n")
            arquivo.write(f"ARQUIVO: {relativo}\n")
            arquivo.write("=" * 72 + "\n\n")

            try:
                conteudo = caminho.read_text(encoding="utf-8")
                arquivo.write(conteudo)
            except UnicodeDecodeError:
                arquivo.write("[Arquivo ignorado: não é texto UTF-8]\n")

            arquivo.write("\n\n")

    return arquivos


def gerar_contexto(arquivos):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    linhas = [
        "# GOTOH — CONTEXTO PARA CONTINUIDADE",
        "",
        f"Última geração: {agora}",
        "",
        "## O que é",
        "",
        "Gotoh é um agente pessoal desenvolvido localmente em Python.",
        "",
        "Seu objetivo é ajudar o usuário em estudos, programação, organização, "
        "projetos, documentos, tarefas, conhecimento, pesquisa e futuramente "
        "ações mais autônomas.",
        "",
        "Programação e Ciência da Computação são prioridades atuais por causa "
        "dos estudos do usuário, mas o Gotoh NÃO deve ser limitado a programação.",
        "",
        "## Princípios",
        "",
        "- Arquitetura modular.",
        "- Separação entre interface e lógica.",
        "- Evitar arquivos gigantes.",
        "- Criar módulos específicos para funcionalidades independentes.",
        "- Manter memória separada de conhecimento.",
        "- Desenvolver gradualmente.",
        "- Não quebrar funcionalidades existentes sem necessidade.",
        "",
        "## Método de estudo",
        "",
        "PDF/aula → entender → atividade → raciocínio → aplicação prática "
        "→ teste → Git → Notion.",
        "",
        "## Estrutura principal",
        "",
        "```text",
        "Gotoh/",
        "├── iniciar.py",
        "├── interface/",
        "├── sistema/",
        "├── conhecimento/",
        "├── dados/",
        "└── projetos/",
        "```",
        "",
        "## Interface",
        "",
        "A interface utiliza Python/Tkinter.",
        "",
        "Arquivos principais:",
        "",
        "- interface/app.py",
        "- interface/tema.py",
        "- interface/componentes.py",
        "- interface/telas/",
        "",
        "A interface possui telas para conversa, estudos, conhecimento, "
        "tarefas, projetos, notas, progresso e configurações.",
        "",
        "## Sistema",
        "",
        "O diretório `sistema/` contém a lógica principal do agente.",
        "",
        "Módulos importantes atualmente:",
        "",
        "- sistema/agente.py",
        "- sistema/documentos.py",
        "- sistema/estudo.py",
        "",
        "## Leitura de PDF",
        "",
        "O Gotoh possui suporte inicial para leitura de PDFs utilizando PyMuPDF.",
        "",
        "`sistema/documentos.py` realiza a extração do texto página por página.",
        "",
        "`sistema/estudo.py` trata o material, permitindo limpeza, análise e "
        "busca de termos.",
        "",
        "## Memória",
        "",
        "A memória persistente fica em:",
        "",
        "`dados/memoria.json`",
        "",
        "Esse arquivo é propositalmente excluído deste pacote de contexto "
        "porque pode conter informações pessoais.",
        "",
        "## Conhecimento",
        "",
        "O diretório `conhecimento/` contém informações estruturadas utilizadas "
        "pelo Gotoh.",
        "",
        "Existe documentação sobre programação e sobre o próprio estado do projeto.",
        "",
        "## Web",
        "",
        "O Gotoh possui módulo de pesquisa web, utilizado para consultas externas.",
        "",
        "## Git",
        "",
        "O projeto utiliza Git localmente.",
        "",
        "O repositório não está atualmente conectado a um GitHub remoto.",
        "",
        "## Como executar",
        "",
        "```bash",
        "cd /home/karpano/Gotoh",
        "source .venv/bin/activate",
        "python iniciar.py",
        "```",
        "",
        "## Arquivos incluídos neste snapshot",
        "",
    ]

    for caminho in arquivos:
        linhas.append(f"- `{caminho.relative_to(RAIZ)}`")

    linhas.extend(
        [
            "",
            "## Como usar este arquivo em outra IA",
            "",
            "Primeiro forneça este arquivo para a IA e explique que ele contém "
            "o contexto arquitetural do projeto.",
            "",
            "Depois forneça `codigo-atual.txt`, que contém os arquivos de código "
            "e documentação incluídos no snapshot.",
            "",
            "Prompt recomendado:",
            "",
            "> Este é o projeto Gotoh. Leia primeiro o CONTEXTO.md para entender "
            "a arquitetura e as decisões do projeto. Depois leia o codigo-atual.txt "
            "para conhecer o código atual. Não faça alterações ainda. Primeiro "
            "analise a estrutura e me diga quais arquivos estão relacionados ao "
            "problema que vou apresentar.",
            "",
            "## Regra importante",
            "",
            "Este arquivo é um snapshot e não substitui os arquivos reais do projeto.",
            "Depois de alterações importantes, execute novamente:",
            "",
            "```bash",
            "python gerar-contexto.py",
            "```",
            "",
            "Isso atualizará o contexto e o código exportado.",
            "",
        ]
    )

    ARQUIVO_CONTEXTO.write_text(
        "\n".join(linhas),
        encoding="utf-8",
    )


def main():
    arquivos = gerar_codigo()
    gerar_contexto(arquivos)

    print("Contexto gerado com sucesso.")
    print(f"Arquivos incluídos: {len(arquivos)}")
    print(f"Contexto: {ARQUIVO_CONTEXTO}")
    print(f"Código:   {ARQUIVO_CODIGO}")


if __name__ == "__main__":
    main()
