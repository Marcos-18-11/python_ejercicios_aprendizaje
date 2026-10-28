#solicita la introducción de una contraseña, si es correcta le dice que es un usuaro válido,
# si no , se le vuelve a preguntar, al tercer intento le dice que no es un usuario válido.

contraseña_correcta=123
intentos=2
acertado=False


while acertado==False and intentos !=0:
    contraseña_introducida=int(input("Introduzca su contraseña"))
    if contraseña_introducida==contraseña_correcta:
        print("Usuario válido")
        acertado=True
    elif contraseña_introducida!=contraseña_correcta and intentos>0:
        intentos=intentos-1
        print("Contraseña incorrecta, vuelva a intentarlo")
    elif contraseña_introducida!=contraseña_correcta and intentos<=0:
        print("Usuario bloqueado")
