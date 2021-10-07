from pytest import fixture

from src.cliente import Cliente
from src.conta_corrente import ContaCorrente


class Test_Cliente:

    @fixture
    def joao(self):
        return Cliente("João", "111.111.111-11", "Programador" )

    @fixture
    def agencia(self):
        return 1

    @fixture
    def conta(self):
        return 1

    def test_saldo_da_conta_deve_ser_100_reais_apos_a_criacao(self, joao, agencia, conta):

        conta = ContaCorrente(joao, agencia, conta)

        assert conta.saldo == 100

        assert conta.saldo == 200, "o saldo deveria ser maior"