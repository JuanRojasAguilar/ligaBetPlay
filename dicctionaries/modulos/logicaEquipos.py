from .liga_globals import clear_screen, equipos_title, global_equipos

def agregar():
    print(equipos_title)
    nombre_equipo = input("Cuál es el nombre del equipo? ").capitalize()
    #PJ, PG, PP, PE, GF, GC, TP
    equipo = {
            "Nombre": nombre_equipo,
            "PJ": 0,
            "PG": 0,
            "PP": 0,
            "GF": 0,
            "GC": 0,
            "TP": 0,
            }
    global_equipos.append(equipo)
    print(global_equipos)
    input("Presiona ENTER para continuar...")
    clear_screen()
