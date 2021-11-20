"""
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do 
objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. 
Dica: acrescente um método especial str() à classe Bichinho.
"""

class Bichinho:
    def __init__(self, nome, fome=100, saude=100, idade=1, brincadeira=100):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.brincadeira = brincadeira

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

    def alimenta(self, qtde):
        if (self.fome + qtde) > 100:
            self.fome = 100
        else:
            self.fome += qtde
        self.brincadeira -= (qtde/1.5)
        print(f'{self.nome} se alimentou com {qtde} de comida.')

    def brincar(self, tempo):
        ponto = tempo*20
        if (self.brincadeira + ponto) > 100:
            self.brincadeira = 100
        else:
            self.brincadeira += ponto
        self.fome -= (tempo*10)

        print(
            f'{self.nome} brincou por {tempo} minutos e acumulou {ponto} pontos de brincadeira.')

    def __str__(self):
        print(f'Status de {self.nome}:'
          f'\n\tFOME: {self.fome}'
          f'\n\tSAUDE: {self.saude}'
          f'\n\tIDADE: {self.idade}'
          f'\n\tBRINCADEIRA: {self.brincadeira:.2f}'
          f'\n\tHUMOR: {(self.saude + self.fome + self.brincadeira)/3:.2f}')


nome = str(input('Nomeie seu Tamagotchi: '))
a = Bichinho(nome)
opcaolis = [1, 2, 3, 4, 25]

while True:
    opcao1 = int(input(
        'MENU:\n\t1 - Brincar\n\t2 - Alimentar\n\t3 - Ferramentas\n\t4 - Dormir\nComando: '))
    while opcao1 not in opcaolis:
        opcao1 = int(input('Digite um comando válido: '))
    if opcao1 == 1:
        tempo = float(input('Quantos minutos quer brincar?: '))
        a.brincar(tempo)
    elif opcao1 == 2:
        alimento = float(input('Quanto de comida irá comer?: '))
        a.alimenta(alimento)
    elif opcao1 == 3:
        while True:
            opcao2 = int(input('Ferramentas:\n\t1 - Alterar Fome\n\t2 - Alterar Saude'
            '\n\t3 - Alterar Idade\n\t4 - Voltar ao Menu\nComando: '))
            while opcao2 not in opcaolis:
                opcao2 = int(input('Digite um comando válido: '))
            if opcao2 == 1:
                fome = int(input('Digite um novo valor para fome: '))
                a.altera_fome(fome)
            elif opcao2 == 2:
                saude = int(input('Digite um novo valor para saude: '))
                a.altera_saude(saude)
            elif opcao2 == 3:
                idade = int(input('Digite um novo valor para idade: '))
                a.altera_fome(idade)
            else:
                break
    elif opcao1 == 25:
        a.__str__()
    else:
        print(f'{a.nome} dormiu')
        break
