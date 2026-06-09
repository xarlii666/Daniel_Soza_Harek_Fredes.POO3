from abc import ABC, abstractmethod
#Sistema de gestión para una pastelería con productos como pasteles, cupcakes y galletas.
class Producto(ABC):
    def __init__(self, nombre, precio_base, ingredientes):
        self._nombre = nombre
        self._precio_base = precio_base
        self._ingredientes = ingredientes
        self._disponible = True
#metodos para obtener informacion del producto
    def get_nombre(self):
        return self._nombre

    def get_disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        self._disponible = estado

#metodos abstractos para descripcion y calculo de precio
    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def calcular_precio(self):
        pass
#clase de pastel
class Pastel(Producto):
    def __init__(self, nombre, precio_base, ingredientes, tamaño):
        super().__init__(nombre, precio_base, ingredientes)
        self._tamaño = tamaño

    def descripcion(self):
        return "Pastel '" + self._nombre + "' de tamaño " + self._tamaño

    def calcular_precio(self):
        if self._tamaño.lower() == "grande":
            return self._precio_base * 1.6
        elif self._tamaño.lower() == "mediano":
            return self._precio_base * 1.3
        else:
            return self._precio_base

#cupcakes
class Cupcake(Producto):
    def __init__(self, nombre, precio_base, ingredientes, cantidad):
        super().__init__(nombre, precio_base, ingredientes)
        self._cantidad = cantidad

    def descripcion(self):
        return "Cupcakes '" + self._nombre + "' en paquete de " + str(self._cantidad) + " unidades"
#calculo de precio con descuento por cantidad
    def calcular_precio(self):
       
        total_normal = self._precio_base * self._cantidad
        return total_normal * 0.95
#clase de galletas
class Galleta(Producto):
    def __init__(self, nombre, precio_base, ingredientes, es_sin_gluten):
        super().__init__(nombre, precio_base, ingredientes)
        self._es_sin_gluten = es_sin_gluten

    def descripcion(self):
        if self._es_sin_gluten:
            return "Galleta '" + self._nombre + "' (Sin Gluten)"
        return "Galleta '" + self._nombre + "' (Clasica)"

    def calcular_precio(self):
        # Recargo del 10% si es un producto sin gluten
        if self._es_sin_gluten:
            return self._precio_base * 1.1
        return self._precio_base
#clase de ordenes
class Orden:
    def __init__(self, cliente):
        self._cliente = cliente
        self._productos_elegidos = []
        self._pagada = False
#metodos de orden
    def get_cliente(self):
        return self._cliente
#metodo para agregar productos a la orden
    def agregar_producto(self, producto):
        if not producto.get_disponible():
            print("Error: El producto no está disponible.")
            return
        self._productos_elegidos.append(producto)
        print("Producto agregado a la orden.")
#metodo para calcular el total de la orden
    def calcular_total_orden(self):
        total = 0
        for p in self._productos_elegidos:
            total += p.calcular_precio()
        return total
#   metodo para pagar la orden
    def pagar(self):
        if len(self._productos_elegidos) == 0:
            print("No puedes pagar una orden vacía.")
            return False
        self._pagada = True
        return True
#metodo para mostrar el resumen de la orden
    def mostrar_resumen(self):
        print("\n resumen de la orden")
        print("cliente: " + self._cliente)
        for p in self._productos_elegidos:
            print("- " + p.descripcion() + " ($" + str(p.calcular_precio()) + ")")
        print("Total: $" + str(self.calcular_total_orden()))
        if self._pagada:
            print("Estado: pagada")
        else:
            print("Estado: pendiente")
#sistema de pasteleria
class SistemaPasteleria:
    def __init__(self):
        self._inventario = []
        self._precargar_datos()
#metodo para precargar datos al inventario
    def _precargar_datos(self):
        self._inventario.append(Pastel("Fresa Feliz", 2500, ["harina", "fresas"], "Grande"))
        self._inventario.append(Cupcake("Chocolate", 1200, ["harina", "chocolate"], 6))
        self._inventario.append(Galleta("Avena harek", 300, ["avena harek", "miel"], True))

    def agregar_al_inventario(self, producto):
        self._inventario.append(producto)

    def buscar_producto(self, nombre):
        for p in self._inventario:
            if p.get_nombre().lower() == nombre.lower():
                return p
        return None
#metodo para mostrar el catalogo de productos
    def mostrar_catalogo(self):
        if not self._inventario:
            print("el inventario esta completamente vacio papu.")
            return
        print("\n catalogo de productos")
        for p in self._inventario:
            print("Nombre: " + p.get_nombre() + " | " + p.descripcion() + " | Precio Base: $" + str(p._precio_base))
#menu del sistema
def menu():
    sistema = SistemaPasteleria()
    orden_actual = None
#menu principal del sistema
    while True:
        print("\nLA PASTELERIA DELPAPU")
        print("1. Registrar nuevo producto en Inventario")
        print("2. Mostrar menu de productos")
        print("3. Crear orden / Agregar productos / Pagar con papu dolares")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion: ")
#opciones del menu
        if opcion == "1":
            print("\nregistrar nuevo producto")
            tipo = input("Tipo (Pastel / Cupcake / Galleta): ").lower()
            nombre = input("Nombre: ")
            precio = float(input("Precio Base: "))
            ingredientes = input("Ingredientes (separados por coma): ").split(",")
#validacion de tipo de producto y creacion del nuevo producto
            if tipo == "pastel":
                tamaño = input("Tamaño (Venti/Mediano/Chico): ")
                nuevo = Pastel(nombre, precio, ingredientes, tamaño)
            elif tipo == "cupcake":
                cantidad = int(input("Cantidad en el paquete: "))
                nuevo = Cupcake(nombre, precio, ingredientes, cantidad)
            elif tipo == "galleta":
                singluten = input("¿Es sin gluten? (si/no): ").lower() == "si"
                nuevo = Galleta(nombre, precio, ingredientes, singluten)
            else:
                print(" Tipo no válido lee bien las opciones.")
                continue
#agregar el nuevo producto al inventario
            sistema.agregar_al_inventario(nuevo)
            print(" Producto registrado con exito.")

        elif opcion == "2":
            sistema.mostrar_catalogo()

        elif opcion == "3":
            if orden_actual is None:
                cliente = input("Nombre del cliente para la nueva orden: ")
                orden_actual = Orden(cliente)
            
            print("\n gestionar orden de " + orden_actual.get_cliente().upper() + ")")
            print("a) Agregar producto a la orden")
            print("b) Ver resumen actual de la orden")
            print("c) Pagar orden con papu dolares")
            print("d) Volver al menú principal")
            sub_opcion = input("Seleccione (a-d): ").lower()
#sub opciones para gestionar la orden
            if sub_opcion == "a":
                nombre_p = input("Nombre del producto que desea llevar: ")
                prod = sistema.buscar_producto(nombre_p)
                if prod is not None:
                    orden_actual.agregar_producto(prod)
                else:
                    print(" El producto no existe en el catálogo.")
            elif sub_opcion == "b":
                orden_actual.mostrar_resumen()
            elif sub_opcion == "c":
                exito = orden_actual.pagar()
                if exito:
                    orden_actual.mostrar_resumen()
                    print("\n Venta completada con éxito,buenos papus dias")
                    orden_actual = None 
            elif sub_opcion == "d":
                print("Regresando al menú")
#opcion para salir del sistema
        elif opcion == "4":
            print(" Saliendo de la pasteleria del papu.")
            break
        else:
            print(" Opcion imposible.")
#punto de entrada del programa
if __name__ == "__main__":
    menu()
    