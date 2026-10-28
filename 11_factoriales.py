#Realizar un programa que solicite la introducción de un número y calcule su factorial

numero_factorial=int(input("Introduzca el número: "))
resultado=1
for c in range(1,numero_factorial+1):
    resultado=resultado*c
    
    
print(f"Resultado: {resultado}")