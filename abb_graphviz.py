import csv
from graphviz import Digraph

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    # INSERTAR
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)

    # BUSCAR
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    # ELIMINAR
    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)

        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)

        else:

            if nodo.izquierda is None:
                return nodo.derecha

            elif nodo.derecha is None:
                return nodo.izquierda

            temp = self._minimo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.valor)

        return nodo

    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    # CARGAR DESDE ARCHIVO
    def cargar_archivo(self, ruta):
        try:
            with open(ruta, 'r') as archivo:

                for linea in archivo:
                    numeros = linea.strip().split(',')

                    for num in numeros:
                        if num.strip() != "":
                            self.insertar(int(num.strip()))

            print("Datos cargados correctamente.")

        except Exception as e:
            print("Error al cargar archivo:", e)

    # GENERAR GRAPHVIZ
    def graficar(self):
        dot = Digraph()

        def agregar_nodos(nodo):
            if nodo:
                dot.node(str(nodo.valor))

                if nodo.izquierda:
                    dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                    agregar_nodos(nodo.izquierda)

                if nodo.derecha:
                    dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                    agregar_nodos(nodo.derecha)

        agregar_nodos(self.raiz)

        dot.render("arbol_binario", view=True)


# MENU INTERACTIVO
def menu():

    arbol = ArbolBinarioBusqueda()

    while True:

        print("\n===== MENU ABB =====")
        print("1. Insertar número")
        print("2. Buscar número")
        print("3. Eliminar número")
        print("4. Cargar desde archivo")
        print("5. Visualizar árbol (Graphviz)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            valor = int(input("Ingrese número a insertar: "))
            arbol.insertar(valor)
            print("Número insertado.")

        elif opcion == "2":

            valor = int(input("Ingrese número a buscar: "))
            encontrado = arbol.buscar(valor)

            if encontrado:
                print("El número existe en el árbol.")
            else:
                print("El número NO existe.")

        elif opcion == "3":

            valor = int(input("Ingrese número a eliminar: "))
            arbol.eliminar(valor)
            print("Número eliminado.")

        elif opcion == "4":

            ruta = input("Ingrese ruta del archivo (.txt o .csv): ")
            arbol.cargar_archivo(ruta)

        elif opcion == "5":

            arbol.graficar()

        elif opcion == "6":

            print("Saliendo del programa.")
            break

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    menu()