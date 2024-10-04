#Asignamos una variable para el peso de los payasos y las muñecas
payasos = int(112)
muñecas = int(75)
#Creamos otras dos variables, las cuales utilizaremos para pedir el número de payasos y muñecas, además de calcular después
vp = int(input('¿Cuántos payasos se han vendido? ') )
vm = int(input('¿Y muñecas? '))
#Asignamos a la variable "peso" la multiplicación de la cantidad de payasos y muñecas por su peso (asignado al principio), además de su correspondiente suma
peso = (vp * payasos) + (vm * muñecas)
#Imprimimos un mensaje que recurra a la variable "peso", mostrando el peso total del pedido
print('El peso total del pedido es ', peso)