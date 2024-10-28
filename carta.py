class Carta: 
    def __init__(self,palo,valor):#Metodos
        self.palo = palo#Propiedades
        self.valor = valor #Propiedades
    def __repr__(self):#Metodos
        return f"{self.valor} de {self.palo}"