#Declaramos las variables de precio y edad
edad = int(input('Introduce tu edad '))

#Establecemos las codiciones por rangos de edad, señalando que el 0 no es válido en el primer rango de edad
if edad <= 3 and edad !=0:
    print('Puedes entrar gratis')
elif edad >= 4 and edad < 18:
    print('Son 5€')
elif edad == 0:
    print('Prohibido el juego a neonatos ¿A qué vas a jugar tú?')
else:
    print('Tu entrada serán 10€')
#Para cada rango hemos personalizado un mensaje distinto con el precio correspondiente