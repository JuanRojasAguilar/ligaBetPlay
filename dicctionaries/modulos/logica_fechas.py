from tabulate import tabulate

from .liga_globals import fechas_title, clear_screen, global_equipos, encontrar_equipo

def editar_fecha():
  print(tabulate(global_equipos, headers="keys",tablefmt="grid"))
  primer_equipo = input("\nCómo se llama el equipo local? ").capitalize()
  equipo1 = encontrar_equipo(primer_equipo)
  if not(equipo1):
    print("No existe ese equipo")
    input("Pulsa ENTER para volver al menu principal")
    return

  segundo_equipo = input("Cómo se llama el equipo visitante? ").capitalize()
  equipo2 = encontrar_equipo(segundo_equipo)
  if not(equipo2):
    print("No existe ese equipo")
    input("Pulsa ENTER para volver al menu principal")
    return
  
  clear_screen()
  print(fechas_title)
  goles_primer_equipo = int(input(f"Cuántos goles metió {primer_equipo}: "))
  goles_segundo_equipo = int(input(f"Cuantos goles metió {segundo_equipo}: "))

  equipo1["PJ"] += 1
  equipo1["GF"] += goles_primer_equipo
  equipo1["GC"] += goles_segundo_equipo

  equipo2["PJ"] += 1
  equipo2["GF"] += goles_segundo_equipo
  equipo2["GC"] += goles_primer_equipo

  if goles_primer_equipo > goles_segundo_equipo:
    equipo1["TP"] += 3
    equipo1["PG"] += 1
    equipo2["PP"] += 1
  elif goles_segundo_equipo > goles_primer_equipo:
    equipo2["TP"] += 3
    equipo2["PG"] += 1
    equipo1["PP"] += 1
  else:
    equipo1["TP"] += 1
    equipo1["PE"] += 1
    equipo2["TP"] += 1
    equipo2["PE"] += 1

  print(tabulate([equipo1, equipo2], headers="keys", tablefmt="grid"))
  input("Presiona enter para volver al menú principal")
  return
