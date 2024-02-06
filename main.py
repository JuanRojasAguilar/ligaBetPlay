from globals import clear_screen

from menus import main_title, menu_equipos, menu_reportes

def menu_principal():
    print(main_title)
    print("1.Registrar equipo \n2.Registrar fecha de juego \n3.Reportes \n4.Salir\n")
    option = input()
    if(option == '1'):
        clear_screen()
        menu_equipos()
        pass
    elif option == '2':
        pass
    elif option == '3':
        clear_screen()
        menu_reportes()
    else:
        clear_screen()
        exit()

def main():
    menu_principal()

main()