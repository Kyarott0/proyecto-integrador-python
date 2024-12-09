# PROYECTO INTEGRADOR, INVENTARIO DE TIENDA

import sqlite3


# CONEXIÓN BASE DE DATOS
def conectar():
    return sqlite3.connect("inventario.db")


# CREACION TABLA DE DATOS
def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            descripcion TEXT NULL,
            cantidad INTEGER NOT NULL, 
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
            )"""
    )
    conexion.commit()
    conexion.close()


# REGISTRAMOS UN NUEVO PRODUCTO
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad de stock: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)",
        (nombre, descripcion, cantidad, precio, categoria),
    )
    conexion.commit()
    conexion.close()
    print(f"El producto {nombre} ha sido registrado correctamente.\n")


# VISUALIZACION DE PRODUCTOS
def visualizar_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if len(productos) == 0:
        print("\nNo hay productos registrados.")
    else:
        print("\nListado de productos: ")
        for producto in productos:
            print(
                f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: $ {producto[4]}, Categoría: {producto[5]}"
            )
    conexion.close()


# ACTUALIZACIÓN DE PRODUCTO
def actualizar_producto():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto)
    )
    conexion.commit()
    conexion.close()
    print(
        f"Producto con ID: {id_producto} actualizado de la tabla de productos correctamente."
    )


# ELIMINACIÓN DE PRODUCTO
def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    conexion.close()
    print(
        f"El producto con ID: {id_producto} se ha eliminado de la tabla de productos correctamente"
    )


# FUNCION PARA LISTAR PRODUCTOS CON BAJO STOCK
def reporte_bajo_stock():
    cantidad_minima = int(input("Ingrese el mínimo de stock que debería haber: "))

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (cantidad_minima,))
    productos = cursor.fetchall()

    print("\nProductos con bajo stock: ")
    for producto in productos:
        print(
            f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: $ {producto[4]}, Categoría: {producto[5]}"
        )

    conexion.close()


# FUNCION PARA BUSCAR PRODUCTOS POR ID
def buscar_por_id():
    p_id = int(input("Ingrese el ID del producto que quiere buscar."))

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (p_id,))
    producto = cursor.fetchone()

    if producto:
        print(
            f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoría: {producto[5]}"
        )
    else:
        print(f"No se encontró un producto con el ID {p_id}.")

    conexion.close()


# FUNCIÓN PARA BUSCAR PRODUCTOS POR CATEGORIA
def filtrar_por_categoria():
    categoria = input("Ingrese la categoría por la que quiere filtrar:")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE categoria = ?", (categoria,))
    productos = cursor.fetchall()

    if productos:
        print(f"\nProductos con categoría '{categoria}': ")
        for producto in productos:
            print(
                f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: $ {producto[4]}, Categoría: {producto[5]}"
            )
    else:
        print(f"No se encontraron productos con la categoría: {categoria}")
    conexion.close()


# MENU PRINCIPAL
def menu():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar un producto")
        print("2. Visualizar productos")
        print("3. Actualizar la cantidad de un producto")
        print("4. Eliminar producto")
        print("5. Reporte de bajo stock")
        print("6. Buscar producto por ID")
        print("7. Filtrar productos por categoría")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            visualizar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            buscar_por_id()
        elif opcion == "7":
            filtrar_por_categoria()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# INICIALIZACIÓN

if __name__ == "__main__":
    crear_tabla()
    menu()
