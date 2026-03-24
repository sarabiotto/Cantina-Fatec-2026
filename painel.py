from produto import Produto, Aluno
from estrutura import FilaEstoque, ListaPagamento
from faker import Faker
import random

fake = Faker('pt_BR')
estoque_geral = {}
historico_vendas = ListaPagamento()
estatisticas_consumo = {} 

def adicionar_estoque(nome, p_c, p_v, venc, qtd):
    if nome not in estoque_geral:
        estoque_geral[nome] = FilaEstoque()
    novo_lote = Produto(nome, p_c, p_v, venc, qtd)
    estoque_geral[nome].enfileirar(novo_lote)

def realizar_venda(aluno, nome_prod, qtd_pedida):
    if nome_prod not in estoque_geral or estoque_geral[nome_prod].inicio is None:
        return

    fila = estoque_geral[nome_prod]
    total_recebido = 0
    
    while qtd_pedida > 0 and fila.inicio:
        lote = fila.inicio.produto
        qtd_disponivel = lote.get_quantidade()
        
        if qtd_disponivel <= qtd_pedida:
            unidades = qtd_disponivel
            qtd_pedida -= unidades
            fila.desenfileirar()
        else:
            unidades = qtd_pedida
            lote.set_quantidade(lote.get_quantidade() - unidades)
            qtd_pedida = 0
        total_recebido += unidades * lote.get_preco_venda()

    venda_info = {"cliente": aluno.get_nome(), "item": nome_prod, "valor": total_recebido}
    historico_vendas.registrar_venda(venda_info)

    estatisticas_consumo[nome_prod] = estatisticas_consumo.get(nome_prod, 0) + 1
    
    print(f"Venda OK: {aluno.get_nome()} comprou {nome_prod}")

def gerar_minimundo():
    print("\n GERANDO 10 VENDAS AUTOMÁTICAS COM FAKER...")
    
    # Cadastros iniciais
    adicionar_estoque("Torcida",1.8, 3.0, "20/05/2026", 50)
    adicionar_estoque("Coca-cola 200ml", 2.0, 3.0, "15/05/2026", 40)
    adicionar_estoque("Bombom", 0.8, 2.0, "10/05/2026", 30)

    cursos = ["IA", "ESG"]
    produtos = ["Torcida", "Coca-cola 200ml", "Bombom"]

    for _ in range(10):
        aluno_fake = Aluno(fake.name(), random.choice(cursos))
        prod_fake = random.choice(produtos)
        qtd_fake = random.randint(1, 3)
        realizar_venda(aluno_fake, prod_fake, qtd_fake)

def mostrar_relatorio():
    print("\n" + "="*35)
    print("      RELATÓRIO DE CONSUMO")
    print("="*35)
    
    if estatisticas_consumo:
        mais_vendido = max(estatisticas_consumo, key=estatisticas_consumo.get)
        print(f"Item mais consumido: {mais_vendido}")
        print(f"Frequência: {estatisticas_consumo[mais_vendido]} pedidos")
    else:
        print("Nenhuma venda realizada.")
    print("="*35)

if __name__ == "__main__":
    gerar_minimundo()
    mostrar_relatorio()