#Exercício 05

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
impares = [n for n in [n1, n2, n3] if n % 2 != 0]
if not impares:
        print("Não há números ímpares.")
else:
        maior_impar = max(impares)
        print("O maior número ímpar é:", maior_impar)
