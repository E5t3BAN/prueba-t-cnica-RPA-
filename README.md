# prueba tecnica instruciones.
Estos ejercicios estan desarrollados en python
## Ejercicio 1.
Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término. Ejemplos:

Entrada : numero=3, terminos=5
Salida : 37035 #(3 + 33 + 333 + 3333 + 33333)

Entrada : numero=5, terminos=3
Salida : 615 #(5 + 55 + 555)

####  Función numeroRepetido(numero, nterminos)
Esta función toma dos parámetros:

numero (int): El número que se repite en la serie.
nterminos (int): El número de términos en la serie.
La función itera sobre la serie y calcula la suma total de los términos concatenados.

####Ejemplos de uso:

print(numeroRepetido(3, 5)) # Salida: xxxx
print(numeroRepetido(5, 3)) # Salida: xxxx

####Cómo usar

1.  Clona el repositorio o copia el código en tu entorno de desarrollo.
2. Ejecuta el archivo `py ejercicio_1py`.
3.  Puedes modificar los parámetros numero y nterminos para probar diferentes casos.


##Ejercicio 2.
Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las siguientes condiciones:

1. El número debe ser divisible por cinco.
2. Si el número es mayor que 600, no se incluye en la salida.
3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.

Ejemplos:

Entrada : [24, 150, 300, 660, 295, 1050, 50]
Salida : [150, 300, 295]

Entrada : [110, 720, 307, 555, 1095, 12, 300, 1000]
Salida : [110, 555]

####Función listaFiltrados(listado)
Esta función toma un parámetro:

listado (list): La lista de números de entrada.
La función itera sobre la lista y agrega los números que cumplen las condiciones a una lista de salida.

####Condiciones de Filtrado:
1. Los números deben ser divisibles por cinco.
2. Si el número es mayor que 1000, se detiene el procesamiento y se retorna el resultado.
3. Si el número es mayor que 600, no se incluye en la salida.


####Ejemplo de Uso:

entrada = [500, 1200, 525, 1100, 1000, 1500]
resultado = listaFiltrados(entrada)
print(resultado) # Salida: xxxx

####Cómo usar

1. Clona el repositorio o copia el código en tu entorno de desarrollo.
2. Ejecuta el archivo `py ejercicio_2.py`.
3. Puedes modificar el parámetro entrada para probar diferentes casos.

##Ejercicio 3.
Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz de salida (no importa el orden). Ejemplos:

Entrada : list = [12, 25, 1, 1, 7, 25] Salida : [[12], [7], [25, 25], [1, 1]]
Entrada : list = [6, 7, 8, 9] Salida : [[6], [7], [8], [9]]


####Función agrupacionNumeros(lista)
Esta función toma un parámetro:

lista (list): La lista de números de entrada.
La función itera sobre la lista y agrupa los números similares en conjuntos utilizando un diccionario.

####Ejemplo de Uso:

entrada = [12, 25, 1, 1, 7, 25]
resultado = agrupacionNumeros(entrada)
print(resultado) # Salida: xxxx


####Cómo usar
1. Clona el repositorio o copia el código en tu entorno de desarrollo.
2. Ejecuta el archivo `py ejericio_3.py`.
3. Puedes modificar el parámetro entrada para probar diferentes casos.

##Ejercicio 4.
En un negocio reciben periódicamente productos para la venta, se requiere desarrollar un programa de consola (o terminal) que cumpla con los siguientes requerimientos:

1. Se requiere organizar el inventario en los siguientes grupos: dairy, cleaning y grain.
2. Cada grupo tiene que estar asociado a un elemento de otra lista que almacena las existencias de ese grupo en la misma posición, como en el siguiente ejemplo:

dairy_products = [“Fairlife Milk”, “Alta Dena Milk”, “Queensland Butter”]
dairy_stock = [28, 36, 50]
En donde, por ejemplo, el producto del grupo dairy “Alta Dena Milk” tiene una existencia de 36 unidades.

3. Para un producto entrante, se debe poder registrar en el sistema: el nombre del producto, la cantidad y el grupo al que pertenece.


4. Si el producto no existe en la lista, se debe agregar al final con su cantidad entrante, pero si existe se debe actualizar el número de existencias sumando la nueva cantidad.

5. El programa debe permitir visualizar todo el inventario de productos y existencias.

####Funcionalidades

1. Inicialización del Inventario
Los productos y sus existencias iniciales se organizan en los siguientes grupos:

Grupo Dairy:

Productos: Fairlife Milk, Alta Dena Milk, Queensland Butter
Existencias: 28, 36, 50
Grupo Cleaning:

Productos: Windex, Lysol, Mr. Clean
Existencias: 20, 15, 30
Grupo Grain:

Productos: Rice, Quinoa, Oats
Existencias: 40, 25, 35

2. Registro de Producto
La función registrar_producto(nombre_producto, cantidad, grupo) permite registrar un nuevo producto en el inventario o actualizar las existencias de un producto existente. Se solicita al usuario ingresar el nombre del producto, la cantidad y el grupo al que pertenece.

3. Mostrar Inventario
La función mostrar_inventario() muestra todo el inventario de productos y existencias organizados por grupos.

4. Menú de Opciones
El programa presenta un menú de opciones que permite al usuario seleccionar entre registrar un producto, mostrar el inventario o salir del programa.

####Cómo Usar
1. Clona el repositorio o copia el código en tu entorno de desarrollo.
2. Ejecuta el archivo `py ejercicio_4.py`.
3. Sigue las instrucciones en el menú para registrar productos, mostrar el inventario o salir del programa.
