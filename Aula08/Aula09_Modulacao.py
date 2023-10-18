# Nesta aula iremos aprender sobre modulação que em outras linguagens pode ser conhecida
# como função, método e etc.

# Modulação é uma forma de organizar o código, dividindo em partes menores, que podem ser
# chamadas de funções ou métodos.

# Exemplo de função:
# def nome_da_funcao(parametros):
#     codigo

def soma(a, b):
    print("A soma é igual a", a + b)

def subtracao(a, b):
    print("A subtração é igual a", a - b)

def multiplicacao(a, b):
    print("A multiplicação é igual a", a * b)

def divisao(a, b):
    if b == 0:
        print("Não é possível dividir por zero")
    else:
        print("A divisão é igual a", a / b)

# Chamada de função ou método  
numero = 10
numero2 = 20
soma(numero, numero2)

subtracao(numero, numero2)

multiplicacao(numero, numero2)

divisao(numero, numero2)