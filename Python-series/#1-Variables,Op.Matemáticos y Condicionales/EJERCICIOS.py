#1-.Variables.
nombre = "Daniel" #La variable es nombre, "Daniel" es el valor de la variable.

#2-.OPERADORES MATEMATICOS.
#suma y resta +-
#division = /
#multiplicacion = *
#modulo = %

#CONDICIONALES.
#if(si..), elif(si...), else(sino...)

#EJERCICIOS
"""Vamos a empezar con un ejercicio muy básico. Vamos a crear un programa que le pida al usuario dos números, los sume y luego muestre el resultado en pantalla."""
#Le pedimos al usuario que introduzca los dos números de la suma.
#Pasando el type de string a int(numeros enteros) con el int.
numero1=int(input("Introduzca el primer numero de la suma: "))
numero2=int(input("Introduzca el segundo numero de la suma: "))

#Realizamos la suma.
suma= numero1 + numero2

#Imprimir o mostrar el resultado por pantalla.
print(suma)

#PRINTEO UNA LÍNEA PARA SEPARAR EJERCICIOS.
print("-------------------")

"""Vamos a crear un programa que le pida al usuario su edad y luego le dirá si es mayor de edad o no."""
edad=input("Introduzca su edad porfavor: ") #Le pedimos al usuario su edad en numero entero(int).

if edad >= 18: #Realizamos el condicional si es mayor o igual a 18.
    print("CORRECTO:Eres mayor de edad")
else: #Si no es mayor o igual a 18 entonces:
    print("ERROR:No eres mayor de edad")

#EJERCICIO MODIFICADO CON TRY-EXCEPT.
try:
    edad = int(edad)
#Realizamos el condicional if.
    if type(edad) == int and edad >= 18:
        print("CORRECTO: Eres mayor de edad")
    elif type(edad)==int and edad == 17:
        print("ERROR: Te falta un año para ser mayor de edad")
    else:
        print("ERROR: No eres mayor de edad")
except ValueError:
    print("Por favor, introduzca solo números enteros")

if edad >= 18:
    print("CORRECTO:Eres mayor de edad")
else:
    print("ERROR:No eres mayor de edad")

