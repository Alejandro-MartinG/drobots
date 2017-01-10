#!/usr/bin/python
# -*- coding:utf-8; mode:python -*-

import sys
import Ice
Ice.loadSlice('drobots.ice')
import drobots
import math
import random
from Player import PlayerI


class Client(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        adapter = broker.createObjectAdapter("PlayerAdapter")
        servant = PlayerI()

        id = broker.stringToIdentity("Alex")
        adapter.add(servant, id)

        direct_prx = adapter.createDirectProxy(id)
        adapter.activate()
        player = drobots.PlayerPrx.checkedCast(direct_prx)
        if not player:
            raise RuntimeError('Invalid player proxy')

        client_prx = broker.propertyToProxy("Game_proxy")
        game = drobots.GamePrx.checkedCast(client_prx)
        if not game:
            raise RuntimeError('Invalid game proxy')

        name = "alex" + str(random.randint(1, 10))
        game.login(player, name)

        self.shutdownOnInterrupt()
        broker.waitForShutdown()

sys.exit(Client().main(sys.argv))
