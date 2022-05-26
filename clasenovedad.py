class novedad:
    __legajo=None
    __importe=None
    __concepto=None
    __codigo=None
    def __init__(self,legajo,imp,concepto,cod,):
        self.__legajo=legajo
        self.__importe=imp
        self.__concepto=concepto
        self.__codigo=cod
    def getLegajo(self):
        return self.__legajo
    def getCodigo(self):
        return self.__codigo
    def getImporte(self):
        return self.__importe
