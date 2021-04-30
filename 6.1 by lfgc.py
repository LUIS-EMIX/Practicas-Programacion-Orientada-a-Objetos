def dibujartablero(t):
    print(" %s | %s | %s" % (t[0][0], t[0][1], t[0][2]))
    print("-------------")
    print(" %s | %s | %s" % (t[1][0], t[1][1], t[1][2]))
    print("-------------")
    print(" %s | %s | %s" % (t[2][0], t[2][1], t[2][2]))
tablero = [[" ", "o", " "],
           [" ", " ", "o"],
           ["x", "x", " "]]

dibujartablero(tablero)
pos_x = int(input("\ningresar coordenada x:"))
pos_y = int(input("\ningresar coordenada y: "))
if tablero[pos_x][pos_y] != " ":
    print("posicion invalida!")
    exit()
tablero[pos_x][pos_y] = "x"
dibujartablero(tablero)
if pos_x == 2 and pos_y == 2:
    print("\nganaste!!")