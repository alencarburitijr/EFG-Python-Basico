auxiliar = 0
for i in range(int(input("Digite a quantidade de números: "))):
    numero = int(input("Digite um número: "))
    if numero > auxiliar:
        auxiliar = numero

print("O maior número digitado foi: ", auxiliar)