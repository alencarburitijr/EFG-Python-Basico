# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

paisA = 80000
paisB = 200000

anos = 1

while paisA < paisB:
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
    print("População do país A: ",paisA, " - ", anos, " anos")
    print("População do país B: ",paisB, " - ", anos, " anos")
    anos += 1

print("A população do país A ultrapassará a população do país B em ",anos, " anos")
