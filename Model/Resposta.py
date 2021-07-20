
class Resposta:
    def __init__(self,id_formulario="",resposta1="", resposta2="",resposta3="",resposta4=""):
        self.__id_formulario = id_formulario
        self.__resposta1 = resposta1
        self.__resposta2 = resposta2
        self.__resposta3 = resposta3
        self.__resposta4 = resposta4

    def getId_formulario(self):
        return self.__id_formulario

    def getResposta1(self):
        return self.__resposta1
    
    def getResposta2(self):
        return self.__resposta2

    def getResposta3(self):
        return self.__resposta3

    
    def getResposta4(self):
        return self.__resposta4
    
    
    def setId_formulario(self,id_formulario):
        self.__id_formulario = id_formulario
    
    def setResposta1(self,resposta1):
        self.__resposta1 = resposta1

    def setResposta2(self,resposta2):
        self.__resposta2 = resposta2
        
    def setResposta3(self,resposta3):
        self.__resposta3 = resposta3

    
    def setResposta4(self,resposta4):
        self.__resposta4 = resposta4