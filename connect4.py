import random
import re

print('Grupo 7C\n')
print('Andrea Melissa Perez Dominguez    - 20002447')
print('Mario Augusto Schweinfurth Molina - 20001843')
escalaT = re.compile('[5-9][x][6-9]')
escalaT2 = re.compile('[1][0][x][1][0]')
piezaR = "\033[0;31;01mO\033[0;37;01m"
piezaV = "\033[0;32;01mO\033[0;37;01m"
j1 = 0
j2 = 0
emp = 0
true = True
puntos = 0
'''
# iba a ser una maquina para jugar pero fallo
def maquina(x,y):
    def mejorH(x,y):
        for i in range(x):
    		for j in range(y-3):
    			if tablero[i][j] == piezaV and tablero[i][j+1] == piezaV and tablero[i][j+2] == piezaV and tablero[i][j+3] == ' ':
                    jugada(j+3,1)
                    return True
                if tablero[i][j] == piezaV and tablero[i][j+1] == piezaV and tablero[i][j+2] == ' ' and tablero[i][j+3] == piezaV:
                    jugada(j+2,1)
                    return True
                if tablero[i][j] == piezaV and tablero[i][j+1] == ' ' and tablero[i][j+2] == piezaV and tablero[i][j+3] == piezaV:
                    jugada(j+1,1)
                    return True
                if tablero[i][j] == ' ' and tablero[i][j+1] == piezaV and tablero[i][j+2] == piezaV and tablero[i][j+3] == piezaV:
                    jugada(j,1)
                    return True

    def mejorV(x,y):
        for i in range(x):
            for j in range(y-4):
    			if tablero[j][i] == piezaV and tablero[j+1][i] == piezaV and tablero[j+2][i] == piezaV and tablero[j+3][i] == ' ':
                    jugada(i,1)
                    return True

    def mejorD(x,y):
        for i in range(y-3):
    		for j in range(x-3):
    			if tablero[j][i] == piezaV and tablero[j+1][i+1] == piezaV and tablero[j+2][i+2] == piezaV and tablero[j+3][i+3] == ' ':
                    jugada(i+3,1)
                    return True

    def mejorDN(x,y):
        for i in range(y-3):
    		for j in range(3, x):
    			if tablero[j][i] == piezaV and tablero[j-1][i+1] == piezaV and tablero[j-2][i+2] == piezaV and tablero[j-3][i+3] == ' ':
                    jugada(i+3,1)
                    return True

    def jugadaH(x,y):
        for i in range(x):
    		for j in range(y-2):
    			if tablero[i][j] == piezaV and tablero[i][j+1] == piezaV and tablero[i][j+2] == ' ':
                    jugada(j+2,1)

    def jugadaV(x,y):
        for i in range(x):
            for j in range(y-2):
    			if tablero[j][i] == piezaV and tablero[j+1][i] == piezaV and tablero[j+2][i] == ' ':
                    jugada(i,1)
                    return True

    def jugadaD(x,y):
        for i in range(y-2):
    		for j in range(x-2):
    			if tablero[j][i] == piezaV and tablero[j+1][i+1] == piezaV and tablero[j+2][i+2] == ' ':
                    jugada(i+2,1)
                    return True

    def jugadaDN(x,y):
        for i in range(y-2):
    		for j in range(2, x):
    			if tablero[j][i] == piezaV and tablero[j-1][i+1] == piezaV and tablero[j-2][i+2] == ' ':
                    jugada(i+2,1)
                    return True

    def bloqueoH(x,y):
        for i in range(x):
    		for j in range(y-3):
    			if tablero[i][j] == piezaR and tablero[i][j+1] == piezaR and tablero[i][j+2] == piezaR and tablero[i][j+3] == ' ':
                    jugada(j+3,1)
                    return True
                if tablero[i][j] == piezaR and tablero[i][j+1] == piezaR and tablero[i][j+2] == ' ' and tablero[i][j+3] == piezaR:
                    jugada(j+2,1)
                    return True
                if tablero[i][j] == piezaR and tablero[i][j+1] == ' ' and tablero[i][j+2] == piezaR and tablero[i][j+3] == piezaR:
                    jugada(j+1,1)
                    return True
                if tablero[i][j] == ' ' and tablero[i][j+1] == piezaR and tablero[i][j+2] == piezaR and tablero[i][j+3] == piezaR:
                    jugada(j,1)
                    return True

    def bloqueoV(x,y):
        for i in range(x):
            for j in range(y-4):
    			if tablero[j][i] == piezaR and tablero[j+1][i] == piezaR and tablero[j+2][i] == piezaR and tablero[j+3][i] == ' ':
                    jugada(i,1)
                    return Trues

    def bloqueoD(x,y):
        for i in range(y-3):
    		for j in range(x-3):
    			if tablero[j][i] == piezaR and tablero[j+1][i+1] == piezaR and tablero[j+2][i+2] == piezaR and tablero[j+3][i+3] == ' ':
                    jugada(i+3,1)
                    return Trues

    def bloqueoDN(x,y):
        for i in range(y-3):
    		for j in range(3, x):
    			if tablero[j][i] == piezaR and tablero[j-1][i+1] == piezaR and tablero[j-2][i+2] == piezaR and tablero[j-3][i+3] == ' ':
                    jugada(i+3,1)
                    return Trues

    if mejorH(x,y):
        break
    if mejorV(x,y):
        break
    if mejorD(x,y):
        break
    if mejorDN(x,y):
        break
    if bloqueoH(x,y):
        break
    if bloqueoV(x,y):
        break
    if bloqueoD(x,y):
        break
    if bloqueoDN(x,y):
        break
    if jugadaH(x,y):
        break
    if jugadaV(x,y):
        break
    if jugadaD(x,y):
        break
    if jugadaDN(x,y):
        break
    if puntos == 0:
        if y == 7:
            jugada(4,1)
            break
        elif y == 9:
            jugada(5,1)
            break
        else:
            jugada(random.randint(1,y),1)
            break

def maquina2(x,y):
    def mejorH(x,y):
        for i in range(x):
    		for j in range(y-3):
    			if tablero[i][j] == piezaR and tablero[i][j+1] == piezaR and tablero[i][j+2] == piezaR and tablero[i][j+3] == ' ':
                    jugada(j+3,0)
                    return True
                if tablero[i][j] == piezaR and tablero[i][j+1] == piezaR and tablero[i][j+2] == ' ' and tablero[i][j+3] == piezaR:
                    jugada(j+2,0)
                    return True
                if tablero[i][j] == piezaR and tablero[i][j+1] == ' ' and tablero[i][j+2] == piezaR and tablero[i][j+3] == piezaR:
                    jugada(j+1,0)
                    return True
                if tablero[i][j] == ' ' and tablero[i][j+1] == piezaR and tablero[i][j+2] == piezaR and tablero[i][j+3] == piezaR:
                    jugada(j,0)
                    return True
    def mejorV(x,y):
        for i in range(x):
            for j in range(y-4):
    			if tablero[j][i] == piezaR and tablero[j+1][i] == piezaR and tablero[j+2][i] == piezaR and tablero[j+3][i] == ' ':
                    jugada(i,0)
                    return True
    def mejorD(x,y):
        for i in range(y-3):
    		for j in range(x-3):
    			if tablero[j][i] == piezaR and tablero[j+1][i+1] == piezaR and tablero[j+2][i+2] == piezaR and tablero[j+3][i+3] == ' ':
                    jugada(i+3,0)
                    return True
    def mejorDN(x,y):
        for i in range(y-3):
    		for j in range(3, x):
    			if tablero[j][i] == piezaR and tablero[j-1][i+1] == piezaR and tablero[j-2][i+2] == piezaR and tablero[j-3][i+3] == ' ':
                    jugada(i+3,0)
                    return True
    def jugadaH(x,y):
        for i in range(x):
    		for j in range(y-2):
    			if tablero[i][j] == piezaR and tablero[i][j+1] == piezaR and tablero[i][j+2] == ' ':
                    jugada(j+2,0)
    def jugadaV(x,y):
        for i in range(x):
            for j in range(y-2):
    			if tablero[j][i] == piezaR and tablero[j+1][i] == piezaR and tablero[j+2][i] == ' ':
                    jugada(i,0)
                    return True
    def jugadaD(x,y):
        for i in range(y-2):
    		for j in range(x-2):
    			if tablero[j][i] == piezaR and tablero[j+1][i+1] == piezaR and tablero[j+2][i+2] == ' ':
                    jugada(i+2,0)
                    return True
    def jugadaDN(x,y):
        for i in range(y-2):
    		for j in range(2, x):
    			if tablero[j][i] == piezaR and tablero[j-1][i+1] == piezaR and tablero[j-2][i+2] == ' ':
                    jugada(i+2,0)
                    return True
    def bloqueoH(x,y):
        for i in range(x):
    		for j in range(y-3):
    			if tablero[i][j] == piezaV and tablero[i][j+1] == piezaV and tablero[i][j+2] == piezaV and tablero[i][j+3] == ' ':
                    jugada(j+3,0)
                    return True
                if tablero[i][j] == piezaV and tablero[i][j+1] == piezaV and tablero[i][j+2] == ' ' and tablero[i][j+3] == piezaV:
                    jugada(j+2,0)
                    return True
                if tablero[i][j] == piezaV and tablero[i][j+1] == ' ' and tablero[i][j+2] == piezaV and tablero[i][j+3] == piezaV:
                    jugada(j+1,0)
                    return True
                if tablero[i][j] == ' ' and tablero[i][j+1] == piezaV and tablero[i][j+2] == piezaV and tablero[i][j+3] == piezaV:
                    jugada(j,0)
                    return True
    def bloqueoV(x,y):
        for i in range(x):
            for j in range(y-4):
    			if tablero[j][i] == piezaV and tablero[j+1][i] == piezaV and tablero[j+2][i] == piezaV and tablero[j+3][i] == ' ':
                    jugada(i,0)
                    return Trues
    def bloqueoD(x,y):
        for i in range(y-3):
    		for j in range(x-3):
    			if tablero[j][i] == piezaV and tablero[j+1][i+1] == piezaV and tablero[j+2][i+2] == piezaV and tablero[j+3][i+3] == ' ':
                    jugada(i+3,0)
                    return Trues
    def bloqueoDN(x,y):
        for i in range(y-3):
    		for j in range(3, x):
    			if tablero[j][i] == piezaV and tablero[j-1][i+1] == piezaV and tablero[j-2][i+2] == piezaV and tablero[j-3][i+3] == ' ':
                    jugada(i+3,0)
                    return Trues
    if mejorH(x,y):
        break
    if mejorV(x,y):
        break
    if mejorD(x,y):
        break
    if mejorDN(x,y):
        break
    if bloqueoH(x,y):
        break
    if bloqueoV(x,y):
        break
    if bloqueoD(x,y):
        break
    if bloqueoDN(x,y):
        break
    if jugadaH(x,y):
        break
    if jugadaV(x,y):
        break
    if jugadaD(x,y):
        break
    if jugadaDN(x,y):
        break
    if puntos == 0:
        if y == 7:
            jugada(4,0)
            break
        elif y == 9:
            jugada(5,0)
            break
        else:
            jugada(random.randint(1,y),0)
            break
'''
#para generar la lista que funcionara como tabla del juego
def tabla(x,y):
    global tablero
    tablero = []
    for i in range(0,x):
        tablero.append([])
        for j in range(0,y):
            tablero[i].append(' ')
    return tablero

# para agregar una ficha en la linea seleccionada donde 'y' determina el color de la ficha.
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

# para desplegar la lista de modo que se mire como un tablero.
def desplegart(x,y):
    for i in range(0,y):
        if i == 0:
            print('|', end='')
            print(i+1, end=' |')
        elif i == y-1:
            print(i+1, end=' |\n')
        else:
            print(i+1, end=' |')
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

# para verificar si despues de una ugada realizada, se a ganado el juego.
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

# interaz de jugador contra jugador
def hvsh(p,r,x,y,z):
    global j1, j2, emp, tablero, n1, n2, true
    cont = 0
    tiradas = p*r
    if z == 0:
        print(x,"va primero\n")
    else:
        print(y,"va primero\n")
    while True:
        if z == 0:
            print("Es el turno de!", x)
            try:
                posi = int(input("\nIngrese la fila que desee: "))
                #verificar que la linea sea valida
                if posi>0 and posi < r+1:
                    #verificar si el juego ya empato antes de hacer la jugada
                    if cont == (p * r)-1:
                        print("Es un empate!")
                        emp += 1
                        print("\nQuieres la revancha? s/n")
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
                        print('tiradas faltantes!', tiradas-1)
                        tiradas -= 1
                        print('jugador:', x, 'con fichas', piezaR, end=" || ")
                        print('jugador:', y, 'con fichas', piezaV)
                        print('')
                        if verificacion(p,r,piezaR):
                            print(x,"gano la partida!\n")
                            j2+= 1
                            print("\nQuieres la revancha? s/n")
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
                posi = int(input("\nIngrese la fila que desee: "))
                if posi>0 and posi < r+1:
                    if cont == (p * r)-1:
                        print("Es un empate!")
                        emp += 1
                        print("\nQuieres la revancha? s/n")
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
                        print('\ntiradas faltantes!', tiradas-1)
                        tiradas -= 1
                        print('jugador:', x, 'con fichas', piezaR, end=" || ")
                        print('jugador:', y, 'con fichas', piezaV)
                        print('')
                        if verificacion(p,r,piezaV):
                            print(y,"gano la partida!\n")
                            j2+= 1
                            print("\nQuieres la revancha? s/n")
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
'''
#iba a ser la interfaz para que la maquina jugara contra la maquina2
def mvsm(p,r,z):
    cont = 0
    tiradas = p*r
    if z == 0:
        print("Maquina 1 va primero\n")
    else:
        print("Maquina 2 va primero\n")
    while True:
        if z == 0:
            print("Es el turno de Maquina 1!")
            if cont == (p * r)-1:
                print("Es un empate!")
                print("\nQuieres la revancha? s/n")
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
            maquina(p,r)
            desplegart(p,r)
            tiradas -= 1
            print('tiradas faltantes!', tiradas)
            print('Maquina 1 con fichas', piezaV, end=" || ")
            print('Maquina 2 con fichas', piezaR)
            if verificacion(p,r,piezaV):
                print("Maquina 1 gano la partida!\n")
                print("\nQuieres la revancha? s/n")
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
        elif z == 1:
            print("Es el turno de Maquina 2!")
            if cont == (p * r)-1:
                print("Es un empate!")
                print("\nQuieres la revancha? s/n")
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
            maquina2(p,r)
            desplegart(p,r)
            tiradas -= 1
            print('tiradas faltantes!', tiradas)
            print('Maquina 1 con fichas', piezaV, end=" || ")
            print('Maquina 2 con fichas', piezaR)
            if verificacion(p,r,piezaR):
                print("Maquina 1 gano la partida!\n")
                print("\nQuieres la revancha? s/n")
                revancha = input(">>>")
                if revancha == "s":
                    z -= 1
                    del tablero
                    tabla(p,r)
                    desplegart(p,r)
                    return True
                else:
                    del tablero
                    true = False
                    break
            z -= 1
            cont += 1
'''
#menu principal
def main():
    global j1, j2, emp, tablero, true
    while True:
        print("1. HvsH")
        print('2. MvsH.... fallo :(')
        print('3. MvsM.... fallo :(')
        print('4. salir')
        try:
            opcion = int(input(""))
            if opcion == 1:
                true = True
                while true:
                    print("Ingrese el tamanio de la tabla: ")
                    try:
                        p = int(input("Fila: "))
                        if p > 4 and p < 11:
                            while true:
                                try:
                                    r = int(input("Columna: "))
                                    if r > 5 and r < 11:
                                        tabla(p,r)
                                        print('')
                                        desplegart(p,r)
                                        n1 = input("\nnombre del 1 jugador: ")
                                        n2 = input("nombre del 2 jugador: ")
                                        j = random.randint(0,1)
                                        while hvsh(p,r,n1,n2,j):
                                            print('oooh shit, here we go again\n')
                                        true = False
                                    else:
                                        print('el tamanio de la columna es invalido.\n')
                                except ValueError:
                                    print('dato ingresado no es una numero.\n')
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
