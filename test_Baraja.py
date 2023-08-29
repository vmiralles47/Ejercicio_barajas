from Baraja import Baraja

mi_baraja = Baraja()
print("clase BARAJA hecha clases NAIPE")
print("Palos de la baraja: ", mi_baraja.palos)
print("Números de la baraja:", mi_baraja.numeros)

mi_baraja.crea_Baraja()
print("BARAJA CREADA: ")
mi_baraja.muestra_Baraja()


print("")
print("VAMOS A BARAJAR: ")

# la muestra de la baraja mezclada está dentro del método "mezclar" para facilitar el test
mi_baraja.mezclar()

print("")
print("Cortamos la baraja:")
mi_baraja.cortar()
mi_baraja.muestra_Baraja()

print("Y AHORA A REPARTIR:")
jugadores = int(input("Num jugadores: "))
cartas = int(input("Num cartas: "))
mi_baraja.Reparte_cartas(jugadores, cartas)
print("")
print("Mazo sin las cartas repartidas:")
mi_baraja.muestra_Baraja()
print("Baraja el mazo sin las cartas repartidas:")
mi_baraja.mezclar()

print("Fin. Gracias :-)")
