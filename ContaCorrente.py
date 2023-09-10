class ContaCorrente:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo


    def getNumero(self):
        return self.__numero
    def setNumero(self, numero):
        self.__numero = numero


    def getTitular(self):
        return self.__titular
    def setTitular(self, titular):
        self.__titular = titular


    def getSaldo(self):
        return self.__saldo    
    def setSaldo(self, saldo):
        self.__saldo = saldo


    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultarSaldo(self):
        return self.__saldo
    

    def __str__(self):
        return "Conta: "+ str(self.__numero) + '\n' + 'Nome: ' + self.__titular + '\n' + 'Saldo: ' + str(self.__saldo)


#numero = input("Número da conta corrente: ")
#titular = input("Nome do titular da conta: ")
#saldo_inicial = float(input("Saldo inicial da conta: "))

conta_corrente = ContaCorrente(123, 'titular', 1000)
print(conta_corrente)


depositar = float(input('Valor que deseja depositar: '))
sacar = float(input('Valor que deseja sacar: '))

conta_corrente.depositar(depositar)
print("Saldo após depósito:", conta_corrente.consultarSaldo())

conta_corrente.sacar(sacar)
print("Saldo após saque:", conta_corrente.consultarSaldo())