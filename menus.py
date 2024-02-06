from main import menu_principal
from globals import clear_screen, equipos_title

import logicaEquipos

def menu_equipos():
    print(equipos_title)
    print("1.Registrar Equipo \n2.Borrar equipo \n3.Menu principal\n")
    option = input()
    if option == '1':
        clear_screen()
        logicaEquipos.agregar()
    elif option == '2':
        clear_screen()
        logicaEquipos.borrar()
    else:
        clear_screen()
        menu_principal()


def menu_reportes():
    title = """
            +++++++++++++++++++++++
            + REPORTES DEL TORNEO +
            +++++++++++++++++++++++
            """
    print(title)
    print("A.Nombre del equipo con más goles anotados \nB.Nombre del equipo con más puntos \nC. Nombre del equipo con más partidos ganados \nD. Total de goles anotados por todos los equipos \nE.Promedio de goles anotados en el torneo \nF. Regresar al menú principal")

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