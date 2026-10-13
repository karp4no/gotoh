# GOTOH — CONTEXTO PARA CONTINUIDADE

Última geração: 05/10/2026 15:40:07

## O que é

Gotoh é um agente pessoal desenvolvido localmente em Python.

Seu objetivo é ajudar o usuário em estudos, programação, organização, projetos, documentos, tarefas, conhecimento, pesquisa e futuramente ações mais autônomas.

Programação e Ciência da Computação são prioridades atuais por causa dos estudos do usuário, mas o Gotoh NÃO deve ser limitado a programação.

## Princípios

- Arquitetura modular.
- Separação entre interface e lógica.
- Evitar arquivos gigantes.
- Criar módulos específicos para funcionalidades independentes.
- Manter memória separada de conhecimento.
- Desenvolver gradualmente.
- Não quebrar funcionalidades existentes sem necessidade.

## Método de estudo

PDF/aula → entender → atividade → raciocínio → aplicação prática → teste → Git → Notion.

## Estrutura principal

```text
Gotoh/
├── iniciar.py
├── interface/
├── sistema/
├── conhecimento/
├── dados/
└── projetos/
```

## Interface

A interface utiliza Python/Tkinter.

Arquivos principais:

- interface/app.py
- interface/tema.py
- interface/componentes.py
- interface/telas/

A interface possui telas para conversa, estudos, conhecimento, tarefas, projetos, notas, progresso e configurações.

## Sistema

O diretório `sistema/` contém a lógica principal do agente.

Módulos importantes atualmente:

- sistema/agente.py
- sistema/documentos.py
- sistema/estudo.py

## Leitura de PDF

O Gotoh possui suporte inicial para leitura de PDFs utilizando PyMuPDF.

`sistema/documentos.py` realiza a extração do texto página por página.

`sistema/estudo.py` trata o material, permitindo limpeza, análise e busca de termos.

## Memória

A memória persistente fica em:

`dados/memoria.json`

Esse arquivo é propositalmente excluído deste pacote de contexto porque pode conter informações pessoais.

## Conhecimento

O diretório `conhecimento/` contém informações estruturadas utilizadas pelo Gotoh.

Existe documentação sobre programação e sobre o próprio estado do projeto.

## Web

O Gotoh possui módulo de pesquisa web, utilizado para consultas externas.

## Git

O projeto utiliza Git localmente.

O repositório não está atualmente conectado a um GitHub remoto.

## Como executar

```bash
cd /home/karpano/Gotoh
source .venv/bin/activate
python iniciar.py
```

## Arquivos incluídos neste snapshot

- `README.md`
- `conhecimento/estado-projeto.md`
- `conhecimento/indice.md`
- `conhecimento/metodo-estudo.md`
- `conhecimento/perfil-estudante.md`
- `conhecimento/programacao/fundamentos.md`
- `iniciar.py`
- `interface/__init__.py`
- `interface/app.py`
- `interface/app_backup.py`
- `interface/app_dashboard.py`
- `interface/app_memoria.py`
- `interface/componentes.py`
- `interface/telas/__init__.py`
- `interface/telas/configuracoes.py`
- `interface/telas/conhecimento.py`
- `interface/telas/conversa.py`
- `interface/telas/estudos.py`
- `interface/telas/inicio.py`
- `interface/telas/notas.py`
- `interface/telas/progresso.py`
- `interface/telas/projetos.py`
- `interface/telas/tarefas.py`
- `interface/tema.py`
- `sistema/agente.py`
- `sistema/config.json`
- `sistema/conhecimento.py`
- `sistema/documentos.py`
- `sistema/estudo.py`
- `sistema/gotoh.py`
- `sistema/memoria.py`
- `sistema/roteador.py`
- `sistema/web.py`

## Como usar este arquivo em outra IA

Primeiro forneça este arquivo para a IA e explique que ele contém o contexto arquitetural do projeto.

Depois forneça `codigo-atual.txt`, que contém os arquivos de código e documentação incluídos no snapshot.

Prompt recomendado:

> Este é o projeto Gotoh. Leia primeiro o CONTEXTO.md para entender a arquitetura e as decisões do projeto. Depois leia o codigo-atual.txt para conhecer o código atual. Não faça alterações ainda. Primeiro analise a estrutura e me diga quais arquivos estão relacionados ao problema que vou apresentar.

## Regra importante

Este arquivo é um snapshot e não substitui os arquivos reais do projeto.
Depois de alterações importantes, execute novamente:

```bash
python gerar-contexto.py
```

Isso atualizará o contexto e o código exportado.
