from liga_globals import clear_screen, equipos_title, global_equipos

def agregar():
    print(equipos_title)
    nombre_equipo = input("Cuál es el nombre del equipo? ").capitalize()
    equipo = {
        "Nombre": nombre_equipo,
        "PJ": 0,
        "PG": 0,
        "PP": 0,
        "PE": 0,
        "GF": 0,
        "GC": 0,
        "TP": 0,
        }
    global_equipos.append(equipo)
    clear_screen()