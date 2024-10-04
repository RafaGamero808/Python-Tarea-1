#Creamos una variable y pedimos al usuario que introduzca su edad
edad = int(input('¿Cuántos años tienes? ' ))
#Utilizamos el "if" para confirmar su mayoría de edad
if edad >= 18:
    print('Felicidades, puedes sacarte el carnet de conducir.')
#Utilizamos la variable "elif" para el caso contrario, imprimiendo un mensaje distinto
elif edad < 18:
    print('Pues espérate a cumplir los 18. Te toca ir en bici.')