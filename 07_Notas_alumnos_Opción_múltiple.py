# lee la nota de un alumno y depndiendo del número 
# (0-10) le indica si es suspenso(menos de 5), aprovado(5 a 6),
# notable(7 a 8) o sobresaliente(9 o 10); indicar si la nota es o no válida

nota = int(input("Introduzca la nota de este alumno"))


match nota:
        case 0|1|2|3|4:
            print("Suspenso")
        case 5|6:
            print("Aprovado")
        case 7|8:
            print("Notable")
        case 9|10:
            print("Sobresaliente")
        case _:
            print("Nota no computable")

