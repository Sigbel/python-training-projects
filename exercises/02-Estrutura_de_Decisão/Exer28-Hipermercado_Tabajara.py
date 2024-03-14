"""
Exercício 28 - Hipermercado Tabajara

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
"""

tipo = str(input("Digite o tipo de carne desejada (F) - File Duplo / (A) - Alcatra / (P) Picanha: ")).upper()
quantidade = float(input("Digite a quantidade de carne: "))
cartao = str(input("Pagamento com cartão Tabajara (S) - Sim / (N) - Não: ")).upper()
calculo_file = 0
calculo_picanha = 0
calculo_alca = 0

print()
if tipo == "F":
    if 0 < quantidade <= 5:
        calculo_file = quantidade * 4.9
    else:
        calculo_file = quantidade * 5.8
    if cartao == "S":
        calculo_file_cartao = calculo_file - (calculo_file * 0.05)
        print(f"O tipo de Carne escolhido foi File Duplo\nA quantidade foi: {quantidade} Kg\nO preço total foi: R$ {calculo_file:.2f}\nO desconto foi de R$ {calculo_file*0.05:.2f}\n"
              f"E o valor final é R$ {calculo_file_cartao:.2f}")
    elif cartao == "N":
        print(f"O tipo de Carne escolhido foi File Duplo\nA quantidade foi: {quantidade} Kg\nO preço pago foi: R$ {calculo_file:.2f}")
    else:
        print("Digite um parâmetro válido!")
elif tipo == "A":
    if 0 < quantidade <= 5:
        calculo_alca = quantidade * 5.9
    else:
        calculo_alca = quantidade * 6.8
    if cartao == "S":
        calculo_alca_cartao = calculo_alca - (calculo_alca * 0.05)
        print(
            f"O tipo de Carne escolhido foi Alcatra\nA quantidade foi: {quantidade} Kg\nO preço total foi: R$ {calculo_alca:.2f}\nO desconto foi de R$ {calculo_alca*0.05:.2f}\n"
            f"E o valor final é R$ {calculo_alca_cartao}")
    elif cartao == "N":
        print(
            f"O tipo de Carne escolhido foi Alcatra\nA quantidade foi: {quantidade} Kg\nO preço pago foi: R$ {calculo_alca:.2f}")
    else:
        print("Digite um parâmetro válido!")
elif tipo == "P":
    if 0 < quantidade <= 5:
        calculo_picanha = quantidade * 6.9
    else:
        calculo_picanha = quantidade * 7.8
    if cartao == "S":
        calculo_picanha_cartao = calculo_picanha - (calculo_picanha * 0.05)
        print(f"O tipo de Carne escolhido foi Picanha\nA quantidade foi: {quantidade} Kg\nO preço total foi: R$ {calculo_picanha:.2f}\nO desconto foi de R$ {calculo_picanha*0.05:.2f}\n"
              f"E o valor final é R$ {calculo_picanha_cartao}")
    elif cartao == "N":
        print(f"O tipo de Carne escolhido foi Picanha\nA quantidade foi: {quantidade} Kg\nO preço pago foi: R$ {calculo_picanha:.2f}")
    else:
        print("Digite um parâmetro válido!")
else:
    print("Digite um letra válida!")





