class Nodo:

    def __init__(self, valor):

        self.valor = valor

        self.hijo_dch = None
        self.hijo_izq = None

    def __str__(self):
        return f'{self.valor}'

    def __repr__(self):
        return f'{self.hijo_izq}<{self.valor}>{self.hijo_dch}'


class Arbol_binario:

    def __init__(self,nodo):

        self.raiz = nodo
        self.lista_arbol_binario = []
        self.hijos_menores = []
        self.hijos_mayores = []

    def buscar(self):

        for i in self.lista_arbol_binario:

            if i >= self.valor:

                if i.hijo_izq == self.valor:
                    return f'Nodo encontrado: {self.hijo_izqu}<{self.valor}<{self.hijo_dch}'

            elif i <= self.valor:
                if i.hijo_dch == self.valor:
                    return f'Nodo encontrado: {self.hijo_izqu}<{self.valor}<{self.hijo_dch}'

            elif i == self.valor:
                return f'Nodo encontrado: {self.hijo_izqu}<{self.valor}<{self.hijo_dch}'

            elif not isinstance(lista_arbol, self.valor):

                return 'Nodo no encontrado'

    def insertar(self, nuevo_valor):

        self.lista_arbol_binario.append(nuevo_valor)

        if self.raiz is None:

            self.raiz = Nodo(nuevo_valor)
    
        elif nuevo_valor > self.raiz:
            
            if self.raiz.hijo_dch is None:
                self.raiz.hijo_dch = Nodo(nuevo_valor)
            else:
                self.insertar(self.raiz.hijo_dch.hijo_dch, nuevo_valor)

        elif nuevo_valor < self.raiz:
            
            if nodo.hijo_izq is None:
                nodo.hijo_izq = Nodo(nuevo_valor)
            else:
                self.insertar(self.hijo_izq.hijo_izq, nuevo_valor)

    def coste_ultima_busqueda(self, lista):
  
        contador = 0
        for i in lista:

            if isinstance(i, lista):

                for p in i:

                    contador = contador + 1
    
            if p == valor:

                return contador
                break
    
            elif i == valor:
                return contador
                break

            else:
                contador= contador + 1 


    def mostrar_arbol(self):
        pass



valores = [66, 34, 79, 26, 83, 39, 32, 60, 22, 74, 37, 80, 82, 50, 73, 31, 44, 33, 51]

contador = 0
for i in valores:
    i = Nodo(i)
    i = Arbol_binario(i)

   