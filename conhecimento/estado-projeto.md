# GOTOH — ESTADO DO PROJETO

Última atualização: 05/10/2026

---

# 1. VISÃO GERAL

Gotoh é um agente pessoal desenvolvido localmente em Python.

A ideia principal é criar um assistente pessoal que consiga entender o contexto do usuário, armazenar informações úteis, consultar conhecimentos, ajudar em estudos, organizar tarefas, trabalhar com projetos e futuramente realizar ações mais avançadas.

O Gotoh NÃO deve ser limitado a programação.

Programação e Ciência da Computação são atualmente uma área prioritária porque fazem parte dos estudos do usuário, mas a arquitetura deve permanecer geral e modular para permitir expansão para:

- organização pessoal;
- estudos de outras áreas;
- tarefas;
- projetos;
- pesquisa na web;
- documentos;
- anotações;
- acompanhamento de progresso;
- conhecimento pessoal;
- automações;
- futuras integrações.

A visão de longo prazo é transformar o Gotoh em um verdadeiro agente pessoal.

---

# 2. OBJETIVO PRINCIPAL

Criar um agente que consiga:

1. receber informações do usuário;
2. entender o contexto;
3. guardar informações importantes;
4. recuperar informações quando necessário;
5. ajudar o usuário a estudar;
6. trabalhar com documentos;
7. organizar tarefas;
8. trabalhar com projetos;
9. pesquisar informações na web;
10. manter uma base de conhecimento;
11. acompanhar progresso;
12. futuramente executar ações de forma mais autônoma.

O usuário não deve precisar administrar manualmente cada informação armazenada.

A ideia é que o Gotoh faça cada vez mais desse trabalho automaticamente.

---

# 3. PRINCÍPIOS DO PROJETO

## 3.1 Modularidade

O projeto deve ser dividido em módulos pequenos e responsáveis por funções específicas.

Evitar arquivos gigantes contendo toda a lógica do sistema.

Exemplo:

- interface separada da lógica;
- tema separado da interface;
- leitura de documentos separada do estudo;
- agente separado da interface;
- conhecimento separado da memória;
- funcionalidades futuras devem preferencialmente possuir seus próprios módulos.

---

## 3.2 Separação entre interface e lógica

A interface deve apenas apresentar informações e receber ações do usuário.

A lógica deve permanecer em módulos do sistema.

Isso facilita:

- manutenção;
- testes;
- mudança visual;
- criação de novas interfaces;
- futura migração para outra tecnologia.

---

## 3.3 Gotoh deve ser geral

Não transformar o núcleo do Gotoh em um sistema exclusivamente de programação.

Programação é uma área prioritária atual, não uma limitação estrutural.

A arquitetura deve permitir posteriormente:

- programação;
- faculdade;
- outros estudos;
- organização pessoal;
- projetos;
- tarefas;
- pesquisa;
- documentos;
- conhecimento pessoal;
- outras áreas ainda não definidas.

---

# 4. METODOLOGIA DE ESTUDO

A metodologia definida para o Gotoh acompanha o método de estudo utilizado pelo usuário.

Fluxo principal:

PDF / aula
↓
entender a matéria
↓
atividade
↓
explicar o raciocínio
↓
aplicação prática
↓
testar
↓
Git
↓
registrar no Notion

O Gotoh deve ajudar nesse processo sem substituir completamente o entendimento do usuário.

A prioridade é:

1. entender o conteúdo;
2. realizar a atividade;
3. compreender o raciocínio;
4. aplicar;
5. testar;
6. versionar;
7. registrar o aprendizado.

---

# 5. ESTRUTURA ATUAL DO PROJETO

Localização:

/home/karpano/Gotoh

Estrutura principal:

Gotoh/
├── iniciar.py
├── interface/
├── sistema/
├── conhecimento/
├── dados/
└── projetos/

---

# 6. INTERFACE

A interface atual é feita em Python/Tkinter.

O título da aplicação é:

Gotoh — Agente Pessoal

A interface utiliza arquivos separados para manter a organização visual.

Estrutura conceitual:

interface/
├── app.py
├── tema.py
├── componentes.py
└── telas/

As telas incluem áreas como:

- início;
- estudos;
- conhecimento;
- tarefas;
- projetos;
- notas;
- progresso;
- configurações;
- conversa.

---

# 7. TEMA VISUAL

A interface segue uma proposta de modo escuro.

Características desejadas:

- fundo escuro;
- tons de roxo;
- roxos mais saturados;
- possibilidade de complementos em azul;
- possibilidade de complementos em vermelho;
- tons de cinza para elementos secundários.

As cores devem permanecer centralizadas no módulo de tema sempre que possível.

Arquivo principal:

interface/tema.py

Isso evita espalhar valores visuais por vários arquivos.

---

# 8. TELA DE CONVERSA

Arquivo:

interface/telas/conversa.py

A tela de conversa é responsável pela interação principal com o agente.

Ela apresenta:

- mensagens do Gotoh;
- mensagens do usuário;
- área de entrada;
- componentes visuais da conversa.

A interface utiliza constantes do tema para separar visualmente:

- fundo da conversa;
- fundo do campo de entrada;
- texto do Gotoh;
- texto do usuário;
- tons de roxo;
- elementos secundários.

---

# 9. SISTEMA DO AGENTE

Arquivo principal:

sistema/agente.py

O agente é responsável por interpretar comandos e direcionar ações para diferentes funcionalidades.

Entre as funções já trabalhadas estão comandos relacionados a:

- memória;
- tarefas;
- notas;
- conhecimento;
- documentos;
- estudos;
- pesquisa.

O agente deve continuar sendo o ponto de coordenação das funcionalidades, mas não deve concentrar toda a implementação dentro de um único arquivo.

Quando uma funcionalidade crescer, ela deve ser separada em seu próprio módulo.

---

# 10. MEMÓRIA

O Gotoh possui uma ideia de memória persistente.

Arquivo utilizado:

dados/memoria.json

Esse arquivo NÃO deve ser versionado no Git.

O motivo é que ele pode conter informações pessoais ou dados específicos da utilização do Gotoh.

Por isso ele está no .gitignore.

---

# 11. CONHECIMENTO

O diretório:

conhecimento/

é destinado a informações que fazem parte da base de conhecimento do Gotoh.

Exemplos de conhecimento já planejado/trabalhado:

- método de estudo;
- perfil do estudante;
- fundamentos de programação;
- informações sobre o próprio funcionamento do Gotoh.

Uma área já criada:

conhecimento/programacao/fundamentos.md

Esse material contém fundamentos como:

- variáveis;
- algoritmos;
- funções.

O diretório de conhecimento deve continuar separado da memória pessoal.

---

# 12. DIFERENÇA ENTRE MEMÓRIA E CONHECIMENTO

MEMÓRIA:

Informações sobre o usuário, contexto, preferências, fatos registrados durante o uso e outras informações que precisam ser lembradas.

Exemplo:

dados/memoria.json

CONHECIMENTO:

Conteúdo estruturado que o Gotoh utiliza para estudar, consultar ou compreender determinados assuntos.

Exemplo:

conhecimento/programacao/fundamentos.md

Essa separação deve ser preservada.

---

# 13. LEITURA DE PDF

O Gotoh agora possui suporte inicial para leitura de PDFs.

Arquivo:

sistema/documentos.py

Biblioteca utilizada:

PyMuPDF

Importação atual:

import pymupdf as fitz

Extensão suportada atualmente:

.pdf

---

# 14. FUNCIONAMENTO DA LEITURA DE PDF

O módulo de documentos verifica:

1. se o arquivo existe;
2. se é um PDF;
3. abre o documento;
4. percorre as páginas;
5. extrai o texto;
6. organiza o conteúdo por página;
7. informa estatísticas;
8. retorna erros de forma controlada.

A estrutura retornada inclui informações como:

- sucesso;
- erro;
- texto;
- quantidade de páginas;
- quantidade de páginas com texto;
- nome do arquivo.

A leitura é feita página por página.

O texto é organizado utilizando marcadores como:

--- Página 1 ---

--- Página 2 ---

etc.

---

# 15. ESTUDO A PARTIR DO MATERIAL

Arquivo:

sistema/estudo.py

Esse módulo existe para separar a lógica de estudo da lógica de leitura do arquivo.

Funções principais:

limpar_texto()

Responsável por remover linhas vazias e espaços desnecessários.

buscar_no_material()

Procura um termo dentro do conteúdo e retorna trechos próximos à ocorrência.

analisar_material()

Gera informações básicas sobre o material:

- quantidade de caracteres;
- quantidade de linhas;
- quantidade de palavras;
- texto tratado.

preparar_estudo()

Prepara o material para ser utilizado como conteúdo de estudo.

Pode receber um assunto específico e localizar ocorrências desse assunto no material.

---

# 16. FLUXO ATUAL DE DOCUMENTOS

O conceito atual é:

PDF
↓
sistema/documentos.py
↓
extração do texto
↓
sistema/estudo.py
↓
limpeza e análise
↓
busca por assunto
↓
sistema/agente.py
↓
Gotoh utiliza o conteúdo

Esse modelo deve continuar modular.

No futuro, o fluxo poderá evoluir para:

PDF
↓
extração
↓
análise
↓
identificação de assunto
↓
resumo
↓
explicação
↓
perguntas
↓
atividade prática
↓
teste
↓
registro do aprendizado

---

# 17. LIMITAÇÕES ATUAIS DA LEITURA DE PDF

A implementação atual trabalha principalmente com PDFs que possuem texto selecionável.

PDFs formados apenas por imagens podem não produzir texto através da extração convencional.

OCR poderá ser adicionado futuramente caso seja necessário.

Também será possível futuramente adicionar suporte para outros formatos, por exemplo:

- TXT;
- DOCX;
- Markdown;
- eventualmente outros formatos.

Por enquanto, PDF é a extensão suportada.

---

# 18. PESQUISA NA WEB

O Gotoh possui um módulo de pesquisa na web.

Foi realizado teste utilizando resultados do DuckDuckGo.

A pesquisa web deve futuramente ser integrada ao agente de maneira mais inteligente.

Possibilidades:

- pesquisar assuntos;
- comparar informações;
- encontrar documentação;
- buscar notícias;
- encontrar materiais de estudo;
- pesquisar soluções;
- consultar fontes externas.

A pesquisa web não deve substituir a base de conhecimento local.

Ela deve funcionar como fonte externa complementar.

---

# 19. TAREFAS

O Gotoh já possui lógica para criação/interação com tarefas.

A ideia é permitir comandos naturais para criar e organizar tarefas.

Exemplos conceituais:

- criar tarefa;
- listar tarefas;
- concluir tarefa;
- consultar tarefas.

Futuramente:

- prioridades;
- prazos;
- categorias;
- recorrência;
- integração com projetos;
- lembretes;
- automações.

---

# 20. NOTAS

O Gotoh possui suporte inicial para notas.

A ideia é permitir que o usuário registre informações sem precisar manipular arquivos manualmente.

Futuramente as notas poderão ser relacionadas a:

- estudos;
- projetos;
- tarefas;
- conhecimento;
- reuniões;
- ideias;
- planejamento.

---

# 21. PROJETOS

Existe uma área de projetos planejada para o Gotoh.

O objetivo é permitir que o agente acompanhe projetos do usuário.

Exemplos:

- projetos acadêmicos;
- projetos de programação;
- projetos pessoais;
- projetos profissionais.

No futuro o Gotoh poderá compreender:

- objetivo do projeto;
- arquivos;
- tarefas;
- progresso;
- próximos passos;
- histórico;
- documentação.

---

# 22. PROGRESSO

Existe uma área de progresso na interface.

A ideia futura é permitir acompanhamento de:

- estudos;
- tarefas;
- projetos;
- atividades;
- evolução de conhecimentos.

Essa área ainda pode evoluir bastante.

---

# 23. CONFIGURAÇÕES

Existe uma tela de configurações.

Ela deverá concentrar futuramente opções como:

- aparência;
- comportamento do agente;
- fontes de pesquisa;
- armazenamento;
- preferências;
- configurações de IA;
- integrações.

---

# 24. DEPENDÊNCIAS

O projeto utiliza Python.

Existe um ambiente virtual local:

.venv/

A `.venv/` NÃO deve ser versionada.

O arquivo `.gitignore` deve continuar contendo:

.venv/

Também não devem ser versionados:

dados/memoria.json
__pycache__/
*.pyc

e arquivos temporários/material local conforme as regras existentes.

---

# 25. EXECUÇÃO

O projeto possui um arquivo de entrada:

iniciar.py

A execução deve ser feita a partir da raiz:

cd /home/karpano/Gotoh

Ativar o ambiente virtual quando necessário.

Exemplo:

source .venv/bin/activate

Depois:

python iniciar.py

---

# 26. AMBIENTE ATUAL

Sistema utilizado durante o desenvolvimento:

Linux Mint 22.3 Xfce

Python utilizado no ambiente de desenvolvimento:

Python 3.x

Interface:

Tkinter

Biblioteca de PDF:

PyMuPDF

---

# 27. CONTROLE DE VERSÃO

O Gotoh possui Git LOCAL.

Repositório:

/home/karpano/Gotoh

Branch atual:

main

O projeto NÃO está atualmente publicado no GitHub.

Não existe remote origin configurado.

Portanto:

LOCAL
↓
Git local

Atualmente NÃO existe:

GitHub remoto

---

# 28. ÚLTIMO COMMIT

Último commit conhecido:

7aefad6 — adiciona leitura e estudo de PDFs no Gotoh

Commit anterior:

03b2018 — estrutura inicial do Gotoh

O commit 7aefad6 contém as alterações relacionadas à implementação da leitura e estudo de PDFs e ajustes associados.

---

# 29. DECISÃO SOBRE GITHUB

Por enquanto o Gotoh será mantido como projeto local.

Não é necessário publicar o projeto no GitHub neste momento.

Motivos:

- projeto ainda está em desenvolvimento;
- contém componentes pessoais;
- memória pode conter informações pessoais;
- a prioridade atual é desenvolver a arquitetura;
- o controle de versão local já atende à necessidade atual.

Caso no futuro seja necessário publicar, deve-se avaliar antes:

- dados pessoais;
- memória;
- arquivos locais;
- credenciais;
- configurações;
- chaves de API;
- arquivos temporários;
- banco de dados;
- materiais privados.

---

# 30. ARQUITETURA DESEJADA

A arquitetura geral deve evoluir aproximadamente para:

INTERFACE
↓
AGENTE
↓
ORQUESTRADOR
↓
MÓDULOS
├── memória
├── conhecimento
├── documentos
├── estudo
├── tarefas
├── notas
├── projetos
├── pesquisa web
├── progresso
└── futuras integrações

A interface não deve precisar conhecer os detalhes internos de cada módulo.

---

# 31. FUTURA CAMADA DE IA

O Gotoh deverá futuramente utilizar uma camada de IA mais avançada.

Essa camada poderá ser responsável por:

- compreender linguagem natural;
- resumir documentos;
- explicar conteúdos;
- gerar planos de estudo;
- responder perguntas;
- interpretar tarefas;
- decidir qual módulo utilizar;
- combinar memória + conhecimento + pesquisa;
- executar ações.

O agente deve ser construído de forma que a IA possa ser trocada futuramente sem precisar reconstruir toda a interface.

---

# 32. AGENTE PESSOAL

A visão final do Gotoh é mais ampla que um chatbot.

O objetivo é que ele funcione como um agente pessoal.

Exemplo conceitual:

Usuário:
"Tenho uma prova de algoritmos sexta-feira."

Gotoh poderá futuramente:

1. entender a data;
2. consultar tarefas;
3. consultar conhecimentos;
4. verificar materiais disponíveis;
5. montar plano;
6. criar tarefas;
7. acompanhar execução;
8. responder dúvidas;
9. registrar o progresso.

---

# 33. ESTUDOS FUTUROS

A área de estudos deve evoluir para permitir:

- importar material;
- identificar assuntos;
- gerar resumo;
- explicar conteúdo;
- fazer perguntas;
- criar exercícios;
- avaliar respostas;
- sugerir aplicação prática;
- acompanhar desempenho;
- registrar aprendizado.

O objetivo não é apenas "ler PDF".

O objetivo é transformar material em um processo de aprendizagem.

---

# 34. RELAÇÃO COM A FACULDADE

O Gotoh deve ajudar nos estudos da faculdade sem alterar desnecessariamente o método exigido pelos professores.

Prioridade:

1. seguir a linha de ensino da disciplina;
2. realizar a atividade;
3. passar na matéria;
4. compreender o conteúdo;
5. aplicar posteriormente em projetos.

A ferramenta deve complementar o estudo, não criar uma metodologia incompatível com as exigências da disciplina.

---

# 35. ÁREAS DE CONHECIMENTO FUTURAS

O sistema de conhecimento poderá crescer para:

conhecimento/
├── programacao/
├── ciencia-computacao/
├── faculdade/
├── projetos/
├── estudos/
└── outras-areas/

A estrutura deve permanecer flexível.

Não assumir que tudo será programação.

---

# 36. SEGURANÇA E PRIVACIDADE

Como o projeto é pessoal e local:

- memória pessoal não deve ser publicada;
- credenciais não devem ser armazenadas no código;
- chaves de API não devem ser commitadas;
- arquivos temporários não devem ser versionados;
- dados pessoais devem permanecer fora do controle de versão público.

Se integrações externas forem adicionadas, utilizar variáveis de ambiente ou outro mecanismo seguro.

---

# 37. ESTADO ATUAL

FUNCIONALIDADES JÁ TRABALHADAS:

[X] Interface Tkinter
[X] Tema escuro
[X] Navegação entre telas
[X] Sistema de conversa
[X] Agente inicial
[X] Memória
[X] Tarefas
[X] Notas
[X] Conhecimento
[X] Pesquisa web
[X] Leitura de PDF
[X] Extração de texto de PDF
[X] Análise básica de material
[X] Busca de termos dentro do material
[X] Preparação de material para estudo
[X] Estrutura modular inicial
[X] Git local

---

# 38. FUNCIONALIDADES A EVOLUIR

[ ] Melhorar entendimento de linguagem natural
[ ] Integrar IA mais avançada
[ ] Melhorar memória
[ ] Busca semântica no conhecimento
[ ] Sistema de estudo mais completo
[ ] Resumo automático de PDFs
[ ] Perguntas automáticas sobre PDFs
[ ] Geração de exercícios
[ ] Avaliação de respostas
[ ] OCR para PDFs escaneados
[ ] Suporte a outros formatos de documentos
[ ] Melhor sistema de tarefas
[ ] Projetos mais completos
[ ] Sistema de progresso
[ ] Automações
[ ] Integrações externas
[ ] Execução de ações pelo agente
[ ] Empacotamento como aplicativo desktop
[ ] Melhor tratamento de erros
[ ] Testes automatizados

---

# 39. PRÓXIMA PRIORIDADE

A próxima prioridade deve ser consolidar a arquitetura antes de adicionar funcionalidades demais.

Ordem recomendada:

1. estabilizar a leitura de documentos;
2. estabilizar o sistema de estudos;
3. melhorar a comunicação entre agente e módulos;
4. organizar memória e conhecimento;
5. melhorar tarefas;
6. melhorar projetos;
7. adicionar IA mais avançada;
8. adicionar automações;
9. transformar o Gotoh em um agente mais autônomo.

---

# 40. REGRA PARA NOVAS FUNCIONALIDADES

Antes de criar uma funcionalidade nova, perguntar:

1. Essa função pertence ao agente?
2. É uma função independente?
3. Deve virar um módulo separado?
4. Precisa armazenar dados?
5. Precisa de conhecimento?
6. Precisa de memória?
7. Precisa da web?
8. Deve funcionar sem internet?
9. Precisa de interface própria?
10. Como poderá ser expandida futuramente?

Evitar colocar tudo dentro de sistema/agente.py.

---

# 41. REGRA PARA ALTERAÇÕES NO PROJETO

Evitar grandes reescritas desnecessárias.

Preferir:

- mudanças pequenas;
- módulos separados;
- testes após cada etapa;
- Git antes de grandes alterações;
- confirmação do funcionamento antes de continuar.

Quando uma alteração envolver vários arquivos, verificar:

git diff --check

e:

git status

antes do commit.

---

# 42. FLUXO DE DESENVOLVIMENTO

Fluxo recomendado:

1. definir o objetivo;
2. identificar o módulo responsável;
3. alterar o menor número de arquivos possível;
4. testar;
5. verificar erros;
6. verificar Git;
7. fazer commit;
8. continuar.

Comandos básicos:

cd /home/karpano/Gotoh

git status

git diff --check

git diff

git add <arquivos>

git commit -m "descrição da alteração"

---

# 43. FLUXO DE ESTUDO DO GOTHO

Quando o usuário fornecer um PDF ou aula:

1. receber o material;
2. identificar o assunto;
3. extrair o texto;
4. limpar o material;
5. analisar o conteúdo;
6. localizar conceitos importantes;
7. explicar o conteúdo;
8. realizar a atividade;
9. explicar o raciocínio;
10. aplicar em projeto;
11. testar;
12. versionar quando aplicável;
13. registrar o aprendizado.

---

# 44. PRINCÍPIO CENTRAL

O Gotoh não deve ser apenas uma interface bonita.

Também não deve ser apenas um chatbot.

O objetivo é construir progressivamente:

CONHECIMENTO
+
MEMÓRIA
+
CONTEXTO
+
FERRAMENTAS
+
IA
+
AÇÕES

formando um agente pessoal capaz de ajudar o usuário de maneira cada vez mais autônoma.

---

# 45. VISÃO DE LONGO PRAZO

A visão final é:

Gotoh
│
├── Conversa
├── Memória
├── Conhecimento
├── Estudos
├── Documentos
├── Tarefas
├── Notas
├── Projetos
├── Pesquisa
├── Progresso
├── Automações
└── Agente

Tudo integrado por um núcleo capaz de compreender o contexto e decidir qual recurso utilizar.

O sistema deve crescer gradualmente.

Não tentar construir tudo de uma vez.

A prioridade é criar uma base sólida, modular e expansível.

---

# 46. ESTADO DO PROJETO NO MOMENTO DESTE DOCUMENTO

Projeto:

Gotoh — Agente Pessoal

Local:

/home/karpano/Gotoh

Controle de versão:

Git local

Branch:

main

GitHub:

não configurado

Último commit:

7aefad6 — adiciona leitura e estudo de PDFs no Gotoh

Principal evolução recente:

implementação de leitura de PDF e preparação de materiais para estudo.

Estado esperado:

projeto local funcional e versionado.

---

# 47. NOTA PARA FUTURAS SESSÕES

Este arquivo deve ser tratado como uma referência do estado arquitetural do Gotoh.

Quando o projeto sofrer mudanças importantes, atualizar este documento.

Não é necessário registrar cada pequena alteração.

Registrar principalmente:

- novas funcionalidades;
- mudanças de arquitetura;
- decisões importantes;
- novos módulos;
- mudanças de dependências;
- mudanças no fluxo de estudo;
- mudanças na memória;
- mudanças na estrutura de dados;
- mudanças importantes na interface;
- próximos objetivos.

O objetivo é evitar perder o contexto do projeto ao longo do desenvolvimento.

