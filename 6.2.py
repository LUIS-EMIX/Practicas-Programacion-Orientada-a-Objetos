a1 = int(input("introduce numero de filas: "))
a2 = int(input("introduce numero de columnas: "))
a3 = []
for i in range (a1) :
    a3.append([])
    for j in range(a2) :
        valor = float(input("a1 {}, a2 {} : ".format(i+1, j+1)))
        a3[i].append(valor)

print()
for a1 in a3 :
    print("[", end=" ")
    for elemento in a1 :
        print("{}".format(elemento), end=", ")
    print("], ")
print()

b1 = int(input("introduce numero de filas: "))
b2 = int(input("introduce numero de columnas: "))
b3 = []
for i in range (b1) :
    b3.append([])
    for j in range(b2) :
        valor = float(input("b1 {}, b2 {} : ".format(i+1, j+1)))
        b3[i].append(valor)

print()
for b1 in b3 :
    print("[", end=" ")
    for elemento in b1 :
        print("{}".format(elemento), end=", ")
    print("], ")
print()

def sumar_matrices (a3, b3) :
    if len (a3) == len(b3)  and len(a3[0]) == len(b3[0]):
        m3 = []
        for i in range (len(a3)) :
            m3.append([])
            for j in range (len(a3[0])) :
                m3[i].append(a3[i][j] + b3[i][j])
        return m3
    else:
        return None
c = sumar_matrices([a3], [b3])
if c == None:
    print("no se pueden sumar")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila :
            print(elemento, end=" ")
        print("]")