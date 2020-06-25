
from random import randint
class Person:
    SEXO = 'H'
    
    def __init__(self):
        self.__nombre = ''
        self.__edad = 0
        self.__dni = __generaDNI()
        self.__sexo = 'H'
        self.__peso = 0
        self.__altura = 0


    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__dni = __generaDNI()
        self.__peso = 0
        self.__altura = 0


    def __init__(self, nombre='', edad=0, sexo=SEXO, peso=0, altura=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = __generaDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura


    def setnombre(self, nombre):
        self.__nombre = nombre

    def setedad(self, edad):
        self.__edad = edad
    
    def setsexo(self, sexo):
        self.__sexo= sexo

    def setpeso(self, peso):
        self.__peso = peso
    
    def setaltura(self, altura):
        self.__altura = altura


    def calcularIMC(self, peso, altura):
        resultado = peso/(altura^2)

        if resultado<20:
            return -1
        elif 20<=resultado<=25:
            return 0
        elif resultado<25:
            return 1
        

    def esMayorDeEdad(self,edad):
        if edad<18:
            return "Es menor de edad"
        else:
            return "Es mayor de edad"


    def comprobarSexo(self, sexo):
        if sexo==self.__sexo:
            return "Es correcto"
        else:
            return self.setsexo('H')


    def __str__(self):
        return """\
    Nombre: {}
    Edad: {}
    Sexo: {}
    DNI:{}
    Peso: {}
    Altura:{} """.format(self.__nombre, self.__edad, self.__sexo,self.__dni,self.__peso,self.__altura)

    def __generaDNI(self):
        dni = randint(9999999, 1000000000)