"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).
"""

tamanho = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_internet = float(input("Digite a velocidade da internet (Mbps): "))

tempototal = tamanho / velocidade_internet
tempo_min = tempototal//60
tempo_seg = ((tempototal/60)-(tempototal//60))*60

print()
print(f"O tempo estimado de download é: {int(tempo_min)} minutos e {int(tempo_seg)} segundos")
