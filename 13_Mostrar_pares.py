#Realiza un programa que solicite la introducción de un número 
#y después, muestre todos los pares entre 1 y ese número

num1=1
num2=int(input("Introduzca el número: "))


if num1>num2:
    num1,num2=num2,num1
    

for c in range(num1,num2+1):
    if c%2==0:
        print(f"|{c} es par.|")
