import os
os.system ("cls")

perm = str(input("você tem permissão? "))
idade = int(input("qual sua idade? "))

if perm == "s" or idade >= 18:

    print("Acesso permitido!!")

else:

    print("Acesso negado!!")