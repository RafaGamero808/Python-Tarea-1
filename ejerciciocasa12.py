#pedimos el número entero positivo declarando la variable "n"

n=int(input('Introduce un número entero positivo '))
#con la variable i, a la cual le damos el valor 1, podremos empezar la cadena de números impares
i = 1

while i <= n: 
     #establecemos la condición de que al sumarle 2 a "i", ya nos hemos pasado en valor, por lo que "i" sería el último número a imprimir
    if i + 2 > n: 
        print(i) 
    else: #si aún hay números por imprimir después de sumarle 2, imprimiremos "i" con una coma
        print(i, end=",")
    #hacemnos que el valor de "i" aumente su valor en 2, para saltar al siguiente número impar. Con la condición establecida en la línea 8, se daría fin al bucle.
    i = i + 2
