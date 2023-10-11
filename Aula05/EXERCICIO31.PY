produto_numero = 0
total_compra = 0
total_produto = 0
preco_produtos = []

while True:
    preco_produto = float(input("Digite o preço do produto: "))
    if preco_produto == 0:
        break
    preco_produtos.append(preco_produto)
    total_produto += 1
    produto_numero += 1
total_compra = sum(preco_produtos)
print("O total da compra foi: ", total_compra)
dinheiro = float(input("Digite o valor em dinheiro: "))
troco = dinheiro - total_compra
print("\ndetalhes da compra:")
for i in range(total_produto):
    print("produto", i + 1, ":", preco_produtos[i])
print(f"dinheiro: R$ {dinheiro:.2f}")
print(f"troco: R$ {troco:.2f}")
    

