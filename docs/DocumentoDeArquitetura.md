
# Documento de Arquitetura

## Sumário:

[1. Introdução](#1-introdução) <br>

&emsp; [1.1 Finalidade](#11-finalidade) <br>

&emsp; [1.2 Escopo](#12-escopo) <br>

&emsp; [1.3 Definições, Acrônimos e Abreviações ](#13-definições-acrônimo-e-abreviações   ) <br>

&emsp; [1.4 Referências](#14-referências) <br>

&emsp; [1.5 Visão Geral](#15-visão-geral) <br>

[2. Representação de Arquitetura](#2-representação-de-arquitetura) <br>

&emsp; [2.1 Front-end](#21-front-end) <br>

&emsp; [2.2 Back-end](#22-Back-end) <br>

[3. Objetivos e Restrições da Arquitetura](#3-objetivos-restrições-da-arquitetura) <br>

&emsp; [3.1 Requisitos](#31-requisitos) <br>

&emsp; [3.2 Restrições](#32-restrições) <br>

[4. Visualização de Caso de Uso](#4-visualização-de-caso-de-uso) <br>

&emsp; [4.1 Diagrama de Casos de Uso](#41-diagrama-de-casos-de-uso) <br>

&emsp; [4.2 Atores de Casos de Uso](#42-atores-de-casos-de-usos) <br>

&emsp; [4.3 Descrições de Casos de Uso](#43-descrições-de-casos-de-uso) <br>

[5. Visão Lógica](#5-visão-lógica) <br>

[6. Tamanho e Desempenho](#6-tamanho-e-desempenho) <br>

[7. Qualidade](#7-qualidade) <br>

## 1: Introdução

### 1.1: Finalidade


Este documento tem como foco esclarecer o funcionamento da aplicação, suas nuances e o desenvolvimento em questão, ao mesmo tempo que define quais suas funções e os alvos dela.

### 1.2: Escopo


O projeto tem como objetivo auxiliar os alunos na obtenção de informações relativo ao estágio supervisionado e as monitorias dentro do campus da Universidade de Brasília - Faculdade do Gama, será feito através de um bot que irá ser capaz de responder perguntas referentes aos temas citados.

### 1.3: Definições, Acrônimos e Abreviações

| Abreviação |              Significado              |
|------------|:-------------------------------------:|
|     MDS    | Método de Desenvolvimento de Software |
|     Unb    | Universidade de Brasília              |
|     FGA    | Faculdade do Gama                     |

### 1.4: Referências

### 1.5: Visão Geral
O documento vai ser formado por 6 aspectos principais, onde cada um irá descrever as seguintes coisas:
Introdução: Introdução do projeto, suas funcionalidades, público alvo e informações úteis;
Posicionamento: Problematização do tema e uma oportunidade de nicho;
Perfis dos Envolvidos e dos Usuários: Descrição daqueles que irão fazer uso da aplicação;
Visão Geral do Produto: bla bla bla
Recursos do Produto: Descrição dos recursos do produto;
Restrições: Restrições do produto, restrições externas, restrições de usuário.


## 2: Representação de Arquitetura

### 2.1: Front-end

O usuário final vai utilizar todas as funções disponíveis diretamente do aplicativo de mensagens Telegram
### 2.2: Back-end

BlaBlaBla

## 3: Objetivos e Restrições da Arquitetura


### 3.1: Requisitos

É preciso um dispositivo com acesso à internet e com acesso ao Telegram.


### 3.2: Restrições Tecnológicas

A aplicação irá ser executada usando um computador como servidor (através do Ngrok) e ela poderá ser acessada através do Telegram.

A linguagem de programação será python

A base do projeto é a tecnologia Rasa, que dispõe de um conjunto de ferramentas de machine learning para a criação de chatbots

## 4: Visualização de Caso de Uso
### 4.1: Diagrama de Casos de Uso
Foto do Diagrama
### 4.2: Atores de Casos de Uso
| Ator    |                                                                                                    Descrição                                                                                                   |
|---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Usuário | O usuário poderá através de seu dispositivo que tenha telegram conversar com o NiloBot e então  o bot irá responder qualquer dúvida pertinente a respeito dos estágios supervisionado e as  monitorias da FGA. |
### 4.3: Descrições de Casos de Uso
| Caso de Uso |  Descrição  |
|-------------|:-----------:|
|    Caso A   | Descrição A |
|    Caso B   | Descrição B |

## 5: Visão Lógica


Através de um dispositivo que tenha acesso a aplicação Telegram e acesso a internet o usuário poderá inicializar uma conversa com  NiloBot, quando o usuário enviar uma mensagem ao Nilo, essa mensagem será respondida da forma adequada.

A informação referente aos monitores, seus horários e como entrar em contato com ele estarão disponíveis em um google sheet, de onde o bot irá tirar as informações requisitadas pelo usuário.

## 6: Tamanho e Desempenho
BláBláBlá

## 7: Qualidade
O aplicativo vai usar a própria interface gráfica do Telegram, onde o usuário pode enviar perguntas referente aos temas tratados e obter as respostas mais adequadas ao que foi perguntado.



    
    





