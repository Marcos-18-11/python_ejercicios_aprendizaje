#solicita una nota, después otra, y así sucesivamente hasta introducir un cero, 
# en ese momento, no pedirá mas notas y mostrará la nota media d elas notas introducidas

nota=1
media=0
contador=0

while nota>0:
    nota=int(input("Introduzca la nota: "))
    media+=nota
    contador+=1
    
contador-=1
resultado=media/contador

print(f"Número de notas introducidas: {contador}")
print(f"La media de los resultados es {resultado}")