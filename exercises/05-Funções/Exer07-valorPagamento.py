"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma 
conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes 
valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que 
a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar 
a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a 
prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a 
quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte 
forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, 
mais 0,1% de juros por dia de atraso.
"""

def valorPagamento (valor, num_dias):
    if num_dias == 0:
        return valor
    prestacao = valor + (valor*0.03) + (valor*0.01*num_dias)
    return prestacao

# Programa Principal
lista_prestacoes = []
c = 0 

while True:
    prestacao = float(input('Digite o valor da prestação: '))
    if prestacao == 0:
        break
    dias = int(input('Número de dias em atraso: '))
    
    lista_prestacoes.append(valorPagamento(prestacao, dias))
    c += 1

print()
# Relatório
print('~'*50)
print(f'RELATÓRIO'.center(50))
print('~'*50)

print(f'Quantidade de Prestações Pagas: {c}')
print(f'Valor Total de Prestações Pagas: R$ {sum(lista_prestacoes)}')
