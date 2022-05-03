import random


def busqueda_lineal(lista, objetivo):
    match = False
    
    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':
    tam_de_lista = int(input('Dame el tamaño de la lista:   '))
    objetivo = int(input('Que numero quieres encontrar?    '))

    lista = [random.randint(0,100) for i in range(tam_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')