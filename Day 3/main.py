import numpy as np

def leertxt():

    pos = 0
    filename = 'Day 3/input.txt'
    with open(filename, 'r') as f: 

        for line in f.readlines():

            texto = [[int(i) for i in list(line.replace('.', '0').replace('#','1').rstrip())]]

            if pos == 0:
             
                contenido = np.array(texto)
           

            else:
  
                contenido = np.append(contenido, np.array(texto), axis = 0)

            pos += 1

        


    return contenido

def mover(mapa, posicion, movimiento):

    posicion = posicion + movimiento

    posicion[1] = posicion[1] % mapa.shape[1]

    return posicion



    
       


def main():

    posicion   =  np.array((0,0))
    total = 1


    mapa = leertxt() 

    lista_movimientos = [np.array((1,1)), np.array((1,3)), np.array((1,5)), np.array((1,7)), np.array((2,1))]

    for movimiento in lista_movimientos:

        arboles = 0
        posicion   =  np.array((0,0))

        while posicion[0]< mapa.shape[0]:

            
            if mapa[tuple(posicion)] == 1:

                arboles = arboles + 1

            posicion = mover(mapa, posicion, movimiento)

        print('El movimiento: ', movimiento, 'tiene: ', arboles, 'arboles')

        


        total = total * arboles
        print('Resultado final:', total)
    
        

main()




