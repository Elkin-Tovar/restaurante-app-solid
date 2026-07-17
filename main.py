from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n===== REGISTRAR PRODUCTO =====")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))

    producto = Producto(codigo, nombre, categoria, precio)

    if restaurante.registrar_producto(producto):
        print("\n✅ Producto registrado correctamente.")
    else:
        print("\n❌ Ya existe un producto con ese código.")


def registrar_bebida(restaurante: Restaurante) -> None:
    print("\n===== REGISTRAR BEBIDA =====")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    tamano = input("Tamaño: ")
    envase = input("Tipo de envase: ")

    bebida = Bebida(
        codigo,
        nombre,
        categoria,
        precio,
        tamano,
        envase
    )

    if restaurante.registrar_producto(bebida):
        print("\n✅ Bebida registrada correctamente.")
    else:
        print("\n❌ Ya existe un producto con ese código.")


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\n===== REGISTRAR CLIENTE =====")

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")

    cliente = Cliente(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_cliente(cliente):
        print("\n✅ Cliente registrado correctamente.")
    else:
        print("\n❌ Ya existe un cliente con esa identificación.")


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def main() -> None:
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            registrar_bebida(restaurante)

        elif opcion == "3":
            registrar_cliente(restaurante)

        elif opcion == "4":
            restaurante.listar_productos()

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            print("\n¡Gracias por utilizar el sistema!")
            break

        else:
            print("\n❌ Opción no válida.")


if __name__ == "__main__":
    main()