class Cajero:
    saldo = 1000

    def consultar(self) -> float:
        return self.saldo

    def depositar(self, monto) -> None:
        while True:
            try:
                monto = input("\nIngrese monto a depositar: ")
                m = float(monto)

                if m > 0:
                    self.saldo += m
                    print("\nDepósito exitoso.")
                    break
                else:
                    print("Error. Solo se deposita montos mayores a 0.\n")
                    continue

            except ValueError:      # Mensaje de error
                print("Error. Solo se permiten números.\n")
                continue

    def retirar(self, monto) -> None:
        while True:
            try:
                monto = input("\nIngrese monto a retirar: ")
                m = float(monto)

                if m > self.saldo:
                    print("Error. El monto solicitado supera su saldo actual.\n")
                    continue
                elif m > 0:
                    self.saldo -= m
                    print("\nRetiro exitoso.")
                    break    
                else:
                    print("Error. Solo se retiran montos mayores a 0.\n")
                    continue

            except ValueError:
                print("Error. Solo se permiten números.\n")
                continue
