#solicita la introduccion de dos números y calcula la suma de toddos los números comprendidos entre ellos incluidos

primer_numero=int(input("Introduzca el primer número: "))
segundo_numero=int(input("Introduzca el segundo número: "))

resultado=0

if primer_numero>segundo_numero:
    primer_numero,segundo_numero=segundo_numero,primer_numero
    
             
for num in range(primer_numero,segundo_numero+1):
        resultado+=num
    
print(f"El resultado total es {resultado}")
