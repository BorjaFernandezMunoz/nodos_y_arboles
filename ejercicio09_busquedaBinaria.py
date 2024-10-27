class Nodo (self, valor):

    def __init__(self):

        self.valor = valor

        self.hijo_dch = None
        self.hijo_izq = None

    def __str__(self):
        return f'{self.valor}'

    def __repr__(self):
        return f'{self.hijo_izq}<{self.valor}>{self.hijo_dch}'


class Arbol_binario (self):

    def __init__(self):

        self.raiz = None
        self.lista_arbol_binario = []
        self.hijos_menores = []
        self.hijos_mayores = []

    def buscar(self, ):

        for i in lista_arbol_binario:

            if i >= self.valor:

                if i.hijo_izq == self.valor:
                    return f'Nodo encontrado: {self.hijo_izqu}<{self.valor}<{self.hijo_dch}'

            elif i <= self.valor:
                if i.hijo_dch == self.valor:
                    return f'Nodo encontrado: {self.hijo_izqu}<{self.valor}<{self.hijo_dch}'

            elif i == self.valor:
                return f'Nodo encontrado: {self.hijo_izqu}<{self.valor}<{self.hijo_dch}'

            elif self.valor not isinstance(lista_arbol):

                return 'Nodo no encontrado'

    def insertar(self, nodo, nuevo_valor):
    
        if nodo not isinstance(Nodo):

            raise ValueError(f"{nodo} no es un nodo")
    
        elif self.raiz is None:

            self.raiz = Nodo(nuevo_valor)
    
        elif nuevo_valor > self.raiz:
            
            if nodo.hijo_dch is None:
                nodo.hijo_dch = Nodo(nuevo_valor)
            else:
                self.insertar(nodo.hijo_dch, nuevo_valor)

        elif nuevo_valor < self.raiz:
            
            if nodo.hijo_izq is None:
                nodo.hijo_izq = Nodo(nuevo_valor)
            else:
                self.insertar(nodo.hijo_izq, nuevo_valor)

    def coste_ultima_busqueda(self, self.lista_arbol_binario):
  
        contador = 0
        for i in lista:

            if isinstance(i, list):

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