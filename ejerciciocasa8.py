#Introducimos primero las variables
n1 = input('Introduce un dividendo ')
n2 = input('Introduce un divisor ')

#Aseguramos que los inputs son números con el comando isdigit

if not n1.isdigit() or not n2.isdigit():
    print('ERROR, PON NÚMEROS EN CONDICIONES, HAZ EL FAVOR.')

elif n2 == 0:
    print('ERROR. NO SE PUEDE DIVIDIR POR CERO')

#Utilizamos un else, ya que en cualquier caso ajeno a los dos indicados anteriormente, sería una división válida
#Marcamos el int antes de n1 y n2, porque en caso contrario da error (no entiendo del todo por qué)
else:
    print(int(n1) / int(n2))