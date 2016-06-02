import sys
import Ice
Ice.loadSlice('drobots.ice')
import drobots


class Player(drobots.Player):
    def __init__(self, adapter):
        self.adaptador = adapter
        self.contadorCreados = 0
        self.contadorRobots=0

    def win(self, current=None):
        print("Win")
        current.adapter.getCommunicator().shutdown()

    def lose(self, current=None):
        print("Lose")
        current.adapter.getCommunicator().shutdown()

    def gameAbort(self, current=None):
        print("Break!!!!!!1")
        current.adapter.getCommunicator().shutdown()

    def makeController(self, robot, current=None):
        print("Make controller")

        return robot
