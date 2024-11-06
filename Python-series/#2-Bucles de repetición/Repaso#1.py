#nombre = "Pepito"
#resultado= 5%1
#print(resultado)

"""Declara dos variables precio y cantidad que representen el precio unitario de un producto y la cantidad de unidades compradas.
Calcula el total multiplicando precio por cantidad.
Usa un condicional if para verificar si el total supera 20€. Si es así, muestra un mensaje diciendo "No hay dinero suficiente", y si no, "Realiza la resta del coste total a lo que tenemos" PRINTEALO Y DI 'COMPRA REALIZADA DINERO RESTANTE:."""
#inicializamos las variables
unidades_compra_manzanas = 5 #Variable de las unidades de manzanas que queremos comprar
precio_unitario_manzana = 2 #Variable del precio unitario de esas manzanas que queremos comprar.
coste_total_compra = unidades_compra_manzanas * precio_unitario_manzana
dinero_disponible=20 #Variable del dinero disponible para la compra de manzanas.
dinero_disponible_despues_compra = dinero_disponible - coste_total_compra

#Realización del if.
if coste_total_compra > dinero_disponible:
    print("No hay dinero suficiente, NO SE PUEDE REALIZAR LA COMPRA")
else:
    print(f'COMPRA REALIZADA, dinero disponible final = {dinero_disponible_despues_compra}€')


