---
id: docArquitetura
title: Documento Arquitetura
sidebar_label: Documento Arquitetura
---

#### Histórico de versão

| Data       | Versão | Descrição            | Autor(es)       |
| ---------- | ------ | -------------------- | --------------- |
| 08/11/2019 | 0.1 | Adição do template do Documento de Arquitetura | Byron Kamal |
| 15/11/2019 | 0.2 | Adição tópico visão geral de introdução e tópico de qualidade | Luís Cláudio T. Lima |
| 15/11/2019 |0.3| Adição MER e DER - Tópico Visão de Dados | Byron Kamal|
| 15/11/2019 | 0.4 | Adição tópico Estilos e padrões arquiteturais| Byron Kamal|
| 15/11/2019 | 0.5 | Adição tópico Metas e Restrições da Arquitetura| Rafael Teodosio|

## 1. Introdução
[A introdução do Documento de Arquitetura de Software fornece uma visão geral do documento inteiro. Ela inclui a finalidade, o escopo, as definições, os acrônimos, as abreviações, as referências e a visão geral do Documento de Arquitetura de Software.]

### 1.1 Finalidade
Este documento oferece uma visão geral arquitetural abrangente do sistema, usando diversas visões arquiteturais para representar diferentes aspectos do sistema. O objetivo deste documento é capturar e comunicar as decisões arquiteturais significativas que foram tomadas em relação ao sistema.

[Esta seção define o papel ou finalidade do Documento de Arquitetura de Software, na documentação do projeto como um todo, e descreve rapidamente a estrutura do documento. O público-alvo específico do documento é identificado, com uma indicação de como ele espera usar o documento.]

### 1.2 Escopo
 [Uma breve descrição da utilidade do Documento de Arquitetura de Software, do que é afetado por esse documento ou influenciado por ele.]

### 1.3 Definições, Acrônimos e Abreviações
[Esta subseção contém as definições de todos os termos, acrônimos e abreviações necessários para interpretar corretamente o Documento de Arquitetura de Software.  Essas informações podem ser fornecidas fazendo referências ao Glossário do projeto.]

### 1.4 Referências
[Esta subseção fornece uma lista completa dos documentos mencionados em outra parte do Documento de Arquitetura de Software. Identifique cada documento por título, número do relatório (se aplicável), data e organização de publicação. Especifique as fontes a partir das quais as referências podem ser obtidas. Essas informações podem ser fornecidas por um anexo ou outro documento.]
### 1.5 Visão Geral

Este tópico visa detalhar as soluções arquiteturais desenvolvidas no sistema. Desta forma,serão abordados os seguintes aspectos:

* Representação Arquitetural
* Restrições e Metas Arquiteturais
* Visão de Casos de Uso
* Visão Lógica
* Visão de Processos
* Visualização da Implementação
* Visão de Dados
* Tamanho e Desempenho
* Qualidade

## 2. Representação Arquitetural 
[Esta seção descreve qual é a arquitetura de software do sistema atual e como ela é representada. Da Visão de Casos de Uso, Visão Lógica, Visão de Processos, Visão de Implantação e Visão de Implementação, enumera as visões necessárias e, para cada visão, explica quais tipos de elementos de modelo ela contém.]

## 3. Metas e Restrições da Arquitetura 
- É necessária a conexão com internet para utilização do App.
- A informação pessoal do usuário será armazenada no banco de dados.
- A aplicação terá suporte somente para Android.
- A IDE utilizada para o desenvolvimento do App é o Android Studio versão 3.4.1 ou o Gennymotion.
- O Front-End e o Back-End será feito em JavaScript.
- Serão usadas as plataformas React-Native para o Front-end e NodeJS para o Back-end.
- Os dados extraídos do Front-End serão armazenados no banco de dados PostgreSQL.
- Será feita uma arquitetura de microsserviços, para um melhor funcionamento e desempenho do sistema, não possuindo dependências entre si.
- O sistema não terá uma grande quantidade de dados, mesmo assim deverá ser feita a persistência desses dados utilizando o banco relacional PostgreSQL.
- A aplicação deve ser terminada até o final da disciplina de Desenho e Arquitetura de Software.

## 4. Visão de Casos de Uso 
[Esta seção lista casos de uso ou cenários do modelo de casos de uso quando eles representam funcionalidade central e significativa do sistema final ou, quando têm uma grande cobertura arquitetural — eles experimentam muitos elementos arquiteturais ou quando enfatizam ou ilustram um ponto complexo e específico da arquitetura.]
4.1 Realizações de Casos de Uso
[Esta seção ilustra o funcionamento do software, apresentando algumas realizações (ou cenários) de casos de uso selecionadas e explica como os diversos elementos do modelo de design contribuem para a respectiva funcionalidade.]

## 5. Visão Lógica 
[Esta seção descreve as partes significativas do ponto de vista da arquitetura do modelo de design, como sua divisão em subsistemas e pacotes. Além disso, para cada pacote significativo, ela mostra sua divisão em classes e utilitários de classe. Apresente as classes significativas do ponto de vista da arquitetura e descreva suas responsabilidades, bem como alguns relacionamentos, operações e atributos de grande importância.]

### 5.1 Visão Geral
[Esta subseção descreve toda a decomposição do modelo de design em termos de camadas e de hierarquia de pacotes.]

### 5.2 Pacotes de Design Significativos do Ponto de Vista da Arquitetura
[Para cada pacote significativo, inclua uma subseção com o respectivo nome, uma breve descrição e um diagrama com todos os pacotes e classes significativos nele contidos. 
Para cada classe significativa no pacote, inclua o respectivo nome, uma breve descrição e, opcionalmente, uma descrição de algumas das suas principais responsabilidades, operações e atributos.]

## 6. Visão de Processos 
[Esta seção descreve a decomposição do sistema em processos leves (threads simples de controle) e processos pesados (agrupamentos de processos leves). Organize a seção em grupos de processos que se comunicam ou interagem. Descreva os modos principais de comunicação entre processos, como transmissão de mensagens e interrupções.]

## 7. Visão de Implantação 
[Esta seção descreve uma ou mais configurações da rede física (hardware) na qual o software é implantado e executado. Ela é uma visão do Modelo de Implantação. No mínimo, para cada configuração, ela deve indicar os nós físicos (computadores, CPUs) que executam o software e suas interconexões (barramento, LAN, ponto a ponto, etc.) É incluído também um mapeamento dos processos da Visão de Processos nos nós físicos.]

## 8. Visão da Implementação 
[Esta seção descreve a estrutura geral do modelo de implementação, a divisão do software em camadas e os subsistemas no modelo de implementação e todos os componentes significativos do ponto de vista da arquitetura.]

## 9. Visão de Dados
### 9.1 Modelo Entidade-Relacionamento (M-ER)
#### Versão 1
[![MER](assets/mer.png)](assets/mer.png)

### 9.2 Diagrama Entidade-Relacionamento (D-ER)
#### Versao 1
[![DER v1](assets/der_v1.png)](assets/der_v1.png)

#### Versao 2
[![DER v2](assets/der_v2.png)](assets/der_v2.png)

## 10. Estilos/padrões arquiteturais
### 10.1 Arquitetura Monolítica vs Distribuída
No projeto optou-se por uma arquitetura baseada em microserviços, que segue uma estrutura distribuída. Nesse modelo tem como base a organização do software em diversos sistemas independentes que se comunicam, no caso desse projeto via protocolo HTTP, e formam um sistema maior. Além de permitir uma alta coesão e um baixo acoplamento, uma arquitetura distribuída facilita questões de infraestrutura, como facilidade de gerenciamento de múltiplos servidores e tolerância a falhas.

### 10.2 MVC
O Node JS, utilizado no backend do projeto, se baseia em um modelo  MVC (Model-View-Controller). O projeto apresenta as tradicionais camadas Model e Controller, porém o papel da View, que tem o papel de decidir como e qual dado será exibido, é substituído pelo front-end, desenvolvido em React Native. A parte de abstração e comunicação com o Banco de Dados é feito através do ORM (Object-relational mapping) Sequelize.

### Cliente-servidor
Mesmo utilizando uma arquitetura baseada em microserviços, o projeto é dividido back-end e o front-end. Por mais que a aplicação seja um aplicativo mobile, a interface ainda se trata de um cliente e todo o sistema por trás que recebe as requisições de um servidor, funcionando como um modelo cliente-servidor clássico. Além disso, alguns serviços específicos no back-end, como o de autenticação, tem o papel apenas de registrar os usuários em um banco independente e renovar/criar tokens de acesso para os mesmos, servido basicamente como um servidor 


## 11. Tamanho e Desempenho 
[Uma descrição das principais características de dimensionamento do software que têm um impacto na arquitetura, bem como as restrições do desempenho desejado.]

## 12. Qualidade 

A arquitetura utilizada contribui para com o software em diversos aspectos. Os padrões arquiteturais das nossas principais frentes do sistema contribuem para a escalabilidade da aplicação, pois contribui altamente para a separação clara de responsabilidades e seus componentes podem ser facilmente substituídos por outros de sua própria implementação. Essa característica da clara separação de conceitos do MVC trás diversos outros benefícios para a aplicação em geral, como testabilidade e manutenabilidade.

Os seguintes itens conferem ao sistema aspectos de qualidade, bem como a descrição da abordagem realizada para satisfazer esses aspectos.

| Item       | Solução | Descrição                                      |
|------------|---------|------------------------------------------------|
| Escalabilidade | Arquitetura de Micros serviços | Em prol de permitir que o sistema evolua sem grandes gargalos, o sistema de modularização aplicado pela arquitetura de micros serviços propicia alterações no funcionamento de um serviço sem alterações em grande escala nos demais serviços relacionados, permitindo modificações mais pontuais e uma integração facilitada do sistema.  |
| Confiabilidade | Manutenção Periódica e Modularização do Sistema | Pela modularização do sistema permitir menor impacto de um micros serviço no funcionamento de outro, a prática de manutenções periódicas permite a solução de problemas de forma pontual e sem impedir o funcionamento de demais serviços, ao contrário de abordagens monolíticas  |
| Segurança | Dados criptografados e Servidor Remoto | Para garantir a segurança de informações sensíveis, a abordagem utilizada será a encriptação de dados e utilização de Hashes, permitindo que informações puras não trafeguem por mais módulos da aplicação do que o necessário, armazenando-as no servidor remoto e acessando-as por meio das hashes.  |
| Portabilidade | Arquitetura de Micros serviços | A Utilização da arquitetura de micros serviços permite o desenvolvimento do Backend da aplicação desacoplado do Frontend, permitindo então que esse Frontend seja adaptado para diferentes plataformas, com um funcionamento equivalente conforme o que foi implementado no Backend, contando ainda com a independência de funcionamento de cada serviço.  |