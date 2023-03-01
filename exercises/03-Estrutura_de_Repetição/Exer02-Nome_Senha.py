"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do 
usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

login = input("Digite o nome de usuário: ").upper()
senha = input("Digite a senha: ").upper()

while login == senha:
    print("Digite uma senha diferente do login! ")
    senha = input("Digite a senha: ")

print("Login Concluído!")
    
