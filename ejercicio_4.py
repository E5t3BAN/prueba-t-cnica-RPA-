# Inicializamos los productos y existencias en cada grupo
dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
dairy_stock = [28, 36, 50]

cleaning_products = ["Windex", "Lysol", "Mr. Clean"]
cleaning_stock = [20, 15, 30]

grain_products = ["Rice", "Quinoa", "Oats"]
grain_stock = [40, 25, 35]

# Función para registrar un producto entrante
def registrar_producto(nombre_producto, cantidad, grupo):
    global dairy_products, dairy_stock, cleaning_products, cleaning_stock, grain_products, grain_stock
    if grupo.lower() == 'dairy':
        if nombre_producto in dairy_products:
            indice = dairy_products.index(nombre_producto)
            dairy_stock[indice] += cantidad
        else:
            dairy_products.append(nombre_producto)
            dairy_stock.append(cantidad)
    elif grupo.lower() == 'cleaning':
        if nombre_producto in cleaning_products:
            indice = cleaning_products.index(nombre_producto)
            cleaning_stock[indice] += cantidad
        else:
            cleaning_products.append(nombre_producto)
            cleaning_stock.append(cantidad)
    elif grupo.lower() == 'grain':
        if nombre_producto in grain_products:
            indice = grain_products.index(nombre_producto)
            grain_stock[indice] += cantidad
        else:
            grain_products.append(nombre_producto)
            grain_stock.append(cantidad)
    else:
        print("Grupo inválido.")

# Función para mostrar todo el inventario
def mostrar_inventario():
    print("Inventario:")
    print("Grupo Dairy:")
    for producto, existencia in zip(dairy_products, dairy_stock):
        print(f"Producto: {producto}, Existencia: {existencia}")
    print("Grupo Cleaning:")
    for producto, existencia in zip(cleaning_products, cleaning_stock):
        print(f"Producto: {producto}, Existencia: {existencia}")
    print("Grupo Grain:")
    for producto, existencia in zip(grain_products, grain_stock):
        print(f"Producto: {producto}, Existencia: {existencia}")

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("_____Menu:_____")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Salir")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            grupo = input("Ingrese el grupo del producto (dairy, cleaning, grain): ")
            registrar_producto(nombre, cantidad, grupo)
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()