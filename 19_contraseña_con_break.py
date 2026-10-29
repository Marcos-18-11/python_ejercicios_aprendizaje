#solicita la introducción de una contraseña, si es correcta le dice que es un usuaro válido,
# si no , se le vuelve a preguntar, al tercer intento le dice que no es un usuario válido.

contraseña_correcta=123
intentos=3
acierto=False


while intentos>0:
    contraseña_introducida=int(input("Introduzca su contraseña"))
    
    if contraseña_introducida==contraseña_correcta:
        print("Usuario válido")
        acierto=True
        break
        
    else:
        intentos=intentos-1
        print("Contraseña incorrecta")
        

if acierto:
    print("Bienvenido")
else:
    print("Usuario bloqueado")

