from baraja import Baraja
from mano import Mano

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.barajar()
    def jugar(self):
        manoJugador1 = Mano()
        manoJugador1.añadirCarta(self.baraja.sacarCarta())
        print(f"Tu mano es {manoJugador1.cartas}")
        print(f"Total: {manoJugador1.valor}")
        while manoJugador1.valor < 21:
            accion = input("¿Quieres PEDIR carta o PASAR?")
            if accion == "p":
                manoJugador1.añadirCarta(self.baraja.sacarCarta())
                print(f"Tu mano es {manoJugador1.cartas} J1")
                print(f"Total: {manoJugador1.valor}")
            else:
                print(f"Tu puntuacion final es {manoJugador1.valor}")
                return
        
        manoJugador2 = Mano()
        manoJugador2.añadirCarta(self.baraja.sacarCarta())
        print(f"Tu mano es {manoJugador2.cartas}")
        print(f"Total: {manoJugador2.valor}")
        while manoJugador2.valor < 21:
            accion = input("¿Quieres PEDIR carta o PASAR?")
            if accion == "p":
                manoJugador2.añadirCarta(self.baraja.sacarCarta())
                print(f"Tu mano es {manoJugador2.cartas} J2")
                print(f"Total: {manoJugador2.valor}")
            else:
                print(f"Tu puntuacion final es {manoJugador2.valor}")
                return
        if manoJugador1.valor > mano

if __name__ == '__main__':
    print("JUEGO DE 21")
    juego = Juego()
    juego.jugar()
