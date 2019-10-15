# Guia de contribuição

## Como posso contribuir?

Para contribuir com nosso projeto, antes você precisa realizar o Fork do nosso repositório, e após isso você precisa seguir os seguintes tópicos deste guia :

* [1. Código de Conduta](#1-regras-e-código-de-conduta) <br>
* [2. Política de Issues](#2-política-de-issues) <br>
* [3. Política de Branches(GitFlow)](#3-política-de-branches) <br>
* [4. Política de commits](#4-política-de-commits) <br>
* [5. Modelo para Pull Requests](#5-política-de-merges-e-pull-requests) <br>

### 1. Regras e código de conduta.

É de extrema importância que antes de fazer qualquer alteração em nosso projeto, que seja lido o nosso [Código de conduta](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/CODE_OF_CONDUCT.md), para que esteja claro as regras e boas condutas que esperamos para que exista uma contribuição saudável e respeitosa.

### 2. Política de Issues

Um ótimo começo para que se inicie a sua contribuição, seja a abertura de uma Issue.

Uma Issue pode ser utilizada de várias formas, desde relatar um Bug até sugerir uma evolução ou funcionalidade ao projeto.

As *Issues* devem possuir título, descrição, no mínimo um assinante responsável, *labels*, *milestone*(a sprint que a issue se encontra) e *estimated*(pontuação) para as issues pontuadas.

Para que a Issue esteja correta, ela precisa seguir os modelos de Issues Templates que se encontram em nosso repositório :

* [Bug Report Template](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/ISSUE_TEMPLATE/bug_report.md)
* [Funcionalidade Template](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/ISSUE_TEMPLATE/funcionalidade.md)
* [General Issue Template](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/ISSUE_TEMPLATE/general-issue.md)

### 3. Política de branches

Para gerir nossa política de branches, utilizamos a ferramenta do [GitFlow](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/pol%C3%ADtica_branches_commits/Git-flow.md).

Para compreender nossa [Política de branches](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/pol%C3%ADtica_branches_commits/Git-flow.md) e a ferramenta do [GitFlow](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/pol%C3%ADtica_branches_commits/Git-flow.md) basta acessar a palavra “GitFlow” ou “Política de Branches” destacadas neste tópico.

### 4. Política de Commits

Os commits devem ser feitos usando o parâmetro `-s` para indicar sua assinatura no commit.

```
git commit -s
```
A issue vinculada a este commit (caso exista), deve ser citada no commit, para isso, basta adicionar `#<numero_da_issue>`.

```
 #5 Fazendo guia de contribuição
```

** \*\*Por padrão, o caracter `#` define uma linha de comentário no arquivo da mensagem do commit. Para resolver este problema, use o commando:**
```
git config --local core.commentChar '!'
```

Igualmente, para commits em dupla deve ser usado o comando `-s` , e deve ser adicionado a assinatura da sua dupla.

```
git commit -s
```
Comentário do commit:
```
#5 Fazendo guia de contribuição

Signed-off-by: eliseukadesh67 <eliseu.kadesh1967@gmail.com>
```

Para que ambos envolvidos no commit sejam incluídos como contribuintes no gráfico de commits do GitHub, basta incluir a instrução `Co-authored-by:` na mensagem:

```
#5 Fazendo guia de contribuição

Signed-off-by: eliseukadesh67 <eliseu.kadesh1967@gmail.com>
Signed-off-by: gabriel-paiva <gabrielpaivaaguiar.gp@gmail.com>

Co-authored-by: eliseukadesh67 <eliseu.kadesh1967@gmail.com>
Co-authored-by: gabriel-paiva <gabrielpaivaaguiar.gp@gmail.com>

```
Para commits que incluem uma pequena mudança em uma issue que já teve sua resolução encerrada, deve-se iniciar a mensagem do commit com `HOTFIX #<numero_da_issue> <mensagem>`

Exemplo de comentário do commit:
```
HOTFIX #5 Atualizando guia de contribuição do projeto
```

### 5. Política de Merges e Pull Requests

O Pull Request é uma forma mais técnica de propor uma mudança estrutural no código do projeto.

Primeiramente para que o Pull Request esteja correto, ele precisa seguir o [Pull Request Template](https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/develop/.github/pull_request_template.md) que está presente em nosso repositório.

#### Code Review


Para a revisão e análise do Pull Request, o *Code review* deve ser feito por um ou mais membros da equipe que não participaram das modificações.

## Quem pode contribuir?

Qualquer pessoa que esteja disposta a ajudar pode contribuir com nosso projeto, tanto sugerindo evoluções e funcionalidades, quanto reportando Bugs.

Todos que tenham algo a contribuir com nosso projeto são mais que bem vindos, e serão recebidos com gratidão e respeito.




