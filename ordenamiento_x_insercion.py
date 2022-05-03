import random


def ordenamiento_x_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        
        lista[posicion_actual] = valor_actual
    
    return lista


if __name__ == '__main__':
    tam_de_lista = int(input('Dame el tamaño de la lista:   '))

    lista = [random.randint(0,100) for i in range(tam_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_x_insercion(lista)
    print(lista_ordenada)
    print(lista)