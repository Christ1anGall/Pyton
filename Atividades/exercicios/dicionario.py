""" meu_dicionario = {'chave': 'valor'}

type(meu_dicionario)


# Forma builtin
meu_dicionario = dict(primeiro=1, segundo=2, terceiro=3)


# Tentando criar duas chaves iguais
meu_dicionario = {'chave': 'valor_1', 'chave': "valor_2"}


# Podemos também passar uma lista contendo tuplas, representando chave e valor:
meu_dicionario = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])

print(meu_dicionario)


lista_1 = ['primeiro', 'segundo', 'terceiro', 'quarto']
lista_2 = [1, 2, 1]

meu_dicionario = dict(zip(lista_1, lista_2))


print(meu_dicionario)
 """



d1 = dict({"nome":"Kenzinho","cidade":"Curitiba","modulo":"M5"})

print(d1["nome"])
print(d1["cidade"])
print(d1["modulo"])
print(d1.get("telefone","a chave telefone não existe"))

print(d1.keys())
print(d1.values())

lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["999-999-999", False, 28]

d2 = dict(zip(lista_1, lista_2))

print(d2)


d1.update(d2)

print(d1)

d1.pop('casado')
print(d1)

idade = d1.pop('idade')

print(idade)

print(d1)

d1.clear()

print(d1)

d1.update(d2)
