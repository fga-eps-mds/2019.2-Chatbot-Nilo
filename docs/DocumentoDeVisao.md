# Documento de Visão

## Sumário:
 [1. Introdução](#1-introdução) <br>
&emsp; [1.1 Proposito](#11-propósito) <br>
&emsp; [1.2 Escopo](#12-escopo) <br>
&emsp; [1.3 Definições, Acrônimos e Abreviações](#13-definições-acrônimos-e-abreviações) <br>
&emsp; [1.4 Referências](#14-referências) <br>
&emsp; [1.5 Visão Geral](#15-visão-geral) <br>
[2. Posicionamento](#20-posicionamento) <br>
&emsp; [2.1. Oportunidade de Negócios](#21-oportunidade-de-negócios) <br>
&emsp; [2.2. Instrução do Problema](#22-instrução-do-problema) <br>
&emsp; [2.3. Instrução de Posicionamento](#23-instrução-de-posicionamento) <br>
[3. Descrições da Parte Interessada e do Usuário](#3-descrição-da-parte-interessadas-e-do-usuário) <br>
&emsp; [3.1 Resumo da parte interessada](#31-resumo-da-parte-interessada) <br>
&emsp; [3.2 Resumo do usuário](#32-resumo-do-usuário) <br>
&emsp; [3.3 Ambiente do Usuário](#33-ambiente-do-usuário) <br>
&emsp; [3.4 Principais Necessidades dos Usuários Envolvidos](#34-principais-necessidades-dos-usuários-envolvidos) <br>
&emsp; [3.5 Perfis das Partes interessadas](#35-perfis-das-partes-interessadas) <br>
&emsp; &emsp; [3.5.1: Equipe de Desenvolvimento](#351-equipe-de-desenvolvimento) <br>
&emsp; &emsp; [3.5.2: Professores](#352-professores) <br>
&emsp; &emsp; [3.5.3: Monitor](#353-monitor) <br>
&emsp; [3.6: Perfis de Usuários](#36-perfis-de-usuários) <br>
&emsp; [3.7: Necessidades Principais do Usuários](#37-necessidades-principais-do-usuários) <br>
[4: Descrição da Solução](#4-descrição-da-solução) <br>
&emsp; [4.1: Perspectiva do Produto](#41-perspectiva-do-produto) <br>
&emsp; [4.2: Resumo de Recursos](#42-resumo-de-recursos) <br>
&emsp; [4.3: Licenciamento](#43-licenciamento) <br>
[5: Recursos do produto](#5-recursos-do-produto) <br>
[6: Restrições do Produto](#6-restrições-do-produto) <br>
&emsp; [6.1: Restrições de Implementação](#61-restrições-de-implementação) <br>
&emsp; [6.2: Restrições de Design](#62-restrições-de-design) <br>
&emsp; [6.3: Restrições de Uso](#63-restrições-de-uso) <br>
&emsp; [6.4: Restrição de Confiabilidade](#64-restrição-de-confiabilidade) <br>




## 1: Introdução

### 1.1: Propósito:
Este documento tem como propósito especificar as funcionalidades, o objetivo e as propostas do Chatbot Nilo de forma clara e sucinta.

### 1.2: Escopo
O Chatbot Nilo é um projeto da matéria MDS(Métodos de Desenvolvimento de Software ) do curso de Engenharia de Software da UnB(Universidade de Brasília ) do campus gama (FGA).

### 1.3: Definições, Acrônimos e Abreviações
* UnB - Universidade de Brasília
* MDS - Métodos de Desenvolvimento de Software
* Nilo - Nome do Chatbot
* Chatbot - Espécie de robô virtual que pode conduzir uma conversa com um usuário humano através de um serviço de chat.
* FGA - Faculdade do Gama

### 1.4: Referências
 - IBM: Documento de Visão. Disponível em: [https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html ]( https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html )

 - Chatbot Lino. Disponível em: [ https://botlino.github.io/docs/ ]( https://botlino.github.io/docs/ )

### 1.5: Visão Geral
Esse documento servirá como guia do produto, explicando seu objetivo, recursos, restrições, entre outros detalhes. Ele está organizado na seguinte ordem:

* Introdução
* Posicionando
* Descrições
* Visão Geral do Produto
* Recursos do Produto
* Restrições


## 2.0: Posicionamento    
### 2.1: Oportunidade de Negócios
Informações sobre estágio, disponibilidade para horários de monitorias e informações sobre os monitores, não são disponibilizadas de forma de fácil acesso para os alunos.

Dito isto, o Noli tem como objetivo automatizar essas informações, disponibilizando informações sobre o estágio, encontradas no site da UnB e permitir que monitores se cadastrem no Chatbot para que os monitorados possam ir atrás deles de forma mais simples e rápida.
### 2.2: Instrução do Problema
| Os problemas de | Afeta | Cujo impacto é | Uma boa solução seria |
| -------------- | -------- | ------------------ | ---------------------------- |
| Dificuldade no acesso de informações sobre o estágio supervisionado na faculdade e a constante busca de monitoria por parte dos alunos | O processo da graduação na faculdade | Atraso na graduação e falta de conhecimento em matérias | Disponibilizar uma forma automática de obter essas informações |

### 2.3: Instrução de Posicionamento
| Para | Que | O Nilo | Que | Diferente de | Nosso produto |
| ---- | --- | ------ | --- | ------------ | ------------- |
| Estudantes da FGA | Desejam saber sobre o estágio ou que querem ter mais informações sobre seus monitores | É um Chabot | Informa sobre o estágio e facilita o contato com monitores | Sites e documentos da UnB | Disponibiliza informações sobre estágio e permite o cadastro de monitores/alunos por matéria |

## 3: Descrição da Parte Interessadas e do Usuário
### 3.1: Resumo da Parte Interessada
| Nome | Descrição | Responsabilidade |
| ---- | --------- | ---------------- |
| Equipe de desenvolvimento | Graduandos em Engenharia de Software, cursando a disciplina Métodos de Desenvolvimento de Software, pela Universidade de Brasília. | Desenvolver o software no período estipulado, bem como testá-lo e implementá-lo |
| Joênio Costa e Carla Rocha | Professores da Universidade de Brasília, do curso de Engenharia de Software. | Orientar, acompanhar e avaliar o projeto |
| Isaque Alves | Monitor responsável pelo grupo de desenvolvimento. | Orientar e ajudar a equipe de desenvolvimento à entender as tecnologias utilizadas no projeto. |

### 3.2: Resumo do Usuário
| Nome | Descrição | Responsabilidades |
|----- | --------- | ----------------- |
| Estudantes da FGA. | Pessoas interessadas em informações sobre estágio e sobre monitoria. | Utilizar o ChatBot no Telegram. |

### 3.3: Ambiente do Usuário
O usuário poderá acessar o Nilo através da plataforma do Telegram, que pode ser acessado através de um navegador ou através do seu aplicativo, que está disponível para computadores e para smartphones, também é necessária uma conexão ativa com a internet.

### 3.4: Principais Necessidades dos Usuários Envolvidos
Os usuários conversarão com o Nilo através do Telegram sempre que precisarem de informações sobre o estágio ou sobre monitorias das matérias que ele cursa ou dá monitoria.

### 3.5: Perfis das Partes interessadas
#### 3.5.1: Equipe de Desenvolvimento
| Representantes | Descrição | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | --------- | ---- | ---------------- | ------------------- | ------------ |
| Murilo Gomes de Souza, Eliseu Kadesh, Gabriel Paiva, Victor Yukio, Washington Bispo e Thiago Guilherme | Desenvolvedores do Projeto | Alunos da Universidade de Brasília, cursando Métodos de Desenvolvimento de Software | Desenvolver e testar o software, assim como elaborar documentação, praticar metodologias ágeis | Desenvolver o produto no período estipulado, como todos seus requisitos atendidos | Alto |

#### 3.5.2: Professores
| Representantes | Descrição | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | --------- | ---- | ---------------- | ------------------- | ------------ |
| Joênio Costa e Carla Rocha | Professores das disciplinas Métodos de Desenvolvimento de Software e Engenharia de Produto de Software respectivamente, pela Universidade de Brasília | Professor | Orientar, acompanhar e avaliar o processo de desenvolvimento | Avaliar o produto em sua completude | Baixo |

#### 3.5.3: Monitor
| Representante | Descrição | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | --------- | ---- | ---------------- | ------------------- | ------------ |
| Isaque Alves | Monitor da disciplinas Métodos de Desenvolvimento de Software responsável pelo grupo de desenvolvimento | Monitor | Orientar e ajudar a equipe de desenvolvimento à entender as tecnologias utilizadas no projeto | Ter guiado a equipe de desenvolvimento a um bom projeto | Baixo |

### 3.6: Perfis de Usuários
| Representantes | Descrição | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | --------- | ---- | ---------------- | ------------------- | ------------ |
| Estudantes da FGA | Graduandos da UnB-FGA que se interessam por informações sobre monitorias e estágios | Estudantes | Testar e dar feedback sobre o ChatBot e suas respostas | Ter as informações desejadas respondidas de maneira correta pelo Chatbot | Alto |

### 3.7: Necessidades Principais do Usuários
| Necessidade | Prioridade | Interesse | Solução Atual | Solução Proposta |
| ----------- | ---------- | --------- | ------------- | ---------------- |
| Obter informações sobre estágio pela Universidade | Alta | Facilitar o acesso à informação com maior praticidade | Procurar no site da UnB ou ir atrás da coordenação/secretaria | Obter a informação desejada através do ChatBot pelo Telegram |
| Saber monitores da matéria e em qual(is) horários/salas o monitor está disponível | Alta | Permitir que os monitores e os alunos de cada matéria se cadastrem para facilitar a comunicação | Ir atrás do professor da matéria para pedir informações sobre os monitores | Cadastrar alunos e monitores de cada matéria através do ChatBot no Telegram |


## 4: Descrição da Solução
### 4.1: Perspectiva do Produto
O NiloBot tem como principais objetivos ser uma maneira rápida e direta de se obter  as informações referentes a todo o processo de estágios, informando qual caminho a pessoa deve seguir e quais documentos seriam necessários. Além disso deseja-se criar um  meio de facilitar o acesso dos alunos aos seus  monitores, criando assim um local onde os monitores poderiam se inscrever e os alunos poderiam perguntar todos os monitores de uma matéria e os horários disponíveis de cada um junto com seu contato.

### 4.2: Resumo de Recursos
| Benefício para o cliente | Recursos de suporte |
|------------------------- | ------------------- |
| Comunicação com o ChatBot através da linguagem natural | A conversa entre o ChatBot e o usuário humano ocorre como uma conversa humana normal |
| Fácil acesso a informações sobre estágio | O ChatBot responde de acordo com a informação sobre o estágio de acordo com o que o usuário pergunta |
| Ter informações sobre os monitores de certa matéria | O ChatBot permite que os usuários vejam os dados e horários dos monitores de cada matéria caso o monitor esteja cadastrado |

### 4.3: Licenciamento
O ChatBot será distribuído sob a licença MIT para softwares livres, que dá liberdade para todos que o adquirirem de modificar, distribuir, sublicenciar, vender e contribuir para o software.

## 5: Recursos do produto
*São recursos do ChatBot Nilo:*
* Conversar com os usuários em linguagem natural.
* Permitir que monitores se cadastrem e passem suas informações para os alunos daquela matéria.
* Permitir que alunos de certa matéria recebam informações sobre seus monitores caso os monitores estejam cadastrados.
* Responder perguntas sobre o estágio supervisionado para os usuários.

## 6: Restrições do Produto
### 6.1: Restrições de Implementação
Uso do framework Rasa em qual é utilizada a linguagem Python para desenvolver scripts para o ChatBot, uso do MongoDB para o banco de dados.

### 6.2: Restrições de Design
O Nilo têm que ter uma personalidade intuitiva para facilitar o entendimento do usuário.

### 6.3: Restrições de Uso
* Conexão ativa com a internet
* Aplicativo e conta do Telegram

### 6.4: Restrição de Confiabilidade
Para que o Nilo funcione de forma correta, serão feitos testes para garantir a confiabilidade do produto.


