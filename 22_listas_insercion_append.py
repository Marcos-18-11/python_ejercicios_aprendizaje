#solicitar la introduccion de números, uno a uno y los guardamos en una lista,
#después de pedir cada uno, volver a preguntar hasta que diga que no

resp="s"
lista=[]
dato=0
while resp=="s" or resp=="S":
    try:
        dato=int(input("Introduzca un número en la lista"))
        lista.append(dato)
        resp=(input("¿Quiere introducir algún número más en la lista?(s/n)"))
    except ValueError:
        print("No es un valor numérico, vuelva a intentarlo")
    
  
print("Inserción de datos finalizada")
print(lista)