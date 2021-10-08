from pytest import fixture, raises


from src.cliente import Cliente
from src.conta_corrente import ContaCorrente


class Test_Cliente:

    @fixture
    def joao(self):
        return Cliente("João", "111.111.111-11", "Programador" )

    @fixture
    def pedro(self):
        return Cliente("Pedro", "222.222.222-22", "Designer" )

    @fixture
    def agencia(self):
        return 1

    @fixture
    def numero_da_conta_joao(self):
        return 1

    @fixture
    def numero_da_conta_pedro(self):
        return 2

    def test_saldo_da_conta_deve_ser_100_reais_apos_a_criacao(self, joao, agencia, numero_da_conta_joao):

        conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
        assert conta.saldo == 100

    def test_numero_da_conta_joao_deve_ser_um_inteiro(self, joao, agencia):
        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, agencia, "001")

    def test_numero_da_conta_joao_deve_ser_maior_que_zero(self, joao, agencia, numero_da_conta_joao):
        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, agencia, 0)

        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, agencia, -7)

        conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
        assert conta.numero == numero_da_conta_joao

    def test_agencia_deve_ser_um_inteiro(self, joao, numero_da_conta_joao):
        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, "001", numero_da_conta_joao)

    def test_agencia_deve_ser_maior_que_zero(self, joao, agencia, numero_da_conta_joao):
        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, 0, numero_da_conta_joao)

        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, -7, numero_da_conta_joao)

        conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
        assert conta.agencia == agencia

    def test_saldo_deve_ser_inteiro(self, joao, agencia, numero_da_conta_joao):
        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
            conta.saldo = "45"

    def test_saldo_deve_ser_maior_que_zero(self, joao, agencia, numero_da_conta_joao):
        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
            conta.saldo = -80

    def test_valor_transferido_deve_ser_debitado_da_conta_de_origem(self, joao, agencia, numero_da_conta_joao, pedro, numero_da_conta_pedro):
        contaJoao = ContaCorrente(joao, agencia, numero_da_conta_joao)
        contaPedro = ContaCorrente(pedro, agencia, numero_da_conta_pedro)

        contaJoao.transferir(60, contaPedro)
        assert contaJoao.saldo == 40

    def test_valor_transferido_deve_ser_creditado_na_conta_de_destino(self, joao, agencia, numero_da_conta_joao, pedro, numero_da_conta_pedro):
        contaJoao = ContaCorrente(joao, agencia, numero_da_conta_joao)
        contaPedro = ContaCorrente(pedro, agencia, numero_da_conta_pedro)

        contaJoao.transferir(60, contaPedro)
        assert contaPedro.saldo == 160

    def test_sacar_deve_debitar_o_valor_da_conta(self, joao, agencia, numero_da_conta_joao):
        conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
        conta.sacar(80)
        assert conta.saldo == 20

    def test_nao_deve_sacar_se_o_valor_sacado_for_maior_que_o_valor_da_conta(self, joao, agencia, numero_da_conta_joao):
        with raises(ValueError) as excecao:
            conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
            conta.sacar(180)

    def test_depositar_deve_acrescentar_o_valor_ao_saldo_da_conta(self, joao, agencia, numero_da_conta_joao):
        conta = ContaCorrente(joao, agencia, numero_da_conta_joao)
        conta.depositar(80)
        assert conta.saldo == 180

