# GOF's Criacionais

### Histórico de versão
| Data | Versão | Descrição | Autor(es) |
| ---- | ------ | --------- | --------- |
| 18/10/2019 | 0.1 | Criação do documento | Henrique Martins |

## Introdução

(Acrescentar)

---

## Abstract Factory

### O que é?

Este padrão permite a criação de famílias de objetos relacionados ou dependentes por meio de uma única interface e sem que a classe concreta seja especificada. Uma fábrica é a localização de uma classe concreta no código em que objetos são construídos.

(Imagem)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Como um aplicativo pode ser independente de como seus objetos são criados?
 1. Como uma classe pode ser independente de como os objetos que ela exige são criados?
 1. Como as famílias de objetos relacionados ou dependentes podem ser criadas?

### Benefícios

 1. Isolamento de classes concretas
 1. Troca fácil de famílias de produtos
 1. Promove consistência entre produtos

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |
| Problema 3 |  |

(Dizer porque soluções são úteis ou não)

---

## Builder

### O que é?

Builder é um padrão criacional que permite a separação da construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes representações.

(Imagem de exemplo)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Como uma classe (o mesmo processo de construção) pode criar representações diferentes de um objeto complexo?
 1. Como uma classe que inclui a criação de um objeto complexo pode ser simplificada?

### Benefícios

 1. Permite variar a representação interna de um produto.
 1. Encapsula código para construção e representação.
1. Fornece controle sobre as etapas do processo de construção.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Factory Method

### O que é?

Factory Method é um padrão de projeto de software que permite às classes delegar para subclasses decidirem, isso é feito através da criação de objetos que chamam o método fabrica especificado numa interface e implementado por um classe filha ou implementado numa classe abstrata e opcionalmente sobrescrito por classes derivadas.

(Imagem de exemplo)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Problema 1
 1. Problema 2

### Benefícios

 1. Permite a construção de classes com um componente de um tipo que não foi predeterminado, mas definido apenas em uma "interface" ou definido como um tipo dinâmico.
 1. Permite a construção de subclasses para um pai cujo tipo de componente não foi predeterminado, mas definido apenas em uma interface ou definido como um tipo dinâmico.
 1. Permite um código mais legível nos casos em que existem vários construtores, cada um por um motivo diferente.
 1. Permite que uma classe adie a instanciação para subclasses e evite a instanciação direta de um objeto do tipo de classe pai.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Object pool

### O que é?

(Descrição do padrão)

(Imagem de exemplo)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Problema 1
 1. Problema 2

### Benefícios

 1. Benefício 1
 1. Benefício 2

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Prototype

### O que é?

Prototype é um padrão de projeto de software criacional que permite a criação de novos objetos a partir de um modelo original ou protótipo que é clonado.

(Imagem de exemplo)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Como os objetos podem ser criados para que os objetos a serem criados possam ser especificados em tempo de execução?
 1. Como as classes carregadas dinamicamente podem ser instanciadas?

### Benefícios

 1. Benefício 1
 1. Benefício 2

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |

(Dizer porque soluções são úteis ou não)

---

## Singleton

### O que é?

Singleton é um padrão de projeto de software que garante a existência de apenas uma instância de uma classe, mantendo um ponto global de acesso ao seu objeto.

(Imagem de exemplo)

### Estrutura mínima

(Imagem da estrutura mínima do padrão)

### Problemas solucionados pelo padrão

 1. Como é possível garantir que uma classe tenha apenas uma instância?
 1. Como a instância única de uma classe pode ser acessada facilmente?
 1. Como uma classe pode controlar sua instanciação?
 1. Como o número de instâncias de uma classe pode ser restrito?

### Benefícios

 1. Benefício 1
 1. Benefício 2

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Problema 1 |  | 
| Problema 2 |  |
| Problema 3 |  | 
| Problema 4 |  |

(Dizer porque soluções são úteis ou não)

---

### Referências

[Wikipédia - Abstract Factory](https://pt.wikipedia.org/wiki/Abstract_Factory)

[GeeksforGeeks - Abstract Factory Pattern](https://www.geeksforgeeks.org/abstract-factory-pattern/)

[Wikipédia - Abstract factory pattern](https://en.wikipedia.org/wiki/Abstract_factory_pattern)

[Wikipédia - Builder](https://pt.wikipedia.org/wiki/Builder)

[Wikipédia - Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)

[Wikipédia - Factory Method](https://pt.wikipedia.org/wiki/Factory_Method)

[Wikipédia - Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)

[Wikipédia - Prototype](https://pt.wikipedia.org/wiki/Prototype)

[Wikipédia - Prototype pattern](https://en.wikipedia.org/wiki/Prototype_pattern)

[Wikipédia - Singleton](https://pt.wikipedia.org/wiki/Singleton)

[Wikipédia - Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern)