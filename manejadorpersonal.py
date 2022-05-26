from clasepersonal import personal
from manejadornovedad import novedad
import numpy as np
import csv

class manejadorPersonal:
    __dimension=None
    __incremento=None
    __cantidad=None
    __arreglo=None
    def __init__(self):
        self.__dimension=5
        self.__incremento=5
        self.__cantidad=0
        self.__arreglo=np.empty(5,dtype=personal)
    def agregar(self,instancia):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__cantidad
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = instancia
        self.__cantidad+=1
    def leercsv(self):
        archivo=open('personal.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for row in reader:
            if bandera:
                bandera=False
            else:
                instancia=personal(row[0],row[1],row[2],row[3],row[4])
                self.agregar(instancia)
        archivo.close()
    def buscarlegajo(self,numero):
        i=0
        while i < self.__dimension and self.__arreglo[i].getLegajo() != numero:
            i+=1
        if i == self.__dimension:
            i=-1
        return i
    def retornarSueldoLegajo(self,numerodeLegajo):
        sueldo=None
        n=self.buscarlegajo(numerodeLegajo)
        if n != -1:
            sueldo=self.__arreglo[i].getSueldo
        return sueldo
