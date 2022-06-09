import random

def ordenamiento_x_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izq = lista[:medio]
        der = lista[medio:]
        print(izq, '*' * 5, der)

        #llamada recursiva en cada mitad
        ordenamiento_x_mezcla(izq)
        ordenamiento_x_mezcla(der)

        #iteradores para recorrer sublistas
        i=0
        j=0
        #iterador para la lista principal
        k = 0

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i+=1
            else:
                lista[k] = der[j]
                j+=1
            
            k+=1
        
        while i < len(izq):
            lista[k] = izq[i]
            i+=1
            k+=1

        while j < len(der):
            lista[k] = der[j]
            j+=1
            k+=1

        print(f'izq {izq}, der {der}')
        print(lista)
        print('-'*50)

    return lista


if __name__ == '__main__':
    tam_de_lista = int(input('Dame el tamaño de la lista:   '))

    lista = [random.randint(0,100) for i in range(tam_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_x_mezcla(lista)
    print(lista_ordenada)
    print(lista)