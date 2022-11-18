lista_1 = list(range(6,21))

print(lista_1)
print(lista_1[-1])

lista_1[1] = "Kenzie"

print(lista_1)
print(lista_1[2:5])
lista_1[-1] = "Academy"
print(lista_1)

lista_1.remove("Kenzie")
lista_1.remove("Academy")

print(lista_1)

lista_2 = lista_1
lista_2.reverse()
print(lista_2)

lista_1_tamanho = len(lista_1)

lista_2_tamanho = len(lista_2)

print(lista_1_tamanho)
print(lista_2_tamanho)

lista_1.pop()
lista_2.pop()

print(lista_1)

print(lista_2)

lista_1.clear()
lista_2.clear()

print(lista_1)

print(lista_2)
