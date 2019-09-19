---
id: docVisao
title: Documento de Visão
sidebar_label: Documento de Visão
---

# Documento de Visão

### Histórico de versão

| **Data**   | **Versão** | **Descrição**                            | **Autor(es)**        |
| ---------- | ---------- | ---------------------------------------- | -------------------- |
| 18/09/2019 | 0.1        | Iniciação do Documento e Adição Tópico 1 | Marcelo Magalhães    |
| 18/09/2019 | 0.2        | Adição Tópico 4                          | Byron Kamal          |
| 18/09/2019 | 0.3        | Adição Tópico 3                          | Samuel Barros Borges |
| 19/09/2019 | 0.4        | Adição Tópico 2                          | Marcelo Magalhães    |
| 19/09/2019 | 0.5        | Adição Tópico 5                          | Marcelo Magalhães    |

# 1 Introdução

O documento de visão serve para expor o escopo de alto nível do produto, o foco do software a ser desenvolvido e seu valor de mercado, com o objetivo de firmar e nivelar as expectativas das pessoas envolvidas exatamente o que é o software em questão.

## 1.1 Propósito

O documento tem a finalidade de apresentar e estabelecer uma visão ampla sobre o app Driblô de modo a deixar claro sua proposta, características e utilidade.

## 1.2 Escopo

O projeto tem como finalidade facilitar a criação e a administração de peladas, ajudando principalmente a comunicação entre os membros, gerência de informações importantes como horários, locais e valores da pelada, também possui foco no controle das equipes formadas e ordem das partidas, visando assim economizar tempo e deixar a experiência dos participantes mais simples e agradável.

## 1.3 Definições, acrônimos e abreviações

**Driblô** - Nome do sistema a ser desenvolvido
**Pelada** - Evento onde pessoas se juntam para jogar partidas de futebol
**Usuário, Jogador, Peladeiros, Participante** - Usuário da aplicação participante do evento
**Administrador** - Usuário que administra a pelada
**Front-end** - Parte do software responsável pela interface de interação com o usuário
**Back-end** - Parte do software responsável pelas regras de negócio da aplicação

## 1.4 Referências

- IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_3.0.1/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.htm. Acesso em: 18 set. 2019;
- Projeto Translate.me - Documento de visão, Acessado em: 18/09/2019. Disponível em: https://translate-me.github.io/docs/documentos/projeto/doc_de_visao/
- Projeto EmbelezaMais - Documento de visão, Acessado em: 18/09/2019. Disponível em: https://github.com/Software-Design-2017/EmbelezaMais/wiki/Documento-de-Visão-Framework#1-introdução

## 1.5 Visão geral

Este documento é dividido em 5 tópicos que descrevem os detalhes e características do software proposto, sendo as partes:

- **Introdução:** na qual o projeto é introduzido de maneira geral;
- **Posicionamento:** em que é descrito o problema que motivou a criação do produto, as oportunidades de negócio e o posicionamento do produto no mercado;
- **Descrição de Usuário:** este tópico descreve o perfil das partes envolvidas e interessadas no projeto;
- **Visão Geral do Produto:** fornece uma visão geral de alto nível das capacidades e recursos do produto e configurações dos sistemas;
- **Restrições:** as restrições de design, restrições externas, como requisitos operacionais ou regulamentares.

# 2 Posicionamento

## 2.1 Oportunidade de Negócio

O **Driblô** oferece um serviço de gerenciamento de peladas, fazendo a ligação entre os usuários que participam desses eventos. O aplicativo visa solucionar a demanda de um ambiente em que seja possível participantes e organizadores de uma pelada consigam passar informações importante e organizar as questões logísticas, financeiras e operacionais que envolvem uma pelada.

O projeto visa facilitar a criação e a administração de peladas, ajudando principalmente a comunicação entre os membros, gerência de informações importantes como horários, locais e valores da pelada, também possui foco no controle das equipes formadas e ordem das partidas, assim economizando tempo e deixando a experiência dos participantes mais simples e agradável.

## 2.2 Descrição do Problema

Os principais problemas da criação até a realização e manutenção de uma pelada podem ser agrupados em 3 tópicos principais, comunicação ineficiente, dificuldade em gerenciar pessoas e dificuldade no controle financeiro, que serão melhor descritos abaixo.

- **2.2.1 Comunicação:**
  É comum que toda a comunicação e organização da pelada seja feita através de aplicativos de mensagens como o WhatsApp, Telegram ou Messenger, com isso a comunicação fica bastante ineficiente e complicada, pois qualquer pessoa pode escrever nos grupos fazendo com que mensagens importantes sejam perdidas. A confirmação de presença costuma ser feita através de listas que devem ser copiadas e coladas diversas vezes o que gera bastante trabalho e faz com que a lista seja bastante imprecisa, além disso como qualquer membro do grupo pode editar as informações da lista fica facilmente adulterada.
- **2.2.2 Gerência de pessoas:**
  Uma das etapas que geram a maior perda de tempo em uma pelada é a dificuldade de um acordo na separação e ordenação dos times, pessoas chegando atrasadas, times desbalanceados e definição de quem é o proximo a jogar são algumas das maiores dificuldades na gerência dos membros das peladas.
- **2.2.3 Controle Financeiro:**
  Como muitas vezes a pelada tem custos como aluguel do campo ou quadra, bola e coletes, o gerenciamento desse dinheiro de forma correta é bem trabalhoso levando em conta a quantidade de pessoas, a quantidade de dinheiro, a dificuldade em conseguir troco e a falta de um histórico de pagamentos confiável, o que pode gerar confusões.

## 2.3 Instrução de Posição do Produto

| Para          | peladeiros                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Que           | necessitam de uma ferramenta que auxilie no gerenciamento de peladas                                                                  |
| O **Driblô**  | é um aplicativo                                                                                                                       |
| Que           | facilita a administração de peladas, melhorando a comunicação, gerência de informações, controle das equipes e ordenação das partidas |
| Diferente de  | outros aplicativos do tipo                                                                                                            |
| Nosso produto | oferece uma experiência mais simples, intuitiva e agradável para os participantes.                                                    |

# 3 Descrição de Usuário

## 3.1 Partes Envolvidas

### 3.1.1 Usuários

São os usuários finais da aplicação em si, interessados em utilizar o sistema finalizado.

### 3.1.2 Desenvolvedores

Consistem de um grupo de dez alunos cursando a matéria Arquitetura e Desenho de Software na Universidade de Brasília no segundo semestre de 2019. Estes são responsáveis por desenvolver, documentar e realizar a manutenção do sistema.

### 3.1.3 Professores e Monitores

Responsáveis por definir critérios de qualidade, prazos de entrega, definir padrões de projetos a serem utilizados e por fim, avaliar o sistema.

## 3.2 Usuários Finais

Os usuários finais do sistema consistem de pessoas engajadas na prática de partidas recreacionais de futebol amador (peladas), não existindo outras restrições.

## 3.3 Principais Necessidades do Usuário

Os potenciais usuários desse sistema enfrentam vários pequenos problemas que podem ser facilmente resolvidos, mas que quando acumulados se tornam um verdadeiro empecilho. Estes problemas são:

- Dificuldade de agendamento das partidas;
- Dificuldade na divisão balanceada dos times;
- Dificuldade na divisão dos custos da reserva do local;
- Dificuldade na divulgação do local escolhido;
- Dificuldade na formulação e divulgação das regras.

## 3.4 Ambiente de Usuário

O Ambiente atual do usuário apresenta sérios problemas de eficiência, com o agendamento feito por aplicativo de mensagens, o que prejudica a eficiência do processo de agendamento e precisão da lista de participantes. A divulgação do local e das regras, por também serem feitas por estes aplicativos, não possuem garantia de recebimento do usuário, podendo ser perdidas no meio de mensagens cotidianas.

## 3.5 Alternativas e Concorrência

Existem alguns aplicativos que se propõem a resolver a questão de agendamento de partidas, mas nenhum destes divide o escopo completo com o produto proposto. Os aplicativos existentes são:

- Appito
- BoraJogar

## 4. Visão Geral do Produto

O **Driblô** trata-se de um aplicativo mobile que tem como objetivo auxiliar pessoas/jogadores com o controle de peladas. Os usuários do aplicativo poderão utilizá-lo para facilitar a criação de grupos de participantes da pelada e gerir o evento, evitando assim perda de tempo e otimizando a comunicação do grupo.

### 4.1 Perspectiva do Produto

O aplicativo tem como principal característica ajudar pessoas/jogadores a organizar e gerenciar melhor suas peladas e para realizar tal propósito o **Driblô** oferece uma usabilidade amigável, recursos que facilitem o controle da partida e a integração e competitividade saudável entres os grupo de jogadores.

### 4.2 Funcionalidades do Produto

Os recursos e funcionalidades do aplicativo **Driblô** compreendem serviços implementados de forma independente, buscando facilitar o controle das peladas e integração entre os jogadores. Os recursos estão descritos abaixo.

#### 4.2.1 Login e Cadastro

O aplicativo possui um sistema de cadastro que permite a inscrição do usuário e um sistema de Login para que o usuário possa utilizar os recursos disponíveis.

#### 4.2.2 Criação de Grupos

O dono do grupo (usuário que criou o grupo) poderá adicionar outros usuários e, assim, facilitar a comunicação centralizando assuntos em relação à pelada no aplicativo. Ele também poderá colocar conceder papel de administrador do grupo para outros integrantes.

#### 4.2.4 Controle da Pelada

O dono do grupo poderá definir regras data, horário, tipo de campo (futsal, society), tamanho dos times, local da pelada e formar os times através do sorteio dos integrantes, que será sorteado pela própria aplicação. Durante a execução da pelada será possível iniciar partidas (temporizador), ordenar times nas lista de espera, finalizar partida baseado nas regras (limite de gols ou de tempo) e controlar substituições de jogadores.

#### 4.2.5 Controle de Pagamento

O aplicativo ajudará na divisão dos custos da pelada. Insumos como campo, bola, coletes dos times, etc, geram custos para a realização da pelada e para facilitar o pagamento, o app conta com um controle de pagamento em que é possível definir o preço dos insumos, dividir o valor entre os participantes e marca quem pagou e quanto.

## 5: Restrições

#### 5.1 Restrições de Design

O design será simples onde apenas o essencial tem lugar à vista, pensado em deixar o aplicativo bastante intuitivo e fácil de usar.

#### 5.2 Restrições de Implementação

O sistema será desenvolvido utilizando a linguagem JavaScript junto ao Node.js e o framework React Native.

#### 5.3 Restrições de Uso

Para o uso de algumas funcionalidades como fazer o cadastro, enviar convites e editar informações é necessário que o usuário tenha acesso a um dispositivo conectado à internet.

## 6: Referências

- IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_3.0.1/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.htm. Acesso em: 18 set. 2019;
- Projeto Translate.me - Documento de visão, Acessado em: 18/09/2019. Disponível em: https://translate-me.github.io/docs/documentos/projeto/doc_de_visao/
- Projeto EmbelezaMais - Documento de visão, Acessado em: 18/09/2019. Disponível em: https://github.com/Software-Design-2017/EmbelezaMais/wiki/Documento-de-Visão-Framework#1-introdução
