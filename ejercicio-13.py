#sistema de inventario

inventario = [] 
salir = False
stateMenu = 0

while not salir:
    if stateMenu == 0:
        print("\n📜 Menu de opciones \n" 
           "1. Agregar productos al inventario \n"
           "2. Mostrar productos en inventario \n"
           "3. Buscar un producto en el inventario \n"
           "4. Salir \n")

        stateMenu = int(input("ingresa una opcion del menu: "))

    elif stateMenu == 1:
        print(f"🔖 AGREGAR PRODUCTO\n"
              "ingresa informacion del producto: \n")
        nombre = input("nombre: ")
        cantidad = int(input("cantidad: "))
        valor = int(input("valor: "))
        
        nuevoProducto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "valor": valor
        }
        inventario.append(nuevoProducto)
        stateMenu = 0 


    elif stateMenu == 2:
        valorTotal = 0

        if len(inventario) != 0:
            print(f"🔖 INVENTARIO\n"
              "🛒 Los productos de tu inventario son:" )

            for producto in inventario:
                valorTotal += producto["valor"] * producto["cantidad"]
                print(f"{producto}")

            print(f"\n🧮 El VALOR total del inventario es de: {valorTotal}")
        else:
              print("🚫 TU INVENTARIO NO TIENE PRODUCTOS")

        stateMenu = 0 

    elif stateMenu == 3:
        nombre = input(f"🔖 BUSCAR PRODUCTO\n"
                       "ingresa el nombre: ")
        
        isproducto = False
        for producto in inventario:
            if producto["nombre"] == nombre:
               isproducto = True
               break
            
        if isproducto:
            print("Producto encontrado✅")
            print(producto)
            stateMenu = 0 
        else:
            print("Producto no encontrado❌")
            stateMenu = 0 

    
    elif stateMenu == 4:
        salir = True
