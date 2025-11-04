class Cliente:
    def __init__(self,nome: str):
        self.__nome: str = nome
    def getNome(self):
        return self.__nome
    def toString(self):
        return f"Nome: {self.__nome}"
class Mercado:
    def __init__(self,n_caixas: int):
        self.caixas: list[Cliente | None] = []
        self.fila: list[Cliente] = []
        for i in range(n_caixas):
            self.caixas.append (None)
    def toString(self):
        self.string_caixas:str = "Caixas: ["
        for elemento in range(len(self.caixas)):
            if(self.caixas[elemento] != None):
                self.string_caixas += f'{self.caixas[elemento]}'
            else:
                self.string_caixas += "-----"
            if(elemento < len(self.caixas)-1):
                self.string_caixas += ","
        self.string_caixas += "]"
        self.string_fila:str = "Fila: ["
        for elemento in range(len(self.fila)):
            self.string_fila += f"{self.fila[elemento].getNome()}"
            if(elemento < len(self.fila)-1):
                self.string_fila += ","
        self.string_fila = "]\n"
        return f"{self.string_caixas}\n{self.string_fila}"