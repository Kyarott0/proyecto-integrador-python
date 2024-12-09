# Inventario de Tienda

Este proyecto es un Sistema de gestión de inventario para una tienda, desarrollado en Python con SQLite como base de datos. 
Permite registrar, visualizar, actualizar y eliminar productos, así como generar reportes de bajo stock, buscar productos por ID y filtrar por diferentes categorías de cada producto.

## Características

- Conexión a SQLite: Almacena y gestiona la información en una base de datos local.
- Registro de productos: Agrega productos al inventario con detalles como nombre, descripción, cantidad, precio y categoría.
- Visualización de productos: Muestra todos los productos disponibles indicando solamente su nombre, precio y categoría.
- Actualización de productos: Permite modificar la cantidad en stock de un producto.
- Eliminación de productos: Borra productos específicos por ID.
- Reportes de bajo stock: Lista productos con cantidad inferior al mínimo establecido.
- Búsqueda por ID: Encuentra detalles de un producto específico mediante su ID, muestra todos los datos que se tenga del producto.
- Filtrar por categorías: Filtra todos los productos que compartan la misma categoría ingresada.
- Menú interactivo: Ofrece una interfaz de consola simple para navegar entre las funcionalidades.

## Requisitos

- Python 3.x
- Biblioteca estándar de Python (`sqlite3` incluida por defecto)


## Instalación

1. Clona este repositorio o descarga los archivos:
   git clone https://github.com/Kyarott0/proyecto-integrador-python.git
   cd proyecto-integrador-python
2. Asegúrate de tener Python instalado:
   python --version
3. Ejecuta el programa:
   python inventario.py


## Uso
    Al iniciar el programa, se crea automáticamente la base de datos inventario.db (si no existe) con la tabla productos.

    Menú principal:
        Opción 1: Agregar un producto.
        Opción 2: Visualizar todos los productos.
        Opción 3: Actualizar la cantidad de un producto.
        Opción 4: Eliminar un producto.
        Opción 5: Generar un reporte de bajo stock.
        Opción 6: Buscar un producto por ID.
        Opción 7: Filtrar productos por categoría
        Opción 8: Salir del programa.

