---
id: estrutural
title: GOF's Estruturais
sidebar_label: GOF's Estruturais
---

### Histórico de versão
| Data | Versão | Descrição | Autor(es) |
| ---- | ------ | --------- | --------- |
| 18/10/2019 | 0.1 | Criação do documento | Henrique Martins |
| 23/10/2019 | 0.2 | Adicionando imagens e benefícios para padrões | Henrique Martins |
| 23/10/2019 | 0.3 | Adição da introdução | Henrique Martins |
| 24/10/2019 | 0.4 | Adição dos problemas solucionados pelos padrões | Henrique Martins |
| 25/10/2019 | 0.5 | Adição da viabilidade do modelo Decorator ao projeto | Rafael Teodosio, Samuel Borges|
| 25/10/2019 | 0.6 | Adição da viabilidade do modelo Proxy ao projeto | Luis Claudio T. Lima e João Pedro Mota|
| 25/10/2019 | 0.6.2 | Correção do template do modelo Proxy | Luis Claudio T. Lima e João Pedro Mota|

## Introdução

Os padrões estruturais se preocupam com a forma como classes e objetos são compostos para formar estruturas maiores. Os de classes utilizam a herança para compor interfaces ou implementações, e  os de objeto descrevem maneiras de compor objetos para obter novas funcionalidades. A flexibilidade obtida pela composição de objetos provém da capacidade de mudar a composição em tempo de execução o que não é possível com a composição estática (herança de classes).

---

## Adapter

### O que é?

O padrão do adaptador é um padrão de design de software que permite que a interface de uma classe existente seja usada como outra interface. É frequentemente usado para fazer com que as classes existentes funcionem com outras pessoas sem modificar seu código-fonte.

[![Exemplo](assets/exemplo_adapter.png)](assets/exemplo_adapter.png)

### Estrutura mínima

[![Diagrama](assets/adapter.png)](assets/adapter.png)

### Problemas solucionados pelo padrão

 1. Como uma classe pode ser reutilizada que não possui uma interface que um cliente exige?
 2. Como as classes que possuem interfaces incompatíveis podem trabalhar juntas?
 3. Como uma interface alternativa pode ser fornecida para uma classe?

### Benefícios

 1. Princípio de responsabilidade única. Você pode separar a interface ou o código de conversão de dados da lógica de negócios principal do programa.
 1. Princípio Aberto / Fechado. Você pode introduzir novos tipos de adaptadores no programa sem quebrar o código do cliente existente, desde que eles funcionem com os adaptadores por meio da interface do cliente.

### Aplicável no Driblô?

Este padrão de projeto não será aplicado no Driblô, considerando seu período de desenvolvimento e uso (disciplina de Arquitetura e Desenho de Software) e a implementação das classes no projeto. Não há a necessidade de fazer a adaptação de classes de terceiros, não sendo necessário esse padrão para o projeto.

---

## Bridge

### O que é?

O Bridge é um padrão de design destinado a "desacoplar uma abstração de sua implementação, para que os dois possam variar independentemente". O Bridge usa encapsulamento, agregação e pode usar herança para separar responsabilidades em diferentes classes.

[![Exemplo](assets/exemplo_bridge.png)](assets/exemplo_bridge.png)

### Estrutura mínima

[![Diagrama](assets/bridge.png)](assets/bridge.png)

### Problemas solucionados pelo padrão

 1. Como uma abstração e sua implementação podem variar independentemente?
 1. Como uma implementação pode ser selecionada e trocada em tempo de execução?

### Benefícios

 1. Você pode criar classes e aplicativos independentes de plataforma.
 1. O código do cliente funciona com abstrações de alto nível. Não está exposto aos detalhes da plataforma.
 1. Princípio Aberto / Fechado. Você pode introduzir novas abstrações e implementações independentemente uma da outra.
 1. Princípio de responsabilidade única. Você pode se concentrar na lógica de alto nível na abstração e nos detalhes da plataforma na implementação.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Composite

### O que é?

Composite é um padrão de projeto de software utilizado para representar um objeto formado pela composição de objetos similares. Este conjunto de objetos pressupõe uma mesma hierarquia de classes a que ele pertence. Tal padrão é, normalmente, utilizado para representar listas recorrentes - ou recursivas - de elementos. Além disso, este modo de representação hierárquica de classes permite que os elementos contidos em um objeto composto sejam tratados como se fossem um objeto único. Desta forma, os métodos comuns às classes podem ser aplicados, também, ao conjunto agrupado no objeto composto.

[![Exemplo](assets/exemplo_composite.png)](assets/exemplo_composite.png)

### Estrutura mínima

[![Diagrama](assets/composite.png)](assets/composite.png)

### Problemas solucionados pelo padrão

 1. Como uma hierarquia parte-todo pode ser representada para que os clientes possam tratar objetos individuais e composições de objetos de maneira uniforme?

### Benefícios

 1. Você pode trabalhar com estruturas de árvores complexas de maneira mais conveniente: use polimorfismo e recursão a seu favor.
 1. Princípio Aberto / Fechado. Você pode introduzir novos tipos de elementos no aplicativo sem quebrar o código existente, que agora funciona com a árvore de objetos.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 

(Dizer porque soluções são úteis ou não)

---

## Decorator

### O que é?

Decorator é um padrão de projeto que permite adicionar um comportamento a um objeto já existente em tempo de execução, ou seja, agrega dinamicamente responsabilidades adicionais a um objeto. Decorators oferecem uma alternativa flexível ao uso de herança para estender uma funcionalidade, com isso adiciona-se uma responsabilidade ao objeto e não à classe.

[![Exemplo](assets/exemplo_decorator.png)](assets/exemplo_decorator.png)

### Estrutura mínima

[![Diagrama](assets/decorator.png)](assets/decorator.png)

### Problemas solucionados pelo padrão

 1. Como as responsabilidades podem ser adicionadas dinamicamente a um objeto?
 1. Como a funcionalidade de um objeto pode ser estendida em tempo de execução?

### Benefícios

 1. Você pode estender o comportamento de um objeto sem criar uma nova subclasse.
 1. Você pode adicionar ou remover responsabilidades de um objeto em tempo de execução.
 1. Você pode combinar vários comportamentos envolvendo um objeto em vários decoradores.
 1. Princípio de responsabilidade única. Você pode dividir uma classe monolítica que implementa muitas variantes possíveis de comportamento em várias classes menores.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Como as responsabilidades podem ser adicionadas dinamicamente a um objeto? | Sim, pois a adição dinâmica de responsabilidades é uma realidade no escopo do projeto | 
| Como a funcionalidade de um objeto pode ser estendida em tempo de execução? | Sim, pois a extensão de funcionalidades durante o tempo de execução é pertinente ao projeto  |
---

## Facade

### O que é?

O Padrão Façade é do tipo estrutural. É usado quando um sistema é muito complexo ou difícil de entender, já que possui um grande número de classes independentes ou se trechos de código fonte estão indisponíveis. Este padrão esconde as complexidades de um sistema maior e provê uma interface simplificada ao cliente. Tipicamente envolve uma única classe responsável por englobar uma série de membros requeridos pelo cliente. Estes membros acessam o sistema em nome do Façade e escondem os detalhes de implementação. 

[![Exemplo](assets/exemplo_facade.png)](assets/exemplo_facade.png)

### Estrutura mínima

[![Diagrama](assets/facade.png)](assets/facade.png)

### Problemas solucionados pelo padrão

 1. Interface simples pode ser fornecida para um subsistema complexo.
 2. Evita acoplamento rígido entre clientes e objetos em um subsistema.

### Benefícios

 1. Você pode isolar seu código da complexidade de um subsistema.

 2. Controle de acesso aos serviços.

### Aplicável no Driblô?

O uso do facade é utilizado na API Gateway, onde os serviços são isolados e somente através dela é possível acessar os micros-serviços. Essa camada é responsável por validar e redirecionar as requisições entre o backend e o frontend evitando o acoplamento do sistema.

[![Exemplo](assets/facade_gate.png)](assets/facade_gateway.png)
---

## Flyweight

### O que é?

Flyweight é apropriado quando vários objetos devem ser manipulados em memória sendo que muitos deles possuem informações repetidas. Dado que o recurso de memória é limitado, é possível segregar a informação repetida em um objeto adicional que atenda as características de imutabilidade e comparabilidade (que consiga ser comparado com outro objeto para determinar se ambos carregam a mesma informação).

[![Exemplo](assets/exemplo_flyweight.png)](assets/exemplo_flyweight.png)

### Estrutura mínima

[![Diagrama](assets/flyweight.png)](assets/flyweight.png)

### Problemas solucionados pelo padrão

 1. Como um grande número de objetos refinados pode ser suportado com eficiência?

### Benefícios

 1. Você pode economizar muita memória RAM, assumindo que seu programa tenha vários objetos semelhantes.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 

(Dizer porque soluções são úteis ou não)

---

## Proxy

### O que é?

Proxy é um padrão estrutural que permite fornecer um substituto ou espaço reservado para outro objeto. Um proxy controla o acesso ao objeto original, permitindo que você execute algo antes ou depois que a solicitação chega ao objeto original.

[![Exemplo](assets/exemplo_proxy.png)](assets/exemplo_proxy.png)

### Estrutura mínima

[![Diagrama](assets/proxy.png)](assets/proxy.png)

### Problemas solucionados pelo padrão

 1. Como o acesso a um objeto pode ser controlado?
 1. Como funcionalidade adicional pode ser fornecida ao acessar um objeto?

### Benefícios

 1. Você pode controlar o objeto de serviço sem que os clientes saibam disso.
 1. Você pode gerenciar o ciclo de vida do objeto de serviço quando os clientes não se importam com isso.
 1. O proxy funciona mesmo que o objeto de serviço não esteja pronto ou não esteja disponível.
 1. Princípio Aberto / Fechado. Você pode introduzir novos proxies sem alterar o serviço ou os clientes.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Sim | 
| Problema 2 | Sim |

Elas interceptam os requests e os encaminham aos seus respectivos middlewares. O próprio middleware é capaz de realizar essas funcionalidades adicionais antes de encaminhar a rota.
O acesso a rotas é muito importante em qualquer aplicação, tendo em vista a necessidade de se acessar partes distintas da mesma, executando qualquer tarefa utilizando como base solicitação/resposta.

### Exemplo de aplicação no app Driblô

[![proxy](assets/padroes_gof/proxy_exemplo_driblo.png)](assets/padroes_gof/proxy_exemplo_driblo.png)


---

### Referências

[Wikipédia - Padrão de projeto de software](https://pt.wikipedia.org/wiki/Padr%C3%A3o_de_projeto_de_software)

[Wikipédia - Adapter](https://pt.wikipedia.org/wiki/Adapter)

[Wikipédia - Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)

[Refactoring Guru - Adapter](https://refactoring.guru/design-patterns/adapter)

[Wikipédia - Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)

[Refactoring Guru - Bridge](https://refactoring.guru/design-patterns/bridge)

[Wikipédia - Composite](https://pt.wikipedia.org/wiki/Composite)

[Refactoring Guru - Composite](https://refactoring.guru/design-patterns/composite)

[Wikipédia - Decorator](https://pt.wikipedia.org/wiki/Decorator)

[Refactoring Guru - Decorator](https://refactoring.guru/design-patterns/decorator)

[Wikipédia - Façade](https://pt.wikipedia.org/wiki/Fa%C3%A7ade)

[Wikipédia - Facade pattern](https://en.wikipedia.org/wiki/Facade_pattern)

[Refactoring Guru - Facade](https://refactoring.guru/design-patterns/facade)

[Wikipédia - Business_delegate](https://pt.wikipedia.org/wiki/Business_delegate)

[Wikipédia - Flyweight](https://pt.wikipedia.org/wiki/Flyweight)

[Refactoring Guru - Flyweight](https://refactoring.guru/design-patterns/flyweight)

[Wikipédia - Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)

[Refactoring Guru - Proxy](https://refactoring.guru/design-patterns/proxy)

[w3sDesign](http://w3sdesign.com/?gr=s02&ugr=proble#gf)
