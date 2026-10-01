import json
from pathlib import Path
from datetime import datetime


BASE = Path(__file__).resolve().parent.parent
ARQUIVO_MEMORIA = BASE / "dados" / "memoria.json"


# =========================
# MEMÓRIA BÁSICA
# =========================

def criar_memoria_inicial():
    return {
        "usuario": {
            "nome": "Rodrigo"
        },
        "preferencias": {
            "idioma": "pt-BR",
            "nivel": "iniciante",
            "estilo_aprendizado": "pratico"
        },
        "estudos": {
            "curso": "Ciência da Computação"
        },
        "tarefas": [],
        "notas": [],
        "projetos": [],
        "memorias": []
    }


def carregar_memoria():
    if not ARQUIVO_MEMORIA.exists():
        memoria = criar_memoria_inicial()
        salvar_memoria(memoria)
        return memoria

    with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
        memoria = json.load(arquivo)

    # Garante compatibilidade com versões anteriores
    memoria.setdefault("usuario", {})
    memoria.setdefault("preferencias", {})
    memoria.setdefault("estudos", {})
    memoria.setdefault("tarefas", [])
    memoria.setdefault("notas", [])
    memoria.setdefault("projetos", [])
    memoria.setdefault("memorias", [])

    return memoria


def salvar_memoria(memoria):
    ARQUIVO_MEMORIA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        ARQUIVO_MEMORIA,
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(
            memoria,
            arquivo,
            ensure_ascii=False,
            indent=2
        )


# =========================
# MEMÓRIAS
# =========================

def adicionar_memoria(texto, categoria="geral"):
    texto = texto.strip()

    if not texto:
        return False

    memoria = carregar_memoria()

    memoria["memorias"].append({
        "texto": texto,
        "categoria": categoria,
        "data": datetime.now().isoformat(timespec="seconds")
    })

    salvar_memoria(memoria)

    return True


def listar_memorias():
    memoria = carregar_memoria()
    return memoria.get("memorias", [])


def buscar_memorias(termo):
    termo = termo.strip().lower()

    if not termo:
        return []

    memorias = listar_memorias()
    resultados = []

    for item in memorias:
        texto = item.get("texto", "").lower()
        categoria = item.get("categoria", "").lower()

        if termo in texto or termo in categoria:
            resultados.append(item)

    return resultados


def remover_memoria(indice):
    memoria = carregar_memoria()
    memorias = memoria.get("memorias", [])

    if 0 <= indice < len(memorias):
        memorias.pop(indice)
        salvar_memoria(memoria)
        return True

    return False


def limpar_memorias():
    memoria = carregar_memoria()
    memoria["memorias"] = []
    salvar_memoria(memoria)


# =========================
# TAREFAS
# =========================

def adicionar_tarefa(tarefa):
    tarefa = tarefa.strip()

    if not tarefa:
        return False

    memoria = carregar_memoria()

    memoria["tarefas"].append({
        "texto": tarefa,
        "concluida": False,
        "data": datetime.now().isoformat(timespec="seconds")
    })

    salvar_memoria(memoria)

    return True


def concluir_tarefa(indice):
    memoria = carregar_memoria()
    tarefas = memoria["tarefas"]

    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_memoria(memoria)
        return True

    return False


def remover_tarefa(indice):
    memoria = carregar_memoria()
    tarefas = memoria["tarefas"]

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_memoria(memoria)
        return True

    return False


def listar_tarefas():
    memoria = carregar_memoria()
    return memoria["tarefas"]


def buscar_tarefas(termo):
    termo = termo.strip().lower()

    if not termo:
        return []

    tarefas = listar_tarefas()

    return [
        tarefa
        for tarefa in tarefas
        if termo in tarefa["texto"].lower()
    ]


# =========================
# NOTAS
# =========================

def adicionar_nota(nota):
    nota = nota.strip()

    if not nota:
        return False

    memoria = carregar_memoria()

    memoria["notas"].append({
        "texto": nota,
        "data": datetime.now().isoformat(timespec="seconds")
    })

    salvar_memoria(memoria)

    return True


def listar_notas():
    memoria = carregar_memoria()
    return memoria["notas"]


def buscar_notas(termo):
    termo = termo.strip().lower()

    if not termo:
        return []

    notas = listar_notas()

    return [
        nota
        for nota in notas
        if termo in nota.get("texto", "").lower()
    ]


def remover_nota(indice):
    memoria = carregar_memoria()
    notas = memoria["notas"]

    if 0 <= indice < len(notas):
        notas.pop(indice)
        salvar_memoria(memoria)
        return True

    return False


# =========================
# PROJETOS
# =========================

def adicionar_projeto(nome, descricao=""):
    nome = nome.strip()
    descricao = descricao.strip()

    if not nome:
        return False

    memoria = carregar_memoria()

    memoria["projetos"].append({
        "nome": nome,
        "descricao": descricao,
        "data": datetime.now().isoformat(timespec="seconds")
    })

    salvar_memoria(memoria)

    return True


def listar_projetos():
    memoria = carregar_memoria()
    return memoria["projetos"]


def buscar_projetos(termo):
    termo = termo.strip().lower()

    if not termo:
        return []

    projetos = listar_projetos()
    resultados = []

    for projeto in projetos:
        nome = projeto.get("nome", "").lower()
        descricao = projeto.get("descricao", "").lower()

        if termo in nome or termo in descricao:
            resultados.append(projeto)

    return resultados


# =========================
# PERFIL
# =========================

def obter_usuario():
    memoria = carregar_memoria()
    return memoria.get("usuario", {})


def obter_preferencias():
    memoria = carregar_memoria()
    return memoria.get("preferencias", {})


def obter_estudos():
    memoria = carregar_memoria()
    return memoria.get("estudos", {})


def atualizar_usuario(campo, valor):
    campo = campo.strip()

    if not campo:
        return False

    memoria = carregar_memoria()
    memoria.setdefault("usuario", {})
    memoria["usuario"][campo] = valor

    salvar_memoria(memoria)

    return True


def atualizar_preferencia(campo, valor):
    campo = campo.strip()

    if not campo:
        return False

    memoria = carregar_memoria()
    memoria.setdefault("preferencias", {})
    memoria["preferencias"][campo] = valor

    salvar_memoria(memoria)

    return True


def atualizar_estudo(campo, valor):
    campo = campo.strip()

    if not campo:
        return False

    memoria = carregar_memoria()
    memoria.setdefault("estudos", {})
    memoria["estudos"][campo] = valor

    salvar_memoria(memoria)

    return True


# =========================
# RESUMO
# =========================

def resumo_memoria():
    memoria = carregar_memoria()

    return {
        "usuario": memoria.get("usuario", {}),
        "preferencias": memoria.get("preferencias", {}),
        "estudos": memoria.get("estudos", {}),
        "quantidade_tarefas": len(memoria.get("tarefas", [])),
        "quantidade_notas": len(memoria.get("notas", [])),
        "quantidade_projetos": len(memoria.get("projetos", [])),
        "quantidade_memorias": len(memoria.get("memorias", []))
    }
