'''
#SIN METODOS SETTER NI GETTERS
class Millas():
    def __init__(self, distancia=0) -> None:
        self.distancia = distancia

    def convertir_a_km(self):
        return (self.distancia * 1.609344)


if __name__ == '__main__':
    avion = Millas()

    avion.distancia = 200

    print(avion.distancia)
    print(avion.convertir_a_km())
'''


'''#UTILIZANDO GETTERS Y SETTERS
class Millas():
    def __init__(self, distancia=0) -> None:
        self.distancia = distancia

    def convertir_a_km(self):
        return (self.distancia * 1.609344)

    #metodo getter
    def get_distancia(self):
        return self._distancia

    #metodo setter
    def set_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        self._distancia = valor
        

if __name__ == '__main__':
    avion = Millas()

    avion.distancia = 200
    avion.set_distancia(120)

    print(avion._distancia)
    print(avion.get_distancia())
    print(avion.convertir_a_km())
'''

'''#CON LA FUNCION PROPERTY
class Millas():
    def __init__(self) -> None:
        self._distancia = 0

    #metodo getter
    def get_distancia(self):
        print('---get---')
        return self._distancia

    #metodo setter
    def set_distancia(self, recorrido):
        print('---set---')
        self._distancia = recorrido
    
    #metodo deleter
    def del_distancia(self):
        print('---del---')
        del self._distancia
    
    def convertir_a_km(self):
        return (self._distancia * 1.609344)

    distancia = property(get_distancia, set_distancia, del_distancia)
        

if __name__ == '__main__':
    avion = Millas()

    avion.distancia = 150
    print(avion.distancia)
'''

#CON LA FUNCION @property
class Millas():
    def __init__(self) -> None:
        self._distancia = 0

    #metodo getter
    #usando decorador property
    @property
    def get_distancia(self):
        print('---get---')
        return self._distancia

    #metodo setter
    @get_distancia.setter
    def set_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        self._distancia = valor
    
        

if __name__ == '__main__':
    avion = Millas()

    avion.set_distancia = 200
    
        
    print(avion.get_distancia)

