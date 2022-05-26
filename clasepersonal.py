class personal:
    __legajo=None
    __dni=None
    __apellido=None
    __nombre=None
    __sueldo=None
    __sueldoaCobrar=None
    def __init__(self,legajo,dni,ap,nom,sueldo):
        self.__legajo=legajo
        self.__dni=dni
        self.__apellido=ap
        self.__nombre=nom
        self.__sueldo=sueldo
    def getLegajo(self):
        return self.__legajo
    def getSueldo(self):
        return self.__sueldo
    def sueldoacobrar(self,n):
        self.__sueldoaCobrar=n
    def __gt__(self, other):
        bandera=None
        if self.__apellido > other.__apellido:
            bandera=True
        elif self.__apellido == other.__apellido and self.__nombre > other.__nombre:
            bandera= True
        else:
            bandera=False
        return  bandera
