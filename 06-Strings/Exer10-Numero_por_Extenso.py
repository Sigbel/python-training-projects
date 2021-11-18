"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e 
imprima-o na tela por extenso.
"""
dezenas_maior = {2:'Vinte', 3: 'Trinta', 4: 'Quarenta', 5: 'Cinquenta', 6: 'Sessenta', 7: 'Setenta', 8: 'Oitenta',
9: 'Noventa'}
dezenas = ['Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
'dezenove']
unidades = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove'] 

numero = int(input('Digite um número entre 0 e 99: '))
str_numero = str(numero)

if numero < 10:
    print(unidades[numero])
elif 10 <= numero < 20:
    print(dezenas[numero-10])
elif int(str_numero[0]) >= 2 and int(str_numero[1]) == 0:
    print(dezenas_maior[int(str_numero[0])]) 
else:
    print(f'{dezenas_maior[int(str_numero[0])]} e {unidades[int(str_numero[1])]}')

