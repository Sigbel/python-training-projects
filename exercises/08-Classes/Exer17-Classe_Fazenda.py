"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que 
ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os 
bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o 
programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""
from random import randint

class Bichinho:
    def __init__(self, nome, fome, brincadeira, saude=100, idade=1, ):
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

print('Fazenda Tamagotchi'.center(40, '-'))
qtde_animais = int(input('Digite a quantidade de animais na fazenda: '))
lista_animais = []

for n in range(qtde_animais):
    nome_animal = str(input('Digite o nome do animal: ')).upper()
    lista_animais.append(Bichinho(nome_animal, randint(30,100), randint(30,100)))

opcao1lis = [1, 2, 3, 4, 25]
opcao2lis = [1, 2, 3, 4, 5]
ord_list_animais = ord_list_animais = [v.nome for v in lista_animais]

while True:
    opcao1 = int(input(
        'MENU:\n\t1 - Brincar com todos\n\t2 - Alimentar todos\n\t3 - Ferramentas\n\t4 - Dormir\nComando: '))
    while opcao1 not in opcao1lis:
        opcao1 = int(input('Digite um comando válido: '))
    if opcao1 == 1:
        tempo = float(input('Quantos minutos quer brincar?: '))
        for n in lista_animais:
            n.brincar(tempo)
    elif opcao1 == 2:
        alimento = float(input('Quanto de comida irá comer?: '))
        for n in lista_animais:
            n.alimenta(alimento)
    elif opcao1 == 3:
        while True:
            opcao2 = int(input('Ferramentas:\n\t1 - Alterar Fome\n\t2 - Alterar Saude'
                               '\n\t3 - Alterar Idade\n\t4 - Alterar Nome\n\t5 - Voltar ao Menu\nComando: '))
            while opcao2 not in opcao2lis:
                opcao2 = int(input('Digite um comando válido: '))
            if opcao2 == 1:
                opcao_bichos = str(input(f'Selecione um os bichos da lista a seguir\n\t{ord_list_animais}\nAnimal: ')).upper()
                fome = int(input('Digite um novo valor para fome: '))
                lista_animais[ord_list_animais.index(opcao_bichos)].altera_fome(fome)
            elif opcao2 == 2:
                opcao_bichos = str(input(f'Selecione um os bichos da lista a seguir\n\t{ord_list_animais}\nAnimal: ')).upper()
                saude = int(input('Digite um novo valor para saude: '))
                lista_animais[ord_list_animais.index(opcao_bichos)].altera_fome(saude)
            elif opcao2 == 3:
                opcao_bichos = str(input(f'Selecione um os bichos da lista a seguir\n\t{ord_list_animais}\nAnimal: ')).upper()
                idade = int(input('Digite um novo valor para idade: '))
                lista_animais[ord_list_animais.index(opcao_bichos)].altera_fome(idade)
            elif opcao2 == 4:
                opcao_bichos = str(input(f'Selecione um os bichos da lista a seguir\n\t{ord_list_animais}\nAnimal: ')).upper()
                nome = str(input('Digite um novo nome: ')).upper()
                lista_animais[ord_list_animais.index(opcao_bichos)].altera_nome(nome)
            else:
                break
    elif opcao1 == 25:
        for n in lista_animais:
            n.__str__()
    else:
        for n in lista_animais:
            print(f'{n.nome} dormiu')
        break
