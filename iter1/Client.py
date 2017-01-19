import sys
import Ice
Ice.loadSlice('drobots.ice')
import drobots
import Player


class Client(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        adapter = broker.createObjectAdapter('PlayerAdapter')
        servant = Player.Player(adapter)

        game_proxy = broker.stringToProxy(argv[1])
        game = drobots.GamePrx.checkedCast(game_proxy)

        id = broker.stringToIdentity("Alex")
        player_proxy = adapter.add(servant, id)
        player = drobots.PlayerPrx.checkedCast(player_proxy)

        adapter.activate()
        game.login(player, 'Alejandro')

        self.shutdownOnInterrupt()
        broker.waitForShutdown()
        return servant.value

sys.exit(Client().main(sys.argv))
