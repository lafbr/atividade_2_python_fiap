import os
os.system ("cls")

usuario = str(input("insira o seu usuario: "))

senha = int(input("Insira sua senha: "))


if usuario == "admin" and senha == 123 :

    print("login realizado com sucesso!")
else:

    print(" login errado, verifique os dados digitados!!")