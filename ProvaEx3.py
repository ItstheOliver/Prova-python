#Exercício 03

pergunta = input("Você quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit?: ")

if pergunta == "Fahreinheit para celcius":
    Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5/9
    print("A temperatura em Celsius é:", Celsius)
elif pergunta == "Celcius para fahreinheit":
    Celsius = float(input("Digite a temperatura em Celsius: "))
    Fahrenheit = (Celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é:", Fahrenheit)
