class ContaBancaria:
    def __init__(self, nomeCliente, numConta, agencia, saldo):
        self.__nomeCliente = nomeCliente
        self.__numConta = numConta
        self.__agencia = agencia
        self.__saldo = saldo


    def getConta(self):
        return self.__numConta
    def setConta(self, numConta):
        self.__numConta = numConta


    def getCliente(self):
        return self.__nomeCliente
    def setCliente(self, nomeCliente):
        self.__nomeCliente = nomeCliente

    def getAgencia(self):
        return self.__agencia
    def setAgencia(self, agencia):
        self.__agencia = agencia


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
        return "Conta: "+ str(self.__numConta) + '\n' + 'Nome: ' + str(self.__nomeCliente) + '\n' + 'Agencia: ' + str(self.__agencia) + '\n' + 'Saldo: ' + str(self.__saldo)


class ContaPoupanca(ContaBancaria):
    def __init__(self, nomeCliente, numConta, agencia, saldo, diaRendimento, taxaRendimento):
        super().__init__(nomeCliente, numConta, agencia, saldo)
        self.diaRendimento = diaRendimento
        self.taxaRendimento = taxaRendimento
    

    def calcularNovoSaldo(self, diaAtual):
        if diaAtual == self.diaRendimento:
            self.setSaldo (self.getSaldo() * (1 + self.taxaRendimento / 100))
            print('Rendimento de R$ ' + self.getSaldo() + 'aplicado.')
    
    def __str__(self):
        return super().__str__() + f"\nDia rendimento: {self.diaRendimento}\nTaxa rendimento: {self.taxaRendimento}"
    

class ContaEspecial(ContaBancaria):
    def __init__(self, nomeCliente, numConta, agencia, saldo, valorLimite):
        super().__init__(nomeCliente, numConta, agencia, saldo)
        self.valorLimite = valorLimite

    def __str__(self):
        return super().__str__() + f'\nValor Limite: {self.valorLimite}'
    def sacar(self, valor):
        if valor <= self.getSaldo() + self.valorLimite:
            self.setSaldo(self.getSaldo() - valor)
            print('Saque de R$ ' + valor + 'realizado.')
        else:
            print('Limite Saque excedido.')


contaB = ContaBancaria("João Batista", "12345-99", '001', 1000)
print(contaB)
contaB.depositar(400)
contaB.sacar(100)
contaB.consultarSaldo()
print()


contaP = ContaPoupanca("Maria Fatima", "97445-42", '002', 1500.0, 25, 2.3)
print(contaP)
diaAtual = 10
contaP.calcularNovoSaldo(diaAtual)
contaP.consultarSaldo()
print()


contaE = ContaEspecial('Rubens Afonso', '99823', '003', 1100, 300)
print(contaE)
contaE.sacar(1500)
contaE.consultarSaldo()
print()
