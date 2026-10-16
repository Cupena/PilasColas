pila = []

def evaluar_vacio(pila):
    return len(pila) == 0

def calcular_limite(pila, limite):
    return len(pila) >= limite
    
def agregar_elemento(pila, elemento):
    if calcular_limite(pila, limite):
        return "Tope excedido . . ."
    else:
        pila.append(elemento)
        return "Elemento agregado."

def leer_cantidad(pila):
    print("Cantidad de elementos: ", len(pila))

def retirar_elemento(pila):
    if evaluar_vacio(pila):
        return "Caja vacia" 
    else:
        eliminado = pila.pop()
        return f"Elemento retirado: , {eliminado}"

def menu():
    return """===   MENU   ===
    1. Agregar
    2. Cantidad
    3. Retirar
    4. Mostrar Ultimo elemento
    5. Salir"""

def error():
    return "Ingrese un numero del 1 al 4."

def mostrar_ultElemento(pila):
    if evaluar_vacio(pila):
        return "Caja vacia"
    else:
        return f"El ultimo elemento es: , {pila[-1]}"

def principal():
    while True:
        print(menu())
        try:
            op = int(input("Elija su opcion: "))
        except ValueError:
            print(error())
            continue

        if op == 1:
            elemento = input("Ingrese su elemento: ")
            print(agregar_elemento(pila, elemento))
        elif op ==2:
            leer_cantidad(pila)
        elif op == 3:
            print(retirar_elemento(pila))
        elif op ==4:
            print(mostrar_ultElemento(pila))
        elif op == 5:
            break
        else:
            print(error())

try:
    limite = int(input("Ingrese el limite de la caja: "))
except ValueError:  
    error()

principal()