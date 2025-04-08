from cola import Cola
class Supermercado:
    fila = Cola()

    def agregar_cliente(self, cliente):
        print(f"{cliente} se agrega a la fila")
        self.fila.encolar(cliente)

    def atender_cliente(self):
        if self.fila.esta_vacia():
            print("No hay mas clientes para atender, andá a descansar")
        else:
            cliente = self.fila.desencolar()
            print(f"{cliente} es atendido")

    def mostrar_siguiente(self):
        cliente = self.fila.ver_frente()
        print(f"{cliente} es el siguiente en la fila")