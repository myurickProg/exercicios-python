nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

index_arroba = email.find("@")
servidor = email[index_arroba:]
print(servidor)

index_espaco = nome.find(" ")
primeiro_nome = nome[:index_espaco]

print(f"Usuário {primeiro_nome} cadastrado com sucesso com o email {email}")
primeira_letra = email[0]
print(f"confirmação enviada ao email: {primeira_letra}***{servidor}")


