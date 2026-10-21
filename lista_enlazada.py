def crear_nodo(nombre):
    """Crea un nodo utilizando un diccionario."""
    return {"nombre": nombre, "siguiente": None}

def agregar_turno(cabeza, nombre):
    """Registra un turno al final de la lista."""
    nuevo_nodo = crear_nodo(nombre)
    if cabeza is None:
        print(f"Turno registrado para {nombre} (Posición: 1).")
        return nuevo_nodo
    
    actual = cabeza
    posicion = 1
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
        posicion += 1
    
    actual["siguiente"] = nuevo_nodo
    print(f"Turno registrado para {nombre} (Posición: {posicion + 1}).")
    return cabeza

def buscar_turno(cabeza, nombre):
    """Busca un estudiante por nombre (distingue mayúsculas/minúsculas) y muestra su posición."""
    actual = cabeza
    posicion = 1
    while actual is not None:
        if actual["nombre"] == nombre:
            print(f"Estudiante '{nombre}' encontrado en la posición {posicion}.")
            return posicion
        actual = actual["siguiente"]
        posicion += 1
    print(f"Estudiante '{nombre}' no se encuentra en la lista de turnos.")
    return -1

def eliminar_turno(cabeza, nombre):
    """Cancela el turno del primer estudiante que coincida con el nombre."""
    if cabeza is None:
        print("La lista está vacía. No hay turnos para cancelar.")
        return None

    # Caso 1: El primer nodo es el que se va a eliminar
    if cabeza["nombre"] == nombre:
        print(f"Confirmación: Turno de '{nombre}' cancelado exitosamente.")
        return cabeza["siguiente"]

    # Caso 2: Buscar en el resto de la lista
    actual = cabeza
    while actual["siguiente"] is not None:
        if actual["siguiente"]["nombre"] == nombre:
            # Enlazamos el nodo actual con el subsiguiente para saltar el eliminado
            actual["siguiente"] = actual["siguiente"]["siguiente"]
            print(f"Confirmación: Turno de '{nombre}' cancelado exitosamente.")
            return cabeza
        actual = actual["siguiente"]

    print(f"No se encontró ningún turno a nombre de '{nombre}' para cancelar.")
    return cabeza

def mostrar_turnos(cabeza):
    """Muestra todos los turnos en orden y cuenta la cantidad total."""
    if cabeza is None:
        print("\n--- No hay turnos registrados en el sistema (Cantidad: 0) ---")
        return
    
    print("\n--- Lista de Turnos en Orden ---")
    actual = cabeza
    cantidad = 0
    while actual is not None:
        cantidad += 1
        print(f"{cantidad}. {actual['nombre']}")
        actual = actual["siguiente"]
    print(f"--------------------------------")
    print(f"Cantidad total de turnos: {cantidad}\n")

def menu():
    """Menú interactivo por consola."""
    cabeza = None
    while True:
        print("\n=== MENÚ TURNOS LABORATORIO ===")
        print("1. Registrar turno (al final)")
        print("2. Buscar turno por nombre")
        print("3. Cancelar turno (primera coincidencia)")
        print("4. Mostrar todos los turnos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            if nombre:
                cabeza = agregar_turno(cabeza, nombre)
            else:
                print("Error: El nombre no puede estar vacío.")
                
        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ").strip()
            buscar_turno(cabeza, nombre)
            
        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante a cancelar: ").strip()
            cabeza = eliminar_turno(cabeza, nombre)
            
        elif opcion == "4":
            mostrar_turnos(cabeza)
            
        elif opcion == "5":
            print("Saliendo del sistema de turnos.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()