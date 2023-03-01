"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, 
       deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

"""
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self, nova_base, nova_altura):
        print(f'Base alterada de {self.base} para {nova_base}\nAltura alterada de {self.altura} para {nova_altura}')
        self.base = nova_base
        self.altura = nova_altura
        print()

    def retorna_lados(self):
        print(f'Valores atuais de lados:\nBase - {self.base}\nAltura - {self.altura} ')
        print()

    def calc_area(self):
        print(f'Área: {self.base * self.altura}')
        print()

    def calc_perim(self):
        print(f'Perímetro: {(self.base*2) + (self.altura*2)}')
        print()

a = Retangulo(10,20)
a.mudar_lados(15,30)
a.retorna_lados()
a.calc_area()
a.calc_perim()
a.mudar_lados(20,40)
a.retorna_lados()
a.calc_area()
a.calc_perim()