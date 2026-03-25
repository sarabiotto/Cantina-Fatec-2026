from produto import Produto, Consumidor
from estrutura import FilaEstoque, ListaPagamento
from faker import Faker
import random
from datetime import datetime
import pickle
import os

fake = Faker('pt_BR')
estoque_geral = {}
historico_vendas = ListaPagamento()
estatisticas_consumo = {} 

def adicionar_estoque(nome, p_c, p_v, d_compra, venc, qtd):
    if nome not in estoque_geral:
        estoque_geral[nome] = FilaEstoque()
    novo_lote = Produto(nome, p_c, p_v, d_compra, venc, qtd)
    estoque_geral[nome].enfileirar(novo_lote)

def realizar_venda(consumidor, nome_prod, qtd_pedida):
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

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    venda_info = {
        "cliente": consumidor.get_nome(),
        "categoria": consumidor.get_categoria(),
        "curso": consumidor.get_curso(),
        "item": nome_prod, 
        "valor": total_recebido,
        "data_hora": agora
    }
    historico_vendas.registrar_venda(venda_info)

    estatisticas_consumo[nome_prod] = estatisticas_consumo.get(nome_prod, 0) + 1
    
    print(f"Venda OK: {consumidor.get_nome()} ({consumidor.get_categoria()}) comprou {nome_prod} - R${total_recebido:.2f}")

def gerar_minimundo():
    print("\n GERANDO 10 VENDAS AUTOMÁTICAS COM FAKER...")
    
    adicionar_estoque("Torcida", 1.8, 3.0, "01/03/2026", "20/05/2026", 50)
    adicionar_estoque("Coca-cola 200ml", 2.0, 3.0, "01/03/2026", "15/05/2026", 40)
    adicionar_estoque("Bombom", 0.8, 2.0, "01/03/2026", "10/05/2026", 30)

    cursos = ["IA", "ESG"]
    categorias = ["aluno", "servidor", "professor"]
    produtos = ["Torcida", "Coca-cola 200ml", "Bombom"]

    for _ in range(10):
        consumidor_fake = Consumidor(fake.name(), random.choice(categorias), random.choice(cursos))
        prod_fake = random.choice(produtos)
        qtd_fake = random.randint(1, 3)
        realizar_venda(consumidor_fake, prod_fake, qtd_fake)

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

def salvar_dados():
    dados = {
        'estoque': estoque_geral,
        'vendas': historico_vendas,
        'estatisticas': estatisticas_consumo
    }
    
    with open('dados_cantina.pkl', 'wb') as arquivo:
        pickle.dump(dados, arquivo)
    
    print("\n[Sistema] Dados salvos com sucesso no arquivo 'dados_cantina.pkl'!")

def carregar_dados():
    global estoque_geral, historico_vendas, estatisticas_consumo
    
    if os.path.exists('dados_cantina.pkl'):
        with open('dados_cantina.pkl', 'rb') as arquivo:
            dados = pickle.load(arquivo)
            
            estoque_geral = dados['estoque']
            historico_vendas = dados['vendas']
            estatisticas_consumo = dados['estatisticas']
            
        print("[Sistema] Dados carregados com sucesso!\n")
    else:
        print("[Sistema] Nenhum arquivo de dados anterior encontrado. Iniciando sistema limpo.\n")

if __name__ == "__main__":
    carregar_dados()
    
    if not estoque_geral:
        gerar_minimundo()
        
    mostrar_relatorio()
    
    salvar_dados()