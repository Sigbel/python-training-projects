"""
Exercício 14 - Leet Spek

Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das 
letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso 
do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada 
para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de 
traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
"""
from random import randint

leet = {
    'A': ['4', '@', "^" , 'ä', 'ª', 'aye'],
    'B': ['8', '6', '|3' , 'ß', 'P>' , '|' ],
    'C': ['[', '¢', '<', '('],
    'D': ['|))', 'o|', '[)', 'I>' , '|>', '?'],
    'E': ['3', '&' , '£', 'ë', '[-', '€', 'ê', '|=-'],
    'F': ['|=' , 'ph', '|#'],
    'G': ['6', '&' , '(_+', '9', 'C-', 'gee'],
    'H': ['#' , '/-/', '[-]', '{=}', '<~>', '|-|', ']~[', '}{', ']-[', '?', '8', '}-{'],
    'I': ['1', '!', '|' , '&' , 'eye', '3y3', 'ï', '][', '[]'],
    'J': ['j', ';', '_/', '</', '(/'],
    'K': ['X', '|<', '|{', ']{', '}<' , '|('],
    'L': ['1', '7', '1_', '|' , '|_' ,  '#' , '¬', '£'],
    'M': ['//.', '^^', '|v|', '[V]', '|\/|', '(u)', '[]V[]', '(V)', 'IVI'],
    'N': ['//', '^/', '|\|', '/\/', '[\]', '<\>', '{\}', '[]\[]', 'n', '/V', '₪'],
    'O': ['0', '()', '?p', '*', 'ö'],
    'P': ['|^', '|*', '|o', '|^(o)', '|>', '|"', '9', '[]D', '|̊,' , '|7'],
    'Q': ['q', '9', '(_,)o'],
    'R': ['|2', '|?', '|^', 'lz', '[z','12', 'Я'],
    'S': ['5', '$', 'z', '§', 'ehs'],
    'T': ['7', '+', '-|-', '1', "']['", '"|"'],
    'U': ['(_)', '|_|', 'v', 'ü'],
    'V': ['\/'],
    'W': ['\/\/', 'vv', "'//" , '\^/', '(n)', '\V/', '\//', '\X/', '\|/'],
    'X': ['><', 'Ж', 'ecks', ')('],
    'Y': ['Y', 'j', '`/', '¥'],
    'Z': ['2', 'z', '~\_', '~/_', '%'],
}

while True:
    palavra = str(input('Digite uma palavra: ')).upper()
    l_palavra = []

    for c1 in palavra:
        tamanho = len(leet[c1])
        l_palavra.append(leet[c1][randint(0,tamanho-1)])

    print(''.join(l_palavra))