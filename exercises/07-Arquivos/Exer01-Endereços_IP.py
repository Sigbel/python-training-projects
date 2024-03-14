"""
Exercício 1 - Endereços de IP

Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um 
relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""
def valida_ip(ip):
    formata = ip.replace('\n', '')
    ip_parts = formata.split('.')
    if len(ip_parts) > 4:
        return 0
    for ip_part in ip_parts:
        if not ip_part.isdigit():
            return 0
        if 0 > int(ip_part) or int(ip_part) > 255:
            return 0
    return 1

ips_validos = []
ips_invalidos = []

# Verifica o arquivo de entrada contendo os IPs e separa os válidos e inválidos.
with open('01_Endereços_IP.txt', 'r') as file:
    for c1 in file:
        valida = valida_ip(c1)
        if valida == 1:
            ips_validos.append(c1.replace('\n', ''))
        else:
            ips_invalidos.append(c1.replace('\n', ''))

# Cria um novo arquivo de saída contendo os IPs devidamente classificados.
with open('01_Relatório_IP.txt', 'w+') as file2:
    file2.write('[Enderecos validos:]\n')
    for c2 in ips_validos:
        file2.write(c2 + '\n')
    file2.write('\n')
    file2.write('[Enderecos invalidos:]\n')
    for c3 in ips_invalidos:
        file2.write(c3 + '\n')
