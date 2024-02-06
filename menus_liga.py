from liga_globals import clear_screen, equipos_title, main_title, fechas_title

import logicaEquipos
import logica_fechas

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
    print(main_title)
    print("1.Registrar equipo \n2.Registrar fecha de juego \n3.Reportes \n4.Salir\n")
    option = input()
    if(option == '1'):
        clear_screen()
        menu_equipos()
        pass
    elif option == '2':
        clear_screen()
        menu_fechas()
    elif option == '3':
        clear_screen()
        menu_reportes()
    else:
        clear_screen()
        exit()

def menu_reportes():
    print("Menu reportes")
    print("A.Nombre del equipo con más goles anotados \nB.Nombre del equipo con más puntos \nC.Nombre del equipo con más partidos ganados \nD.Total de goles anotados por todos los equipos \nE.Promedio de goles anotados en el torneo \nF.Regresar al menú principal")

    option = input().upper()

    if option == 'A':
        pass
    elif option == 'B':
        pass
    elif option == 'C':
        pass
    elif option == 'D':
        pass
    else:
        clear_screen()
        menu_principal()

def menu_fechas():
    print(fechas_title)
    print("1.Añade una fecha \n2.Menú principal\n")
    option = input()
    if option == '1':
        clear_screen()
        logica_fechas.agregar()
        menu_principal()
    else:
        clear_screen()
        menu_principal()

