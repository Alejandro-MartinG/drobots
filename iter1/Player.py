import sys
import Ice
Ice.loadSlice('drobots.ice')
import drobots


class Player(drobots.Player):
    def __init__(self, adapter_player):
        self.adapter = adapter_player
        self.value = None

    def win(self, current=None):
        print("Win")
        self.value = 0
        current.adapter.getCommunicator().shutdown()

    def lose(self, current=None):
        print("Lose")
        self.value = 1
        current.adapter.getCommunicator().shutdown()

    def getID(self, current=None):
        return '05712082D'
