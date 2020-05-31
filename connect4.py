import random
import re

escalaT = re.compile('[5-9][x][6-9]')
escalaT2 = re.compile('[1][0][x][1][0]')
piezaR = "\033[0;31;01mO\033[0;37;01m"
piezaV = "\033[0;32;01mO\033[0;37;01m"
j1 = 0
j2 = 0
emp = 0
true = True

def tabla(x,y):
    global tablero
    tablero = []
    for i in range(0,x):
        tablero.append([])
        for j in range(0,y):
            tablero[i].append(' ')
    return tablero

def jugada(x,y):
    global tablero, piezaR, piezaV
    diccionario = {1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9}
    if x in diccionario:
        x = diccionario[x]
        tablero.reverse()
        if y == 0:
            for i in range(0,len(tablero)):
                if tablero[i][x] == ' ':
                    tablero[i].pop(x)
                    tablero[i].insert(x,piezaR)
                    tablero.reverse()
                    return True
        else:
            for i in range(0,len(tablero)):
                if tablero[i][x] == ' ':
                    tablero[i].pop(x)
                    tablero[i].insert(x,piezaV)
                    tablero.reverse()
                    return True
        tablero.reverse()
    else:
        return False

def desplegart(x,y):
    for i in range(0,x):
        for j in range(0,y):
            if j == 0:
                print('|', end='')
                print(tablero[i][j], end=' |')
            elif j == y-1:
                print(tablero[i][j], end=' |\n')
            else:
                print(tablero[i][j], end=' |')
    for i in range(0,y+1):
        if i == y:
            print('---')
        else:
            print('---', end='')

def verificacion(x,y,z):
	for i in range(x):
		for j in range(y-3):
			if tablero[i][j] == z and tablero[i][j+1] == z and tablero[i][j+2] == z and tablero[i][j+3] == z:
				return True

	for i in range(x):
		for j in range(y-4):
			if tablero[j][i] == z and tablero[j+1][i] == z and tablero[j+2][i] == z and tablero[j+3][i] == z:
				return True

	for i in range(y-3):
		for j in range(x-3):
			if tablero[j][i] == z and tablero[j+1][i+1] == z and tablero[j+2][i+2] == z and tablero[j+3][i+3] == z:
				return True

	for i in range(y-3):
		for j in range(3, x):
			if tablero[j][i] == z and tablero[j-1][i+1] == z and tablero[j-2][i+2] == z and tablero[j-3][i+3] == z:
				return True

def hvsh(p,r,x,y,z):
    global j1, j2, emp, tablero, n1, n2, true
    cont = 0
    if z == 0:
        print(x,"va primero")
    else:
        print(y,"va primero")
    while True:
        if z == 0:
            print("Es el turno de", x)
            try:
                posi = int(input("Ingrese la fila que desee: "))
                if posi>0 and posi < r+1:
                    if cont == (p * r)-1:
                        print("Es un empate!")
                        emp += 1
                        print("Quieres la revancha? s/n")
                        revancha = input(">>>")
                        if revancha == "s":
                            z += 1
                            del tablero
                            tabla(p,r)
                            desplegart(p,r)
                            break
                        else:
                            del tablero
                            true = False
                            break
                    elif jugada(posi,z):
                        desplegart(p,r)
                        if verificacion(p,r,piezaR):
                            print(x,"gano la partida!\n")
                            j2+= 1
                            print("Quieres la revancha? s/n")
                            revancha = input(">>>")
                            if revancha == "s":
                                z += 1
                                del tablero
                                tabla(p,r)
                                desplegart(p,r)
                                return True
                            else:
                                del tablero
                                true = False
                                break
                        z += 1
                        cont += 1
                    else:
                        print('no hay espacio! :( \n')
                else:
                    print('esa linea no existe! :(\n')
            except ValueError:
                print('esa opcion no es una linea! :(\n')

        elif z == 1:
            print("Es el turno de", y)
            try:
                posi = int(input("Ingrese la fila que desee: "))
                if posi>0 and posi < r+1:
                    if cont == (p * r)-1:
                        print("Es un empate!")
                        emp += 1
                        print("Quieres la revancha? s/n")
                        revancha = input(">>>")
                        if revancha == "s":
                            z = 1
                            del tablero
                            tabla(p,r)
                            desplegart(p,r)
                            break
                        else:
                            del tablero
                            true = False
                            break
                    elif jugada(posi,z):
                        desplegart(p,r)
                        if verificacion(p,r,piezaV):
                            print(y,"gano la partida!\n")
                            j2+= 1
                            print("Quieres la revancha? s/n")
                            revancha = input(">>>")
                            if revancha == "s":
                                z -= 1
                                del tablero
                                tabla(p,r)
                                desplegart(p,r)
                                break
                            else:
                                del tablero
                                true = False
                                break
                        z -= 1
                        cont += 1
                    else:
                        print('no hay espacio! :( \n')
                else:
                    print('esa linea no existe! :(\n')
            except ValueError:
                print('esa opcion no es una linea! :(\n')

def main():
    global j1, j2, emp, tablero, true
    while True:
        print("1. HvsH")
        print('2. MvsH.... proximamente')
        print('3. MvsM.... proximamente')
        print('4. salir')
        try:
            opcion = int(input(""))
            if opcion == 1:
                while True:
                    print("Ingrese el tamanio de la tabla: ")
                    try:
                        p = int(input("Fila: "))
                        if p > 4 and p < 11:
                            r = int(input("Columna: "))
                            if r > 5 and r < 11:
                                tabla(p,r)
                                desplegart(p,r)
                                n1 = input("\nIngrese el 1 jugador: ")
                                n2 = input("Ingrese el 2 jugador: ")
                                j = random.randint(0,1)
                                while hvsh(p,r,n1,n2,j):
                                    print('oooh shit, here we go again')
                                break

                            else:
                                print('el tamanio de la columna es invalido.\n')
                        else:
                            print('el tamanio de la fila es invalido.\n')
                    except ValueError:
                        print('eso no es un numero.\n')



            elif opcion == 4:
                print('bye')
                break
            else:
                print('opcion invalida')
        except ValueError:
            print("opcion invalida")

main()
