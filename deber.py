# -------------------------------
# Actividad 1: Clase Pila
# -------------------------------

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return "La pila está vacía"

    def mostrar_cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return "La pila está vacía"

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar_pila(self):
        return self.elementos

# Simulación: historial de navegación
historial = Pila()
historial.apilar("Página: Google")
historial.apilar("Página: YouTube")
historial.apilar("Página: Wikipedia")

print("Historial actual:", historial.mostrar_pila())
print("Retrocediendo:", historial.desapilar())
print("Historial después de retroceder:", historial.mostrar_pila())


# -------------------------------
# Actividad 2: Clase Cola
# -------------------------------

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            return "La cola está vacía"

    def ver_frente(self):
        if not self.esta_vacia():
            return self.elementos[0]
        else:
            return "La cola está vacía"

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar_cola(self):
        return self.elementos

# Simulación: cola en un banco
cola_banco = Cola()
cola_banco.encolar("Cliente 1")
cola_banco.encolar("Cliente 2")
cola_banco.encolar("Cliente 3")

print("Cola actual:", cola_banco.mostrar_cola())
print("Atendiendo:", cola_banco.desencolar())
print("Cola después de atender:", cola_banco.mostrar_cola())
