---
id: comportamental
title: GOF's Comportamentais
sidebar_label: GOF's Comportamentais
---

### Histórico de versão
| Data | Versão | Descrição | Autor(es) |
| ---- | ------ | --------- | --------- |
| 18/10/2019 | 0.1 | Criação do documento | Henrique Martins |
| 20/10/2019 | 0.2 | Adicionando imagens e benefícios para padrões | Henrique Martins |
| 23/10/2019 | 0.3 | Adição da introdução | Henrique Martins |
| 24/10/2019 | 0.4 | Adição Tópico Chain of Responsibility | Byron Kamal|
| 24/10/2019 | 0.5 | Adição da Viabilidade do Command Pattern| Samuel Borges e Rafael Teodosio |
| 24/10/2019 | 0.6 | Adição da Viabilidade do Iterator| Samuel Borges e Rafael Teodosio |
| 25/10/2019 | 0.7 | Adição da Viabilidade do Strategy| João Pedro Mota e Luís Cláudio T. Lima |
| 25/10/2019 | 0.8 | Adição da Viabilidade do Template Method| João Pedro Mota e Luís Cláudio T. Lima |
| 25/10/2019 | 0.9 | Adição da Viabilidade do Memento| João Pedro Mota e Luís Cláudio T. Lima |
| 25/10/2019 | 0.10 | Adição da Viabilidade do State| Marcelo Araújo |
| 25/10/2019 | 0.11 | Adição da Viabilidade do Visitor| Marcelo Araújo |
| 25/10/2019 | 0.11.2 | Correção do template do Memento, Strategy e Template Method| João Pedro Mota e Luís Cláudio T. Lima |

## Introdução
<p align="justify">
Os padrões comportamentais se concentram nos algoritmos e atribuições de responsabilidades entre os objetos. Eles não descrevem apenas padrões de classes ou de objetos, mas também os padrões de comunicação entre os objetos. Ao fazer isso, esses padrões aumentam a flexibilidade na realização dessa comunicação. Os padrões comportamentais de classes utilizam a herança para distribuir o comportamento entre classes, e os padrões de comportamento de objeto utilizam a composição de objetos em contrapartida a herança. Alguns descrevem como grupos de objetos cooperam para a execução de uma tarefa que não poderia ser executada por um objeto sozinho. Abaixo estão os padrões comportamentais.
</p>

---

## Chain of Responsibility

### O que é?

<br />

<p align="justify">
Chain of Responsibility é um padrão cuja principal função é evitar a dependência entre um objeto receptor e um objeto solicitante. Consiste em uma série de objetos receptores e de objetos de solicitação, onde cada objetos de solicitação possui uma lógica interna que separa quais são tipos de objetos receptores que podem ser manipulados. O restante é passado para o próximo objetos de solicitação da cadeia.
</p>

[![Exemplo](assets/exemplo_chain_of_responsibility.png)](assets/exemplo_chain_of_responsibility.png)

<br />

### Estrutura mínima

<br />

[![Diagrama](assets/chain_of_responsibility.png)](assets/chain_of_responsibility.png)

<br />

### Benefícios

<br />

 1. Reduz o grau de acoplamento. A dissociação solicitará o remetente e o destinatário.
 1. Objeto simplificado. O objeto não precisa conhecer a estrutura da cadeia.
 1. Aprimora a flexibilidade das tarefas atribuídas a objetos. Alterando os membros da cadeia ou alterando sua ordem, permita adicionar ou excluir responsabilidades dinamicamente.
 1. Aumenta a solicitação de processamento de nova classe de muito conveniente.

<br />

### Aplicável no Driblô?

<br />

<p align="justify">
 Está solução é aplicavél ao Driblô. 
 O caso de uso desse padrão no ecossistema do <strong>NodeJS</strong> é o <strong>middleware</strong> do <strong>ExpressJS</strong> Com esse padrão, é configurado uma cadeia de funções (middlewares) que avaliam o objeto de solicitação e decidem agir ou ignorá-lo.
 </p>

 <p align="justify">
 Middlewares são uma implementação específica desse padrão, pois, em vez de apenas um membro da cadeia atender à solicitação, pode-se argumentar que todos eles poderiam fazê-lo. Esse padrão trabalha assíncrona, onde, em vez de verificar se a função retorna um valor ou não, é verificado quais valores são passados ​​para o próximo callback que eles chamam. <br />
A seguir temos um trecho de código onde o <strong>middlaware</strong> é aplicado:
 </p>
<br />

[![Chain of Responsibility](assets/padroes_gof/exemplo_A_chain.png)](assets/padroes_gof/exemplo_A_chain.png)

<br/>

[![Chain of Responsibility](assets/padroes_gof/exemplo_B_chain.png)](assets/padroes_gof/exemplo_B_chain.png)

--------

## Command

### O que é?

Command é um padrão no qual um objeto é usado para encapsular toda informação necessária para executar uma ação ou acionar um evento em um momento posterior.

[![Exemplo](assets/exemplo_command.png)](assets/exemplo_command.png)

### Estrutura mínima


[![Diagrama](assets/command.png)](assets/command.png)

### Problemas solucionados pelo padrão

 1. Como o acoplamento de um pedido a um pedido pode ser evitado?
 1. Como um objeto pode ser configurado com uma solicitação?

### Benefícios

 1. Torna o código extensível, pois é possível adicionar novos comandos sem alterar o código existente.
 1. Reduz o acoplamento do invocador e receptor de um comando.

### Aplicável no Driblô?


| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Usuário pode mudar de ideia em relação às informações passadas anteriormente.| Sim, pois facilitar a implementação de um sistema de desfazimento de ações seria bastante pertinente ao projeto. | 
| Problema 2 |  |
| Projeto visa entregar o minimo produto viável e crescer conforme necessário. | Sim, pois facilitar a adição de comandos novos ajudaria no desenvolvimento. |

---

## Interpreter

### O que é?

Interpreter é um dos padrões de projeto de software, famosos como "Design Patterns", muito utilizado para a resolução de problemas quando a modelagem de sistemas ou softwares. Esse padrão esta incluso na categoria de Padrão Comportamental, ou seja, ele busca solucionar problemas de modelagem que tratam o comportamento de classes.

(Imagem de exemplo)

### Estrutura mínima

[![Diagrama](assets/interpreter.png)](assets/interpreter.png)

### Problemas solucionados pelo padrão

 1. Como pode ser definida uma gramática para um idioma simples para que as frases no idioma possam ser interpretadas?

### Benefícios

 1. É fácil alterar e estender a gramática. Como o padrão usa classes para representar regras gramaticais, você pode usar a herança para alterar ou estender a gramática. As expressões existentes podem ser modificadas incrementalmente, e novas expressões podem ser definidas como variações das antigas.
 1. A implementação da gramática também é fácil. As classes que definem nós na árvore de sintaxe abstrata têm implementações semelhantes. Essas classes são fáceis de escrever e geralmente sua geração pode ser automatizada com um compilador ou gerador de analisador.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Não |

As intenções e os problemas resolvidos pelo Interpreter não possuem nenhum benefício ao Driblô, portanto não será aplicado.

---

## Iterator

### O que é?

No Iterator um iterador é usado para percorrer um container e acessar seus elementos. O padrão Iterator desacopla os algoritmos dos recipientes, porém em alguns casos, os algoritmos são necessariamente específicos dos containers e, portanto, não podem ser desacoplados.

[![Exemplo](assets/exemplo_iterator.png)](assets/exemplo_iterator.png)

### Estrutura mínima

[![Diagrama](assets/iterator.png)](assets/iterator.png)

### Problemas solucionados pelo padrão

 1. Como os elementos de um objeto agregado podem ser acessados e percorridos sem expor sua representação subjacente?

### Benefícios

 1. Princípio de responsabilidade única. Você pode limpar o código do cliente e as coleções extraindo algoritmos volumosos volumosos em classes separadas.
 1. Princípio Aberto / Fechado. Você pode implementar novos tipos de coleções e iteradores e passá-los para o código existente sem quebrar nada.
 1. Você pode iterar sobre a mesma coleção em paralelo porque cada objeto iterador contém seu próprio estado de iteração.
 1. Pelo mesmo motivo, você pode atrasar uma iteração e continuar quando necessário.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Acessar e percorrer os elementos de um objeto sem expor sua representação subjacente.| Não é aplicável ao projeto pois a tecnologia utilizada para desenvolvimento já disponibiliza métodos que resolvem os problemas de natureza semelhante existentes. |

---

## Mediator

### O que é?

Mediador é um padrão de projeto usado frequentemente quando deseja-se encapsular como os objetos interagem, ou seja, a comunicação entre os objetos é estabelecida através do Mediator. Este padrão é considerado um padrão comportamental, pois o padrão pode alterar o comportamento da aplicação (programa).O Mediator promove o fraco acoplamento ao evitar que objetos se referiram uns aos outros explicitamente.

[![Exemplo](assets/exemplo_mediator.png)](assets/exemplo_mediator.png)

### Estrutura mínima

[![Exemplo](assets/mediator.png)](assets/mediator.png)


### Problemas solucionados pelo padrão

 1. Como evitar o acoplamento rígido entre um conjunto de objetos em interação?
 2. Como a interação entre um conjunto de objetos pode ser alterada independentemente?

### Benefícios

 1. Diminuí consideravelmente o acoplamento (entre os Colegas) e consequentemente aumenta o reuso.
 2. Ocorre a eliminação de relacionamentos muitos para muitos (N para N)
 3. A política de comunicações fica centralizada no Mediator, logo, podemos alterar essa política sem precisar alterar os Colegas. 

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Sim |
| Problema 2 | Sim |

O padrão ***Mediator*** foi implementado no serviço ***Driblo***, é um padrão de projeto que promove o acoplamento livre de objetos, removendo a necessidade das classes se comunicarem diretamente, este padrão foi muito útil para tratar a interação entre entidades.

***Trecho da controladora responsável pelo relacionamento entre jogador e pelada***

[![mediator userpelada](assets/mediator-exemplo2.png)](assets/mediator-exemplo2.png)

***Trecho da controladora responsável pelo relacionamento entre jogador e time***

[![mediator userpelada](assets/mediator-exemplo1.png)](assets/mediator-exemplo1.png)

Como pode ser observado, foi necessário a criação de uma controladora que possue o comportamento de mediador, e por sua vez, retira a responsabilidade de um objeto especifico em se relacionar com um ou mais objetos, deixando essa responsabilidade de interação com a controladora.

---

<br>

## Memento

### O que é?

Memento é um padrão de projeto de software documentado no Catálogo Gang of Four, sendo considerado como um padrão comportamental. Ele permite armazenar o estado interno de um objeto em um determinando momento, para que seja possível retorná-lo a este estado, sem que isso cause problemas com o encapsulamento.

[![Exemplo](assets/exemplo_memento.png)](assets/exemplo_memento.png)

### Estrutura mínima

[![Diagrama](assets/memento.png)](assets/memento.png)

### Problemas solucionados pelo padrão

 1. Sem violar o encapsulamento, como o estado interno de um objeto pode ser capturado e externalizado para que o objeto possa ser restaurado para esse estado posteriormente?

### Benefícios

 1. Você pode produzir snapshots do estado do objeto sem violar seu encapsulamento.
 1. Você pode simplificar o código do autor, deixando o responsável manter o histórico do estado do autor.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Sim |

Em vez de simplesmente retornar ao estado anterior, no Driblô o usaremos para realizar a criação de uma nova pelada, baseada nos dados de uma anterior do mesmo usuário.
Com o uso do Memento, torna-se possível o acesso a estados anteriores do objeto, no caso, a pelada, para que se possa criar uma nova com as mesmas preferências do usuário já definidas. 

---

## Observer

### O que é?

O Observer é um padrão de projeto de software que define uma dependência um-para-muitos entre objetos de modo que quando um objeto muda o estado, todos seus dependentes são notificados e atualizados automaticamente. Permite que objetos interessados sejam avisados da mudança de estado ou outros eventos ocorrendo num outro objeto.

[![Exemplo](assets/exemplo_observer.png)](assets/exemplo_observer.png)

### Estrutura mínima

[![Diagrama](assets/observer.png)](assets/observer.png)

### Problemas solucionados pelo padrão

 1. Como uma dependência de um para muitos entre objetos pode ser definida sem tornar os objetos fortemente acoplados?
 1. Como um objeto pode notificar um número ilimitado de outros objetos?

### Benefícios

 1. Princípio Aberto / Fechado.
 1. Você pode estabelecer relações entre objetos em tempo de execução.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  |
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## State

### O que é?

State é um padrão de projeto de software usado quando o comportamento de um objeto muda, dependendo do seu estado.

[![Exemplo](assets/exemplo_state.png)](assets/exemplo_state.png)

### Estrutura mínima

[![Diagrama](assets/state.png)](assets/observer.png)

### Problemas solucionados pelo padrão

 1. Como um objeto pode alterar seu comportamento quando seu estado interno muda?
 1. Como o comportamento específico do estado pode ser definido para que novos estados possam ser adicionados e o comportamento dos estados existentes possa ser alterado independentemente?

### Benefícios

 1. Princípio de responsabilidade única. Organize o código relacionado a estados específicos em classes separadas.
 1. Princípio Aberto / Fechado. Introduzir novos estados sem alterar as classes de estado existentes ou o contexto.
 1. Simplifique o código do contexto, eliminando condicionais volumosos da máquina de estado.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Sim |
| Problema 2 | Sim |

Solução útil pois o a aplicação trabalha com muitos estados, como por exemplo, a partida pode estar não inicializada, em andamento e finalizada, e o usuário estar logado ou não. O padrão state pode ser aplicado em muito deles para ter um controle melhor dos estados. 

---

## Strategy

### O que é?

O padrão Strategy é um padrão comportamental que permite selecionar um algoritmo em tempo de execução. Em vez de implementar um único algoritmo diretamente, o código recebe instruções em tempo de execução sobre as quais em uma família de algoritmos usar.

[![Exemplo](assets/exemplo_strategy.png)](assets/exemplo_strategy.png)

### Estrutura mínima

[![Diagrama](assets/strategy.png)](assets/strategy.png)

### Problemas solucionados pelo padrão

 1. Uma classe pode ser configurada com um algoritmo em tempo de execução, em vez de implementar um algoritmo diretamente

 2. Um algoritmo pode ser selecionado e trocado em tempo de execução.

### Benefícios

 1. Você pode trocar algoritmos usados dentro de um objeto em tempo de execução.
 1. Você pode isolar os detalhes de implementação de um algoritmo do código que o utiliza.
 1. Você pode substituir herança por composição.
 1. Princípio Aberto / Fechado. Você pode introduzir novas estratégias sem precisar alterar o contexto.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Sim  |
| Problema 2 | Sim |

O padrão ***Strategy*** foi implementado no serviço ***User*** do projeto, este padrão foi muito util para o calculo do ***Overall*** do jogador, visto que para cada tipo posição, o peso da das habilidades(velocidade, chute, defesa, passe, drible) variavam, então ao invés de criar uma enorme estrura condicional, o algoritmo escolhido para o calculo do ***Overall*** é definido em tempo de execução, isso tudo se deve a dinamicidade que o javascript proporciona na exportação de funcões.

***Trecho dos algoritmos para o cálculo do Overall - Antigo***

[![antes-overall](assets/antes-overall.png)](assets/strategy.png)

***Chamada do algoritmo para o calculo do Overall - Antigo***

[![antes-overall](assets/antes-overall-laco.png)](assets/strategy.png)

<br>

***Import dos algoritmos em apenas um objeto***

[![import-overall](assets/import-overall.png)](assets/import-overall.png)



***Trecho dos algoritmos para o cálculo do Overall - Refatorado***

[![depois-overall](assets/depois-overall.png)](assets/depois-overall.png)

***Chamada do algoritmo para o calculo do Overall - Refatorado***

[![antes-overall](assets/depois-overall-laco.png)](assets/depois-overall-laco.png)


Como pode ser observado, o arquivo que contém os algoritmos de calcular o overall, exporta suas funções mapeando cada uma delas com chave-valor, desse modo, a *controller* de usuário importa esse objeto e em tempo de execução invoca a função especifica passando como chave a posição do jogador.

---

## Template Method

### O que é?

O template method é um dos padrões de design comportamental. O template method é um método em uma superclasse, geralmente uma superclasse abstrata, e define o esqueleto de uma operação em termos de várias etapas de alto nível. Essas etapas são implementadas por métodos auxiliares adicionais na mesma classe que o template method.

[![Exemplo](assets/exemplo_template_method.png)](assets/exemplo_template_method.png)

### Estrutura mínima

[![Diagrama](assets/template_method.png)](assets/template_method.png)

### Problemas solucionados pelo padrão

 1. Como as partes invariantes de um comportamento podem ser implementadas uma vez para que as subclasses possam implementar as partes variantes?
 1. Como as subclasses podem redefinir certas partes de um comportamento sem alterar a estrutura do comportamento?

### Benefícios

 1. Você pode permitir que os clientes substituam apenas certas partes de um algoritmo grande, tornando-os menos afetados pelas alterações que acontecem com outras partes do algoritmo.
 1. Você pode colocar o código duplicado em uma superclasse.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Sim |
| Problema 2 | Sim |

Nas diversas criações no Driblô, como peladas ou jogadores, deve-se definir os campos que estão presentes nos formulários.Cada formulário de criação é único para cada objeto.
O Template method será útil na definição da ordem do preenchimento dos campos na criação. 

---

## Visitor

### O que é?

O padrão de design Visitor é uma maneira de separar um algoritmo de uma estrutura de objeto na qual ele opera. Um resultado prático dessa separação é a capacidade de adicionar novas operações às estruturas de objetos existentes sem modificar as estruturas.

[![Exemplo](assets/exemplo_visitor.png)](assets/exemplo_visitor.png)

### Estrutura mínima

[![Diagrama](assets/visitor.png)](assets/visitor.png)

### Problemas solucionados pelo padrão

 1. Como novas operações podem ser definidas para as classes de uma estrutura de objetos sem alterar as classes?

### Benefícios

 1. Princípio Aberto / Fechado. Você pode introduzir um novo comportamento que possa trabalhar com objetos de diferentes classes sem alterar essas classes.
 1. Princípio de responsabilidade única. Você pode mover várias versões do mesmo comportamento para a mesma classe.
 1. Um objeto visitante pode acumular algumas informações úteis ao trabalhar com vários objetos. Isso pode ser útil quando você deseja percorrer alguma estrutura complexa de objetos, como uma árvore de objetos, e aplicar o visitante a cada objeto dessa estrutura.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Não |

Não há necessidade de usar esse padrão de projeto pois a aplicação não é complexa o suficiente, e não vamos trabalhar com alguma estrutura complexa de objetos, segundo os requisitos levantados.

---

### Referências

[Wikipédia - Padrão de projeto de software](https://pt.wikipedia.org/wiki/Padr%C3%A3o_de_projeto_de_software)

[Source Making - Behavioral patterns](https://sourcemaking.com/design_patterns/behavioral_patterns)

[Wikipédia - Chain of Responsibility](https://pt.wikipedia.org/wiki/Chain_of_Responsibility)

[GeeksforGeeks - Chain of Responsibility](https://www.geeksforgeeks.org/chain-responsibility-design-pattern/)

[Refactoring Guru - Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)

[Wikipédia - Command](https://pt.wikipedia.org/wiki/Command)

[Source Making - Command Design Pattern](https://sourcemaking.com/design_patterns/command)

[Refactoring Guru - Command](https://refactoring.guru/design-patterns/command)

[Wikipédia - Interpreter](https://pt.wikipedia.org/wiki/Interpreter)

[Wikipédia - Interpreter pattern](https://en.wikipedia.org/wiki/Interpreter_pattern)

[GeeksforGeeks - Interpreter Design Pattern](https://www.geeksforgeeks.org/interpreter-design-pattern/)

[Wikipédia - Iterador](https://pt.wikipedia.org/wiki/Iterador)

[Wikipédia - Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern)

[Refactoring Guru - Iterator](https://refactoring.guru/design-patterns/iterator)

[Wikipédia - Mediator](https://pt.wikipedia.org/wiki/Mediator)

[Refactoring Guru - Mediator](https://refactoring.guru/design-patterns/mediator)

[Wikipédia - Memento (Informática)](https://pt.wikipedia.org/wiki/Memento_(inform%C3%A1tica))

[Source Making - Memento Design Pattern](https://sourcemaking.com/design_patterns/memento)

[Refactoring Guru - Memento](https://refactoring.guru/design-patterns/memento)

[Wikipédia - Observer](https://pt.wikipedia.org/wiki/Observer)

[Refactoring Guru - Observer](https://refactoring.guru/design-patterns/observer)

[Wikipédia - State](https://pt.wikipedia.org/wiki/State)

[Source Making - State Design Pattern](https://sourcemaking.com/design_patterns/state)

[Refactoring Guru - State](https://refactoring.guru/design-patterns/state)

[Wikipédia - Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)

[Refactoring Guru - Strategy](https://refactoring.guru/design-patterns/strategy)

[Wikipédia - Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern)

[Refactoring Guru - Template Method](https://refactoring.guru/design-patterns/template-method)

[Wikipédia - Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)

[Refactoring Guru - Visitor](https://refactoring.guru/design-patterns/visitor)

[w3sDesign](http://w3sdesign.com/?gr=s02&ugr=proble#gf)
