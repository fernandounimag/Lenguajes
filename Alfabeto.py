
class Alfabeto():
    alfabeto1 = list()
    alfabeto2 = list()

    def eliminar_repetidos(self, alf):
        r = set(alf)
        return r

    def __init__(self):
        alfabeto1 = list()
        alfabeto2 = list()

    def set_alfabeto1(self, a1):
        self.alfabeto1 = a1

    def set_alfabeto2(self, a2):
        self.alfabeto2 = a2

    def union(self):
        r = list()
        for i in self.alfabeto2:
            self.alfabeto1.append(i)
        r = set(self.alfabeto1)
        return r

    def interseccion(self):
        r = list()
        aux = list()
        for i in self.alfabeto1:
            if i in self.alfabeto2:
                aux.append(i)
        r = set(aux)
        return r

    def diferencia(self):
        r = list()
        aux = list()
        for i in self.alfabeto1:
            if i not in self.alfabeto2:
                aux.append(i)
        r = set(aux)
        return r

    def estrella1(self):
        r = list()
        aux = list()
        if len(self.alfabeto1) > 0:
            for i in self.alfabeto1:
                aux.append(i)
        r = set(aux)
        return r

    def estrella1(self):
        r = list()
        aux = list()
        if len(self.alfabeto2):
            for i in self.alfabeto2:
                pass
