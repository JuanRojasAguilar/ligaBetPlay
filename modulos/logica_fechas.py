from .liga_globals import fechas_title, clear_screen, global_equipos, encontrar_equipo

dias_juegos = ["06-feb-2024", "09-feb-2024", "11-feb-2024", "13-feb-2024", "17-feb-2024"]

def agregar():
  clear_screen()
  print(fechas_title)
  i = 1
  for dias in dias_juegos:
    print(i, dias)
    i += 1
  fecha = input('\nCuál fecha vas a editar? ')

  if(len(global_equipos) < 2):
    print("No hay suficientes equipos registrados, presiona ENTER")
    input()
    return
  if fecha == '1':
    editar_fecha()
  elif fecha == '2':
    editar_fecha()
  elif fecha == '3':
    editar_fecha()
  elif fecha == '4':
    editar_fecha()
  elif fecha == '5':
    editar_fecha()
  else:
    clear_screen()
    return()

def editar_fecha():
  primer_equipo = input("Cómo se llama el primer equipo? ").capitalize()
  indice_primer_equipo = encontrar_equipo(primer_equipo)
  if not(indice_primer_equipo):
    print("No existe ese equipo")
    input("Pulsa ENTER para volver al menu principal")
    agregar()

  segundo_equipo = input("Cómo se llama el segundo equipo? ").capitalize()
  indice_segundo_equipo = encontrar_equipo(segundo_equipo)
  if not(indice_segundo_equipo):
    print("No existe ese equipo")
    input("Pulsa ENTER para volver al menu principal")
    agregar()
  
  clear_screen()
  print(fechas_title)
  goles_primer_equipo = int(input(f"Cuántos goles metió {primer_equipo}: "))
  goles_segundo_equipo = int(input(f"Cuantos goles metió {segundo_equipo}: "))

  indice_primer_equipo[1] += 1
  indice_primer_equipo[5] += goles_primer_equipo
  indice_primer_equipo[6] += goles_segundo_equipo

  indice_segundo_equipo[1] += 1
  indice_segundo_equipo[5] += goles_segundo_equipo
  indice_segundo_equipo[6] += goles_primer_equipo

  if goles_primer_equipo > goles_segundo_equipo:
    indice_primer_equipo[2] += 1
    indice_primer_equipo[7] += 3
    indice_segundo_equipo[3] += 1
  elif goles_segundo_equipo > goles_primer_equipo:
    indice_segundo_equipo[2] += 1
    indice_segundo_equipo[7] += 3
    indice_primer_equipo[3] += 1
  else:
    indice_primer_equipo[4] += 1
    indice_primer_equipo[7] += 1
    indice_segundo_equipo[4] += 1
    indice_segundo_equipo[7] += 1

  print(indice_primer_equipo, indice_segundo_equipo, sep="\n")
  input("Presiona enter para volver al menú principal")
  clear_screen()
