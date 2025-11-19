import random

class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'

    def __eq__(self, other):
        if isinstance(other, Foo):
            return self.x == other.x
        return False

lista_vazia: list[int] = []
lista_vazia_objetos: list[Foo] = []

lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_preenchida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

print(len(lista_vazia))
print(len(lista_preenchida))

lista_vazia.append(10)
lista_preenchida.append(6)
lista_preenchida_objetos.append(Foo(6))

lista_vazia.pop()
lista_preenchida.pop()
lista_preenchida_objetos.pop()

lista_vazia.insert(0, 0)
lista_preenchida.insert(0, 0)
lista_preenchida_objetos.insert(0, Foo(0))

lista_vazia.pop(0)
lista_preenchida.pop(0)
lista_preenchida_objetos.pop(0)

lista_preenchida.insert(2, 99)
lista_preenchida.pop(2)

print(", ".join(map(str, lista_preenchida)))

sequencia = list(range(5))
print(sequencia)

aleatorios = [random.randint(1, 10) for _ in range(5)]
print(aleatorios)

print(lista_preenchida[2])

for item in lista_preenchida:
    print(item)

for i in range(len(lista_preenchida)):
    print(lista_preenchida[i])

procurado = 3
encontrado = False
for item in lista_preenchida:
    if item == procurado:
        encontrado = True
        break
print(encontrado)

print(procurado in lista_preenchida)

pares = [x for x in lista_preenchida if x % 2 == 0]
print(pares)

quadrados = [x ** 2 for x in lista_preenchida]
print(quadrados)

if procurado in lista_preenchida:
    lista_preenchida.remove(procurado)
print(lista_preenchida)

lista_com_repetidos = [1, 2, 2, 3, 2, 4]
lista_com_repetidos = [x for x in lista_com_repetidos if x != 2]
print(lista_com_repetidos)

lista_preenchida.sort()
print(lista_preenchida)

random.shuffle(lista_preenchida)
print(lista_preenchida)
