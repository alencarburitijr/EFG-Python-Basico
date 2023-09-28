# Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato e que o FGTS corresponde a 11% 
# do Salário Bruto, mas não é descontado (é a empresa que deposita).
#  O Salário Líquido corresponde ao Salário Bruto menos os 
# descontos. O programa deverá pedir ao usuário o valor da sua
#  hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela 
# as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

descontoIR = 0.0
descontoINSS = 0.0
fgts = 0.0
salarioBruto = 0.0
descSindicato = 0.0
percSindicato = 0.03
percFGTS = 0.11
percIR = 0
salarioLiquido = 0.0
totalDesconto = 0.0

valorHora = float(input("Digite o valor da hora: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = valorHora * horasTrabalhadas

if salarioBruto > 900 and salarioBruto <= 1500:
    percIR = 5
elif salarioBruto <= 2500:
    percIR = 10
else:
    percIR = 20
    
fgts = salarioBruto * percFGTS
descSindicato = salarioBruto * percSindicato
descontoINSS = salarioBruto * 0.10
descontoIR = salarioBruto * (percIR/100)  
totalDesconto = descontoINSS + descontoIR  
salarioLiquido =  salarioBruto - descontoIR - descontoINSS 

print("Salário Bruto: (", valorHora , " * " , horasTrabalhadas, ")        : R$ " , salarioBruto)
print("(-) IR (",percIR,"%)                     : R$ ",   descontoIR)  
print("(-) INSS ( 10%)                 : R$ ", descontoINSS)
print("FGTS (11%)                      : R$ ", fgts)
print("Total de descontos              : R$ ", totalDesconto)
print("Salário Liquido                 : R$ ", salarioLiquido)

