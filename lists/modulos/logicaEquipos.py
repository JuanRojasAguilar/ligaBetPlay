from .liga_globals import clear_screen, equipos_title, global_equipos

def agregar():
    print(equipos_title)
    nombre_equipo = input("Cuál es el nombre del equipo? ").capitalize()
    #PJ, PG, PP, PE, GF, GC, TP
    equipo = [nombre_equipo,0,0,0,0,0,0,0]
    global_equipos.append(equipo)
    clear_screen()