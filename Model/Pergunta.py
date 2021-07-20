
class Pergunta:
    def __init__(self,id="",texto="", opcao1="",opcao2="",opcao3="",opcao4=""):
        self.__id = id
        self.__texto = texto
        self.__opcao1 = opcao1
        self.__opcao2 = opcao2
        self.__opcao3 = opcao3
        self.__opcao4 = opcao4

    def __repr__(self):
     return str(self.__dict__)


    def getId(self):
        return self.__id

    def getTexto(self):
        return self.__texto

    def getOpcao1(self):
        return self.__opcao1
    
    
    def getOpcao2(self):
        return self.__opcao2
        
    def getOpcao3(self):
        return self.__opcao3
        
    def getOpcao4(self):
        return self.__opcao4

    
    def setOpcao1(self,opcao1):
        self.__opcao1 = opcao1
        
    def setOpcao2(self,opcao2):
        self.__opcao2 = opcao2
        
    def setOpcao3(self,opcao3):
        self.__opcao3 = opcao3
        
    def setOpcao4(self,opcao4):
        self.__opcao4 = opcao4
    