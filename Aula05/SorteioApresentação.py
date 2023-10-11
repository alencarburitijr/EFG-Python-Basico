# Fazer um programa que receba o nome dos alunos e sortei a ordem de apresentação deles.

# Recebe o nome dos alunos
alunos = []
while True:
    nome = input("Digite o nome do aluno: ")
    if nome == "":
        break
    alunos.append(nome)

# Sorteia a ordem de apresentação
from random import shuffle
shuffle(alunos)

# Apresenta a ordem de apresentação
print("A ordem de apresentação será: ")
for aluno in alunos:
    print(aluno)

# Exemplo de saída:
# Luis
# Matheus
# Guilherme
# João Paulo
# Thomas
# Glauber
# Nara
# Leonardo
# Gustavo