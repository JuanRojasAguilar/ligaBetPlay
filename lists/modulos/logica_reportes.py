from .liga_globals import clear_screen, reportes_title, global_equipos

def ganador_categoria(categoria, mensaje):
  print(reportes_title)
  equipo_ganador = ""
  puntos = 0
  for equipo in global_equipos:
    if equipo[categoria] > puntos:
      puntos = equipo[categoria]
      equipo_ganador = equipo["Nombre"]
  print(f"El equipo ganador fue: {equipo_ganador} con {puntos} {mensaje}")
  input("Presiona ENTER para volver a la pantalla principal")
  clear_screen()

def equipo_mayor_goles():
  ganador_categoria(5, "goles")

def equipo_mayor_puntos():
  ganador_categoria(7, "puntos")

def mayor_partidos_ganados():
  ganador_categoria(2, "partidos")

def total_goles():
  goles = 0
  for equipo in global_equipos:
    goles += equipo[5]
  print(f"Se anotaron {goles} goles en el campeonato")
  input("Presiona ENTER para volver a la pantalla principal")
  clear_screen()

def promedio_goles():
  goles = 0
  for equipo in global_equipos:
    goles += equipo[5]
  promedio = goles / len(global_equipos)
  print(f"Se anotaron en promedio {promedio} en el campeonato")
  input("Presiona ENTER para volver a la pantalla principal")
  clear_screen()
