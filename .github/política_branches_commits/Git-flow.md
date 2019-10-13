# Políticas de branches

## Gitflow

### O que é o Gitflow?


O Gitflow é uma ferramento de organização e padronização de branches, para facilitar e controlar de maneira organizada e dinâmica o versionamento de um projeto.

Em vez de utilizar apenas a branch **Master** , o Gitflow divide cada etapa e processo de um projeto em branches, sendo as principais: Master, Develop, Features, Release e Hotfix.

## Develop e Master Branch

A branch Develop serve como uma branch de integração entre features novas de um projeto, ja a branch Master guarda apenas versões finais e oficiais de Releases ja previamente testadas, aprovadas e prontas para o Deploy.

* Diagrama GitFlow Develop branch.
--------------------------------------------------------------------------

![Titulo](https://wac-cdn.atlassian.com/dam/jcr:2bef0bef-22bc-4485-94b9-a9422f70f11c/02%20(2).svg?cdnVersion=577)
-------------------------------------------------
* Com este comando tendo o git-flow instalado previamente, inicializamos o padrão de branches, ja criando a branch Develop.

                $ git flow init

                Initialized empty Git repository in ~/project/.git/

                No branches exist yet. Base branches must be created now.

                Branch name for production releases: [master]

                Branch name for "next release" development: [develop]

                How to name your supporting branch prefixes?

                Feature branches? [feature/]

                Release branches? [release/]

                Hotfix branches? [hotfix/]

                Support branches? [support/]

                Version tag prefix? []

                $ git branch

                *develop
                 master


    * Podemos também criar uma branch Develop desta forma

            $ git checkout develop

## Feature branch

Para cada feature nova devemos criar uma branch própria para essa feature. A feature branch utiliza a branch Develop como sua "branch mãe". Quando a feature é completa, ocorre o merge dela dentro da branch develop.**Ps: As features nunca interagem diretamente com a master**.


* Diagrama GitFlow Feature branch.
--------------------------------------------------------------------------


![Titulo](https://wac-cdn.atlassian.com/dam/jcr:b5259cce-6245-49f2-b89b-9871f9ee3fa4/03%20(2).svg?cdnVersion=577)
-------------------------------------------------


### 1. Iniciando uma feature

* Criamos a nossa feature utilizando o git-flow desta forma

            $ git flow feature start nova_feature

* Podemos criar sem o git-flow desta forma

            $ git checkout develop
            $ git checkout -b nova_feature

### 2. Finalizando a feature

Quando finalizado toda a criação e desenvolvimento da feature, podemos então fazer o **merge** da branch na develop.

* Ao finalizar o desenvolvimento, devera ser realizado o [Pull Request](/.github/pull_request_template.md) de acordo com os padrões estabelecidos.

* Após o Pull Request ser aprovado, a branch poderá ser incluida na Develop, através do `merge`.

## Release Branch

Uma vez que temos a quantidade requerida de features, e todas as features foram testadas e revisadas pela develop(ou a data da Release se aproxima), basicamente será criado um **fork** da branch develop para dentro da branch release.

Ao criarmos esta branch, estaremos começando um novo ciclo de release, então nenhuma feature nova poderá ser adicionada neste ponto, apenas bug fixes ou documentações adicionais.

Assim que estiver pronta para o lançamento, será realizado o merge da release com a master, juntamente com uma **tag** de número de versão. Depois será feito o merge de volta a develop, pois muitas mudanças importantes podem acontecer no processo de release, então é crucial que a develop e a release estejam sincronizadas.


* Diagrama Gitflow Release branch
--------------------------------------------------------------------------


![Titulo](https://wac-cdn.atlassian.com/dam/jcr:a9cea7b7-23c3-41a7-a4e0-affa053d9ea7/04%20(1).svg?cdnVersion=577)
-------------------------------------------------


### 1. Inciando a release

* Criamos uma nova release utilizando o git-flow desta forma

            $ git flow release start 0.1.0
            Switched to a new branch 'release/0.1.0'

* Podemos também criar sem o git-flow desta forma

            $ git checkout develop
            $ git checkout -b release/0.1.0

### 2. Finalizando a release

* Finalizamos a release utilizando o git-flow desta forma

            $ git flow release finish '0.1.0'

* O comando acima irá automaticamente realizar o **merge** na branch master, e de volta para a develop.

* Podemos também ao finalizar a release, voltar a branch master e fazer o push, juntamente com as **tags** de release.

            $ git push origin master --follow-tags

## Hotfix

A hotfix branch é utilizada para uma manutenção de ajustes sevéros que ocorrem em meio a produção de uma release, que não podem esperar até a próxima release.

Diferentemente das demais branches que são filhas da develop branch, a hotfix é "filha" da master branch, ou seja na criação da hotfix, é realizado o **fork** diretamente da master branch para a hotfix.

Assim que realizado os demais ajustes, será realizado o merge de volta a master branch, e também com a develop(ou para a release branch atual), e a branch master terá registrado nela uma tag com a versão atualizada.  

--------------------------------------------------------------------------
* Diagrama GitFLow Hotfix branch



![Titulo](https://wac-cdn.atlassian.com/dam/jcr:61ccc620-5249-4338-be66-94d563f2843c/05%20(2).svg?cdnVersion=577)
-------------------------------------------------

### 1. Inicializando uma hotfix

* Criamos uma hotfix utilizando o git-flow com os seguintes comandos

            $ git flow hotfix start hotfix_branch

* Podemos também criar sem o git-flow

            $ git checkout master
            $ git checkout -b hotfix_branch

### 2. Finalizando uma hotfix

* Ao finalizar o desenvolvimento, devera ser realizado o [Pull Request](/.github/pull_request_template.md) de acordo com os padrões estabelecidos.

* Após o Pull Request ser aprovado, a branch poderá ser incluida na Develop, através do `merge`.

## Bugfix

A Bugfix não é uma branch padrão do Gitflow, porém utilizaremos ela com intúito de resolver bugs que ocorrem na fase de teste da produção.

Esta branch será praticamente uma cópia da develop branch, que após os requeridos reparos, será feito o merge de volta a develop branch.

## 1. Iniciando uma bugfix

* Uma bugfix é iniciada de forma simples usando estes comando git-flow:

            $ git flow bugfix start bugfix_branch
            
## 2. Finalizando uma bugfix

* Ao finalizar a correção dos bugs, devera ser realizado o [Pull Request](/.github/pull_request_template.md) de acordo com os padrões estabelecidos.

* Após o Pull Request ser aprovado, a branch poderá ser incluida na Develop, através do `merge`.

### Observações

* Na finalização de cada branch, será realizado o Pull Request, e assim que aprovado, sera utilizado o comando "finish" ou sera realizado o merge e a exclusão da branch (em alguns casos manualmente sem o uso do git-flow).

## Branches de correção ou adição simples

Estas branches serão utilizados com o intuito de adicionar ou corrigir pequenas alterações, sendo elas : erros de digitação, correção ou adição documentação e erros pequenos em geral.

#### Fix branch

Esta branch será utilizada para corrigir pequenos erros e corrigir documentações.

*A branch deverá ser criada a partir da branch Develop, e seguindo os padrões de nome a seguir.


    $ git checkout develop
    $ git checkout -b Fix/<nome do documento ou correção geral>
     

#### Add branch

Esta branch será utilizada para adicionar documentos que faltam, ou novos documentos.

#### 1. Iniciando

*A branch deverá ser criada a partir da branch Develop, e seguindo os padrões de nome a seguir.


        $ git checkout develop
        $ git checkout -b Ad/<nome do documento>

#### 2. Finalizando

* Ao finalizar as correções, devera ser realizado o [Pull Request](/.github/pull_request_template.md) de acordo com os padrões estabelecidos.

* Após o Pull Request ser aprovado, a branch poderá ser incluida na Develop, através do `merge`


#### 1. Iniciando

*A branch deverá ser criada a partir da branch Develop, e seguindo os padrões de nome a seguir.


        $ git checkout develop
        $ git checkout -b Ad/<nome do documento>

#### 2. Finalizando

* Ao finalizar as correções, devera ser realizado o [Pull Request](/.github/pull_request_template.md) de acordo com os padrões estabelecidos.

* Após o Pull Request ser aprovado, a branch poderá ser incluida na Develop, através do `merge`.

## Referências

- <https://medium.com/empathyco/git-flow-applied-to-a-real-project-c08037e28f88>
- <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>

