from mano import Mano
from baraja import Baraja

miBaraja = Baraja()
miBaraja.barajar()

miMano = Mano()
if miBaraja.quedanCartas():
    miCarta = miBaraja.sacarCarta()
    miMano.añadirCarta(miCarta)

    miMano.añadirCarta(miBaraja.sacarCarta())

miMano.mostrarMano()