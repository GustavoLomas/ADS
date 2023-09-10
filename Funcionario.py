class Funcionario:
    def __init__(self, matricula, nome, dataAdmissao, valorHora, valorHoraExtra, cargo, status):
        self.__matricula = matricula
        self.__nome = nome
        self.__dataAdmissao = dataAdmissao
        self.__valorHora = valorHora
        self.__valorHoraExtra = valorHoraExtra
        self.__cargo = cargo
        self.__status = status

    def getMatricula(self):
        return self.__matricula
    def setMatricula(self, matricula):
        self.__matricula = matricula
    
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
    
    def getDataAdmissao(self):
        return self.__dataAdmissao
    def setDataAdmissao(self, dataAdmissao):
        self.__dataAdmissao = dataAdmissao
    
    def getValorHora(self):
        return self.__valorHora
    def setValorHora(self, valorHora):
        self.__valorHora = valorHora
    
    def getValorHoraExtra(self):
        return self.__valorHoraExtra
    def setValorHoraExtra(self, valorHoraExtra):
        self.__valorHoraExtra = valorHoraExtra
    
    def getCargo(self):
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    def getStatus(self):
        return self.__status
    def setStatus(self, status):
        self.__status = status
    
    def calcularSalario(self, qtdeHorasTrab):
        return self.__valorHora * qtdeHorasTrab
    
    def calcularHorasExtras(self, qtdeHorasExtrasTrab):
        return self.__valorHoraExtra * qtdeHorasExtrasTrab
    
    def reajusteValorHora(self, percentual):
        return self.__valorHora + self.__valorHora * percentual / 100        
    
    def reajusteValorHoraExtra(self, percentual):
        return self.__valorHoraExtra + self.__valorHoraExtra * percentual / 100

    def __str__ (self):
        return "Matricula: " + str(self.__matricula) + "\nNome: " + self.__nome + "\nData de admissão: " + self.__dataAdmissao + "\nValor hora: " + str(self.__valorHora) + "\nValor hora extra: " + str(self.__valorHoraExtra) + "\nCargo: " + self.__cargo + "\nStatus: " + self.__status

funcionario = Funcionario ('0010', 'Gustavo', '10/08/2000', 80, 100, 'TST', 'Ativo')
print (funcionario)

aux = input('Deseja ajustar a hora do funcionario?')
if aux == 'S' or aux =='s':
    reajuste = int(input('Reajuste de hora normal?'))
    reajusteHoraExtra = int(input('Reajuste de hora extra?'))
    print(str(funcionario.reajusteValorHora(reajuste)))
    print(str(funcionario.reajusteValorHoraExtra(reajusteHoraExtra)))