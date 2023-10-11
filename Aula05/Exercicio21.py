numero = int(input("digite um numero"))
primo = True
for n in range(2, numero):
    if numero % n == 0:
        print("nao e primo", n, "e divisor")
        primo = False

if primo:
    print("é primo")
