import csv
from clasenovedad import novedad
from manejadorpersonal import manejadorPersonal

class manejadorNovedad:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def leercsv(self,unmanejador:manejadorPersonal):
        archivo=open('novedades.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for row in reader:
            if bandera:
                bandera=False
            else:
                if unmanejador.buscarlegajo(row[0]) != -1:
                    instancia=novedad(row[0],row[1],row[2],row[3])
                    self.__lista.append(instancia)

    def totalNovedades(self,numero):
        total=0
        for novedad in self.__lista:
            if novedad.getLegajo() == numero:
                if novedad.getCodigo()== 'D':
                    total-= novedad.getImporte()
                else:
                    total+=novedad.getImporte()
        return total
    def listar(self):
        for novedad in self.__lista:
            print(novedad.getLegajo)
