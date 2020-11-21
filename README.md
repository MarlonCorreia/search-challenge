# Search Challenge 

This is my solutions for the search challenge. 

## Why two solutions? 

While looking at the specifications of the challenge, two really important knowledges came into my mind, **Data Structures** and **DataBase**. And I wanted to develop a little bit of both in this challenge. As the challenge description didn't specify the use of any techlonogies I felt it was a little bit of cheating using only `PostgreSQL`, since it has indexes and multi text search functions built in. So here are the differences:

- [Version_1](/version_1)- In memory Solution 

This versions has a focus on the use of clever data Structures that minimize loops when searching. In this solution I creating my version of a simple index systems with single and multiquery search. Since this uses an in memory solution I think it could never be a production version of search engine. 

- [Version_2](/version_2) - PostgreSQL Solution 

This version I decided to focus on the technologies that would actually find it's way to production in an actual search engine. I'm using postgreSQL with it's already weel develop and mature index and search systems. 


## The Problem 

Dentre as muitas responsabilidades do time que desenvolve o sistema de busca da Linx Impulse, duas delas são que as pesquisas que os usuários fazem nos sites de comércio eletrônico precisam ser respondidas de forma rápida com com qualidade. A velocidade está ligada ao tempo de processamento da consulta, enquanto que a qualidade está relacionada com a ordenação dos produtos de acordo com os interesses do usuário.

O desafio para esta vaga consiste em criar um processador de consultas que seja capaz de buscar um termo em um catálogo de produtos. O sistema deve ser feito usando a linguagem C++.

### Entrada

Fornecemos um catálogo de produtos em anexo ("catalogo_produtos.json") que é um arquivo que possui, em cada linha, um produto no formato JSON. Este JSON tem os seguintes campos:

```bash 
{
  "id": int, //Identificador do produto. Ex: 123456
  "name": "string", //Nome do produto, exemplo: "Notebook Asus 4GB RAM 500GB HD Core i3"
}
```

### Saida

O programa deverá esperar consultas serem enviadas via linha de comando e encontrar os produtos que são relacionadas com estas consultas. Limite a saída a, no máximo, 20 resultados ordenados por ID em ordem crescente.

```bash
> ./processador
> Digite aqui sua consulta: perfume
1 - "ID" - "Nome do Produto"
2 - "ID" - "Nome do Produto"
3 - "ID" - "Nome do Produto"
4 - "ID" - "Nome do Produto"
```

### O que será avaliado?

Será avaliada a capacidade do(a) candidato(a) no desenvolvimento do sistema quanto a:

- Padrão de código e boas práticas de desenvolvimento
- Estrutura de dados utilizada
- Eficiência do código implementado
- Organização do repositório
- Documentação do funcionamento do sistema e como o mesmo pode ser executado catalogo_produtos.json 




