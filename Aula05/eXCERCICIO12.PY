#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
#O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

# qual número
numero = int(input("Digite um número entre 1 e 10 para fazer a tabuada: "))

# no intervalo
if 1 <= numero <= 10:
    print(f"Tabuada de {numero}:")

    # Loop do for 
    for lista in range(1, 11):
        estrutura_tabuada_multiplicacao = numero * lista
        print(f"{numero} X {lista} = {estrutura_tabuada_multiplicacao}")

# não tá no intervalo
else:
    print("Apenas entre 1 e 10.")
