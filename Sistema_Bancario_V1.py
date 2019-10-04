class Cliente ():
    def __init__(self, nome, cpf, sexo):
        self.__nome = nome
        self.__cpf = cpf
        self.__sexo = sexo

        @property
        def nome (self):
            return self.nome
        @nome.setter
        def nome(self, nome):
            self.nome = nome

        @property
        def cpf (self):
            return self.cpf
        @cpf.setter
        def cpf (self, cpf):
            self.cpf = cpf

        @property
        def sexo(self):
            return self.sexo

        @sexo.setter
        def sexo(self, sexo):
            self.sexo = sexo


class Conta():
    def __init__(self, nro_conta, cliente, saldo, limite,):
        self.__nro_conta = nro_conta
        self.__cleinte = cliente
        self.__saldo = saldo
        self.__limite = limite

        @property
        def nro_conta (self):
            return self.__nro_conta
        @nro_conta.setter
        def nro_conta(self, nro_conta):
            self.__nro_conta = nro_conta

         @property
        def cliente (self):
             return self.__cleinte
         @cliente.setter
        def cliente(self, cliente):
             self.__cleinte  = cliente

         @property
        def saldo (self):
             return self.__saldo
         @saldo.setter
        def saldo(self, saldo):
             self.__saldo = saldo

         @property
        def limite (self):
             return self.__limite
         @limite.setter
        def limite(self, limite):
             self.__limite = limite

class Historico():
    def __init__(self, data_ciracao, lista_transacoes):
        self.__data_criacao = data_ciracao
        self.__lista_transacoes = lista_transacoes

    @property
    def data_criacao(self):
        return self.__data_criacao

    @data_criacao.setter
    def data_criacao(self, data_ciracao):
        self.__data_criacao = data_ciracao

    @property
    def lista_transacoes(self):
        return self.__lista_transacoes

    @lista_transacoes.setter
    def lista_transacoes(self, lista_transacoes):
        self.__lista_transacoes = lista_transacoes

     def impimir (self):
         for item in self.lista_transacoes
             print(item)

