class Client:
    def __init__(self,id:str ,phone:int):
        self.__id:str = id
        self.__phone:int = phone
    def getPhone(self):
        return self.__phone
    def getId(self):
        return self.__id
    def setPhone(self,phone:int):
        self.__phone = phone
    def setId(self,id:str):
        self.__id = id
    def __str__(self):
        return f"{self.__id}:{self.__phone}"
class Cinema:
    def __init__(self,capacidade:int):
        self.__seats = [None]*capacidade
        self.__search = [None]*capacidade
        self.__verifyindex = capacidade
    def __str__(self):
        print("[",end="")
        ky=" ".join("-" if i is None else str(i)for i in self.__seats)
        ky+="]"
        return ky
    def reserve(self, id: str, phone:int, index:int):
        if index <0 or index>= self.__verifyindex:
            print("fail: cadeira nao existe")
            return False
        elif self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        elif id in self.__search:
            print("fail: cliente ja esta no cinema")
        client = Client(id, phone)
        self.__seats[index] = client
        self.__search.append(client.getId())
        return 
    def cancel(self, id:str):
        if id not in self.__search:
            print("fail: cliente nao esta no cinema")
            return 
        self.__search.remove(id)
        for i, cliente in enumerate(self.__seats):
            if cliente.getId()== id:
                self.__seats[i] = None
                return 
def main():
    cinema:Cinema = Cinema(0)
    while True:
        line= input()
        print(f"${line}")
        args = line.split()
        if args[0]=="end":
            break
        elif args[0]=="init":
            cinema=Cinema(int(args[1]))
        elif args[0]=="show":
            print(cinema) 
        elif args[0]=="reserve":
            cinema.reserve(args[1], int(args[2]), int(args[3]))
        elif args[0]=="cancel":
            cinema.cancel(args[1])
        else:
            print("fail: comando invalido")
main()
    
