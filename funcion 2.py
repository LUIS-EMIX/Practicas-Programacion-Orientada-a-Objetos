class Persona:
    """
    esta clase es para representar una persona
    """
    nombre = ""
    edad = None
    dni = ""

Persona.nombre = "luis"
Persona.edad = 18
Persona.dni = "30913562H"

print(Persona.nombre)
print(Persona.edad)
if Persona.edad >= 18:
    print("mayor de edad")
else:
    print("menor de edad")

print(Persona.dni)