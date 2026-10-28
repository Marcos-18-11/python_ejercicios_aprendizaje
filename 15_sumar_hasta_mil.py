# 1+2+3+4+5...
# ¿Hasta qué número tendremos que llegar para superar o alcanzar el 1000?.

num1=0
sumatorio=0
while num1<1000:
    num1+=1
    sumatorio+=num1
    print(f"Suma número: {num1}")
    
print(f"primer valor en alcanzar el mil: {sumatorio}")