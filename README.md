# Restaurante App - Principios SOLID en Python

## Información del estudiante

**Nombre:** Elkin Esteban Tovar Caicedo

---

# Descripción del sistema

**Restaurante App** es un sistema desarrollado en Python utilizando Programación Orientada a Objetos (POO). Su propósito es administrar el registro y listado de productos, bebidas y clientes mediante un menú interactivo ejecutado desde la consola.

El proyecto está organizado mediante una arquitectura modular, separando los modelos de las clases de servicio para mantener un código más ordenado, reutilizable y fácil de mantener. Además, implementa los principios SOLID solicitados en la actividad, específicamente Responsabilidad Única (SRP), Abierto/Cerrado (OCP) y Sustitución de Liskov (LSP).

---

# Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

---

# Responsabilidad de cada clase

## Producto

Representa un producto general del restaurante. Contiene la información común de cualquier producto, como código, nombre, categoría y precio, además del método `mostrar_informacion()`.

---

## Bebida

Hereda de la clase Producto y representa una bebida del restaurante. Incorpora información específica como el tamaño y el tipo de envase, además de sobrescribir el método `mostrar_informacion()` para mostrar estos datos adicionales.

---

## Cliente

Representa la información de un cliente registrado en el sistema. Contiene la identificación, el nombre y el correo electrónico del cliente.

---

## Restaurante

Es la clase de servicio encargada de administrar las colecciones de productos y clientes. Permite registrar nuevos elementos, validar códigos e identificaciones duplicadas y listar la información registrada.

---

## main.py

Es el punto de inicio del programa. Se encarga de mostrar el menú interactivo, solicitar los datos mediante `input()`, crear los objetos correspondientes y llamar a los métodos de la clase Restaurante. No administra directamente las listas internas del sistema.

---

# Relación entre Producto y Bebida

La clase **Bebida** mantiene una relación de herencia con la clase **Producto**, ya que una bebida representa un tipo específico de producto del restaurante.

Gracias a esta relación, una bebida puede utilizarse en cualquier lugar donde el sistema espere un objeto de tipo Producto, permitiendo administrar todos los productos mediante una única colección y evitando duplicar la lógica del sistema.

Esta implementación favorece el polimorfismo, ya que cada objeto ejecuta su propia versión del método `mostrar_informacion()` sin que el servicio necesite conocer el tipo concreto del objeto.

---

# Principios SOLID aplicados

## S — Responsabilidad Única (SRP)

Cada clase cumple una única responsabilidad dentro del sistema:

- Producto representa un producto.
- Bebida representa un tipo específico de producto.
- Cliente representa la información de un cliente.
- Restaurante administra las operaciones del sistema.
- main.py únicamente coordina la interacción con el usuario.

---

## O — Abierto/Cerrado (OCP)

La clase Bebida amplía el comportamiento de Producto mediante herencia sin modificar la lógica de la clase Restaurante.

El sistema puede aceptar nuevos tipos de productos sin necesidad de cambiar el funcionamiento del servicio principal.

---

## L — Sustitución de Liskov (LSP)

Los objetos de tipo Bebida pueden utilizarse como objetos Producto sin alterar el funcionamiento del sistema.

Durante el listado de productos, el servicio ejecuta el método `mostrar_informacion()` para todos los objetos registrados, independientemente de si corresponden a un Producto o una Bebida.

---

# Instrucciones de ejecución

1. Descargar o clonar el repositorio.
2. Abrir el proyecto en Visual Studio Code o cualquier editor compatible con Python.
3. Acceder a la carpeta del proyecto mediante la terminal.
4. Ejecutar el archivo principal con el siguiente comando:

```bash
python main.py
```

5. Utilizar el menú interactivo para registrar productos, bebidas y clientes, así como visualizar la información almacenada.

---

# Reflexión

Aplicar los principios SOLID durante el desarrollo de un proyecto permite construir programas más organizados, reutilizables y fáciles de mantener. Al asignar responsabilidades específicas a cada clase y aprovechar la herencia y el polimorfismo, el código resulta más flexible para incorporar nuevas funcionalidades sin afectar el funcionamiento existente. Esta práctica favorece el desarrollo de software de mayor calidad y facilita su mantenimiento a largo plazo.
