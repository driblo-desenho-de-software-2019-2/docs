---
id: plano-gcs
title: Plano de Gestão e Configuração de Software
sidebar_label: Plano de GCS
---
<br>

## Histórico de Revisão


| Data | Versão | Descrição | Autor(es) |
|:--:|:--:|:--:|:--:|
| 6/09/2019 | 0.1 | Criação do Documento e adição dos tópicos Introdução, Políticas de commit | Matheus Rodrigues |
| 6/09/2019 | 0.2 | adição do políticas de branch | Matheus Rodrigues |

## 1. Introdução


<p align = "justify">O presente documento tem como finalidade orientar a todos que buscam contribuir com o repositório, apresentando padrões, políticas, ferramentas, instruindo sobre o ambiente de desenvolvimento e qualquer atividade de configuração necessária.</p>

## 2. Políticas
  

### 2.1 Política de Commits
  

<p align = "justify">Os <i>commits</i> devem ser atômicos e seu comentário deve descrevê-lo de forma sucinta. O texto deve descrever o que foi produzido, de forma resumida e em português. Caso o <i>commits</i> não seja destinado para a conclusão da funcionalidade ou documento, deve-se iniciar com o verbo no gerúndio, no entanto, se o <i>commits</i> é destinado a conclusão da funcionalidade ou documento, deve-se iniciar com o verbo no particípio. Além disso, deve conter o número de sua <i>issue</i> correspondente, no seguinte formato:
  
**Repositorio de Documentação**
  
```[#<id da issue>] <Texto começando com letra maiúscula, verbo no gerúndio ou particípio, terminando com ponto final>.```

**Exemplo:**

***<i>commit</i> destinado à conclusão***

```[#1] Criado documento de arquitetura.```

***<i>commit</i> não destinado à conclusão***
  
```[#1] Criando documento de arquitetura.```

**Outros Repositórios**

```[<Tag da issue>] <Texto começando com letra maiúscula, verbo no gerúndio ou particípio, terminando com ponto final>.```

**Exemplo:**

***<i>commit</i> destinado à conclusão***

```[US00] Criada estrutura de usuário.```

***<i>commit</i> não destinado à conclusão***

```[US00] Criando estrutura de usuário.```


### 2.2 Política de Branches


Serão utilizados os princípios do **Gitflow** que ajudarão no controle do que está sendo produzido pela a equipe, onde, ao mesmo tempo falhas serão corrigidas, novas funcionalidades serão implementadas, garantindo o funcionamento do código de produção. O **Gitflow** foi criado em 2010, é considerado um ótimo modelo de <i>branching</i>. É um modelo fortemente baseado em branches, mas focados em entregas de projetos, ele define os papéis de cada branch e como elas devem interagir. Apesar dele ser um pouco mais complexo que outros workflows, ele disponibiliza um framework robusto para gerenciar projetos mais complexos.

<p align = "justify">A <i>master</i> será a <i>branch</i> estável do projeto, sendo ela proveniente da <i>develop</i> por meio de aprovação de <i>pull request</i> ao fim de cada <i>release</i>. Nenhum membro será autorizado a fazer <i>commits</i> diretamente na <i>master</i> ou na <i>develop</i>.</p>  

<p align = "justify">As <i>branches</i> auxiliares são destinadas a implementação de funcionalidades, realização de histórias técnicas e conserto de <i>bugs</i>. Cada uma dessas atividades terá sua própria <i>branch</i>, criada a partir da <i>develop</i>, as <i>Hotfix</i> são as branches criadas a partir da master e servem para resolver de forma rápida, os bugs em produção. Terão como padrão de nomenclatura: </p>
  

``` <Identificador da atividade>-<Nome issue associada a atividade>```

**Exemplos:**

```feature/TS03-Configurar-Ambientes```

```hotfix/BUG-Duplicação-no-Banco```

```feature/US01-Implementar-Login```
  
<p align = "justify">Após o fim do desenvolvimento nas <i>branches</i> auxiliares elas devem ser incorporadas a <i>develop</i> por meio de <i>pull request</i>.</p>

## Referências


> PMI. *Um guia do conhecimento em gerenciamento de projetos.* Guia PMBOK® 5a. ed. - EUA: Project Management Institute, 2013

> Semantic Versioning 2.0.0 . Semantic Versioning Specification (SemVer). Disponível em <[http://semver.org/](http://semver.org/)>

> **PlataformaJogosUnB**. Plano de Gerenciamento de Configuração de Software. Disponível em <[https://github.com/fga-gpp-mds/2017.1-PlataformaJogosUnB/wiki/Plano-de-Gerenciamento-de-Configura%C3%A7%C3%A3o-de-Software](https://github.com/fga-gpp-mds/2017.1-PlataformaJogosUnB/wiki/Plano-de-Gerenciamento-de-Configura%C3%A7%C3%A3o-de-Software)>

  
