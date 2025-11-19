class Client:
    def __init__(self,id:str ,phone:int):
        self.__id:str = id
        self.__phone:int = phone
    def getPhone(self):
        return self.__phone
    def getid(self):
        return self.__id
    def setPhone(self,phone:int):
        self.__phone = phone
    def setid(self,id:str):
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
        if index <0 or index>= self.__verifyIndex:
            print("fail: cadeira nao existe")
            return False
        elif self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        elif id in self.__search:
            print("fail: cliente ja esta no cinema")
        client = Client(id, phone)
        self.__seats[index] = client
        self.__search.append(client.getid())
        return 
    
