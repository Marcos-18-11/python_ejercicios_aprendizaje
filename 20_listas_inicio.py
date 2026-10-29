lista=[4,1,8,2,11]
#muestra cada numero par de la lista
print("Pares")
for num in lista:
    if num%2==0:
        print(num)
        
#sustituye cada elemento d ela lista por su cuadrado 
#y luego imprimes la lista entera y la suma de suma de su contenido
print("Cuadrados")
print("----------------------------------------------------------")
total=0
indice=0
for num in lista:
    lista[indice]=num**2
    total+=lista[indice]
    indice+=1
    
print(lista)
print("-----------------------Total------------------------------")    
print("----------------------------------------------------------")
print(total)

#Solución alternativa
print("--------------Cubos de la lista original------------------")
for indice,num in enumerate(lista):
    lista[indice]=num**2
print(lista)