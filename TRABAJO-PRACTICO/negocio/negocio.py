from datetime import datetime, timedelta


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []


class Cliente:
    def __init__(self,cliente_id, nombre, apellido, dni):
        self.id= cliente_id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tickets = []


    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"

    def __repr__(self):
        return self.__str__()
    
    
    def agregar_ticket(self, ticket):
        self.tickets.append(ticket)
        
       
        

    
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()
   

    @classmethod  #permite buscar productos por su nombre en una lista
    def buscar_producto(cls, nombre, negocio):
        if isinstance(nombre, str):  # Verificar si nombre_producto es una cadena de texto
            nombre_lower = nombre.lower()  # Convertir el nombre a minúsculas
            for producto in negocio.productos:
                if producto.nombre.lower() == nombre_lower:
                    return producto
        return None  # Retorna None si no se encuentra el producto o si nombre no es una cadena de texto

       
        
class Ticket:
    def __init__(self, ticket_id, productos, total, cliente):
        self.ticket_id = ticket_id
        self.productos = productos
        self.total = total
        self.cliente = cliente
        self.fecha = datetime.now()

    def __str__(self):
        ticket_info = f"==============================\n"
        ticket_info += f"        TICKET DE COMPRA\n"
        ticket_info += f"==============================\n"
        ticket_info += f"Ticket ID: {self.ticket_id}\n"
        ticket_info += f"Fecha de Compra: {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}\n"
        ticket_info += f"Productos Comprados:\n"
        for producto in self.productos:
            ticket_info += f"  - {producto.nombre} (Precio: ${producto.precio:.2f})\n"
        ticket_info += f"Total de la Compra: ${self.total:.2f}\n"
        ticket_info += f"==============================\n"
        return ticket_info

class Negocio:
    
    contador_clientes = 0
    
    def __init__(self):
        self.clientes = []
        self.categorias = []
        self.productos = []
        self.tickets = []
        self.ventas_productos = {}  # Seguimiento de las ventas de productos
        self.contador_clientes = 0  # Agregar el contador de clientes en 0
        self.contador_tickets = 0  # Contador de tickets inicializado en 0
    
    
    def agregar_ticket(self, ticket):
        self.tickets.append(ticket)
        # Actualizar el contador de tickets
        self.contador_tickets += 1  # Aumenta el contador de tickets
        # Actualizar las ventas de productos
        for producto in ticket.productos:
            if producto.nombre in self.ventas_productos:
                self.ventas_productos[producto.nombre] += 1
            else:
                self.ventas_productos[producto.nombre] = 1
           
    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados en el negocio.")
        else:
            print("\nListado de Clientes:")
            for cliente in self.clientes:
                print(f"Nombre: {cliente.nombre} {cliente.apellido}, DNI: {cliente.dni}")

    def cargar_categorias(self):
        # Utiliza las instancias de categorías creadas en categoria.py
        categoria1 = Categoria("electrodomesticos")
        categoria2 = Categoria("ropa")
        categoria3 = Categoria("electronica")
        self.categorias = [categoria1, categoria2, categoria3]
        
    def cargar_productos(self):
         # Cargar categorías si no existen
        if not self.categorias:
            categoria1 = Categoria("electrodomesticos")
            categoria2 = Categoria("ropa")
            categoria3 = Categoria("electronica")
            self.categorias = [categoria1, categoria2, categoria3]

        # Agregar productos a las categorías
        categoria_electrodomesticos = self.buscar_categoria("electrodomesticos")
        categoria_ropa = self.buscar_categoria("ropa")
        categoria_electronica = self.buscar_categoria("electronica")

        # Agregar productos solo si no existen
        if not any(producto.nombre == "Televisor" for producto in categoria_electrodomesticos.productos):
            producto1 = Producto("Televisor", 500, categoria_electrodomesticos)
            categoria_electrodomesticos.productos.append(producto1)
            self.productos.append(producto1)

        if not any(producto.nombre == "Camiseta" for producto in categoria_ropa.productos):
            producto2 = Producto("Camiseta", 20, categoria_ropa)
            categoria_ropa.productos.append(producto2)
            self.productos.append(producto2)

        if not any(producto.nombre == "Telefono" for producto in categoria_electronica.productos):
            producto3 = Producto("Telefono", 300, categoria_electronica)
            categoria_electronica.productos.append(producto3)
            self.productos.append(producto3)

        # Agregar otros productos
        if not any(producto.nombre == "Computadora" for producto in categoria_electronica.productos):
            producto4 = Producto("Computadora", 800, categoria_electronica)
            categoria_electronica.productos.append(producto4)
            self.productos.append(producto4)

        if not any(producto.nombre == "Zapatos" for producto in categoria_ropa.productos):
            producto5 = Producto("Zapatos", 50, categoria_ropa)
            categoria_ropa.productos.append(producto5)
            self.productos.append(producto5)

        if not any(producto.nombre == "Refrigerador" for producto in categoria_electrodomesticos.productos):
            producto6 = Producto("Refrigerador", 400, categoria_electrodomesticos)
            categoria_electrodomesticos.productos.append(producto6)
            self.productos.append(producto6)

        if not any(producto.nombre == "Gafas de sol" for producto in categoria_ropa.productos):
            producto7 = Producto("Gafas de sol", 25, categoria_ropa)
            categoria_ropa.productos.append(producto7)
            self.productos.append(producto7)

    def agregar_producto_a_categoria(self, nombre_producto, precio_producto, nombre_categoria):
        categoria = self.buscar_categoria(nombre_categoria)
        if categoria:
            producto = Producto(nombre_producto, precio_producto, categoria)
            categoria.productos.append(producto)
            self.productos.append(producto)
            print(f"Producto '{nombre_producto}' agregado a la categoría '{nombre_categoria}' con éxito.")
        else:
            print(f"No se encontró la categoría '{nombre_categoria}'. Creando nueva categoría...")
            self.cargar_categorias()  # Cargar categorías si no existe la categoría
            categoria = self.buscar_categoria(nombre_categoria)  # Volver a buscar la categoría
            if categoria:
                producto = Producto(nombre_producto, precio_producto, categoria)
                categoria.productos.append(producto)
                self.productos.append(producto)
                print(f"Producto '{nombre_producto}' agregado a la categoría '{nombre_categoria}' con éxito.")
            else:
                print(f"No se pudo crear la categoría '{nombre_categoria}'. Producto no agregado.")

    
    
    def listar_productos(self):
        print("\nListado de Productos por Categoría:")
        for categoria in self.categorias:
            print(f"\nCategoría: {categoria.nombre}")
            if categoria.productos:
                for producto in categoria.productos:
                    if producto:  # Verifica si el producto no es None
                        print(f"Nombre: {producto.nombre}, Precio: {producto.precio}")
                    else:
                        print("Producto inválido.")
            else:
                print("No hay productos en esta categoría.")
        input("\nPresione Enter para continuar...")
        
    def agregar_producto(self, nombre, precio, categoria_nombre):
        categoria = self.buscar_categoria(categoria_nombre)
        if categoria:
            nuevo_producto = Producto(nombre, precio, categoria)
            categoria.productos.append(nuevo_producto)
            self.productos.append(nuevo_producto)
            #print(f"Producto '{nombre}' agregado con éxito.")
        else:
            print(f"No se encontró la categoría '{categoria_nombre}'. Producto no agregado.")

    def buscar_cliente(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None
    
    def agregar_cliente(self, nombre, apellido, dni):
        # Aumentar el contador de clientes
        self.contador_clientes += 1

        # Crear una instancia de Cliente con un ID único
        cliente = Cliente(self.contador_clientes, nombre, apellido, dni)

        # Agregar el cliente a la lista de clientes del negocio
        self.clientes.append(cliente)

        return cliente
        
    def imprimir_tickets_por_mes(self, mes, año):
        try:
            print(f"Tickets del mes {mes} del año {año}:")
            for ticket in self.tickets:
                if ticket.fecha.month == mes and ticket.fecha.year == año:
                    print("------------------------------")
                    print(f"Ticket ID: {ticket.ticket_id}")
                    print(f"Fecha de Compra: {ticket.fecha.strftime('%d/%m/%Y %H:%M:%S')}")
                    print(f"Cliente: {ticket.cliente.nombre} {ticket.cliente.apellido} (DNI: {ticket.cliente.dni})")
                    print("Productos Comprados:")
                    for producto in ticket.productos:
                        print(f"  - {producto.nombre} (Precio: ${producto.precio:.2f})")
                    print(f"Total de la Compra: ${ticket.total:.2f}")
                    print()  # Línea en blanco para separar los tickets
                    print(ticket)
        except ValueError:
            print("Entrada inválida. Ingrese un número válido para el mes y el año.")

 
    
    
    
    def cargar_ventas(self):
        
        cliente1 = Cliente("Juan", "Pérez", "12345678")
        cliente2 = Cliente("Ana", "González", "87654321")
        cliente3 = Cliente("Eva", "García", "33333333")
        cliente4 = Cliente("Manuel", "López", "44444444")
        cliente5 = Cliente("Luis", "Martínez", "55555555")
        cliente6 = Cliente("Laura", "Rodríguez", "66666666")
        cliente7 = Cliente("Carlos", "Sánchez", "77777777")
        
        # Buscar productos por nombre en la lista de productos del negocio
        producto1 = Producto.buscar_producto("Televisor", self)
        producto2 = Producto.buscar_producto("Camiseta", self)
        producto3 = Producto.buscar_producto("Telefono", self)
        producto4 = Producto.buscar_producto("Computadora", self)
        producto5 = Producto.buscar_producto("Zapatos", self)
        producto6 = Producto.buscar_producto("Refrigerador", self)
        producto7 = Producto.buscar_producto("Gafas de sol", self)
        
        
        # Calcular los totales de los tickets
       
        total_ticket1 = producto1.precio + producto2.precio
        total_ticket2 = producto3.precio
        total_ticket3 = producto1.precio + producto2.precio + producto1.precio
        total_ticket4 = producto3.precio + producto2.precio + producto1.precio
        total_ticket5 = producto1.precio + producto2.precio
        total_ticket6 = producto3.precio + producto3.precio + producto3.precio
        total_ticket7 = producto1.precio + producto1.precio + producto1.precio + producto1.precio

        # Crear objetos Ticket con productos
        ticket1 = Ticket(1, [producto1, producto2], total_ticket1, cliente1)
        ticket2 = Ticket(2, [producto3], total_ticket2, cliente2)
        ticket3 = Ticket(3, [producto2, producto2, producto1], total_ticket1 * 3, cliente3)
        ticket4 = Ticket(4, [producto3, producto2, producto1], total_ticket1 * 3, cliente4)
        ticket5 = Ticket(5, [producto2, producto2], total_ticket1 * 2, cliente5)
        ticket6 = Ticket(6, [producto3, producto3, producto3], total_ticket2 * 3, cliente6)
        ticket7 = Ticket(7, [producto1, producto1, producto1, producto1], total_ticket1 * 4, cliente7)


        # Agregar tickets a los clientes directamente a través de su lista de tickets
        cliente1.tickets.append(ticket1)
        cliente2.tickets.append(ticket2)
        cliente3.tickets.append(ticket3)
        cliente4.tickets.append(ticket4)
        cliente5.tickets.append(ticket5)
        cliente6.tickets.append(ticket6)
        cliente7.tickets.append(ticket7)

        # Agregar los clientes a la lista de clientes del negocio
        self.clientes = [cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7]
        # Crear fecha de inicio para los tickets
        fecha_actual = datetime.now()

        # Generar 7 ventas (tickets) automáticamente
        for i in range(7):
            
            # Seleccionar un cliente de la lista de clientes del negocio (alternando entre ellos)
            cliente = self.clientes[i % len(self.clientes)]
            
            # Crear un nuevo ticket con productos vacíos y total en cero
            ticket = Ticket(i + 1, [], 0, None)
            
            # Agregar productos al ticket y calcular el total
            if i % 3 == 0:
                ticket.productos.extend([producto1, producto2])
                ticket.total += producto1.precio + producto2.precio
            elif i % 3 == 1:
                ticket.productos.extend([producto4, producto5])
                ticket.total += producto4.precio + producto5.precio
            else:
                ticket.productos.extend([producto6, producto7])
                ticket.total += producto6.precio + producto7.precio
            
           # Asignar el ticket al cliente seleccionado
            cliente.agregar_ticket(ticket)
            
            # Establecer la fecha del ticket y avanzar un día para cada ticket
            ticket.fecha = fecha_actual.strftime('%d/%m/%Y %H:%M:%S')
            fecha_actual += timedelta(days=1)
            self.tickets.append(ticket)
            
            
        
    def buscar_categoria(self, nombre_categoria):
        for categoria in self.categorias:
            if categoria.nombre == nombre_categoria:
                return categoria
        return None
    
    def imprimir_categoria_mas_popular(self):
        categoria_mas_popular = self.categoria_mas_popular()  # Llama al método que obtiene la categoría más popular
        if categoria_mas_popular:
            print(f"La categoría más popular es: {categoria_mas_popular.nombre}")
        else:
            print("No hay ventas registradas en la categoría.")


    
    def imprimir_clientes_mas_menos_gastaron(self, mes, año):
        
        # Filtrar los tickets para encontrar los del mes y año especificados
        tickets_filtrados = [ticket for ticket in self.tickets if ticket.fecha.month == mes and ticket.fecha.year == año]

        clientes_gastos = {}  # Crear un diccionario para realizar un seguimiento de los gastos de cada cliente
    
        # Calcular los gastos de cada cliente
        for ticket in tickets_filtrados:
            cliente = ticket.cliente
            total_gasto = ticket.total
        
            if cliente in clientes_gastos:
                clientes_gastos[cliente] += total_gasto
            else:
                clientes_gastos[cliente] = total_gasto
    
        # Encontrar el cliente que más gastó
        print("----------------------")
        cliente_mas_gasto = max(clientes_gastos, key=clientes_gastos.get)
    
        # Encontrar el cliente que menos gastó
       
        cliente_menos_gasto = min(clientes_gastos, key=clientes_gastos.get)

        return cliente_mas_gasto, cliente_menos_gasto, clientes_gastos
       
    
    def imprimir_tickets_del_mes(self):
        if not self.tickets:
            print("No hay tickets registrados en el comercio.")
            return

        try:
            mes = int(input("Ingrese el mes del que desea imprimir los tickets (coloque solo un número): "))
            año = int(input("Ingrese el año: "))
            
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para el mes y el año.")
            return
        
        if not (1 <= mes <= 12) or año < 0:
            print("Fecha inválida. Por favor, ingrese un mes válido (entre 1 y 12) y un año válido (mayor o igual a 0).")
            return
        
        tickets_del_mes = [ticket for ticket in self.tickets if ticket.fecha.month == mes and ticket.fecha.year == año]
        
        
        if not tickets_del_mes:
            print(f"No se encontraron tickets para el mes {mes} del año {año}.")
        else:
            print(f"Tickets del mes {mes} del año {año}:")
            for ticket in tickets_del_mes:
                print(f"Ticket {ticket.numero} - Cliente: {ticket.cliente.nombre} {ticket.cliente.apellido}, Total: ${ticket.total}")



    
    def listar_clientes_registrados(self):
        if not self.clientes:
            print("No hay clientes registrados en el negocio.")
        else:
            print("\nClientes Registrados:")
            for cliente in self.clientes:
                print(cliente)
    
    def total_tickets(self):
        return len(self.tickets)


    def producto_mas_vendido(self):
        if not self.tickets:
            return None

        productos_vendidos = {}
        for ticket in self.tickets:
            for producto in ticket.productos:
                if producto.nombre in productos_vendidos:
                    productos_vendidos[producto.nombre] += 1
                else:
                    productos_vendidos[producto.nombre] = 1

        producto_mas_vendido = max(productos_vendidos, key=productos_vendidos.get)
        
        print(productos_vendidos) 
        print(producto_mas_vendido)
        
        return producto_mas_vendido

    def categoria_mas_popular(self):
        if not self.categorias:
            print("No hay categorías registradas en el comercio.")
        else:
            categorias_count = {}
            for categoria in self.categorias:
                categorias_count[categoria] = sum(1 for producto in self.productos if producto.categoria == categoria)

            categoria_mas_popular = max(categorias_count, key=categorias_count.get)
            print(f"La categoría más popular es: {categoria_mas_popular.nombre}")

    def encontrar_producto_menos_vendido(self):
        ventas_productos = self.ventas_productos
        if not ventas_productos:
            return None

        # Encuentra el producto con la menor cantidad de ventas
        producto_menos_vendido = min(ventas_productos, key=ventas_productos.get)
        return producto_menos_vendido
    
    
    # Grupo C-(Vilma Ponce y Logan M.E. Arona)


   