from datetime import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        self.quantidade = quantidade

    def __str__(self):
        venc_formatado = self.data_vencimento.strftime("%d/%m/%Y")
        return f"{self.nome} (Qtd: {self.quantidade} | Vence: {venc_formatado})"
    
class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def __str__(self):
        return f"Aluno: {self.nome} | Curso: {self.curso}"