#pide dos números y muestra el resultado de dividir el mayor entre el menor

num1=float(input("introduzca el primer número: "))
num2=float(input("introduzca el segundo número: "))

if num1>num2:
    print(f"{num1} entre {num2} es igual a {num1/num2}")
else:
    print(f"{num2} entre {num1} es igual a {num2/num1}")
    
