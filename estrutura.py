class No: # Usado pela Fila de Estoque
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

    def desenfileirar(self):
        if self.inicio is None: return None
        lote_removido = self.inicio.produto
        self.inicio = self.inicio.proximo
        if self.inicio is None: self.fim = None
        return lote_removido

# --- NOVA ESTRUTURA PARA PAGAMENTOS (LISTA LIGADA) ---

class NoVenda:
    def __init__(self, dados_venda):
        self.venda = dados_venda # Dicionário com: cliente, item, valor
        self.proximo = None

class ListaPagamento:
    def __init__(self):
        self.cabeca = None # Início da lista de registros

    def registrar_venda(self, dados_venda):
        novo_no = NoVenda(dados_venda)
        # Inserção no início (Lógica de Pilha para histórico recente)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no