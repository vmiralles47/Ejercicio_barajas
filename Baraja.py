class Naipe():
    def __init__(self):
        self.numero = ""
        self.palo = ""
        self.id = ""
        self.repartido = False
        # self.en_juego
        # self.imagen...

    def creaNaipe(self, num, palo):
        self.numero = num
        self.palo = palo
        self.id = self.numero+self.palo

    def muestraNaipe(self):
        print(self.id)


class Baraja_de_naipes():
    def __init__(self):
        self.mazo = []
        self.palos = ["o", "c", "e", "b"]
        self.numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
        self.barajada = False

    def crearBaraja_de_naipes(self):

        for p in self.palos:
            for n in self.numeros:
                mi_naipe = Naipe()
                mi_naipe.creaNaipe(n, p)
                self.mazo.append(mi_naipe)

        print("Creada baraja de ", len(self.mazo), " naipes")

    def muestraBaraja_de_naipes(self):
        display_baraja = []
        # imprime en filas de 10
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

    def cortar(self):  # coge la mitad inferior del mazo y la pone arriba
        mazo_aux = []
        for i in range(0, int(len(self.mazo)/2)):
            mazo_aux.append(self.mazo.pop(0))
        for j in range(0, len(mazo_aux)):
            self.mazo.append(mazo_aux[j])

    def mezclar(self):
        mazo_barajado = []
        vueltas = int(input("¿Cuántas veces quieres barajar?:"))
        contador = 1
        # barajo intercambiado cartas cada 3 posiciones, 3 veces
        while contador <= vueltas:
            for n in range(0, 3):
                for i in range(n, len(self.mazo), 3):
                    naipe = self.mazo[i]
                    mazo_barajado.append(naipe)
            self.mazo = mazo_barajado
            # self.mazo.cortar() -- puede invocarse un método dentro de otro método?

            print("barajo mazo de ", len(self.mazo),
                  " cartas", contador, "veces, cogiendo de 3 en 3")

            self.muestraBaraja_de_naipes()
            mazo_barajado = []
            contador = contador + 1
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

            # reparte cartas por turno a cada jugador tantesel ultimo jugador tantas veces como num_cartas
            ronda = 1
            while ronda <= num_cartas:
                for i in range(0, num_jugadores):
                    # extrae el primer elemento de la baraja
                    carta = self.mazo.pop(0)
                    carta.repartido = True
                    manos_jugadores[i].append(carta)
                ronda = ronda+1
            # imprime las manos de los jugadores.esto sería un método del juego que use la baraja, en caso de haberlo.
            display_mano = []
            for i in range(0, num_jugadores):
                print("Mano jugador ", i+1, ":")
                for j in range(0, num_cartas):
                    display_mano.append(manos_jugadores[i][j].id)
                print(display_mano)
                display_mano = []
                print("")


"""""
    def mezclar_repartiendo(self):
        self.Reparte_cartas(2, 20)
        for j in range(0, 20):
            self.mazo.append(self.manos_jugadores[1][j])
        for j in range(0, 20):
            self.mazo.append(self.manos_jugadores[0][j])
"""
