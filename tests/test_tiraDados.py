from parchis.JuegoParchis import Parchis




def test_tiraDados1():
    Parchis.tiraDados()
    assert Parchis.dado1 >= 1 and Parchis.dado1 <= 6
    assert Parchis.dado2 >= 1 and Parchis.dado2 <= 6

def test_pintaTablero1():
    parchisObj = Parchis("Tony","Sara")
    parchisObj.TAM_TABLERO = 10
    tablero = parchisObj.pintaTablero
    tableroTest = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\n"
    tableroTest += parchisObj.nombreJ1 + "\tI\t\t\t\t\t\t\t\t\t\tF\n"
    tableroTest += parchisObj.nombreJ2 + "\tI\t\t\t\t\t\t\t\t\t\tF\n"
    print("Tablero prueba: \n" + tableroTest)
    print("Tablero recibido: \n")
    print(parchisObj.pintaTablero())
    assert tableroTest == parchisObj.pintaTablero()