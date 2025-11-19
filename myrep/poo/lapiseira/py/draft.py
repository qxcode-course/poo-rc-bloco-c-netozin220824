class Grafite:
    def __init__(self,calibre:float,dureza:str,tamanho:int):
        self.__calibre:float = calibre
        self.__dureza:str = dureza
        self.__tamanho:int = tamanho
    def sagePerSheet(self):
        if self.__dureza == "HB": 
            return 1
        if self.__dureza == "2B":
            return 2
        if self.__dureza == "4B":
            return 4
        else:
            return 6
    def setTamanho(self,tamanho:int):
        self.__tamanho = tamanho
    def __str__(self):
        return f"[{self.__calibre}:{self.__dureza}:{self.__tamanho}]"
    def get_calibre(self):
        return self.__calibre
    def get_dureza(self):
        return self.__dureza
    def get_Tamanho(self):
        return self.__tamanho
class Lapiseira:
    def __init__(self, calibre: float = 0, lead: Grafite | None = None):
        self.__calibre = calibre
        self.__lead = lead
        self.__barrel = []
    def hasGrafite(self) -> bool:
        return self.__lead is not None
    def insert(self, grafite: Grafite):
        if self.__calibre != grafite.get_calibre():
            print("fail: calibre incompatível")
            return
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return 
        self.__barrel.append(grafite)
    def pull(self):
        if self.__lead is not None: 
            print("fail: ja existe grafite no bico")
            return
        if len(self.__barrel) == 0:
            print("fail: não existe grafite no tambor")
            return
        self.__lead = self.__barrel[0]
        self.__barrel.pop(0)
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return 
        self.__lead = None
    def write(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite no bico")
            return
        if self.__lead.get_Tamanho() <= 10:
            print("fail: tamanho insuficiente")
            return
        k = self.__lead.sagePerSheet()
        if self.__lead.get_Tamanho() - k < 10:
            print("fail: folha incompleta")
            self.__lead.setTamanho(10)
            return
        self.__lead.setTamanho(self.__lead.get_tamanho() - k)
    def __str__(self):
        lead = "[]" if self.__lead is None else str(self.__lead)
        ans = f"calibre: {self.__calibre}, bico: {lead}, tambor: <"
        for i, p in enumerate(self.__barrel):
            if p is not None:
                ans+= str(p)
        ans +=">"
        return ans
def main():
    lapiseira: Lapiseira= Lapiseira()
    while True:
        line= input()
        print(f"${line}")
        args= line.split()
        if args[0]=="end":
            break
        elif args[0]=="init":
            lapiseira= Lapiseira(float(args[1]))   
        elif args[0]=="show":
            print(lapiseira) 
        elif args[0]=="insert":
            grafite= Grafite(float(args[1]),args[2],int(args[3]))
            lapiseira.insert(grafite)
        elif args[0]=="remove":
            lapiseira.remove()
        elif args[0]=="write":
            lapiseira.write()
        elif args[0]=="pull":
            lapiseira.pull()
        else:
            print("fail: comando invalido")
main()