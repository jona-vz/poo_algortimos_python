import random


def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista
    



if __name__ == '__main__':
    tam_de_lista = int(input('Dame el tamaño de la lista:   '))

    lista = [random.randint(0,100) for i in range(tam_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)
    print(lista)