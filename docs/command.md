# Command Pattern

### Histórico de versão
| Data | Versão | Descrição | Autor(es) |
| ---- | ------ | --------- | --------- |
| 20/10/2019 | 0.1 | Criação do documento | Samuel Borges |
| 20/10/2019 | 0.2 | Complementação dos topicos 1 e 4 | Marcelo Magalhães |
| 20/10/2019 | 0.3 | Pertinência em relação ao Driblô | Samuel Borges |

## Command

### O que é?

O command pattern é um Design Pattern comportamental no qual um objeto é usado para encapsular toda a informação necessária para realizar uma ação ou um evento em um momento posterior. Essas informações incluem o nome do Método, o Objeto a qual o método pertence, e os valores para os parâmetros do método.

Dessa forma o padrão Command encapsula uma solicitação vinculando um conjunto de ações em um receptor especifico. Para fazer isto ele precisa empacotar as ações e o receptor em um objeto que expõe um único método normalmente chamado execute(). Quando execute() é chamado ele invoca as ações no receptor. Externamente nenhum outro objeto sabe o que realmente será invocado ou mesmo em qual receptor.

### Estrutura mínima

![Command Pattern](assets/command_pattern.jpg)

### Problemas solucionados pelo padrão

 1. Como desacoplar o invocador de uma solicitação da solicitação em si? 
 1. Como emitir solicitações para objetos nada sabendo sobre a operação que está sendo solicitada ou sobre o receptor da mesma?

### Benefícios

 1. Separa o objeto que invoca a operação do objeto que "sabe como realizar" a operação.
 1. Evita necessidade conhecer os detalhes específicos de uma classe Receptora, tornando o código mais simples e desacoplado evitando amontoados no código.
 1. Facilita a adição de comandos novos, porque mudar as classes exitentes se torna desnecessário.
 1. Facilita o desfazimento (Undo) dos métodos chamados anteriormente. 
 1. Facilita a implementação de registros de ações executadas (logging) e sistemas transacionais.

### Aplicável no Driblô?

| Problema | Solução é útil ao Driblô? |
| ------- | :-----: |
| Usuário pode mudar de ideia em relação às informações passadas anteriormente.| Sim, pois facilitar a implementação de um sistema de desfazimento de ações seria bastante pertinente ao projeto. | 
| Projeto visa entregar o minimo produto viável e crescer conforme necessário. | Sim, pois facilitar a adição de comandos novos ajudaria no desenvolvimento. |


### Referências

[Wikipédia - Command Pattern](https://pt.wikipedia.org/wiki/Command_pattern)

[Wikipédia - Command Pattern - PTBR](https://pt.wikipedia.org/wiki/Command)

[GoFPatterns - Command Pattern](https://www.gofpatterns.com/behavioral-design-patterns/behavioral-patterns/command-pattern.php)

[DevMedia - Padrões de Projetos: Introdução aos Padrões Front Controller e Command](https://www.devmedia.com.br/padroes-de-projetos-introducao-aos-padroes-front-controller-e-command/30644)

[Source Making - Command Design Pattern](https://sourcemaking.com/design_patterns/command)

