"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia = input("Digite o dia: ")
mes = input("Digite o mês: ")
ano = input("Digite o ano: ")

if len(ano) == 4:
    ano = int(ano)
    if len(mes) == 2:
        mes = int(mes)
        if 1 <= mes <= 12:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if len(dia) == 2:
                    dia = int(dia)
                    if 1 <= dia <= 31:
                        print(f"O a data inserida foi (dd/mm/aaaa): {dia}/{mes}/{ano}")
                    else:
                        print("Digite um dia válido!")
                else:
                    print("O dia deve conter 2 digitos!")
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if len(dia) == 2:
                    dia = int(dia)
                    if 1 <= dia <= 30:
                        print(f"O a data inserida foi (dd/mm/aaaa): {dia}/{mes}/{ano}")
                    else:
                        print("Digite um dia válido!")
                else:
                    print("O dia deve conter 2 digitos!")
            else:
                if len(dia) == 2:
                    dia = int(dia)
                    if 1 <= dia <= 28:
                        print(f"O a data inserida foi (dd/mm/aaaa): {dia}/{mes}/{ano}")
                    else:
                        print("Digite um dia válido!")
        else:
            print("Digite um mês válido!")
    else:
        print("O mês deve conter 2 digitos!")
else:
    print("O ano deve conter 4 digitos!")