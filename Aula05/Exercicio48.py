#faca um programa que peça um numero inteito positivo e em seguida mostre este numero invertido

#solite um numero inteito do usuario

numero = int(input("Digite um numero inteiro positivo: "))

#verificar se o numero é positivo

if numero <= 0:
    print("O numero deve ser positivo.")

else:
    numero_invertido = 0

    #inverte o numero usando um loop while

    while numero > 0:
        #pega o ultimo digito do numero
        digito = numero % 10
        #adiciona o digito no numero invertido
        numero_invertido = numero_invertido * 10 + digito
        #remove o ultimo digito do numero
        numero = numero // 10
        print("numero_invertido:", numero_invertido)