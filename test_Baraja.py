from clase_naipe import Baraja_de_naipes

mi_baraja = Baraja_de_naipes()
print("Palos de la baraja: ", mi_baraja.palos)
print("Números de la baraja:", mi_baraja.numeros)

mi_baraja.crearBaraja_de_naipes()
print("BARAJA CREADA: ")
mi_baraja.muestraBaraja_de_naipes()


print("")
print("VAMOS A BARAJAR: ")

mi_baraja.mezclar()

print("")
print("LA CORTA: ")
mi_baraja.cortar()
mi_baraja.muestraBaraja_de_naipes()
# print(mi_baraja.baraja)
print("Y AHORA A REPARTIR:")
jugadores = int(input("Num jugadores: "))
cartas = int(input("Num cartas: "))
mi_baraja.Reparte_cartas(jugadores, cartas)
print("")
print("Mazo sin las cartas repartidas:")
mi_baraja.muestraBaraja_de_naipes()
print("Baraja el mazo sin las cartas repartidas:")
mi_baraja.mezclar()
