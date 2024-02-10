import os

def clear_screen(): 
  os.system("clear")

global_equipos = []

def encontrar_equipo(nombre):
  for equipo in global_equipos:
    if equipo["Nombre"] == nombre:
      return equipo

main_title = """
    ++++++++++++++++++++++++++++++
    + LIGA BETPLAY COLOMBIA 2024 +
    ++++++++++++++++++++++++++++++
    """

equipos_title = """ 
    +++++++++++++++++++ 
    + MENU DE EQUIPOS + 
    +++++++++++++++++++
"""

reportes_title ="""
            +++++++++++++++++++++++
            + REPORTES DEL TORNEO +
            +++++++++++++++++++++++
            """

fechas_title = """
            +++++++++++++++++++
            + FECHAS DE JUEGO +
            +++++++++++++++++++
"""
