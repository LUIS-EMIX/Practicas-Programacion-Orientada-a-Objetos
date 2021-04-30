class CuentaJoven:
    """
    esta clase es para representar una cuenta joven
    """

    titular = ""
    edad = None
    cantidad = None
CuentaJoven.titular = "luis"
CuentaJoven.edad = 18
CuentaJoven.cantidad = 12000

print(CuentaJoven.titular)
print(CuentaJoven.edad)
if CuentaJoven.edad >= 18:
    print("mayor de edad: (verdadero)")
else:
    print("menor de edad: (falso)")

print(CuentaJoven.cantidad)

retirar = int(input("cantidad a retirar:"))
print(retirar)
resta = CuentaJoven.cantidad-retirar
print(resta)
print("cuenta joven de:", CuentaJoven.titular)
bonificacion = ("bonificacion:",resta)
print(bonificacion)