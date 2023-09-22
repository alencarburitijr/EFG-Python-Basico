# Estrutura condicional
# Uma estrutura de condição é uma parte fundamental da programação 
# que permite que o programa faça decisões com base em condições.

# Se - If
# Senão - Else
# Senão se - Elif

if 1 == 2:
    print("1 é igual a 1")
else:
    print("1 não é igual a 1")

idade = input("Digite sua idade: ")

if int(idade) >= 18:
    print("Você é maior de idade")
elif int(idade) >= 16 and int(idade) < 18:
    print("Você está quase lá") 
else:
    print("Você é menor de idade")

# Desafio 01
# Crie um programa que receba a idade de uma pessoa e verifique se ela 
# é obrigada a votar ou não. Se ela não for obrigada, verifique se ela já
# pode votar quando tiver entre 16 e 18 anos.

# Desafio 02
# Crie um programa que receba um número de 1 a 20 e verifique se ele é
# par ou ímpar.


numero = input("Digite um número de 1 a 20: ")

try:
    numero = int(numero)
    if numero >= 0 and numero <= 20:
        if int(numero) % 2 == 0 and numero != 0:
            print("O número", numero, "é par")
        elif numero == 0:
            print("O número", numero, "é neutro")
        else:
            print("O número", numero, "é ímpar")
    else:
        print("O número digitado não está entre 1 e 20")
    
except Exception:
    print("Você não digitou um número válido")
    exit()
    



# Desafio 03

