from random import randint
class Parchis:
    TAM_TABLERO = 10
    dado1 = 0
    dado2 = 0

    def __init__(self, nombreJ1, nombreJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2

    def tiraDados():
        Parchis.dado1 = randint(1, 6)
        Parchis.dado2 = randint(1, 6)

    def pintaTablero(self):
        resultado = "\tI"

        for i in range(1, Parchis.TAM_TABLERO):
            resultado += "\t" + str(i)
        resultado += "\tF\n" + self.nombreJ1 + "\tI"

        for i in range(1, Parchis.TAM_TABLERO):

            
            resultado += "\t"
        resultado += "\tF\n" + self.nombreJ2 + "\tI"

        for i in range(1, Parchis.TAM_TABLERO):

            resultado += "\t"
        resultado += "\tF\n"
        print(resultado)

        return resultado
    
    def avanzaPosiciones(numeroJugador):
        parchisObj = Parchis("test1","test2")
        parchisObj.tiraDados()
        if numeroJugador == 1:
            parchisObj.fichaJ1 += parchisObj.dado1 + parchisObj.dado2
            if parchisObj.fichaJ1 > parchisObj.TAM_TABLERO:
                parchisObj.fichaJ1 = parchisObj.TAM_TABLERO
                parchisObj.fichaJ1 -= parchisObj.dado1 + parchisObj.dado2
                parchisObj.fichaJ1 -= 1
        elif numeroJugador == 2:
            parchisObj.fichaJ2 += parchisObj.dado1 + parchisObj.dado2
            if parchisObj.fichaJ2 > parchisObj.TAM_TABLERO:
                parchisObj.fichaJ2 = parchisObj.TAM_TABLERO
                parchisObj.fichaJ2 -= parchisObj.dado1 + parchisObj.dado2
                parchisObj.fichaJ2 -= 1