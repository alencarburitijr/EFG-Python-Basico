resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print(f'Você digitou {quant} números e a soma entre eles foi {soma}')
print()
print(f'Você digitou {quant} números e a média foi {soma/quant:.2f}')
print()
print(f'O maior valor foi {maior} e o menor foi {menor}')
print()