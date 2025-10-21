#sistema de venta de frutas

ventas = [] 
salir = False
stateMenu = 0
totalVentas = 0

while not salir:
    if stateMenu == 0:
        print(f"\nMenu de opciones:\n1. Comprar una fruta\n2. Ver carrito\n3. Salir\n")

        stateMenu = int(input("ingresa una opcion del menu: "))

    elif stateMenu == 1:
        print(f"ingresa informacion de la fruta: \n")
        nombre = input("nombre: ")
        cantidad = int(input("cantidad: "))
        valor = int(input("valor: "))
        
        nuevaFruta = {
            "nombre": nombre,
            "cantidad": cantidad,
            "valor": valor
        }

        totalVentas += valor * cantidad
        ventas.append(nuevaFruta)
        stateMenu = 0 

    elif stateMenu == 2:
        print(f"Tu carrito: \n")
        
        for fruta in ventas:
            print(fruta)
        stateMenu = 0 
    
    elif stateMenu == 3:
        salir = True

print(f"\nTOTAL VENTAS ES: \n {totalVentas}")