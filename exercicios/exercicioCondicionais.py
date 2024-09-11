produtos = ["rojão", "peido de veia", "palitinho"]
precos = [5, 3, 1]

novo_produto = input("Digite o nome do novo produto: ")
novo_produto = novo_produto.lower()

produtos.append(novo_produto)

novo_preco = input("Digite o preco do produto: ")
novo_preco = novo_preco.lower()

precos.append(novo_preco)


produto = input("Digite o nome do produto: ")
produto = produto.lower()


if produto in produtos:
    index_produto = produtos.index(produto)
    preco = precos[index_produto]
    print(f"Produto: {produto}\nPreço: {preco}")
else:
    print("produto inválido!")