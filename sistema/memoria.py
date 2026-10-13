import json
import os

CAMINHO_MEMORIA = os.path.join("dados", "memoria.json")

def carregar_memoria():
    if not os.path.exists(CAMINHO_MEMORIA):
        return {
            "usuario": {},
            "preferencias": {},
            "estudos": {},
            "tarefas": [],
            "notas": [],
            "projetos": [],
            "memorias": []
        }
    try:
        with open(CAMINHO_MEMORIA, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "usuario": {},
            "preferencias": {},
            "estudos": {},
            "tarefas": [],
            "notas": [],
            "projetos": [],
            "memorias": []
        }

def salvar_memoria(dados):
    os.makedirs("dados", exist_ok=True)
    with open(CAMINHO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def adicionar_tarefa(tarefa):
    memoria = carregar_memoria()
    memoria["tarefas"].append({"texto": tarefa, "concluida": False})
    salvar_memoria(memoria)

def listar_tarefas():
    memoria = carregar_memoria()
    return memoria.get("tarefas", [])

def adicionar_nota(texto):
    memoria = carregar_memoria()
    memoria["notas"].append(texto)
    salvar_memoria(memoria)

def listar_notas():
    memoria = carregar_memoria()
    return memoria.get("notas", [])

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

def concluir_tarefa(indice):
    memoria = carregar_memoria()
    tarefas = memoria.get("tarefas", [])

    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_memoria(memoria)
        return True

    return False

def remover_tarefa(indice):
    memoria = carregar_memoria()
    tarefas = memoria.get("tarefas", [])

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_memoria(memoria)
        return True

    return False


def remover_nota(indice):
    memoria = carregar_memoria()
    notas = memoria.get("notas", [])

    if 0 <= indice < len(notas):
        notas.pop(indice)
        salvar_memoria(memoria)
        return True

    return False
