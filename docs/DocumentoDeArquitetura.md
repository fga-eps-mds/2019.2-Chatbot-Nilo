
# Documento de Arquitetura

## Histórico de Versões

| Data | Versão | Descrição | Autor |
| ---- | ------ | --------- | ----- |
| 23/09| 1.0.0 | Adição do Template do Documeto | Washington Bispo |
|25/09| 1.0.1 | Adição do 1.4, 2.2, 4.1, 4.2, 4.3 e 6 | Washington Bispo|
| 25/09| 1.0.2 | Revisão geral e formatação | Thiago Guilherme |

## Sumário:

[1. Introdução](#1-introdução) <br>

&emsp; [1.1 Finalidade](#11-finalidade) <br>

&emsp; [1.2 Escopo](#12-escopo) <br>

&emsp; [1.3 Definições, Acrônimos e Abreviações ](#13-definições-acrônimos-e-abreviações ) <br>

&emsp; [1.4 Referências](#14-referências) <br>

&emsp; [1.5 Visão Geral](#15-visão-geral) <br>

[2. Representação de Arquitetura](#2-representação-de-arquitetura) <br>

&emsp; [2.1 Front-end](#21-front-end) <br>

&emsp; [2.2 Back-end](#22-Back-end) <br>

[3. Objetivos e Restrições da Arquitetura](#3-objetivos-e-restrições-da-arquitetura) <br>

&emsp; [3.1 Requisitos](#31-requisitos) <br>

&emsp; [3.2 Restrições](#32-restrições-tecnológicas) <br>

[4. Visualização de Caso de Uso](#4-visualização-de-caso-de-uso) <br>

&emsp; [4.1 Diagrama de Casos de Uso](#41-diagrama-de-casos-de-uso) <br>

&emsp; [4.2 Atores de Casos de Uso](#42-atores-de-casos-de-uso) <br>

&emsp; [4.3 Descrições de Casos de Uso](#43-descrições-de-casos-de-uso) <br>

&emsp; &emsp; [4.3.1 Consultar Informações Sobre Estágio](#431-consultar-informações-sobre-estágio)<br>

&emsp; &emsp; [4.3.2 Consultar Monitores e Horários de Monitorias](#432-consultar-monitores-e-horários-de-monitorias) <br>

&emsp; &emsp; [4.3.3 Marcar Monitorias](#433-marcar-monitorias) <br>

&emsp; &emsp; [4.3.4 Consultar Informações Sobre Estágio](#434-cadastrar-Monitores) <br>

[5. Visão Lógica](#5-visão-lógica) <br>

[6. Tamanho e Desempenho](#6-tamanho-e-desempenho) <br>

[7. Qualidade](#7-qualidade) <br>

## 1: Introdução

### 1.1: Finalidade


Este documento tem como foco esclarecer o funcionamento da aplicação, suas nuances e o desenvolvimento em questão, ao mesmo tempo que define quais suas funções e os alvos dela.

### 1.2: Escopo


O projeto tem como objetivo auxiliar os alunos na obtenção de informações relativo ao estágio supervisionado e as monitorias dentro do campus da Universidade de Brasília - Faculdade do Gama, será feito através de um bot que será capaz de responder as perguntas referentes aos temas citados.

### 1.3: Definições, Acrônimos e Abreviações

| Abreviação |              Significado              |
|------------|:--------------------------------------:|
|     MDS    | Métodos de Desenvolvimento de Software |
|     Unb    | Universidade de Brasília              |
|     FGA    | Faculdade do Gama                     |

### 1.4: Referências
>Documento de Arquitetura de Software; Disponível em http://mds.cultura.gov.br/extend.formal_resources/guidances/examples/resources/sadoc_v1.htm#_Toc447085892; Acesso em <25 de Setembro de 2019>
>The Rasa Core dialogue engine; Disponível em: https://rasa.com/docs/core/; Acesso em 25 de Setembro de 2019.
YUKIO, Victor; GUILHERME, Thiago; KADESH, Eliseu; BISPO, Washington; GOMES, Murilo; AGUIAR, Gabriel; 
>Documento de Visão: https://github.com/fga-eps-mds/2019.2-Chatbot-Nilo/blob/documenta%C3%A7%C3%A3o/docs/DocumentoDeVisao.md; Acesso em <25 de Setembro de 2019>



### 1.5: Visão Geral
O documento vai ser formado por 6 aspectos principais, onde cada um irá descrever as seguintes coisas:
* Introdução: Introdução do projeto, suas funcionalidades, público alvo e informações úteis;
* Posicionamento: Problematização do tema e uma oportunidade de nicho;
* Perfis dos Envolvidos e dos Usuários: Descrição daqueles que irão fazer uso da aplicação;
* Visão Geral do Produto: Como podemos observar nosso produto e seus objetivos
* Recursos do Produto: Descrição dos recursos do produto;
* Restrições: Restrições do produto, restrições externas, restrições de usuário.


## 2: Representação de Arquitetura

### 2.1: Front-end

O usuário final vai utilizar todas as funções disponíveis diretamente do aplicativo de mensagens Telegram
### 2.2: Back-end

Nossa arquitetura vai usar o Rasa-Boilerplate como um iniciador e como linguagem principal será usado Python.

## 3: Objetivos e Restrições da Arquitetura


### 3.1: Requisitos

É preciso um dispositivo com acesso à internet e com acesso ao Telegram.


### 3.2: Restrições Tecnológicas

A aplicação irá ser executada usando um computador como servidor (através do Ngrok) e ela poderá ser acessada através do Telegram.

A linguagem de programação será python

A base do projeto é a tecnologia Rasa, que dispõe de um conjunto de ferramentas de machine learning para a criação de chatbots

## 4: Visualização de Caso de Uso
### 4.1: Diagrama de Casos de Uso
<p align ="center">
  <img src="https://i.imgur.com/U2bKCNm.png">
  </p>
  
### 4.2: Atores de Casos de Uso

| Ator    |                                                                                                    Descrição                                                                                                   |
|---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Estudante | O usuário poderá através de seu dispositivo que tenha telegram conversar com o NiloBot e então  o bot irá responder qualquer dúvida pertinente a respeito dos estágios supervisionado e as  monitorias da FGA. |
| Professor| Será o responsável por preencher os dados de seus monitores. |
| Monitor | Responsável por marcar as monitorias e informar o local que vai acontecer. |

### 4.3: Descrições de Casos de Uso
#### 4.3.1: Consultar Informações Sobre Estágio 
Breve Descrição: Este caso de uso permite que o usuário faça perguntas referentes aos processos que envolvem o estágio supervisionado e o bot o responderá da maneira adequada.

#### 4.3.2: Consultar Monitores e Horários de Monitorias
Breve Descrição: Este caso de uso permite o usuário perguntar quais os horários de uma determinada monitoria, perguntar diretamente os horários e qual a sala de atendimento, de um monitor ou de todos os monitores de uma determinada matéria.

#### 4.3.3: Marcar Monitorias 
Breve Descrição: Este caso de uso permite o monitor informar ao bot quando vai ser realizada uma monitoria e aonde ela vai acontecer.

#### 4.3.4: Cadastrar Monitores
Breve Descrição: Este caso de uso serve para o professor informar ao bot quais são seus monitores e as maneiras de entrar em contato com eles.

## 5: Visão Lógica


Através de um dispositivo que tenha acesso a aplicação Telegram e acesso a internet, o usuário poderá inicializar uma conversa com o NiloBot, quando o usuário enviar uma mensagem ao Nilo, essa mensagem será respondida da forma adequada.

A informação referente aos monitores, seus horários e como entrar em contato com ele estarão disponíveis em um google sheet, de onde o bot irá tirar as informações requisitadas pelo usuário.

## 6: Tamanho e Desempenho
O projeto será capaz de atender algumas dezenas de pessoas e a sua velocidade irá variar de acordo com a qualidade do servidor que servirá de Host.

## 7: Qualidade
O aplicativo vai usar a própria interface gráfica do Telegram, onde o usuário pode enviar perguntas referente aos temas tratados e obter as respostas mais adequadas ao que foi perguntado.



    
    







