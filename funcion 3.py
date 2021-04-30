class Cuenta:
    """
    esta clase es para representar una cuenta
    """
    titular = ""
    cantidad = None

Cuenta.titular = "luis"
Cuenta.cantidad = 10000
print(Cuenta.titular)
print(Cuenta.cantidad)
n = int(input("ingresar la cantidad:"))
if n > 0:

    sumaT = Cuenta.cantidad + n
    print(n)
    print(sumaT)
retirar = int(input("cantidad a retirar:"))
print(retirar)
resta = Cuenta.cantidad - retirar
print(resta)