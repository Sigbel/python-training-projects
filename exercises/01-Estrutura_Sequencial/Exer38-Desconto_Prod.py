"""
Exercício 38 - Desconto no Produto 

Um produto de uma loja custa um valor X, mas para aquele dia em específico havia uma promoção de 12% para qualquer produto. Calcule o valor do produto mediante
o desconto fornecido.
"""

v_prod = float(input("Digite o valor do produto: "))

desconto = v_prod - (v_prod * 0.12)

print(f"O valor com desconto de 12% é: {desconto:.2f}")