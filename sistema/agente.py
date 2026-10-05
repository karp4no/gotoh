from sistema.conhecimento import (
    buscar_conhecimento,
    resumir_resultados,
)

from sistema.roteador import consultar
from sistema.documentos import obter_informacoes_pdf
from sistema.estudo import preparar_estudo, buscar_no_material


MATERIAL_ESTUDO_ATUAL = None

from sistema.memoria import (
    adicionar_memoria,
    buscar_memorias,
    listar_memorias,
    adicionar_tarefa,
    listar_tarefas,
    adicionar_nota,
    listar_notas,
)


def normalizar(texto):
    return texto.strip().lower()


def consultar_conhecimento(termo):
    resultado = consultar(termo)
    if resultado["encontrou"]:
        return resultado["resposta"]
    return "Ainda não tenho informações sobre esse assunto no meu conhecimento local."


def analisar_pdf(caminho):
    global MATERIAL_ESTUDO_ATUAL

    resultado = obter_informacoes_pdf(caminho)

    if not resultado["sucesso"]:
        return f"Não consegui abrir o PDF: {resultado["erro"]}"

    estudo = preparar_estudo(resultado["texto"])

    MATERIAL_ESTUDO_ATUAL = {
        "arquivo": resultado["arquivo"],
        "caminho": caminho,
        "texto": resultado["texto"],
    }

    return (
        f"Encontrei o PDF: {resultado["arquivo"]}\n\n"
        f"Páginas: {resultado["paginas"]}\n"
        f"Palavras extraídas: {estudo["estatisticas"]["palavras"]}\n\n"
        "O material foi carregado temporariamente para estudo. "
        "Ele ainda não foi salvo como conhecimento permanente."
    )


def consultar_material_atual(termo):
    if not MATERIAL_ESTUDO_ATUAL:
        return "Nenhum PDF foi carregado nesta sessão."

    resultados = buscar_no_material(MATERIAL_ESTUDO_ATUAL["texto"], termo)

    if not resultados:
        return (
            f"Não encontrei informações sobre {termo} "
            "no PDF carregado."
        )

    resposta = (
        f"Encontrei estas partes no PDF "
        f"{MATERIAL_ESTUDO_ATUAL["arquivo"]}:\n\n"
    )

    for resultado in resultados[:5]:
        resposta += f"{resultado["trecho"]}\n\n"

    return resposta.strip()


def processar_comando(texto):
    comando = normalizar(texto)

    if not comando:
        return "Não recebi nenhum comando."

    if comando.startswith("analise o pdf ") or comando.startswith("analise esse pdf "):
        partes = texto.split(" ", 3)

        if len(partes) == 4:
            caminho = partes[3].strip()
            return analisar_pdf(caminho)

        return "Use assim: analise o PDF /caminho/do/arquivo.pdf"



    # MEMÓRIA

    if comando.startswith("lembra que "):
        conteudo = texto[len("lembra que "):].strip()

        if adicionar_memoria(conteudo):
            return f"Entendi. Vou lembrar disso: {conteudo}"

        return "Não consegui salvar essa memória."


    if comando.startswith("lembre que "):
        conteudo = texto[len("lembre que "):].strip()

        if adicionar_memoria(conteudo):
            return f"Entendi. Vou lembrar disso: {conteudo}"

        return "Não consegui salvar essa memória."


    if comando.startswith("guarda que "):
        conteudo = texto[len("guarda que "):].strip()

        if adicionar_memoria(conteudo):
            return f"Certo. Guardei isso: {conteudo}"

        return "Não consegui salvar essa memória."


    if comando.startswith("guardar que "):
        conteudo = texto[len("guardar que "):].strip()

        if adicionar_memoria(conteudo):
            return f"Certo. Guardei isso: {conteudo}"

        return "Não consegui salvar essa memória."


    if comando.startswith("o que você lembra"):
        partes = texto.split("sobre", 1)

        if len(partes) == 2:
            termo = partes[1].strip()
            resultados = buscar_memorias(termo)

            if not resultados:
                return f"Não encontrei nenhuma memória sobre {termo}."

            resposta = "Encontrei estas memórias:\n"

            for memoria in resultados:
                resposta += f"- {memoria['texto']}\n"

            return resposta.strip()

        memorias = listar_memorias()

        if not memorias:
            return "Ainda não tenho memórias registradas."

        resposta = "Estas são algumas coisas que lembro:\n"

        for memoria in memorias:
            resposta += f"- {memoria['texto']}\n"

        return resposta.strip()


    # TAREFAS

    if comando.startswith("cria uma tarefa"):
        partes = texto.split(":", 1)

        if len(partes) == 2:
            tarefa = partes[1].strip()

            if adicionar_tarefa(tarefa):
                return f"Tarefa criada: {tarefa}"

        return "Use assim: cria uma tarefa: estudar Python."


    if comando.startswith("adiciona uma tarefa"):
        partes = texto.split(":", 1)

        if len(partes) == 2:
            tarefa = partes[1].strip()

            if adicionar_tarefa(tarefa):
                return f"Tarefa criada: {tarefa}"

        return "Use assim: adiciona uma tarefa: estudar Python."


    if comando.startswith("mostra minhas tarefas"):
        tarefas = listar_tarefas()

        if not tarefas:
            return "Você não tem tarefas cadastradas."

        resposta = "Suas tarefas:\n"

        for i, tarefa in enumerate(tarefas, start=1):
            status = "✓" if tarefa.get("concluida") else "○"
            resposta += f"{i}. {status} {tarefa['texto']}\n"

        return resposta.strip()


    # NOTAS

    if comando.startswith("anota que "):
        nota = texto[len("anota que "):].strip()

        if adicionar_nota(nota):
            return f"Anotado: {nota}"

        return "Não consegui salvar a nota."


    if comando.startswith("anota "):
        nota = texto[len("anota "):].strip()

        if adicionar_nota(nota):
            return f"Anotado: {nota}"

        return "Não consegui salvar a nota."


    if comando.startswith("mostra minhas notas"):
        notas = listar_notas()

        if not notas:
            return "Você não tem notas cadastradas."

        resposta = "Suas notas:\n"

        for i, nota in enumerate(notas, start=1):
            resposta += f"{i}. {nota['texto']}\n"

        return resposta.strip()


    if comando.startswith("o que essa aula fala sobre "):
        termo = texto[len("o que essa aula fala sobre "):].strip()
        return consultar_material_atual(termo)


    if comando.startswith("o que esse pdf fala sobre "):
        termo = texto[len("o que esse pdf fala sobre "):].strip()
        return consultar_material_atual(termo)


    if comando.startswith("procure no pdf "):
        termo = texto[len("procure no pdf "):].strip()
        return consultar_material_atual(termo)


    # CONHECIMENTO

    if comando.startswith("o que é "):
        termo = texto[8:].strip()

        return consultar_conhecimento(termo)


    if comando.startswith("o que e "):
        termo = texto[8:].strip()

        return consultar_conhecimento(termo)


    if comando.startswith("explique "):
        termo = texto[9:].strip()

        return consultar_conhecimento(termo)


    if comando.startswith("me explica "):
        termo = texto[11:].strip()

        return consultar_conhecimento(termo)


    # COMANDOS BÁSICOS

    if comando in ["oi", "olá", "ola", "e aí", "e ai"]:
        return "Olá! Sou o Gotoh. O que vamos fazer?"


    if comando in ["quem é você", "quem e voce", "quem é voce"]:
        return (
            "Eu sou o Gotoh, seu agente pessoal. "
            "Posso guardar informações, organizar tarefas, "
            "consultar seu conhecimento e, futuramente, pesquisar na web."
        )


    if comando in ["ajuda", "help"]:
        return (
            "Você pode me dizer coisas como:\n"
            "- lembra que eu quero estudar IA\n"
            "- cria uma tarefa: estudar Python\n"
            "- anota que preciso revisar SQL\n"
            "- mostra minhas tarefas\n"
            "- mostra minhas notas\n"
            "- o que você lembra sobre IA"
        )


    return (
        "Ainda não sei executar esse comando.\n"
        "Tente escrever 'ajuda' para ver o que já consigo fazer."
    )
