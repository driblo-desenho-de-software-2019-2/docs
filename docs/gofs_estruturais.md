# GOF's Estruturais

### Histórico de versão
| Data | Versão | Descrição | Autor(es) |
| ---- | ------ | --------- | --------- |
| 18/10/2019 | 0.1 | Criação do documento | Henrique Martins |
| 25/10/2019 | 0.2 | Adição viabilidade do modelo Composite ao projeto | Luís Cláudio T. Lima e João Pedro Mota|

## Introdução

(Acrescentar)

---

## Adapter

### O que é?

O padrão do adaptador é um padrão de design de software que permite que a interface de uma classe existente seja usada como outra interface. É frequentemente usado para fazer com que as classes existentes funcionem com outras pessoas sem modificar seu código-fonte.

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Como uma classe pode ser reutilizada que não possui uma interface que um cliente exige?
 1. Como as classes que possuem interfaces incompatíveis podem trabalhar juntas?
 1. Como uma interface alternativa pode ser fornecida para uma classe?

### Benefícios

 1. A
 1. B

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |
| Problema 3 |  |

(Dizer porque soluções são úteis ou não)

---

## Bridge

### O que é?

O Bridge é um padrão de design destinado a "desacoplar uma abstração de sua implementação, para que os dois possam variar independentemente". O Bridge usa encapsulamento, agregação e pode usar herança para separar responsabilidades em diferentes classes.

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. A
 1. B

### Benefícios

 1. A
 1. B

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

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Como uma hierarquia parte-todo pode ser representada para que os clientes possam tratar objetos individuais e composições de objetos de maneira uniforme?

### Benefícios

 1. Você pode trabalhar com estruturas de árvores complexas de maneira mais conveniente: use polimorfismo e recursão a seu favor.
 1. Princípio Aberto / Fechado. Você pode introduzir novos tipos de elementos no aplicativo sem quebrar o código existente, que agora funciona com a árvore de objetos.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 | Durante a partida, os times, formados por jogadores, serão afetados uniformemente pelo resultado da mesma. | 

A partir do uso do Composite, espera-se que se torne mais simples a manipulação dos jogadores em relação as suas estatísticas de partidas (vitórias e derrotas).

---

## Decorator

### O que é?

Decorator é um padrão de projeto que permite adicionar um comportamento a um objeto já existente em tempo de execução, ou seja, agrega dinamicamente responsabilidades adicionais a um objeto. Decorators oferecem uma alternativa flexível ao uso de herança para estender uma funcionalidade, com isso adiciona-se uma responsabilidade ao objeto e não à classe.

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. A
 1. B

### Benefícios

 1. A
 1. B

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Facade

### O que é?

O Padrão Façade é do tipo estrutural . É usado quando um sistema é muito complexo ou difícil de entender, já que possui um grande número de classes independentes ou se trechos de código fonte estão indisponíveis. Este padrão esconde as complexidades de um sistema maior e provê uma interface simplificada ao cliente. Tipicamente envolve uma única classe responsável por englobar uma série de membros requeridos pelo cliente. Estes membros acessam o sistema em nome do Façade e escondem os detalhes de implementação. 

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. A
 1. B

### Benefícios

 1. A
 1. B

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Business Delegate

### O que é?

Business é usado para separar a camada de apresentação/externa das regras/lógicas de negócio. A razão para utilizar essa abordagem é reduzir o acoplamento entre as camadas, porque o alto acoplamento pode causar vários problemas no projeto.

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. A
 1. B

### Benefícios

 1. A
 1. B

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Flyweight

### O que é?

Flyweight é apropriado quando vários objetos devem ser manipulados em memória sendo que muitos deles possuem informações repetidas. Dado que o recurso de memória é limitado, é possível segregar a informação repetida em um objeto adicional que atenda as características de imutabilidade e comparabilidade (que consiga ser comparado com outro objeto para determinar se ambos carregam a mesma informação).

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. A
 1. B

### Benefícios

 1. A
 1. B

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Proxy

### O que é?

Texto

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. A
 1. B

### Benefícios

 1. A
 1. B

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

### Referências

[Wikipédia - Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern)

[Wikipédia - Bridge pattern](https://en.wikipedia.org/wiki/Bridge_pattern)

[Wikipédia - Composite](https://pt.wikipedia.org/wiki/Composite)

[Wikipédia - Decorator](https://pt.wikipedia.org/wiki/Decorator)

[Wikipédia - Façade](https://pt.wikipedia.org/wiki/Fa%C3%A7ade)

[Wikipédia - Business_delegate](https://pt.wikipedia.org/wiki/Business_delegate)

[Wikipédia - Flyweight](https://pt.wikipedia.org/wiki/Flyweight)
