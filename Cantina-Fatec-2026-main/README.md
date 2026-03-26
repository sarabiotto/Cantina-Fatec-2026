#Projeto Cantina Fatec 2026

Um sistema de gerenciamento de estoque e vendas desenvolvido em Python para a cantina da faculdade. Este projeto foi criado como parte das disciplinas de **Estrutura de Dados** e **Linguagem de Programação 2**.

## Sobre o Projeto
O objetivo do sistema é controlar o estoque de produtos perecíveis e registrar os pagamentos dos consumidores (alunos, professores e servidores). Para aplicar os conceitos da disciplina, o núcleo do sistema foi construído utilizando **estruturas de dados customizadas** (Nós, Listas Encadeadas e Filas), sem o uso das estruturas nativas do Python.

##  Funcionalidades
* **Controle de Estoque (FIFO):** Os produtos são gerenciados em uma Fila, garantindo que os lotes mais antigos sejam vendidos primeiro.
* **Registro de Vendas:** As vendas são salvas em uma Lista Encadeada (Lista de Pagamentos), registrando nome, categoria, curso, valor e data/hora.
* **Persistência de Dados:** O sistema salva e carrega os dados automaticamente usando a biblioteca `pickle`, para não perder nenhuma informação quando for fechado.
* **Geração de Dados Fake:** Criação rápida de um cenário de testes com 10 vendas automáticas utilizando a biblioteca `Faker`.
* **Relatórios:** Exibição do item mais consumido e estatísticas de vendas.

## Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Paradigma:** Orientação a Objetos (POO)
* **Bibliotecas:** `datetime`, `pickle`, `os`, `random` e `faker`
