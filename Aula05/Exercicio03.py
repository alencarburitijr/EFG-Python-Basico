# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")
while len(nome) < 3:
    print('Quantidade de caracteres no nome está menor que 3 caracteres')
    if len(nome) < 3:
        nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade"))
while idade < 0 or idade > 150:
    print('Idade inválida')
    if idade < 0 or idade > 150:
        idade = int(input("Digite sua idade"))
        
salario = float(input("Digite seu salário"))
while salario <= 0:
    print('Salário inválido')
    if salario <= 0:
        salario = float(input("Digite seu salário"))


sexo = input("Digite o sexo (f ou m): ")
while sexo != "f" and sexo != "m":
    print('Sexo inválido')
    if sexo != "f" and sexo != "m":
        sexo = input("Digite o sexo (f ou m): ")

estadoCivil = input("Digite o estado civil (s, c, v, d): ")
while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
    print('Estado civil inválido')
    if estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
        estadoCivil = input("Digite o estado civil (s, c, v, d): ")
