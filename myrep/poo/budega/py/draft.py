class Person:
    def __init__(self, nome: str):
        self.__nome: str = nome

    def getNome(self):
        return self.__nome

    def __str__(self):
        return self.__nome


class Mercado:
    def __init__(self, n_caixas: int):
        self.counters = [None for _ in range(n_caixas)]
        self.waiting: list[Person] = []

    def __str__(self):
        caixas = ', '.join(
            str(cliente) if cliente is not None else '-----'
            for cliente in self.counters
        )
        espera = ', '.join(str(cliente) for cliente in self.waiting)
        return f'Caixas: [{caixas}]\nEspera: [{espera}]'

    def arrive(self, person: Person):
        self.waiting.append(person)

    def call(self, index: int):
        if index < 0 or index >= len(self.counters):
            print('fail: caixa inexistente')
            return
        if not self.waiting:
            print('fail: sem clientes')
            return
        if self.counters[index] is not None:
            print('fail: caixa ocupado')
            return
        self.counters[index] = self.waiting.pop(0)

    def finish(self, index: int):
        if index < 0 or index >= len(self.counters):
            print('fail: caixa inexistente')
            return None
        if self.counters[index] is None:
            print('fail: caixa vazio')
            return None
        person = self.counters[index]
        self.counters[index] = None
        return person


def main():
    mercado: Mercado | None = None
    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == '':
            continue

        parts = line.split()
        cmd = parts[0]

        # imprime exatamente como o gabarito: com '$' antes
        # ex: "init 2" -> "$init 2"
        print('$' + line)

        if cmd == 'end':
            break
        elif cmd == 'init':
            n_caixas = int(parts[1])
            mercado = Mercado(n_caixas)
        elif cmd == 'show':
            if mercado is not None:
                print(mercado)
        elif cmd == 'arrive':
            nome = parts[1]
            mercado.arrive(Person(nome))
        elif cmd == 'call':
            index = int(parts[1])
            mercado.call(index)
        elif cmd == 'finish':
            index = int(parts[1])
            mercado.finish(index)
        else:
            print('fail: comando invalido')


if __name__ == '__main__':
    main()
