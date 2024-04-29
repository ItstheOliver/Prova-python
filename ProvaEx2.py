#Exercício 02

import math
n1= float(input("Digite um número: "))
n2 = float(input("Digite mais outro número "))
operação= input("Você quer somar os dois números ou subtrair? ")

if operação == "somar":
    print("A soma dos dois números é: ", n1+n2)
else:
    print("A subtração dos dois números é: ", n1-n2)