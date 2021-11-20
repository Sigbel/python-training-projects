"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o 
número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem 
dentro de faixas válidas.
"""
class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def sobe_canal(self):
        if (self.canal + 1) > 200:
            self.canal = 0
        else:
            self.canal = self.canal + 1
        print(f'#CANAL ATUAL: {self.canal} | #VOLUME: {self.volume}')

    def desce_canal(self):
        if (self.canal - 1) < 0:
            self.canal = 200
        else:
            self.canal = self.canal -1
        print(f'#CANAL ATUAL: {self.canal} | #VOLUME: {self.volume}')

    def muda_canal(self, novo_canal):
        if novo_canal > 200:
            self.canal = 200
        elif novo_canal < 0:
            self.canal = 0
        else:
            self.canal = novo_canal
        print(f'#CANAL ATUAL: {self.canal} | #VOLUME: {self.volume}')

    def aum_volume(self):
        if self.volume == 100:
            self.volume = 100
        else:
            self.volume = self.volume +1
        print(f'#CANAL ATUAL: {self.canal} | #VOLUME: {self.volume}')

    def dim_volume(self):
        if self.volume == 0:
            self.volume = 0
        else:
            self.volume = self.volume -1
        print(f'#CANAL ATUAL: {self.canal} | #VOLUME: {self.volume}')

a = TV(0, 100)
a.muda_canal(0)
a.desce_canal()
a.sobe_canal()
a.sobe_canal()
a.aum_volume()
a.aum_volume()
a.aum_volume()
a.aum_volume()
a.dim_volume()
