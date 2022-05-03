class Persona():
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def avanza(self):
        print("Caminando")


class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        print("En bici")


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()