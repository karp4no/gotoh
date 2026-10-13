import json
import os
from datetime import datetime, timedelta
from sistema.memoria import carregar_memoria, salvar_memoria

def criar_plano_estudo(topico: str, dias: int = 7) -> dict:
    """
    Gera uma estrutura de plano de estudo dividida em dias
    com tópicos, roteiro de aula e tarefas diárias.
    """
    data_inicio = datetime.now()
    cronograma = []

    for i in range(dias):
        dia_numero = i + 1
        data_estudo = (data_inicio + timedelta(days=i)).strftime("%Y-%m-%d")
        
        cronograma.append({
            "dia": dia_numero,
            "data": data_estudo,
            "foco": f"Módulo {dia_numero}: Aprofundamento em {topico} (Parte {dia_numero})",
            "conteudo_chave": [
                f"Conceitos fundamentais da etapa {dia_numero}",
                f"Aplicações práticas de {topico}",
                "Revisão de pontos críticos e exercícios"
            ],
            "concluido": False
        })

    plano = {
        "id": f"estudo_{int(datetime.now().timestamp())}",
        "topico": topico,
        "duracao_dias": dias,
        "data_criacao": data_inicio.strftime("%Y-%m-%d %H:%M"),
        "status": "em_andamento",
        "aula_intro": f"Bem-vindo à introdução de {topico}. Nos próximos {dias} dias abordaremos desde os conceitos base até a fixação prática.",
        "cronograma": cronograma
    }

    # Salva no arquivo de memória
    memoria = carregar_memoria()
    if "planos_estudo" not in memoria:
        memoria["planos_estudo"] = []
    
    memoria["planos_estudo"].append(plano)
    salvar_memoria(memoria)

    return plano


def formatar_plano_para_exibicao(plano: dict) -> str:
    """
    Formata o plano de estudo em texto para exibição no chat/GUI.
    """
    texto = f"📚 **Plano de Estudo Gerado: {plano['topico'].title()}** ({plano['duracao_dias']} dias)\n"
    texto += f"🗓️ Criado em: {plano['data_criacao']}\n\n"
    texto += f"🎓 **Aula Introdutória:**\n{plano['aula_intro']}\n\n"
    texto += "📋 **Cronograma Diário:**\n"

    for item in plano["cronograma"]:
        status = "✅" if item["concluido"] else "📌"
        texto += f"{status} **Dia {item['dia']}** ({item['data']}): {item['foco']}\n"
        for sub in item["conteudo_chave"]:
            texto += f"   • {sub}\n"

    return texto
