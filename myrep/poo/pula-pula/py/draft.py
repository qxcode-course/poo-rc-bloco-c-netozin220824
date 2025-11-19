class Criança:
    def __init__(self, nome:str, idade:int):
        self.__nome = nome
        self.__idade = idade
    def getIdade(self):
        return self.__idade
    def getNome(self):
        return self.__nome
    def setIdade(self, idade:int):
        self.__idade = idade
    def setNome(self, nome:str):
        self.__nome = nome
    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
class Pulapula:
    def __init__(self):
        self.__pulando:list[Criança | None] = []
        self.__espera:list[Criança | None] = []
    def arrive(self, nome:str, idade:int):
        criança = Criança(nome, idade)
        self.__espera.insert(0, criança)
    def entrar(self):
        if not self.__espera:
           print(f"fila vazia")
        self.__pulando.insert(0, self.__espera[len(self.__espera)-1])
        self.__espera.pop(len(self.__espera)-1)
    def remove(self, nome:str):
        for i, Criança in enumerate(self.__pulando):
            if Criança.getNome()==nome:
                self.__pulando.pop(i)
                return
            
            