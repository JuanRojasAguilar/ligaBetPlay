from click import clear
from .liga_globals import clear_screen, equipos_title, main_title, fechas_title, reportes_title, global_equipos

from . import logicaEquipos
from . import logica_reportes
from . import logica_fechas

def menu_equipos():
    print(equipos_title)
    print("1.Registrar Equipo \n2.Menu principal\n")
    option = input()
    if option == '1':
        clear_screen()
        logicaEquipos.agregar()
        menu_principal()
    else:
        clear_screen()
        menu_principal()


def menu_principal():
    try:
        clear_screen()
        print(main_title)
        print("1.Registrar equipo \n2.Registrar fecha de juego \n3.Reportes \n4.Salir\n")
        option = int(input())
        if(option == 1):
            clear_screen()
            menu_equipos()
        elif option == 2:
            clear_screen()
            menu_fechas()
        elif option == 3:
            clear_screen()
            menu_reportes()
        elif option == 4:
            clear_screen()
            exit()
        else:
            menu_principal()
    except ValueError:
        menu_principal()

def menu_reportes():
    print(reportes_title)
    print("A.Nombre del equipo con más goles anotados \nB.Nombre del equipo con más puntos \nC.Nombre del equipo con más partidos ganados \nD.Total de goles anotados por todos los equipos \nE.Promedio de goles anotados en el torneo \nF.Regresar al menú principal\n")

    option = input().upper()

    if len(global_equipos) < 2:
        input("No hay suficientes equipos")
        menu_principal()

    if option == 'A':
        clear_screen()
        logica_reportes.equipo_mayor_goles()
        menu_principal()
    elif option == 'B':
        clear_screen()
        logica_reportes.equipo_mayor_puntos()
        menu_principal()
    elif option == 'C':
        clear_screen()
        logica_reportes.mayor_partidos_ganados()
        menu_principal()
    elif option == 'D':
        clear_screen()
        logica_reportes.total_goles()
        menu_principal()
    elif option == "E":
        clear_screen()
        logica_reportes.promedio_goles()
        menu_principal()
    elif option == "F":
        menu_principal()
    else:
        clear_screen()
        menu_reportes()

def menu_fechas():
    print(fechas_title)
    print("1.Añade una fecha \n2.Menú principal\n")
    option = input()
    if option == '1':
        clear_screen()
        logica_fechas.agregar()
        menu_principal()
    elif option == '2':
        clear_screen()
        menu_principal() 
    else:
        clear_screen()
        menu_fechas()

