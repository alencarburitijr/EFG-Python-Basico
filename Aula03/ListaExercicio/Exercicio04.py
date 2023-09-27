# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.lower() in ('a','e','i','o','u'):
    print('A letra', letra, 'é uma vogal')
else:
    print('A letra', letra, 'é uma consoante')