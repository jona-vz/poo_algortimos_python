import random


def busqueda_binaria(lista, inicio, final, objetivo):
    print(f'buscando {objetivo} entre {lista[inicio]} y {lista[final-1]}')
    if inicio > final:
        return False
    medio = (inicio + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    else:
        return busqueda_binaria(lista, inicio, medio-1, objetivo)
    


if __name__ == '__main__':
    tam_de_lista = int(input('Dame el tamaño de la lista:   '))
    objetivo = int(input('Que numero quieres encontrar?    '))

    lista = sorted([random.randint(0,100) for i in range(tam_de_lista)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')