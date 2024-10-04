#Empezamos con una variable a la que recurrir cuando usemos el "for"
nombre = input('Dime tu nombre ')
#Pedimos el número y con el "for", imprimimos el nombre tantas veces como pida el usuario
numero = int(input('Dime también un número '))
for i in range (numero):
    print(nombre)