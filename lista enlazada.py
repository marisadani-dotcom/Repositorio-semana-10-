# 1. Definición del Nodo de la lista enlazada
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

# 2. Funciones auxiliares que te pide el menú
def insertar_final(cabeza, nombre):
    nuevo_nodo = Nodo(nombre)
    if not cabeza:
        return nuevo_nodo
    actual = cabeza
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nuevo_nodo
    return cabeza

def mostrar(cabeza):
    actual = cabeza
    if not actual:
        print("La lista está vacía.")
        return
    while actual:
        print(actual.nombre, end=" -> ")
        actual = actual.siguiente
    print("None")

def buscar(cabeza, nombre):
    actual = cabeza
    posicion = 1
    while actual:
        if actual.nombre == nombre:
            return posicion
        actual = actual.siguiente
        posicion += 1
    return -1

def eliminar(cabeza, nombre):
    if not cabeza:
        return None, False
    
    # Si el elemento a eliminar es la cabeza
    if cabeza.nombre == nombre:
        return cabeza.siguiente, True
        
    actual = cabeza
    while actual.siguiente:
        if actual.siguiente.nombre == nombre:
            actual.siguiente = actual.siguiente.siguiente
            return cabeza, True
        actual = actual.siguiente
    return cabeza, False

def contar(cabeza):
    actual = cabeza
    contador = 0
    while actual:
        contador += 1
        actual = actual.siguiente
    return contador

def menu():
    cabeza = None

# 1. Definición del Nodo de la lista enlazada
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

# 2. Funciones auxiliares que te pide el menú
def insertar_final(cabeza, nombre):
    nuevo_nodo = Nodo(nombre)
    if not cabeza:
        return nuevo_nodo
    actual = cabeza
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nuevo_nodo
    return cabeza

def mostrar(cabeza):
    actual = cabeza
    if not actual:
        print("La lista está vacía.")
        return
    while actual:
        print(actual.nombre, end=" -> ")
        actual = actual.siguiente
    print("None")

def buscar(cabeza, nombre):
    actual = cabeza
    posicion = 1
    while actual:
        if actual.nombre == nombre:
            return posicion
        actual = actual.siguiente
        posicion += 1
    return -1

def eliminar(cabeza, nombre):
    if not cabeza:
        return None, False
    
    # Si el elemento a eliminar es la cabeza
    if cabeza.nombre == nombre:
        return cabeza.siguiente, True
        
    actual = cabeza
    while actual.siguiente:
        if actual.siguiente.nombre == nombre:
            actual.siguiente = actual.siguiente.siguiente
            return cabeza, True
        actual = actual.siguiente
    return cabeza, False

def contar(cabeza):
    actual = cabeza
    contador = 0
    while actual:
        contador += 1
        actual = actual.siguiente
    return contador

# 3. Tu función del menú (colócala abajo de las funciones anteriores)
def menu():
    cabeza = None
    # ... (aquí va el código del menú que ya copiaste)