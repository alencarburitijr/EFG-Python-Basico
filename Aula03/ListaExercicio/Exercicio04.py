# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.lower() in ('a','e','i','o','u'):
    print('A letra', letra, 'é uma vogal')
elif letra in ('1','2','3','4','5','6','7','8','9','0'):
    print('Você digitou um número')
else:
    print('A letra', letra, 'é uma consoante')

