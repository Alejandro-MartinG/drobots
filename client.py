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


        while True:
            try:
                print("logging... ")
                name = "alex" + str(random.randint(1, 10))
                game.login(player, name)
                print("I'm logged bro!!")
                break
            except drobots.GameInProgress:
                print red_nd_bold + "\nGame in progress waiting ... " + end_format
                time.sleep(10)
            except drobots.InvalidProxy:
                print red_nd_bold + "\nInvalid proxy" + end_format
                sys.exit(0)
            except drobots.InvalidName, e:
                print red_nd_bold + "\nInvalid player name :(" + end_format
                print str(e.reason)
                sys.exit(0)

        self.shutdownOnInterrupt()
        broker.waitForShutdown()

sys.exit(Client().main(sys.argv))
