def menuprincipal ():
    continuar = True
    while(continuar):
        opcioncorrecta = False
        while(not opcioncorrecta):
            print("===Menu Principal===")
            print("1-. Listar Pokemons")
            print("2-. Nueva Entrada Pokedex")
            print("3-. Actualizar Pokedex")
            print("4-. Eliminar Entrada Pokedex")
            print("5-. Salir")
            print("===")
             opcion =int(input("Seleccione una opcion: "))

            if opcion <1 or opcion >5:
                print("Opcion Incorrecta, Intente Nuevamente...")
                elif opcion = 5:
                    continuar = False
                    print("Graciasd por usar la Pokedex!")
                    break 
             else:
                opcioncorrecta =  True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    print(opcion)

menuprincipal()


        