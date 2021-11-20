"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

    a. Possua uma classe chamada Ponto, com os atributos x e y. Ø
    b. Possua uma classe chamada Retangulo, com os atributos largura e altura. Ø
    c. Possua uma função para imprimir os valores da classe Ponto. Ø
    d. Possua uma função para encontrar o centro de um Retângulo. Ø
    e. Você deve criar alguns objetos da classe Retangulo. Ø
    f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um 
       objeto da classe Ponto. Ø
    g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os 
       valores de x e y para o centro do objeto. Ø
    h. O valor do centro do objeto deve ser mostrado na tela Ø
    i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo. Ø
"""
class Ponto:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def imprPonto(self):
      print(f'\t(X: {self.x}, Y: {self.y})')

class Retangulo:
   def __init__(self, vertice_inf, vertice_sup):
      self.vertice_inf = vertice_inf
      self.vertice_sup = vertice_sup
   
   def centroRet(self):
      print(f'Ponto Central do "Retângulo":\n\t'
            f'(X: {(self.vertice_sup.x + self.vertice_inf.x)/2:.2f},Y: {(self.vertice_sup.y + self.vertice_inf.y)/2:.2f})')

while True:
   print(' MENU '.center(50, '-'))
   opcao = input('1 - Digitar novos valores para o Retângulo\n2 - Parar programa\nComando: ')
   while opcao != '1' and opcao != '2':
      opcao = input('Digite uma opção válida: ')
   if opcao == '2':
      break
   elif opcao == '1':
      x_inf = int(input('Digite o vértice de partida (X): '))
      y_inf = int(input('Digite o vértice de partida (Y): '))
      vertice_inf = Ponto(x_inf, y_inf)
      x_sup = int(input('Digite o vértice final (X): '))
      y_sup = int(input('Digite o vértice final (Y): '))
      vertice_sup = Ponto(x_sup, y_sup)
      a = Retangulo(vertice_inf, vertice_sup)
      print()

      while True:
         opcao_2 = input('O que deseja fazer?\n\t1 - Imprimir valores do Ponto\n\t2 - Imprimir centro do Rentângulo\n\t'
         '3 - Menu Principal\nComando: ')
         while opcao_2 != '1' and opcao_2 != '2' and opcao_2 != '3':
            opcao_2 = input('Digite uma opção válida: ')
         if opcao_2 == '1':
            print(f'Valores Inferiores:')
            vertice_inf.imprPonto()
            print(f'Valores Superiores:')
            vertice_sup.imprPonto()
         elif opcao_2 == '2':
            a.centroRet()
         else:
            break
         print()
