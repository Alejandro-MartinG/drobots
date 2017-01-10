import sys
import Ice
Ice.loadSlice('drobots.ice')
import drobots


class PlayerI(drobots.Player):
    def __init__(self, current=None):
        self.factories = 1
        self.defenders = 1
        self.attackers = 1

    def win(self, current=None):
        print("Win")
        current.adapter.getCommunicator().shutdown()

    def lose(self, current=None):
        print("Lose")
        current.adapter.getCommunicator().shutdown()

    def gameAbort(self, current=None):
        print("Aborting game!!!")
        current.adapter.getCommunicator().shutdown()

    def makeController(self, bot, current=None):
        print("Make controller starting")
        return robot

    def makeDetectorController(self, current=None):
        print("Make detector starting")
