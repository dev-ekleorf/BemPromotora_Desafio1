
class Formulario:
    def __init__(self,id="",titulo="", descricao="",perguntas=[]):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__perguntas= perguntas

    def getId(self):
        return self.__id

    def getTitulo(self):
        return self.__titulo
    
    def getDescricao(self):
        return self.__descricao

    def getPerguntas(self):
        return self.__perguntas
    
    
    def setId(self,id):
        self.__id = id
    
    def setTitulo(self,titulo):
        self.__titulo = titulo

    def setDescricao(self,descricao):
        self.__descricao = descricao
        
    def setPerguntas(self,perguntas):
        self.__perguntas = perguntas