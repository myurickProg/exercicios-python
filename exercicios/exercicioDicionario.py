dic_produtos = {"doce de batata doce": 32, "panda": 45, "bomba de hidrogenio": 500}
produto_chave = input("Digite o nome do produto: ")
produto_chave = produto_chave.lower()

if produto_chave in dic_produtos:
    preco = dic_produtos.get(produto_chave)
    print(f"preço do produto: {produto_chave} é: R${float(preco):.2f}")
else:
    print("produto inválido!")


