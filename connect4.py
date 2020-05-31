import random
import re

escalaT = re.compile('[5-9][x][6-9]')
escalaT2 = re.compile('[1][0][x][1][0]')
'''
ama = "\033[0;33;01m \n"
ver = "\033[0;32;01m \n"
blanco = '\033[0;37;01m \n'
pieza = 'O'
print(ama , pieza, ver, pieza, blanco)
#print(piezaA)
'''
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
    tablero.reverse()
    for i in range(0,len(tablero)+1):
        if tablero[i][x] == ' ':
            tablero[i].pop(x)
            tablero[i].insert(x,'O')
            break
    tablero.reverse()

def desplegart(x):
    global tablero
    if escalaT.fullmatch(x):
        li = int(x[0])
        colu = int(x[2])
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
            if i == colu:
                print('---')
            else:
                print('---', end='')
    elif escalaT2.fullmatch(x):
        li = int(x[0:2])
        colu = int(x[3:5])
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
            if i == colu:
                print('---')
            else:
                print('---', end='')
    else:
        print('tamanio invalido.')


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
        try:
            opcion = int(input(""))
            if opcion == 1:
                desplegart()
                n1 = input("\nIngrese el 1 jugador: ")
                n2 = input("Ingrese el 2 jugador: ")
                j = random.randint(0,1)
                hvsh(n1,n2,j)
        except ValueError:
            print("Nel")
main()
'''
tablero = tablero(5,6)
desplegart('5x6')
jugada(4)
desplegart('5x6')
'''
