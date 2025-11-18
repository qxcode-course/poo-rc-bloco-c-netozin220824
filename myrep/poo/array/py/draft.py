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
    print('-'.join(str(x) for x in lista_int))
    n=5
    sequencia = list(range(0,n+1))
    print("seguencia", sequencia)
    print("acesso ao indice 2:", lista_int[2])
    print("Percorrendo com for-range:")
    for i in range(len(lista_int)):
        print(valor,end=' ')
    print()
    print("Percorrendo com for-indexado:")
    for i in range(len(lista_int)):
        print(lista_int[i], end=' ')
    print()
    x=2
    encontrado = False
    for valor in lista_int:
        if valor == x:
            encontrado = True
    print(f"encontrado {x}:", encontrado)
    pos = lista_int.index(x) if x in lista_int else -1
    print(f"posicao de {x}: {pos}")
    pares = [valor for valor in lista_int if valor % 2 == 0]
    print("pares:", pares)
    quadrados = [valor ** 2 for valor in lista_int]
    print("quadrados:", quadrados)
    if x in lista_int:
        lista_int.remove(x)
        print(f"removendo {x} (primeira ocorrencia {x})", lista_int)
    lista_int = [valor for valor in lista_int if valor != x]
    print(f"removendo todas as ocorrencias de {x}:", lista_int)
    lista_int = [5, 3, 1, 8, 2]
    lista_int.sort()
    print("lista ordenada:", lista_int)
    print("Metodos em lista de objetos:")
    print("exibindo cada foo:")
    for foo in lista_obj:
        foo.display()
    print('-'.join(str(f) for f in lista_obj))
if __name__ == '__main__':
    main()
