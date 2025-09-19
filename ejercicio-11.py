#11 Cajero automático
saldo = int(100000)

while saldo > 0:
    print(f"Tu saldo es de: {saldo}")
    retiro = int(input("ingresa monto a retirar: "))

    if retiro <= saldo:
        saldo -= retiro
        print(f"retiraste de tu saldo: {retiro}")
    else:
        print(f"Error, saldo no saldo disponible")

    if saldo <= 0:
        print("Tu no tienes saldo actualmente")