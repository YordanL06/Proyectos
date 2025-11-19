class Persona:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre: str, apellido: str, numero_cuenta: str, balance_inicial: float = 0.0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance_inicial = float(balance_inicial)

    def __str__(self):
        return (
            f"Cliente: {self.nombre} {self.apellido}\n"
            f"Cuenta: {self.numero_cuenta}\n"
            f"Balance: Q. {self.balance_inicial:.2f}\n"
        )

    def depositar(self, monto: float = 0.0):
        try:
            monto = float(monto)
        except (ValueError, TypeError):
            print("Monto inválido. Operación cancelada.")
            return False

        if monto <= 0:
            print("El monto a depositar debe ser mayor que 0.")
            return False

        self.balance_inicial += monto
        print("Depósito aceptado.")
        return True

    def retirar(self, monto_retiro: float = 0.0):
        try:
            monto_retiro = float(monto_retiro)
        except (ValueError, TypeError):
            print("Monto inválido. Operación cancelada.")
            return False

        if monto_retiro <= 0:
            print("El monto a retirar debe ser mayor que 0.")
            return False

        if monto_retiro <= self.balance_inicial:
            self.balance_inicial -= monto_retiro
            print("Retiro realizado.")
            return True
        else:
            print("Fondos insuficientes.")
            return False


def crear_cliente():
    print("****** Creando Cliente ******")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    numero_cuenta = input("Número de cuenta: ").strip()

    return Cliente(nombre, apellido, numero_cuenta, balance_inicial=0.0)


def inicio():
    cliente = crear_cliente()
    print("\nCliente creado con éxito:")
    print(cliente)

    while True:
        print("\n------ MENÚ ------")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar datos del cliente")
        print("4. Salir")

        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            monto_text = input("Ingrese monto a depositar: ").strip()
            if monto_text == "":
                print("No ingresaste monto.")
                continue
            cliente.depositar(monto_text)

        elif opcion == "2":
            monto_text = input("Ingrese monto a retirar: ").strip()
            if monto_text == "":
                print("No ingresaste monto.")
                continue
            cliente.retirar(monto_text)

        elif opcion == "3":
            print(cliente)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    try:
        inicio()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Saliendo...")
