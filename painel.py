from produto import Produto
from estrutura import FilaEstoque

estoque_coxinha = FilaEstoque()
lote1 = Produto("Coxinha", 3.00, 6.00, "20/03/2026", 10)
lote2 = Produto("Coxinha", 3.00, 6.00, "25/03/2026", 20)
estoque_coxinha.enfileirar(lote1)
estoque_coxinha.enfileirar(lote2)
print(f"O produto mais velho no estoque é: {estoque_coxinha.inicio.produto}")