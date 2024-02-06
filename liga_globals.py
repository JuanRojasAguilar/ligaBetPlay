import os

def clear_screen(): 
    os.system("clear")

global_equipos = []

def encontrar_indice_equipo(equipo):
  for i, list in enumerate(global_equipos):
    if list.get('Nombre') == equipo:
      return i

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