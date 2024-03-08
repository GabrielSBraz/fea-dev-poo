import random  # Importando a biblioteca random

class ContaCorrente:
    # função __init__ é chamada automaticamente quando um objeto é criado a partir da sua respectiva classe
    def __init__(self, nome: str, renda_mensal: float):
        """ A função __init__ recebe os parâmetros necessários (atributos)
        para a criação do objeto, nesse caso, nome e renda mensal, e gera um ID aleatório."""

        # Abaixo os atributos: ID, nome, renda mensal e saldo da conta corrente
        self.id_cliente = random.randint(10000, 99999)  # Gera um ID aleatório entre 10000 e 99999
        self.nome = nome
        self.renda_mensal = renda_mensal
        self.saldo = 200  # Saldo inicial é R$200

    # Abaixo o método depósito, representando o comportamento de depositar um valor na conta corrente
    def deposito(self, quantidade: float):
        """ Nessa função (método), o cliente conseguirá depositar dinheiro em sua conta """
        self.saldo += quantidade  # O saldo do cliente aumentará
        return f'Depósito de: R${quantidade}. Saldo atual: {self.saldo}'

    # Abaixo o método saque, representando o comportamento de sacar um valor da conta corrente
    def saque(self, quantidade: float):
        """Nesse método, o cliente poderá sacar dinheiro da própria conta"""
        if self.saldo - quantidade < 0:
            raise Exception('Saldo insuficiente, tente novamente')
        else:
            self.saldo -= quantidade  # o saldo do cliente diminuirá
            return f'Saque de R${quantidade}. Saldo atual: {self.saldo}'