"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

    a. Atributos: nome, idade, peso e altura
    b. Métodos: Envelhercer, engordar, emagrecer, crescer. 
    
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        print(f'Status de {self.nome}:')
        print()

    def envelhece(self, anos):
        if self.idade < 21:
            self.altura = ((self.altura*100) + (0.5*anos))/100
        self.idade = self.idade + anos
        print(f'Idade depois de "{anos} anos": {self.idade}')
        print(f'Altura depois de "{anos} anos": {self.altura:.2f}')
        print()

    def engorda(self, quilos):
        self.peso = self.peso + quilos
        print(f'Peso depois de engordar "{quilos} kg": {self.peso}')
        print()

    def emagrece(self, quilos):
        self.peso = self.peso - quilos
        print(f'Peso depois de emagrecer "{quilos} kg": {self.peso}')
        print()

    def cresce(self, cm):
        self.altura = ((self.altura*100) + cm)/100
        print(f'Altura depois de crescer "{cm} cm": {self.altura:.2f}')

a = Pessoa('Maria', 18, 63.5, 1.63)
a.envelhece(5)
a.engorda(5)
a.emagrece(3)
a.cresce(10)

