class Foo:
    def __init__(self, value: int):
        self.value = value

    def display(self):
        print(f"Foo{self.value}")
def main():
    lista_vazia_int: list[int] = []
    lista_vazia_obj: list[Foo] = []
    lista_int: list[int] = [1, 2, 3, 4, 5]
    lista_obj: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]
    print("Lista vazia de inteiros:", lista_vazia_int)
    print("Lista vazia de objetos:", ', '.join(str(x) for x in lista_vazia_obj))
    print("Lista de inteiros:", lista_int)
    print("Lista de objetos:", ', '.join(str(x) for x in lista_obj))
    print('len(lista_int):', len(lista_int))
    lista_int.append(6)
    print("append(6):", lista_int)
    valor=lista_int.pop()
    print("pop():", valor, lista_int)
    lista_int.insert(0, 99)
    print('insert(0, 99):', lista_int)
    valor = lista_int.pop(0)
    print('pop(0) ->', valor, lista_int)
    lista_int.insert(2, 42)
    print('insert(2, 42):', lista_int)
    valor = lista_int.pop(2)
    print('pop(2) ->', valor, lista_int)
    