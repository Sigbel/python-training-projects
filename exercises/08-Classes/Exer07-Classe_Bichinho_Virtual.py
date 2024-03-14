"""
Exercício 7 - Classe: Bichinho Virtual

Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    a. Atributos: Nome, Fome, Saúde e Idade 
    b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 

Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação 
entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta 
informação por que ela pode ser calculada a qualquer momento.
"""
class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def altera_nome(self, n_nome):
        print(f'Nome Antigo: {self.nome} | Nome Atual: {n_nome}\n')
        self.nome = n_nome

    def altera_fome(self, n_fome):
        if n_fome < 0:
            self.fome = 0 
        elif n_fome > 100:
            self.fome = 100
        else:
            self.fome = n_fome 

    def altera_saude(self, n_saude):
        if n_saude < 0:
            self.saude = 0 
        elif n_saude > 100:
            self.saude = 100
        else:
            self.saude = n_saude

    def altera_idade(self, n_idade):
        if self.idade > 30:
            print('Morte por velhice.')
            self.idade = n_idade

        elif self.idade < 1:
            print('Idade Inválida.')
        else:
            self.idade = n_idade

    def retorna_nome(self):
        print(f'#NOME ATUAL: {self.nome}')

    def retorna_fome(self):
        print(f'#FOME ATUAL: {self.fome}%')
        humor = (self.fome + self.saude)/2
        print(f'- HUMOR ATUAL: {humor}%')

    def retorna_saude(self):
        print(f'#SAÚDE ATUAL: {self.saude}%')
        humor = (self.fome + self.saude)/2
        print(f'- HUMOR ATUAL: {humor}%')

    def retorna_idade(self):
        print(f'#IDADE ATUAL: {self.idade}%')

a = Bichinho('Alfredo', 100, 100, 1)
a.altera_nome('Lincoln')
a.altera_fome(60)
a.altera_saude(80)
a.altera_idade(30)
a.retorna_nome()
a.retorna_fome()
a.retorna_saude()
a.retorna_idade()
