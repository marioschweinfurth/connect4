import random
import re

escalaT = re.compile('[5-9][x][6-9]')
escalaT2 = re.compile('[1][0][x][1][0]')


def tablero(x,y):
    tablero = []
    for i in range(0,x+2):
        tablero.append([])
        for j in range(0,y+2):
            if i == 0:
                tablero[i].append(j)
            else:
                tablero[i].append(' ')
    return tablero



print('ingrese el tamanio del tablero. tome en cuenta que el tablero no puede ser mas pequenio de 5x6 y no puede ser mas grande de 10x10')
escala = input('tamanio: ')
if escalaT.fullmatch(escala):
    lineas = int(escala[0])
    columnas = int(escala[2])
    tablero = tablero(lineas+1,columnas)
    for i in range(0,lineas+1):
        for j in range(0,columnas+1):
            if j == 0:
                print('|', end='')
                print(tablero[i][j], end=' |')
            elif j == columnas:
                print(tablero[i][j], end=' |\n')
            else:
                print(tablero[i][j], end=' |')
    for i in range(0,columnas+1):
        print('---', end='')
elif escalaT2.fullmatch(escala):
    lineas = int(escala[0:2])
    columnas = int(escala[3:5])
    tablero = tablero(lineas+1,columnas)
    for i in range(0,lineas+1):
        for j in range(0,columnas+1):
            if j == 0:
                print('|', end='')
                print(tablero[i][j], end=' |')
            elif j == columnas:
                print(tablero[i][j], end=' |\n')
            else:
                print(tablero[i][j], end=' |')

else:
    print('tamanio invalido')
