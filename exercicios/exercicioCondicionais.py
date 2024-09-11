produtos = ["rojão", "peido de veia", "palitinho"]
precos = [5, 3, 1]

produto = input("Digite o nome do produto: ")
produto = produto.lower()

if produto in produtos:
    index_produto = produtos.index(produto)
    preco = precos[index_produto]
    print(f"Produto: {produto}\nPreço: {preco}")
else:
    print("produto inválido!")