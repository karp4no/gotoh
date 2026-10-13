import json
import os
from datetime import datetime
from sistema.memoria import carregar_memoria, salvar_memoria

def adicionar_compromisso(titulo: str, data_hora: str = None, descricao: str = "") -> dict:
    """
    Registra um compromisso ou reunião na agenda local.
    """
    memoria = carregar_memoria()
    if "compromissos" not in memoria:
        memoria["compromissos"] = []

    novo_compromisso = {
        "id": f"comp_{int(datetime.now().timestamp())}",
        "titulo": titulo,
        "data_hora": data_hora if data_hora else "Sem data definida",
        "descricao": descricao,
        "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "concluido": False
    }

    memoria["compromissos"].append(novo_compromisso)
    salvar_memoria(memoria)
    return novo_compromisso

def listar_compromissos() -> list:
    memoria = carregar_memoria()
    return memoria.get("compromissos", [])

def formatar_compromissos_para_exibicao() -> str:
    compromissos = listar_compromissos()
    if not compromissos:
        return "📅 Nenhum compromisso ou reunião agendada no momento."

    texto = "📅 **Seus Compromissos e Reuniões:**\n"
    for i, c in enumerate(compromissos, 1):
        status = "✅" if c.get("concluido") else "📌"
        texto += f"{i}. {status} **{c['titulo']}** — 🕒 {c['data_hora']}\n"
        if c.get("descricao"):
            texto += f"   • {c['descricao']}\n"
    return texto
