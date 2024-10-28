from baraja import Baraja

miBaraja = Baraja()
#miBaraja.mostrarCartas()


#miBaraja.barajar()
#miBaraja.mostrarCartas()

if miBaraja.quedanCartas():
    print("Hay cartas")
else:
    print("No hay cartas")

while miBaraja.quedanCartas():
    carta = miBaraja.sacarCarta()
    numCartas = miBaraja.contar()
    print(f"{carta}.Quedan {numCartas}")