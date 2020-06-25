class Accountant:

    def __init__(self, accountant=0):
        self.accountant = accountant

    def constructor_dos(self, accountant=0):
        self.accountant = accountant

    def __str__(self):
        return self.accountant

    def getaccountant(self):
        return self.accountant

    def setaccountant(self, accountant):
        self.accountant = accountant

    def aumentar(self, aumentar_num):
        resultado1 = self.getaccountant()
        resultado2 = resultado1 + aumentar_num
        self.setaccountant(resultado2)
        print(resultado2)

    def disminuir(self, disminuir_num):
        resultado3 = self.getaccountant()
        resultado4 = resultado3 - disminuir
        self.setaccountant(resultado4)
        print(resultado4)

accountant = Accountant(10).aumentar(5)
