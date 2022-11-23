""" import math

def delta(a, b, c):
    return pow(b, 2) - 4 * a * c

def bhaskara(a, b, c):
    resultado_delta = delta(a, b, c)

    if resultado_delta < 0:
        return 'Delta negativo'

    raiz_delta = round(math.sqrt(resultado_delta), 2)

    x1 = round((-b + raiz_delta) / (2 * a), 2)
    x2 = round((-b - raiz_delta) / (2 * a), 2)

    return f'x1={x1}, x2={x2}'

print(bhaskara(1, 5, 2))
# x1=-0.44, x2=-4.56
print(bhaskara(3, 10, 2))
# x1=-0.21, x2=-3.12 """


""" for numero in range(10):
  # Checa se o numero está contido na lista de numeros
    if numero in [4, 5, 6, 7, 8]:
        continue
    print(numero) """

""" 
def corresponding_parenthesis(text: str):
  left = text.count("(")
  right = text.count(")")
  difference = left - right

  if difference > 0:
      return "(" * difference
  elif difference < 0:
      return ")" * (difference * -1)

  return ""
 """
""" 
def remove_more_than_two_repetitions(text: str):
  response = []
  response.append(text[0])
  response.append(text[1])

  print (response)

  for index, char in enumerate(text[2:], 2):
      if text[index - 1] != char or text[index - 2] != char:
          response.append(char)

  return "".join(response)


text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"

text = remove_more_than_two_repetitions(text)
print(text) """
""" 
string = 'Kenzie'

for letra in string:
    print(letra)



for i in range(4):
    print(i)

for _ in range(3):
    print('Olá Kenzie')


contador = 0

while contador <= 5:
    print(f'Contando: {contador}')
    contador += 1

print('Fim da contagem')


minha_string = "Churros"
# Podemos desempacotar a tupla em indice e item
for indice, item in enumerate(minha_string):
    print(indice, item)


result = corresponding_parenthesis("()()")
print(result) """



minha_lista = [3, "abacate", 9.7, [4, 5, 6], (3, "j")]
minha_lista[3]
[4, 5, 6]

# Utilizando a função list() para trabalhar com lista:
minha_lista = list("abc")
minha_lista
['a', 'b', 'c']

minha_lista = list(123)
