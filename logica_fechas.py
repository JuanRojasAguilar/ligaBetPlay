from liga_globals import fechas_title, clear_screen, global_equipos, encontrar_indice_equipo

dias_juegos = ["06-feb-2024", "09-feb-2024", "11-feb-2024", "13-feb-2024", "17-feb-2024"]

def agregar():
  print(fechas_title)
  i = 1
  for dias in dias_juegos:
    print(i, dias)
    i += 1
  fecha = input('\nCuál fecha vas a editar? ')
  if fecha == '1':
    editar_fecha(dias_juegos[0])
  elif fecha == '2':
    editar_fecha(dias_juegos[1])
  elif fecha == '3':
    editar_fecha(dias_juegos[2])
  elif fecha == '4':
    editar_fecha(dias_juegos[3])
  elif fecha == '5':
    editar_fecha(dias_juegos[4])
  else:
    clear_screen()

def editar_fecha(fecha):
  primer_equipo = input("Cómo se llama el primer equipo? ").capitalize()
  segundo_equipo = input("Cómo se llama el segundo equipo? ").capitalize()
  clear_screen()
  print(fechas_title)
  goles_primer_equipo = int(input(f"Cuántos goles metió {primer_equipo}: "))
  goles_segundo_equipo = int(input(f"Cuantos goles metió {segundo_equipo}: "))


  indice_primer_equipo = encontrar_indice_equipo(primer_equipo)
  indice_segundo_equipo = encontrar_indice_equipo(segundo_equipo)

  posicion_primer_equipo = global_equipos[indice_primer_equipo]
  posicion_segundo_equipo = global_equipos[indice_segundo_equipo]

  posicion_primer_equipo['PJ'] += 1
  posicion_primer_equipo['GF'] += goles_primer_equipo
  posicion_primer_equipo['GC'] += goles_segundo_equipo

  posicion_segundo_equipo['PJ'] += 1
  posicion_segundo_equipo['GF'] += goles_segundo_equipo
  posicion_segundo_equipo['GC'] += goles_primer_equipo

  if goles_primer_equipo > goles_segundo_equipo:
    posicion_primer_equipo['PG'] += 1
    posicion_primer_equipo["TP"] += 2
    posicion_segundo_equipo['PP'] += 1
  elif goles_segundo_equipo > goles_primer_equipo:
    posicion_segundo_equipo["PG"] += 1
    posicion_segundo_equipo["TP"] += 2
    posicion_primer_equipo["PP"] += 1
  else:
    posicion_primer_equipo["PE"] += 1
    posicion_primer_equipo["TP"] += 1
    posicion_segundo_equipo["PE"] += 1
    posicion_segundo_equipo["TP"] += 1

  print(posicion_primer_equipo, posicion_segundo_equipo, sep="\n")
  input("Presiona enter para volver al menú principal")
  clear_screen()
