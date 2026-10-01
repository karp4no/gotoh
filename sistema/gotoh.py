import json
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent


def carregar_configuracao():
    caminho = BASE / "sistema" / "config.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


def mostrar_identidade(config):
    print("=" * 50)
    print(f"🤖 {config['nome'].upper()}")
    print("=" * 50)
    print(f"Tipo: {config['tipo']}")
    print(f"Idioma: {config['idioma']}")
    print(f"Nível do estudante: {config['nivel_usuario']}")
    print()
    print("Áreas de estudo:")

    for area in config["areas"]:
        print(f"  • {area}")

    print()
    print("Método:")
    print(" → ".join(config["metodo"]))
    print("=" * 50)


def mostrar_conhecimento():
    caminho = BASE / "conhecimento" / "indice.md"

    conteudo = carregar_arquivo(caminho)

    print("\n📚 BASE DE CONHECIMENTO")
    print("=" * 50)
    print(conteudo)


def main():
    config = carregar_configuracao()

    mostrar_identidade(config)
    mostrar_conhecimento()


if __name__ == "__main__":
    main()
