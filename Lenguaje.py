#clase conjunto
class Lenguaje:
    lenguaje1 = list()
    lenguaje2 = list()

    # constructor
    def __init__(self):
        self.lenguaje1 = list()
        self.lenguaje2 = list()

    #metodos
    def eliminar_repetidos_1(self):
        r = set(self.lenguaje1)
        return r

    def eliminar_repetidos_2(self):
        r = set(self.lenguaje2)
        return r

    def add_elemento_1(self, l):
        if(l not in self.lenguaje1):
            self.lenguaje1.insert(0,l)
            return True
        else:
            return False

    def add_elemento_2(self, l):
        if(l not in self.lenguaje2):
            self.lenguaje2.insert(0,l)
            return True
        else:
            return False

    def operacion_union(self):
        newlist = list()
        aux = list()
        aux = self.lenguaje1 + self.lenguaje2
        newlist = set(aux)
        return newlist

    def operacion_interseccion(self):
        newlist = list()
        aux = list()
        for i in self.lenguaje1:
            if i in self.lenguaje2:
                aux.append(i)
        newlist = set(aux)
        return newlist

    def operacion_diferencia(self):
        newlist = list()
        aux = list()
        for i in self.lenguaje1:
            if i not in self.lenguaje2:
                aux.append(i)
        newlist = set(aux)
        return newlist

    def operacion_concatenacion(self):
        newlist = list()
        newlist = self.lenguaje1 + self.lenguaje2
        return newlist

    def operacion_cardinalidad(self):
        res = ''
        for i in range(0, len(self.lenguaje1)):
            res += ("Cardinalidad: " + self.lenguaje1[i] + " : " + str(len(self.lenguaje1[i])) + "\n")
        for j in range(0, len(self.lenguaje2)):
            res += ("Cardinalidad: " + self.lenguaje2[j] + " : " + str(len(self.lenguaje1[j])) + "\n")
        return res

    def operacion_inversa(self):
        lengua1 = list()
        lengua2 = list()
        res = list()
        for i in self.lenguaje1:
            length_str = len(i)
            lengua1.append(i[length_str::-1])
        for j in self.lenguaje2:
            length_str = len(j)
            lengua2.append(j[length_str::-1])
        res = list(lengua1) + list(lengua2)
        return res

    def operacion_inversa(self):
        lengua1 = list()
        lengua2 = list()
        res = list()
        for i in self.lenguaje1:
            length_str = len(i)
            lengua1.append(i[length_str::-1])
        for j in self.lenguaje2:
            length_str = len(j)
            lengua2.append(j[length_str::-1])
        res = list(lengua1) + list(lengua2)
        return res
