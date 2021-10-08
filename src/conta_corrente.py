from src.exceptions import SaldoInsuficienteError
from src.cliente import Cliente


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__cliente = None
        self.__saldo = 100
        self.__agencia =0
        self.__numero = 0
        self.__saques_nao_permitidos = 0


        self.__set_cliente(cliente)
        self.__set_agencia(agencia)
        self.__set_numero(numero)

        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30/ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O atributo agencia deve ser um inteiro", valor)
        if valor <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")

        self.__agencia = valor


    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O atributo número deve ser um inteiro")
        if valor <= 0:
            raise ValueError("O atributo número  deve ser maior que zero")
        self.__numero = valor


    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O atributo saldo deve ser um inteiro")
        if valor < 0:
            raise SaldoInsuficienteError("",saldo=self.saldo, valor=valor)
        self.__saldo = valor


    @property
    def cliente(self):
        return self.__cliente

    def __set_cliente(self, cliente):
        if(cliente is None):
            raise ValueError("O cliente deve ser informado")
        self.__cliente = cliente

    @property
    def saques_nao_permitidos(self):
        return self.__saques_nao_permitidos

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)
        self.sacar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero.")
        if self.saldo < valor:
            self.__saques_nao_permitidos += 1
            raise SaldoInsuficienteError("", saldo=self.saldo, valor=valor)
        self.saldo -= valor

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser depositado não pode ser menor que zero.")
        self.saldo += valor