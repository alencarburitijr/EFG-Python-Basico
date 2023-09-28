# Faça um Programa que leia três números e mostre o maior e o menor deles.


numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
numero3 = input("Digite o terceiro número: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)
    numero3 = int(numero3)
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1
    if numero3 > maior:
        maior = numero3
    elif numero3 < menor:
        menor = numero3
    print("O maior número é", maior)
    print("O menor número é", menor)

except Exception:
    print("Você não digitou um número válido")
    exit()