class No:
    def __init__(self, produto):
        self.produto = produto  
        self.proximo = None    
class FilaEstoque:
    def __init__(self):
        self.inicio = None 
        self.fim = None   

    def enfileirar(self, produto):
        novo_no = No(produto)
        
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        print(f"Lote de {produto.nome} entrou no estoque!")