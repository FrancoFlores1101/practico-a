from manejadornovedad import manejadorNovedad
from manejadorpersonal import manejadorPersonal

def buscar():
    n=int(input('ingrese el legajo a buscar su sueldo\n'))
    total=manejador1.retornarSueldoLegajo(n)
    total+=manejador2.totalNovedades(n)
    print('el nro de legajo {0} tiene un sueldo a cobrar de {1}'.format(n,total))






def menu():
    print('Menu')
    print(' 1:Buscar por legajo\n 2:Obtener Listado\n 3:Obtener sueldo mas bajo\n 0:salir\n')
    n=int(input())
    while n!= 0:
        if n==1:
            buscar()
        elif n==2:
            listar()
        else:
            masbajo()
    print('1:Buscar por legajo\n 2:Obtener Listado\n 3:Obtener sueldo mas bajo\n 0:salir')
    n=int(input())


if __name__ == '__main__':
    manejador1=manejadorPersonal()
    manejador2=manejadorNovedad()
    manejador1.leercsv()
    manejador2.leercsv(manejador1)
