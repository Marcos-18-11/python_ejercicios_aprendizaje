#Hacer un programa que muestre la suma de todos los números naturales entre 1 y un número leído por teclado

numero_natural=0

limite_sucesion=int(input("Introduzca el número límite de la sucesión: "))

for c in range (1,limite_sucesion+1):
    
    print(f"Número de la sucesión: {c}, es igual a {numero_natural}")
    numero_natural+=c