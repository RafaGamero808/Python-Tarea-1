#Añadimos las variables para el dividendo y divisor, con las que pedimos los números con los que operar al usuario
dividendo = int(input('Introduce un dividendo '))
divisor = int(input('Introduce un divisor '))
#Para el resultado, nos aseguramos de que el divisor no sea 0
if divisor != 0:
    #Creamos una variable para el resultado
    resultado = dividendo / divisor
    print('El resultado es', resultado)
#Utilizamos "else" para imprimir un mensaje de error en caso de que el divisor sea 0
else:
    print('¿Dónde vas, Javier Santaolalla? ERROR!! ERROR!!')