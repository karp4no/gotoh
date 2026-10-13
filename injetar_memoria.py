import sys
from memory_manager import GotohMemory

fatos = [
    ("nome", "Rodrigo Bernardo"),
    ("perfil_profissional", "Estudante de Ciência da Computação, aspirante a AI Engineer, com foco em Inteligência Artificial e Machine Learning."),
    ("formacao_atual", "Bacharelado em Ciência da Computação na Cruzeiro do Sul, de 2026 a 2030."),
    ("experiencia_academica_anterior", "Cursou 2 semestres de Economia presencialmente na Cruzeiro do Sul."),
    ("ingles", "Estudou Inglês por 4 anos na Ponto Com Formação Profissional."),
    ("estilo_comunicacao", "Prefere comunicação direta, natural, simples e prática, em português brasileiro."),
    ("preferencia_para_estudos", "Gosta de explicações de iniciante, com raciocínio curto e aplicação prática, evitando linguagem excessivamente formal ou acadêmica."),
    ("preferencia_para_atividades", "Quando precisa entregar uma atividade da faculdade, prefere receber primeiro uma resposta pronta e depois uma explicação curta do raciocínio."),
    ("preferencia_para_textos_academicos", "Prefere respostas que pareçam naturally escritas por um aluno, sem excesso de formalidade ou aparência de texto gerado por IA."),
    ("metodo_de_estudo", "PDF/aula -> entender a matéria -> atividade -> responder com raciocínio -> aplicação prática -> testar -> Git -> registrar no Notion."),
    ("prioridade_academica", "Seguir primeiro a linha de ensino e os requisitos do professor para passar nas matérias; depois aplicar os conhecimentos em projetos, ONG e Job Hunter."),
    ("organizacao_dos_estudos", "Usa o Notion para registrar aprendizados, atividades, projetos e progresso."),
    ("ritmo_academico", "Costuma realizar aproximadamente uma atividade prática da faculdade por semana."),
    ("objetivo_principal", "Construir carreira na área de tecnologia, especialmente Inteligência Artificial, Machine Learning e futuramente Engenharia de IA."),
    ("meta_financeira", "Busca conquistar independência financeira e ter renda própria, com objetivo mínimo aproximado de R$800 e uma faixa confortável em torno de R$1.000 ou mais."),
    ("preferencia_profissional", "Tem interesse em trabalhar de forma independente e evitar CLT quando houver alternativas viáveis."),
    ("projeto_ativo_gotoh", "Gotoh é seu projeto pessoal de agente de IA/assistente pessoal geral desenvolvido em Python."),
    ("objetivo_gotoh", "Construir um agente pessoal capaz de armazenar e recuperar informações, ajudar nos estudos, organização, tarefas, projetos, pesquisas na web e futuramente aprender e responder sobre diferentes áreas."),
    ("prioridade_gotoh", "Programação e Ciência da Computação são prioridades atuais do Gotoh por causa da faculdade, mas a arquitetura deve permanecer geral e modular para outras áreas da vida."),
    ("arquitetura_gotoh", "Prefere o Gotoh dividido em módulos e arquivos independentes, evitando concentrar toda a lógica em um único arquivo."),
    ("interface_gotoh", "Prefere uma interface desktop visual, organizada e modular, com tema escuro e tons de roxo, podendo utilizar azul, vermelho e cinza como complementos."),
    ("conhecimento_gotoh", "Mantém uma pasta de conhecimento no projeto Gotoh para registrar conteúdos de programação, método de estudo e informações úteis ao agente."),
    ("projeto_job_hunter", "Job Hunter é um projeto pessoal de sistema para busca/análise de vagas, desenvolvido com Python, Flask e SQLite."),
    ("projeto_ong", "Projeto ONG Esperança é um projeto acadêmico de desenvolvimento web, com HTML, CSS e JavaScript, incluindo formulário, validações, armazenamento local e práticas de acessibilidade."),
    ("git", "Usa Git e GitHub nos projetos e valoriza manter os projetos versionados e sincronizados."),
    ("preferencia_git", "Quando está programando, prefere comandos diretos de terminal para verificar status, diff, commits, branches e sincronização."),
    ("preferencia_edicao_codigo", "Prefere comandos completos e diretos para editar arquivos, mas evita alterações gigantescas de uma vez quando o terminal pode dificultar a visualização."),
    ("portfolio", "Quer construir um portfólio real com projetos próprios e acadêmicos, sem inventar experiências profissionais."),
    ("linkedin", "Pretende se posicionar como estudante de Ciência da Computação e aspirante a AI Engineer, com foco em IA e Machine Learning."),
    ("projeto_nexo", "NEXO é uma ideia/projeto relacionado a diagnóstico de pequenos e médios negócios antes da aplicação de IA ou automação."),
    ("criacao_conteudo", "Tem interesse em criar conteúdo para redes sociais e possui projetos relacionados a YouTube, Instagram e TikTok."),
    ("tatuagem", "Possui experiência com tatuagem blackwork e já trabalhou com isso, mantendo interesse na atividade como possível fonte de renda."),
    ("contexto_computador", "Utiliza Linux Mint 22.3 Xfce como sistema principal."),
    ("preferencia_linux", "Gosta de resolver problemas técnicos do computador diretamente pelo terminal quando possível."),
    ("rotina_de_aprendizado", "Aprende melhor alternando teoria, prática, testes e construção de projetos reais."),
    ("habito_de_validacao", "Antes de considerar uma tarefa concluída, gosta de testar o funcionamento, verificar Git/diff/status e só então registrar ou entregar."),
    ("principio_para_projetos", "Não deve modificar um projeto funcional apenas para imitar uma técnica diferente ensinada em aula; deve priorizar os requisitos reais da atividade."),
    ("objetivo_longo_prazo", "Tornar-se profissional de tecnologia com forte domínio de programação, Inteligência Artificial e Machine Learning, construindo independência financeira através das próprias habilidades e projetos."),
]

def injetar():
    db = GotohMemory()
    
    # Identifica o método correto de inserção na sua classe GotohMemory
    metodo = None
    for nome in ["adicionar_fato", "salvar_fato", "adicionar", "salvar", "inserir_fato"]:
        if hasattr(db, nome):
            metodo = getattr(db, nome)
            print(f"-> Usando o método '{nome}' de GotohMemory")
            break
            
    if not metodo:
        print("[!] Erro: Nenhum método de inserção conhecido foi encontrado em GotohMemory.")
        sys.exit(1)
        
    contador = 0
    for chave, valor in fatos:
        try:
            # Tenta passar como tupla ou argumento duplo (chave, valor) ou texto formatado
            try:
                metodo(chave, valor)
            except TypeError:
                metodo(f"{chave}: {valor}")
            contador += 1
        except Exception as e:
            print(f"[!] Falha ao inserir '{chave}': {e}")

    print(f"✓ Sucesso! {contador} fatos sobre o Rodrigo foram registrados no SQLite do Gotoh.")

if __name__ == "__main__":
    injetar()
