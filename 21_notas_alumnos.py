notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
#indica cuantos alumnos han aprovado
aprobados=0
suspensos=0
for num in notas_alumnos:
    if num>=5:
        aprobados+=1
        
print(f"Número de alumnos aprovados: {aprobados}")

#Indica la nota mas alta
alta=0
for nota in notas_alumnos:
    if nota>alta:
       alta=nota    

print(f"La nota mas alta es: {alta}")

print(f"La nota mas alta es {max(notas_alumnos)}, y la nota mas baja es {min(notas_alumnos)}")
del(notas_alumnos[3])

print(f"Lista ordenada: {sorted(notas_alumnos)}")