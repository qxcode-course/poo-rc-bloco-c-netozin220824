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
        self.__seats= [None]*capacidade
        self.__search= [None]*capacidade
        self.__verifyindex=capacidade
    def__str_(self):
    print("[",end="")
    ]")