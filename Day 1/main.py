from itertools import combinations

def leer(file_path):

    f = open(file_path)
    l = [int(i) for i in f]
    f.close()

    return l

def star1(l, num):

    combinaciones = list(combinations(l, num))
    
    for combinacion in combinaciones:

      if sum(combinacion) == 2020:  

          return combinacion[0] * combinacion[1]

def star2(l, num):

    combinaciones = list(combinations(l, num))
    
    for combinacion in combinaciones:

      if sum(combinacion) == 2020:  

          return combinacion[0] * combinacion[1] * combinacion[2]


l = leer('Day 1/input.txt')

print('Solucion 1: ', star1(l, 2))
print('Solucion 2: ', star2(l, 3))
