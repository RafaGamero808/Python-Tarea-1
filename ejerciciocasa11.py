#Establecemos la variable para la edad
edad = int(input('¿Cuántos años tienes? '))
#Creamos otra variable para los años cumplidos
cumplidos = 1

#Ahora formamos el bucle con while y un +=1
while cumplidos <= edad:
    print(f'Has cumplido {cumplidos} años')
    cumplidos += 1
#La "f" antes del mensaje del print la utilizamos para hacer un formateo de cadenas