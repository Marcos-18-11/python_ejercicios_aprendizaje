#Al iniciar el programa se debe mostrar el siguiente menú, 
# 1 añadir nota, 
# 2 Mostrar notas externas, 
# 3 Total de aprobados, 4 Nota media, 
# 5 Mostrar todas
# 6 Salir

#El usuario elige una opción del 1 al 6 
#y el programa le mestra o le ide los datos necesarios, 
# para llevarla acabo, 
# después vuelve a salir el menú hasta que elija la opción de salir
notas=[]
activo=True
while activo:
    print("                            ")
    print("|--------------------------|")
    print("1.| Añadir nota            |")
    print("|--------------------------|")
    print("2.| Mostrar notas extremas |")
    print("|--------------------------|")
    print("3.| Total de aprobados     |")
    print("|--------------------------|")
    print("4.| Nota media             |")
    print("|--------------------------|")
    print("5.| Mostrar todas          |")
    print("|--------------------------|")
    print("6.| Salir                  |")
    print("|--------------------------|")
    print("                            ")
    print("                            ")
    print("____________________________")
    print("                            ")
    opcion=int(input("| Introduzca una de las opciones del menú |"))
    print("____________________________")
    print("                            ")
    print("                            ")
    print("                            ")
    
    match opcion:
        case 1:
            try:
                nota=int(input("Introduzca una nota: "))
                notas.append(nota)
                print("                            ")
                print("|--------------------------|")
                print(f"Nota introducida: | {nota} |")
                print("|--------------------------|")
                print("                            ")
            except ValueError:
                print("                            ")
                print("|------------------------------|")
                print("| Introduzca valores numéricos |")
                print("|------------------------------|")
                print("                            ")
        case 2:
            print("                            ")
            print("|---------------------------|")
            print(f"Nota más alta | {max(notas)}| ")
            print("|--------------------------|")
            print(f"Nota más baja | {min(notas)}| ")
            print("|---------------------------|")
            print("                            ")
        case 3:
            contador=0
            for nota in notas:
                if nota>=5:
                    contador+=1
            print("                            ")
            print("|--------------------------------|")
            print(f"Total de aprobados: | {contador} |")
            print("|--------------------------------|")
            print("                            ")
        case 4:
            contador=0
            total=0
            for nota in notas:
                total+=nota
                contador+=1
            print("                            ")
            print("|------------------------------|")
            print(f"Nota media: | {total/contador} |")
            print("|------------------------------|")
            print("                            ")
            
        case 5:
            print("|--------------------------|")
            print("                             ")
            print(notas)
            print("                             ")
            print("|--------------------------|")
        case 6:
            print("                            ")
            print("                             ")
            print("---------------Fin del programa-----------------------")
            print("                             ")
            print("                            ")
            activo=False
        case _:
            print("                            ")
            print("|                                |")
            print("| -Introduzca una opción válida- |")
            print("|                                |")
            print("                            ")
            
print("                            ")
print("...Cerrando aplicación...")