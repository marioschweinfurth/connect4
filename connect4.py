import random
import re

escalaT = re.compile('[5-9][x][6-9]')
escalaT2 = re.compile('[1][0][x][1][0]')
piezaR = "\033[0;31;01mO\033[0;37;01m"
piezaV = "\033[0;32;01mO\033[0;37;01m"

def tablero(x,y):
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
    x = diccionario[x]
    tablero.reverse()
    if y == 0:
        for i in range(0,len(tablero)+1):
            if tablero[i][x] == ' ':
                tablero[i].pop(x)
                tablero[i].insert(x,piezaR)
                break
    else:
        for i in range(0,len(tablero)+1):
            if tablero[i][x] == ' ':
                tablero[i].pop(x)
                tablero[i].insert(x,piezaV)
                break
    tablero.reverse()

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
	# Check horizontal locations for win
	for i in range(y-3):
		for j in range(x):
			if tablero[j][i] == z and tablero[j][i+1] == z and tablero[j][i+2] == z and tablero[j][i+3] == z:
				return True

	# Check vertical locations for win
	for i in range(y):
		for j in range(x-3):
			if tablero[j][i] == z and tablero[j+1][i] == z and tablero[j+2][i] == z and tablero[j+3][i] == z:
				return True

	# Check positively sloped diaganols
	for i in range(y-3):
		for j in range(x-3):
			if tablero[j][i] == z and tablero[j+1][i+1] == z and tablero[j+2][i+2] == z and tablero[j+3][i+3] == z:
				return True

	# Check negatively sloped diaganols
	for i in range(y-3):
		for j in range(3, x):
			if tablero[j][i] == z and tablero[j-1][i+1] == z and tablero[j-2][i+2] == z and tablero[j-3][i+3] == z:
				return True

def hvsh(p,r,x,y,z):
    global j1, j2, emp, tablero
    cont = 0
    if z == 0:
        print(x,"va primero")
    else:
        print(y,"va primero")
    while True:
        if z == 0:
            print("Es el turno de", x)
            posi = int(input("Ingrese la fila que desee: "))
            jugada(posi,z)
            desplegart(p,r)
            z += 1
            cont += 1
            if cont == p * r:
                print("Es un empate!")
                emp += 1
                break
        elif z == 1:
            print("Es el turno de", y)
            posi = int(input("Ingrese la fila que desee: "))
            jugada(posi,z)
            desplegart(p,r)
            z += 1
            cont += 1
            if cont == p * r:
                print("Es un empate!")
                emp += 1
                break
		#Ignore lo de abajo que solo estoy probando
        if verificacion(p,r,piezaR):
            print(selec,"gano la partida!")
            if selec == x:
                j1 += 1
            else:
                j2 += 1
        elif verificacion(p,r,piezaV):
            print(selec,"gano la partida!")
            if selec == x:
                j1 += 1
            else:
                j2 += 1
            print("Quieres la revancha?")
            p = input(">>>")
            if p == "n":
                break



def main():
    global j1, j2, empa
    while True:
        print("1------HvsH")
        print('2. escala de tablero')
        print('4. salir')
        try:
            opcion = int(input(""))
            if opcion == 1:
                print("Ingrese el tamanio de la tabla: ")
                p = int(input("Columna: "))
                r = int(input("Fila: "))
                tablero(p,r)
                desplegart(p,r)
                n1 = input("\nIngrese el 1 jugador: ")
                n2 = input("Ingrese el 2 jugador: ")
                j = random.randint(0,1)
                hvsh(p,r,n1,n2,j)

            elif opcion == 2:
                escala = input('-->')
                if escalaT.fullmatch(escala):
                    x = int(escala[0])
                    y = int(escala[2])
                elif escalaT2.fullmatch(escala):
                    x = int(escala[0:2])
                    y = int(escala[3:5])
                tablero(x,y)
                desplegart(x,y)

            elif opcion == 4:
                print('bye')
                break
            else:
                print('opcion invalida')
        except ValueError:
            print("Nel")

main()
