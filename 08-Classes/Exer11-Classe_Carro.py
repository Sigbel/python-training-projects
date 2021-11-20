"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

    a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no 
       tanque.
    b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
    c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de 
       combustível no tanque de gasolina.
    d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    e. Forneça um método adicionarGasolina( ), para abastecer o tanque. 
    
Exemplo de uso:

meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""
class Carro:
   def __init__(self, km_litro):
      self.km_litro = km_litro
      self.gasolina = 0

   def obterGasolina(self):
      print(f'Gasolina atual: {self.gasolina:.2f}L') 
   
   def andar(self, km):
      print(f'Anda {km} km')
      litros_gastos = km/self.km_litro
      if self.gasolina - (km/self.gasolina) < 0:
         print(f'A Gasolina no tanque não é suficiente para essa viagem.')
         return
      elif 0 < (self.gasolina - litros_gastos) < 3:
         print(f'Gasolina na reserva, é sugerido o reabastecimento.\n'
         f'QTDE de litros gasto na viagem: {km/self.km_litro:.2f}L')
      self.gasolina = self.gasolina - (km/self.km_litro)

   def adicionarGasolina(self, litros):
      print(f'Adicionado {litros}L de Gasolina.')
      self.gasolina = self.gasolina + litros

meuFusca = Carro(15)          
meuFusca.adicionarGasolina(20)  
meuFusca.andar(280)           
meuFusca.obterGasolina()
