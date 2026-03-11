# Árbol Binario de Búsqueda (ABB) con Visualización en Graphviz
# Autor

Nombre: Pablo Andrés Say Oliva
Carnet: 9490-24 -18876

## Descripción del Proyecto

Este proyecto consiste en la implementación de un **Árbol Binario de Búsqueda (ABB)** utilizando el lenguaje de programación **Python**.

El programa permite al usuario **crear, manipular y visualizar un árbol binario de búsqueda mediante una interfaz de línea de comandos (CLI)**.

Además de las operaciones básicas sobre el árbol, el sistema permite **generar automáticamente una representación gráfica del árbol utilizando Graphviz**, lo que facilita visualizar la estructura de los nodos y sus relaciones.

Este programa fue desarrollado como parte de un ejercicio académico para comprender el funcionamiento de las **estructuras de datos tipo árbol** y su manipulación mediante programación.

---

# Funcionalidades del Programa

El programa incluye las siguientes funcionalidades:

### 1. Insertar

Permite al usuario ingresar un número entero para agregarlo al árbol binario de búsqueda.

El árbol mantiene automáticamente las reglas del ABB:

* Los valores **menores** se insertan en el **subárbol izquierdo**.
* Los valores **mayores** se insertan en el **subárbol derecho**.

---

### 2. Buscar

Permite verificar si un número existe dentro del árbol.

El programa informará si el número:

* **Existe dentro del árbol**, o
* **No se encuentra registrado**.

---

### 3. Eliminar

Permite eliminar un número específico del árbol binario de búsqueda.

El algoritmo maneja los tres casos posibles de eliminación:

* Nodo hoja
* Nodo con un hijo
* Nodo con dos hijos

---

### 4. Cargar datos desde archivo

El programa permite construir el árbol automáticamente cargando números desde un archivo externo.

Se pueden cargar archivos:

* `.txt`
* `.csv`

Los números pueden estar:

* separados por comas
* o en líneas diferentes.

Ejemplo de archivo:

```
50,30,70,20,40,60,80
```

o

```
50
30
70
20
40
60
80
```

Cada número será insertado automáticamente en el árbol.

---

### 5. Generar visualización del árbol

El programa genera una **representación gráfica del árbol utilizando Graphviz**.

Cuando se selecciona la opción de visualización:

* Se crea un archivo llamado:

```
arbol_binario.png
```

* Este archivo muestra los nodos del árbol y sus conexiones.

La imagen se abre automáticamente al generarse.

---

# Requisitos del Sistema

Para ejecutar el programa se requiere:

* **Python 3**
* **Graphviz**
* Librería **graphviz para Python**

---

# Instalación

### 1. Clonar el repositorio

```
git clone https://github.com/USUARIO/NOMBRE_REPOSITORIO.git
```

Entrar a la carpeta del proyecto:

```
cd NOMBRE_REPOSITORIO
```

---

### 2. Instalar dependencias

Instalar la librería de Python:

```
pip install graphviz
```

---

### 3. Instalar Graphviz en el sistema

Descargar Graphviz desde:

https://graphviz.org/download/

Después de instalarlo, asegurarse de que **Graphviz esté agregado al PATH del sistema**.

---

# Ejecución del Programa

Para ejecutar el programa usar el siguiente comando:

```
python abb_graphviz.py
```

Al ejecutarlo aparecerá el siguiente menú interactivo:

```
===== MENU ABB =====
1. Insertar número
2. Buscar número
3. Eliminar número
4. Cargar desde archivo
5. Visualizar árbol (Graphviz)
6. Salir
```

---

# Cómo usar el programa

## Insertar números manualmente

1. Seleccionar la opción **1**
2. Ingresar el número deseado

Ejemplo:

```
Ingrese número a insertar: 50
```

El número será agregado al árbol.

---

## Buscar un número

1. Seleccionar la opción **2**
2. Escribir el número a buscar

El programa indicará si el número existe en el árbol.

---

## Eliminar un número

1. Seleccionar la opción **3**
2. Escribir el número que se desea eliminar

El árbol se actualizará automáticamente.

---

## Cargar datos desde un archivo

1. Seleccionar la opción **4**
2. Escribir la ruta del archivo

Ejemplo:

```
datos.txt
```

o

```
C:/Users/Pablo/Desktop/datos.txt
```

Los números contenidos en el archivo se insertarán automáticamente en el árbol.

---

## Generar la imagen del árbol

1. Seleccionar la opción **5**

El programa generará una imagen del árbol llamada:

```
arbol_binario.png
```

La imagen mostrará gráficamente:

* cada nodo del árbol
* sus conexiones izquierda y derecha

Esto permite visualizar la estructura del árbol binario de búsqueda.

---

# Estructura del Proyecto

```
ArbolBinarioBusqueda/
│
├── abb_graphviz.py
├── datos.txt
├── README.md
```

---
