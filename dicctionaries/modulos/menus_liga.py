from tabulate import tabulate

from .liga_globals import clear_screen, equipos_title, main_title, fechas_title, reportes_title, global_equipos
from . import logicaEquipos
from . import logica_reportes
from . import logica_fechas

def menu_equipos():
    print(equipos_title)
    menu = [["1.","Registrar Equipo"], ["2.","Menu principal"]]
    print(tabulate(menu,tablefmt="grid"))
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
        menu = [["1.","Registrar equipo"],["2.","Registrar fecha de juego"], ["3.","Reportes"], ["4.","Salir"]]
        print(tabulate(menu,tablefmt="grid"))
        option = int(input("\n>>"))
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
    menu = [["A.","Nombre del equipo con más goles anotados"], ["B.","Nombre del equipo con más puntos"], ["C.","Nombre del equipo con más partidos ganados"], ["D.","Total de goles anotados por todos los equipos"], ["E.","Promedio de goles anotados en el torneo"], ["F.","Regresar al menú principal"]]
    print(tabulate(menu, tablefmt="grid"))

    option = input("\n>>").upper()

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
    elif option == "X":
        for equipo in global_equipos:
            print(f"{equipo[0]}")
        input("Presiona ENTER para volver")
        menu_reportes()
    else:
        clear_screen()
        menu_reportes()

def menu_fechas():
  clear_screen()
  print(fechas_title)
  menu=[["1.","Agregar fecha"],["2.","Salir"]]
  print(tabulate(menu,tablefmt="grid"))
  option = input("\n>>")

  if option == '1':
    if(len(global_equipos) < 2):
        print("No hay suficientes equipos registrados, presiona ENTER")
        input()
    else:
        logica_fechas.editar_fecha()
    menu_principal()
  elif option == '2':
    return
  else:
    menu_fechas
