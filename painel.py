from produto import Produto, Aluno
from estrutura import FilaEstoque


estoque_geral = {}

def adicionar_estoque(nome, preco_c, preco_v, vencimento, qtd):
    if nome not in estoque_geral:
        estoque_geral[nome] = FilaEstoque()
    
    novo_lote = Produto(nome, preco_c, preco_v, vencimento, qtd)
    estoque_geral[nome].enfileirar(novo_lote)

def realizar_venda(aluno, nome_produto, qtd_desejada):
    if nome_produto not in estoque_geral or estoque_geral[nome_produto].inicio is None:
        print(f"Erro: Não temos {nome_produto} no estoque!")
        return

    print(f"\n ATENDENDO: {aluno.nome} ({aluno.curso})")
    print(f"Pedido: {qtd_desejada} unidades de {nome_produto}")
    
    fila = estoque_geral[nome_produto]
    total_venda = 0
    
    while qtd_desejada > 0 and fila.inicio is not None:
        lote_atual = fila.inicio.produto
       
        if lote_atual.quantidade <= qtd_desejada:
            unidades_retiradas = lote_atual.quantidade
            qtd_desejada -= unidades_retiradas
            fila.desenfileirar()
        else:
            unidades_retiradas = qtd_desejada
            lote_atual.quantidade -= unidades_retiradas
            qtd_desejada = 0
            
        total_venda += unidades_retiradas * lote_atual.preco_venda

    if qtd_desejada > 0:
        print(f"Atenção: Estoque insuficiente! Faltaram {qtd_desejada} un.")
    
    print(f"Valor Total: R$ {total_venda:.2f}")
    print(f"Venda registrada para {aluno.nome} com sucesso!")

    #  TESTANDO 

aluno1 = Aluno("Sara", "IA")
aluno2 = Aluno("João", "ESG")

adicionar_estoque("Coxinha", 3.00, 6.00, "20/03/2026", 10)
realizar_venda(aluno1, "Coxinha", 5)


