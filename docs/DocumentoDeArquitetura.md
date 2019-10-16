# Documento de Arquitetura

## Histórico de Versões

| Data | Versão | Descrição | Autor |
| ---- | ------ | --------- | ----- |
| 23/09/2019 | 1.0.0 | Adição do Template do Documeto | Washington Bispo |
|25/09/2019 | 1.0.1 | Adição do 1.4, 2.2, 4.1, 4.2, 4.3 e 6 | Washington Bispo|
| 25/09/2019 | 1.0.2 | Revisão geral e formatação | Thiago Guilherme |
| 12/10/2019 | 1.1.0 | Remoção do tópico 4 e renumeração dos tópicos, mudanças nos tópicos 1.1, 1.2, 2, 3 e 4(Antigo tópico 5) | Murilo Gomes |

## Sumário:

[1. Introdução](#1-introdução) <br>

&emsp; [1.1 Finalidade](#11-finalidade) <br>

&emsp; [1.2 Escopo](#12-escopo) <br>

&emsp; [1.3 Definições, Acrônimos e Abreviações ](#13-definições-acrônimos-e-abreviações ) <br>

&emsp; [1.4 Referências](#14-referências) <br>

&emsp; [1.5 Visão Geral](#15-visão-geral) <br>

[2. Representação de Arquitetura](#2-representação-de-arquitetura) <br>

&emsp; [2.1 Diagrama da Arquitetura Rasa](#21-diagrama-da-arquitetura-rasa) <br>

&emsp; [2.1.1 Front-end](#211-Front-end)<br>

&emsp; [2.1.2 Back-end](#212-Back-end) <br>

[3. Objetivos e Restrições da Arquitetura](#3-objetivos-e-restrições-da-arquitetura) <br>

&emsp; [3.1 Requisitos Funcionais](#31-requisitos-funcionais) <br>

&emsp; [3.2 Restrições](#32-restrições-tecnológicas) <br>


[4. Visão Lógica](#4-visão-lógica) <br>

&emsp; [4.1 Visão Geral](#41-visao-geral)<br>

&emsp; [4.2 Pacotes de Design Significativos do Ponto de Vista da Arquitetura](#42-pacotes-de-design-significativos-do-ponto-de-vista-da-arquitetura)<br>

&emsp; [4.2.1 Diagrama de Pacotes](#421-diagrama-de-pacotes)<br>

[5. Tamanho e Desempenho](#5-tamanho-e-desempenho) <br>

[6. Qualidade](#6-qualidade) <br>

## 1: Introdução

### 1.1: Finalidade


Este documento tem como foco esclarecer a arquitetura do ChatBot Nilo, demonstrando esquemas arquiteturais e casos de uso do produto.

### 1.2: Escopo


O Nilo tem como objetivo auxiliar os alunos na obtenção de informações relativas ao estágio supervisionado e mais algumas dúvidas gerais sobre a UnB em si.

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


### 2.1: Diagrama da Arquitetura Rasa

<p align ="center">
  <img src="https://imgur.com/jGKV0bs.png">
  </p>

#### 2.1.1: Front-end
A arquitetura do front-end do produto se refere à parte acima do "connector" e funciona da seguinte forma: o usuário manda a mensagem para o Nilo pelo telegram e após isso a mensagem é enviada para o connector que define a resposta do bot através do back-end do produto, quando a resposta é definida o connector manda a resposta para o telegram através do Nilo.

#### 2.1.2: Back-end

A arquitetura do back-end por sua vez se refere à parte abaixo do connector e funciona da seguinte forma: após recebida a mensagem do usuário, o bot tenta identificar a intenção do usuário e o fluxo no qual o bot precisa respondê-lo, essa informações são contidas no trainer do bot.<br>
As intenções são definidas a partir dos arquivos de intents que contém qual a intenção do usuário de acordo com a mensagem que ele pode ter enviado, a parte das intents faz parte do rasa-nlu.<br>
Os fluxos que o bot deve seguir de acordo com a intent do usuário estão descritos nos arquivos de stories, as respostas pré-definidas do bot(utters), são declaradas e definidas no arquivo domain.yml, os nomes das intents e das ações customizadas(custom actions) também são declarados neste mesmo arquivo, tanto o domain.yml quanto os arquivos de stories fazem parte do modelo de diálogo do Rasa.<br>
Quando a resposta do bot é definida por uma custom action isto é, alguma resposta que depende mais do que uma simples resposta pré-definida, como enviar um documento por exemplo, o bot entra em contato com o rasa-core-sdk que contém as estruturas de custom actions para o Rasa, essas actions têm que ser definidas na linguagem python e no arquivo bot/actions/actions.py.<br>
Após definida a resposta, a resposta é enviada de volta para connector para que o usuário possa ser respondido.<br><br>

**OBS**: A parte referente ao Kibana, Elastic Search e ao Jupyter Notebooks, servem apenas para a parte de análise do bot.

## 3: Objetivos e Restrições da Arquitetura


### 3.1: Requisitos Funcionais

* O ChatBot deve ter integração com o Telegram;
* O ChatBot deve conversar com usuários humanos através da linguagem natural;
* O ChatBot deve respeitar a personalidade do Nilo;

### 3.2: Restrições Tecnológicas

Para o desenvolvimento do Nilo foram usadas as seguintes tecnologias:
* Rasa: Framework utilizado para a criação de chatbots;
* Python: Linguagem base para a utilização do rasa(python 3.6);
* Docker: Ambiente de containers para facilitar o desenvolvimento da aplicação;


## 4: Visão Lógica

### 4.1: Visão Geral

O ChatBot Nilo é construido em cima da tecnologia Rasa e com a utilização da linguagem de programação Python. Os principais componentes do Rasa são: o RasaNLU que identifica a intenção do usuário(intents) e o Rasa Core que determina o modelo de diálogo que o bot deve seguir para responder o usuário(stories). Após identificado o fluxo de dialogo que o bot deve seguir, o bot pode responder o usuário com diferentes tipos: utters e actions. Sendo que utters são textos pre-definidos no arquivo de domain.yml e actions são scripts escritos em Python que podem se constituir de diferentes ações como buscar um documento ou alguma informação em um site.

### 4.2: Pacotes de Design Significativos do Ponto de Vista da Arquitetura

#### 4.2.1: Diagrama de Pacotes
<p align="center">
  <img src="https://imgur.com/zBdICBA.png">
</p>


## 5: Tamanho e Desempenho
O projeto será capaz de atender algumas dezenas de pessoas e a sua velocidade irá variar de acordo com a qualidade do servidor que servirá de Host.

## 6: Qualidade
O aplicativo vai usar a própria interface gráfica do Telegram, onde o usuário pode enviar perguntas referente aos temas tratados e obter as respostas mais adequadas ao que foi perguntado.
