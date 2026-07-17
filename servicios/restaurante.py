from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase encargada de administrar los productos y clientes
    del restaurante.
    """

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un producto o bebida.
        Retorna True si el registro fue exitoso,
        False si el código ya existe.
        """
        for producto_existente in self.productos:
            if producto_existente.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """
        Registra un cliente.
        Retorna True si el registro fue exitoso,
        False si la identificación ya existe.
        """
        for cliente_existente in self.clientes:
            if cliente_existente.identificacion == cliente.identificacion:
                return False

        self.clientes.append(cliente)
        return True

    def listar_productos(self) -> None:
        """
        Lista todos los productos registrados.
        Aplica polimorfismo utilizando el método
        mostrar_informacion().
        """
        if not self.productos:
            print("\nNo existen productos registrados.")
            return

        print("\n========== PRODUCTOS ==========\n")

        for producto in self.productos:
            print(producto.mostrar_informacion())

    def listar_clientes(self) -> None:
        """
        Lista todos los clientes registrados.
        """
        if not self.clientes:
            print("\nNo existen clientes registrados.")
            return

        print("\n========== CLIENTES ==========\n")

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())