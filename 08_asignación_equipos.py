#teniendo en cuenta que alevín es 10 años y benjamín es 16.
#hay que hacer un programa que solicite la edad y nos muestre a que grupo pertenece
# pertenece al más cercano a su edad, la edad debe estar entre 9 y 18 años

limite_inf,limite_sup,benjamin,alevin=9,18,10,16
edad=float(input("Introduzca la edad del muchacho: "))

if edad<limite_inf or edad>limite_sup:
    print("Edad no válida")

else:
    distancia_benjamin=edad-benjamin
    distancia_alevin=alevin-edad
    if distancia_benjamin<distancia_alevin:
        print("Eres benjamín")
    else:
        print("Eres alevín")
