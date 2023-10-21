from datetime import date
from negocio.negocio import Negocio,Cliente,Categoria,Producto,Ticket



# Definición de la función agregar_producto_manualmente
def agregar_producto_manualmente(negocio):
    nombre_producto = input("Ingrese el nombre del producto: ").capitalize()
    precio_producto = float(input("Ingrese el precio del producto: "))
    categoria_nombre = input("Ingrese el nombre de la categoría: ")

    categoria = negocio.buscar_categoria(categoria_nombre)
    if categoria is None:
        categoria = Categoria(categoria_nombre)
        negocio.categorias.append(categoria)

    nuevo_producto = Producto(nombre_producto, precio_producto, categoria)
    negocio.agregar_producto(nuevo_producto)
    print(f"Producto '{nombre_producto}' agregado con éxito.")
    

def mostrar_menu(negocio):
    while True:
        print("\nMenú Principal:")
        print("1. Listar Productos")
        print("2. Agregar Nuevo Producto")
        print("3. Agregar Nuevo Ticket")
        print("4. Imprimir Producto Más Vendido")
        print("5. Imprimir Clientes que Más y Menos Gastaron")
        print("6. Listar Clientes Registrados")
        print("7. Imprimir Total de Tickets")
        print("8. Agregar Cliente")
        print("9. Imprimir Tickets del Mes")
        print("10.Imprimir Categoría Más Popular")
        print("11.Imprimir Producto Menos Vendido")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        
        if opcion == "1":
            negocio.listar_productos()
            
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    precio_producto = float(input("Ingrese el precio del producto: "))
                    break
                except ValueError:
                    print("Ingrese un precio válido (número).")  
            
            categoria_nombre = input("Ingrese el nombre de la categoría: ")
    
            negocio.agregar_producto_a_categoria(nombre_producto, precio_producto, categoria_nombre)
           
                    
        elif opcion == "3":
            # Solicitar los datos del cliente
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            apellido_cliente = input("Ingrese el apellido del cliente: ")
            dni_cliente = input("Ingrese el DNI del cliente: ")

            # Crear una instancia de Cliente con un ID único
            cliente = Cliente(Negocio.contador_clientes + 1, nombre_cliente, apellido_cliente, dni_cliente)

            # Solicitar los productos para el ticket
            productos_ticket = []
            
            while True:
                nombre_producto = input("Ingrese el nombre del producto (o '0' para finalizar): ")
                if nombre_producto == '0':
                     break
                # Buscar los productos en el negocio
                producto = Producto.buscar_producto(nombre_producto, negocio)

                if producto is not None:
                    productos_ticket.append(producto)
                else:
                    print(f"El producto '{nombre_producto}' no se encuentra en la lista de productos del comercio.")

            total_ticket = sum(producto.precio for producto in productos_ticket)

            if productos_ticket:
                ticket_id = negocio.contador_tickets + 1
                ticket = Ticket(ticket_id, productos_ticket, total_ticket, cliente)
                negocio.agregar_ticket(ticket)  # Agregas el ticket al negocio
                print("Ticket agregado con éxito.")
            else:
                print("El ticket no pudo ser agregado porque no se seleccionaron productos válidos.")
    
        elif opcion == "4":
            producto_mas_vendido = negocio.producto_mas_vendido()
            if producto_mas_vendido:
                print(f"El producto más vendido es: {producto_mas_vendido}")
            else:
                print("No hay ventas registradas en el negocio.")
        
        elif opcion == "5":
            try:
                mes = int(input("Ingrese el mes del que desea imprimir los tickets (coloque solo un número): "))
                año = int(input("Ingrese el año: "))
                if 1 <= mes <= 12:
                    cliente_mas_gasto, cliente_menos_gasto, clientes_gastos = negocio.imprimir_clientes_mas_menos_gastaron(mes, año)
                    if cliente_mas_gasto is not None and cliente_menos_gasto is not None:
                        print("Cliente que más gastó:")
                        print(f"Nombre: {cliente_mas_gasto.nombre} {cliente_mas_gasto.apellido}")
                        print(f"DNI: {cliente_mas_gasto.dni}")
                        print(f"Total gastado: ${round(clientes_gastos[cliente_mas_gasto], 2)}")

                        print("\nCliente que menos gastó:")
                        print(f"Nombre: {cliente_menos_gasto.nombre} {cliente_menos_gasto.apellido}")
                        print(f"DNI: {cliente_menos_gasto.dni}")
                        print(f"Total gastado: ${round(clientes_gastos[cliente_menos_gasto], 2)}")
                    else:
                        print("No se encontraron clientes con gastos en el mes y año seleccionados.")
                else:
                    print("Mes incorrecto. Ingrese un mes válido (entre 1 y 12).")
            except ValueError:
                print("Ingrese un número válido para el mes o año.")

                
        elif opcion == "6":
            negocio.listar_clientes_registrados()
        
        elif opcion == "7":
            total_tickets = negocio.total_tickets()
            print(f"Total de tickets: {total_tickets}")
        
        elif opcion == "8":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            apellido_cliente = input("Ingrese apellido del cliente: ")
            dni_cliente = input("Ingrese el DNI del cliente: ")
            cliente = negocio.agregar_cliente(nombre_cliente, apellido_cliente, dni_cliente)
            if cliente is not None:
                print("Cliente agregado con éxito.")
                
        elif opcion == "9":
            try:
                mes = int(input("Ingrese el mes del que desea imprimir los tickets (coloque solo un número): "))
                año = int(input("Ingrese el año: "))
        
                if 1 <= mes <= 12:
                    negocio.imprimir_tickets_por_mes(mes, año)
                else:
                    print("Mes incorrecto. Ingrese un mes válido (entre 1 y 12).")
            except ValueError:
                print("Ingrese un número válido para el mes.")

                
        elif opcion == "10":
            categoria_mas_popular = negocio.categoria_mas_popular()
            if categoria_mas_popular:
                print(f"La categoría más popular es: {categoria_mas_popular}")
            else:
                print("No hay ventas registradas.")
        
        elif opcion == "11":
            producto_menos_vendido = negocio.encontrar_producto_menos_vendido()

            if producto_menos_vendido:
                ventas_menos_vendido = negocio.ventas_productos[producto_menos_vendido]
                print(f"El producto menos vendido es '{producto_menos_vendido}' con {ventas_menos_vendido} ventas.")
            else:
                print("No hay productos vendidos en el negocio.")

                
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break  # Sale del bucle while y finaliza el programa

if __name__ == "__main__":
    
    negocio = Negocio()

    # Cargar categorías y productos
    negocio.cargar_categorias()
    negocio.cargar_productos()

    # Agregar los clientes originales
    cliente1 = negocio.agregar_cliente("Juan", "Pérez", "12345678")
    cliente2 = negocio.agregar_cliente("Ana", "González", "87654321")
    cliente3 = negocio.agregar_cliente("Eva", "García", "33333333")

    # Agregar tres clientes adicionales
    cliente4 = negocio.agregar_cliente("Manuel", "López", "44444444")
    cliente5 = negocio.agregar_cliente("Lucía", "Martínez", "55555555")
    cliente6 = negocio.agregar_cliente("Carlos", "Fernández", "66666666")

    # Agregar los tickets a los clientes originales
    negocio.agregar_ticket(Ticket(1, [Producto.buscar_producto("Televisor", negocio), Producto.buscar_producto("Camiseta", negocio)], 520, cliente1))
    negocio.agregar_ticket(Ticket(2, [Producto.buscar_producto("Telefono", negocio)], 300, cliente2))
    negocio.agregar_ticket(Ticket(3, [Producto.buscar_producto("Camiseta", negocio), Producto.buscar_producto("Televisor", negocio)], 520, cliente1))
    negocio.agregar_ticket(Ticket(4, [Producto.buscar_producto("Televisor", negocio)], 500, cliente2))
    negocio.agregar_ticket(Ticket(5, [Producto.buscar_producto("Telefono", negocio)], 300, cliente3))
    negocio.agregar_ticket(Ticket(6, [Producto.buscar_producto("Televisor", negocio)], 500, cliente3))
    negocio.agregar_ticket(Ticket(7, [Producto.buscar_producto("Camiseta", negocio)], 20, cliente1))

    mostrar_menu(negocio)
    
    # Obtener mes y año del usuario o desde alguna otra fuente
    mes = int(input("Ingrese el mes del que desea imprimir los tickets (coloque solo un número): "))
    año = int(input("Ingrese el año: "))
    
    
    cliente_mas_gasto, cliente_menos_gasto, clientes_gastos = negocio.imprimir_clientes_mas_menos_gastaron(mes, año)

    
    if cliente_mas_gasto is not None and cliente_menos_gasto is not None:
        print("Cliente que más gastó:")
        print(f"Nombre: {cliente_mas_gasto.nombre} {cliente_mas_gasto.apellido}")
        print(f"DNI: {cliente_mas_gasto.dni}")
        print(f"Total gastado: ${round(clientes_gastos[cliente_mas_gasto], 2)}")

        print("\nCliente que menos gastó:")
        print(f"Nombre: {cliente_menos_gasto.nombre} {cliente_menos_gasto.apellido}")
        print(f"DNI: {cliente_menos_gasto.dni}")
        print(f"Total gastado: ${round(clientes_gastos[cliente_menos_gasto], 2)}")
    else:
        print("No se encontraron clientes con gastos en el mes y año seleccionados.")
        
        
     # Grupo C-(Vilma Ponce y Logan M.E. Arona)


    
    