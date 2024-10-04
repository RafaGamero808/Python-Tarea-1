#Pedimos que introduzca la cantidad a invertir al usuario
n = float(input('Introduce tu cantidad a invertir: '))
#Pedimos también que introduzca el interés anual
anual = float(input('Introduce el tipo interés anual: ')) 
#Pedimos la duración de la inversión en años
tiempo = int(input('Introduce cuántos años durará tu inversión: '))

#establecemos un "for" basado en los años a los que ha invertido su capital
for tiempo in range (1, tiempo +1):
    #calculamos el crecimiento del capital y a su vez creamos otra variable para el propio capital
    capital = n * (1 + anual / 100) ** tiempo
    #Imprimimos el año (de manera ordinal) y la cantidad a la que asciende nuestro patrimonio
    print(tiempo, "\t", capital)
