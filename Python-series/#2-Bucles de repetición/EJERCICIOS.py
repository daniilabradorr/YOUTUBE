#BUCLE for , 
secuencia= [1,2,3,4]
for numero in secuencia:
    print(numero)

for numero in range(1,8,2):
    print(numero)

#EJERCICIO FOR
"""Crea una lista de números del 1 al 10 y usa un bucle for para imprimir solo los números pares."""
lista = [1,2,3,4,5,6,7,8,9,10] #Lista de números
#Realización del for.
for numero in lista:
    if numero % 2 ==0:
        print(numero)

#----------------------
#----------------------

#BUCLE while
contador = 0
while contador < 5:
    print(contador)
    contador = contador +1

#EJERCICIO WHILE.
"""Crear una variable suma que comience en 0 y usar un bucle while para sumar números del 1 al 5."""
suma = 0 #Variable suma
numero = 1 #Variabnle 1, empieza en 1 porque suamamos los números del 1 al 5.
#Realizaciópn del bucle WHILE.
while numero < 5:
    suma += numero
    numero += 1
#Imprimimos el resultado final
print(f'Resultado de la suma de los numeros del 1 al 5 = {suma}')
