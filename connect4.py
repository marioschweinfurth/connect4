import random
import re

escalaT = re.compile('[5-9][x][6-9]')
escalaT2 = re.compile('[1][0][x][1][0]')


def tablero(x,y):
    tablero = []
    for i in range(0,x):
        tablero.append([])
        for j in range(0,y):
            tablero[i].append(' ')
    return tablero

def jugada(x):
    global tablero
    diccionario = {1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9}
    x = diccionario[x]
    for i in reverse(tablero):
        if tablero[i][x] == ' ':
            tablero[i].pop(x)
            tablero[i].insert(x,pieza)
            break

def desplegart(x):
    if escalaT.fullmatch(escala):
        li = int(escala[0])
        colu = int(escala[2])
        tablero = tablero(li,colu)
        for i in range(0,li):
            for j in range(0,colu):
                if j == 0:
                    print('|', end='')
                    print(tablero[i][j], end=' |')
                elif j == colu-1:
                    print(tablero[i][j], end=' |\n')
                else:
                    print(tablero[i][j], end=' |')
        for i in range(0,colu+1):
            print('---', end='')
    elif escalaT2.fullmatch(escala):
        li = int(escala[0:2])
        colu = int(escala[3:5])
        tablero = tablero(li,colu)
        for i in range(0,li):
            for j in range(0,colu):
                if j == 0:
                    print('|', end='')
                    print(tablero[i][j], end=' |')
                elif j == colu-1:
                    print(tablero[i][j], end=' |\n')
                else:
                    print(tablero[i][j], end=' |')
        for i in range(0,colu+1):
            print('---', end='')
    else:
        print('tamanio invalido.')
#print('ingrese el tamanio del tablero. tome en cuenta que el tablero no puede ser mas pequenio de 5x6 y no puede ser mas grande de 10x10')
#escala = input('tamanio: ')

def hvsh(x,y,z):
    global j1, j2, emp, tablero
    cont = 0
    if z == 0:
        print(x,"va primero")
    else:
        print(y,"va primero")
    while True:
        if z == 0:
            print("Es el turno de", x)
            posi = ("Ingrese la fila que desee: ")
            #esto no esta terminado
            
def main():
    global j1, j2, empa
    while True:
        print("1------HvsH")
        opcion = int(input(""))
        try:
            if opcion == 1:
                desplegart()
                n1 = input("\nIngrese el 1 jugador: ")
                n2 = input("Ingrese el 2 jugador: ")
                j = random.randint(0,1)
                hvsh(n1,n2,j)
        except ValueError:
            print("Nel")
main()
