from datetime import datetime

class Produto:
    def __init__(self, nome, preco_c, preco_v, vencimento, qtd):
        # Atributos Privados (Encapsulados com __)
        self.__nome = nome
        self.__preco_c = preco_c
        self.__preco_v = preco_v
        self.__vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
        self.__quantidade = qtd

    # --- GETTERS (Para ler os dados) ---
    def get_nome(self):
        return self.__nome

    def get_preco_venda(self):
        return self.__preco_v

    def get_preco_compra(self):
        return self.__preco_c

    def get_vencimento(self):
        return self.__vencimento

    def get_quantidade(self):
        return self.__quantidade

    # --- SETTERS (Para alterar os dados com segurança) ---
    def set_quantidade(self, nova_qtd):
        if nova_qtd >= 0:
            self.__quantidade = nova_qtd
        else:
            print(f"❌ Erro: Quantidade inválida para o produto {self.__nome}")

class Aluno:
    def __init__(self, nome, curso):
        self.__nome = nome
        self.__curso = curso

    def get_nome(self):
        return self.__nome

    def get_curso(self):
        return self.__curso