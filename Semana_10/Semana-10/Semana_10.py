from Cajero import Cajero
c = Cajero()

while True:
    print("Bienvenidos al sistema cajero\n")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir\n")

    while True:
       opc = input("Ingrese una opción: ")

       if  opc in ("1", "2", "3", "4"):
           break
       else:
           print("Error. Opción no válida.\n")

    match opc:
        case "1":
            print(f"\nSaldo disponible es S/{round(c. consultar(),2)}")
        case "2":
            c.depositar(0)
        case "3":
            c.retirar(0)
        case "4":
            quit()      # exit()

    while True:
        conti = input("\n¿Desea continuar? (s/n): ")
        if conti in ("s", "n"):
            break
        else:
            print("Error. Solo se permiten 's' o 'n'.")

    if(conti == "n"): break
    print()
