from pprint import pprint


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.__nome = nome
        self.__cpf = cpf
        self.__profissao = profissao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao


class ContaCorrente:

    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__cliente = cliente
        self.__agencia = agencia
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def saldo(self):
        return self.__saldo

    def __set_saldo(self, saldo):
        if not isinstance(saldo, int):
            return

        if saldo <= 0:
            return

        self.__saldo = saldo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, agencia):
        if not isinstance(agencia, int):
            return

        if agencia <= 0:
            return

        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, numero):
        if not isinstance(numero, int):
            return

        if numero <= 0:
            return

        self.__numero = numero

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
            self.saldo += valor

conta_corrente = ContaCorrente(None, "00", "101")