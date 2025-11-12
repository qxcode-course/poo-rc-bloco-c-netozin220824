class Person:
    def __init__(self,nome: str):
        self.__nome: str = nome
    def getNome(self):
        return self.__nome
    def __str__(self):
        return f"Nome: {self.__nome}"
class Mercado:
    def __init__(self,n_caixas: int):
        self.caixa = [None for _ in range(n_caixas)]
        self.fila = []
    def __str__(self):
        caixas = ', '.join(str(cliente) if cliente is not None else '-----' for cliente in self.caixa)
        espera = ', '.join(str(cliente) for cliente in self.fila)
        return f'Caixas: [{caixas}]\nEspera: [{espera}]'
    def arrive(self,person:Person):
        self.fila.append(person)
    def call(self,index:int):
        if not self.fila:
            print('fail:sem clientes')
            return
        if index <0 or index >= len(self.caixa):
            print('fail:caixa inexistente')
        if self.caixa[index] is not None:
            print('fail:caixa ocupado')
            return
        self.caixa[index] = self.fila.pop(0)
        