class Naipe():
    def __init__(self, num, palo):
        self.numero = num
        self.palo = palo
        self.id = self.numero+self.palo
        self.repartido = False
        # self.en_juego
        # self.imagen...

    def __str__(self):
        # return "{}".format(self.id)
        return f"{self.id}"

    def __repr__(self):
        return self.__str__()


class Baraja():
    def __init__(self):
        self.mazo = []
        self.palos = ["o", "c", "e", "b"]
        self.numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
        self.barajada = False

    def crea_Baraja(self):

        for p in self.palos:
            for n in self.numeros:
                mi_naipe = Naipe(n, p)
                self.mazo.append(mi_naipe)

        print("Creada baraja de ", len(self.mazo), " naipes")

    def __str__(self):
        if self.barajada == True:
            return f"Soy una baraja de {len(self.mazo)} cartas ya barajada"
        else:
            return f"Soy una baraja de {len(self.mazo)} cartas sin barajar"

    def __repr__(self):
        return self.__str__()

    def muestra_Baraja(self):
        # lista auxiliar donde meter los identificadores de los naipes para poder imprimirlos.
        display_baraja = []
        # imprime en filas de 10 los identificadores de cada carta
        for i in range(0, (len(self.mazo)//10)):
            for j in range(i*10, (i*10)+10):
                display_baraja.append(self.mazo[j].id)
            print(display_baraja)
            display_baraja = []
        # para el resto en caso de que haya
        if len(self.mazo) % 10 != 0:
            for i in range(0, (len(self.mazo) % 10)):
                display_baraja.append(self.mazo[i].id)
            print(display_baraja)
            display_baraja = []

    def cortar(self):  # coge la mitad inferior del mazo de naipes y la pone arriba
        mazo_aux = []
        for i in range(0, int(len(self.mazo)/2)):
            mazo_aux.append(self.mazo.pop(0))
        for j in range(0, len(mazo_aux)):
            self.mazo.append(mazo_aux[j])

    def mezclar(self):
        mazo_barajado = []
        # barajo intercambiado cartas cada 3 posiciones, lo corta y lo vuelve a intercambiar. 3 veces
        contador = 1
        while contador <= 3:
            for n in range(0, 3):
                for i in range(n, len(self.mazo), 3):
                    naipe = self.mazo[i]
                    mazo_barajado.append(naipe)
            self.mazo = mazo_barajado

            print("barajo mazo de ", len(self.mazo),
                  " cartas", contador, "veces, cogiendo de 3 en 3")

            self.muestra_Baraja()
            mazo_barajado = []
            contador = contador + 1
        # cambia estado de la Baraja a "barajada"
        self.barajada = True

    def Reparte_cartas(self, num_jugadores, num_cartas):
        if self.barajada == False:
            print("Las cartas no están barajadas.")
        else:
            manos_jugadores = []
            # lista de listas de len variable según num_jugadores. cada jugador tendrá una lista con sus cartas
            for j in range(0, num_jugadores):
                manos_jugadores.append([])
            print("Repartiendo ", num_cartas, "para",
                  len(manos_jugadores), "jugadores")

            # reparte cartas por turno a cada jugador tantas veces como num_cartas
            ronda = 1
            while ronda <= num_cartas:
                for i in range(0, num_jugadores):
                    # extrae el primer elemento de la baraja
                    carta = self.mazo.pop(0)
                    # cambai estado de esa carta a "repartida"
                    carta.repartido = True  # de momento es un atributo que no uso para nada
                    manos_jugadores[i].append(carta)
                ronda = ronda+1
            # podría hacer una clase "Mano" de Naipes, de la que haríamos tantas instancias como num jugadores. con un método "muestra"
            display_mano = []
            for i in range(0, num_jugadores):
                print("Mano jugador ", i+1, ":")
                for j in range(0, num_cartas):
                    display_mano.append(manos_jugadores[i][j].id)
                print(display_mano)
                display_mano = []
                print("")
